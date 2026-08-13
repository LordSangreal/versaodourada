"""Percorre os scripts de Gold nas ROMs USA e BR em passo travado.

O bytecode dos scripts e identico nas duas ROMs (so os ponteiros de texto
mudam), entao o mesmo percurso rende, para cada fala, a chave USA que o
gen1recomp usa e o texto BR correspondente.
"""
import re, os, sys, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from gen2text import decode, is_texty, key as _k
import entradas

REPO = os.path.join(HERE, "repo")
USA_PATH = r"D:\pokemon gold tradução\Pokemon - Gold Version (USA, Europe) (SGB Enhanced).gbc"
BR_PATH = os.path.join(HERE, "br", "Pokemon - Gold Version (BR) (www.romsportugues.com).gbc")

MAP_LENGTH, ATTR_LENGTH = 9, 12
WARP_LENGTH, COORD_LENGTH, BG_LENGTH, OBJECT_LENGTH = 5, 8, 5, 13


# ---------------------------------------------------------------- opcodes
def load_opcodes():
    src = open(os.path.join(REPO, "src/script/gen2/Opcodes.lua"), encoding="utf-8").read()
    ops = {}
    for m in re.finditer(r'\[(0x[0-9a-fA-F]+)\]\s*=\s*\{\s*name\s*=\s*"(\w+)"\s*,\s*size\s*=\s*(\d+)', src):
        ops[int(m.group(1), 16)] = (m.group(2), int(m.group(3)))
    term = set()
    blk = re.search(r'Opcodes\.TERMINATORS\s*=\s*\{(.*?)\}', src, re.S)
    for m in re.finditer(r'(?:\[")?(\w+)(?:"\])?\s*=\s*true', blk.group(1)):
        term.add(m.group(1))
    return ops, term


OPS, TERMINATORS = load_opcodes()
TEXT_NEAR = {"writetext", "jumptext", "jumptextfaceplayer", "repeattext"}
JUMP_NEAR = {"iftrue", "iffalse", "sjump", "scall", "stopandsjump", "sdefer",
             "memjump", "memcall"}
JUMP_COND3 = {"ifequal", "ifnotequal", "ifgreater", "ifless"}
JUMP_FAR = {"farscall", "farsjump", "farwritetext", "farjump"}


class Rom:
    def __init__(self, path):
        self.d = open(path, "rb").read()

    def off(self, bank, addr):
        if addr < 0x4000:
            return addr
        return bank * 0x4000 + (addr - 0x4000)

    def byte(self, bank, addr):
        o = self.off(bank, addr)
        return self.d[o] if 0 <= o < len(self.d) else None

    def word(self, bank, addr):
        lo, hi = self.byte(bank, addr), self.byte(bank, addr + 1)
        return None if lo is None or hi is None else lo | (hi << 8)


def ok_addr(bank, addr):
    return addr is not None and (addr >= 0x4000 or bank == 0) and addr != 0


# ---------------------------------------------------------------- percurso
def walk(usa, br, starts):
    """Anda os scripts em passo travado; devolve {chave_usa: (en, pt)}."""
    out, seen, st = {}, set(), collections.Counter()
    queue = list(starts)
    while queue:
        bank, addr = queue.pop()
        k = _k(bank, addr)
        if k in seen:
            continue
        seen.add(k)
        pc, guard = addr, 0
        while guard < 4000:
            guard += 1
            op_u = usa.byte(bank, pc)
            op_b = br.byte(bank, pc)
            if op_u is None or op_u not in OPS:
                st["op_desconhecido"] += 1
                break
            if op_u != op_b:
                st["divergencia_bytecode"] += 1
                break
            name, size = OPS[op_u]
            au = [usa.byte(bank, pc + 1 + i) for i in range(size)]
            ab = [br.byte(bank, pc + 1 + i) for i in range(size)]
            if any(x is None for x in au) or any(x is None for x in ab):
                break

            def w(a, i=0):
                return a[i] | (a[i + 1] << 8)

            if name in TEXT_NEAR and size >= 2:
                record(out, st, usa, br, bank, w(au), bank, w(ab))
            elif name == "farwritetext" and size >= 3:
                record(out, st, usa, br, au[2], w(au), ab[2], w(ab))
            elif name == "trainertext" or name == "winlosstext":
                if size >= 4:
                    record(out, st, usa, br, bank, w(au), bank, w(ab))
                    record(out, st, usa, br, bank, w(au, 2), bank, w(ab, 2))
            elif name in JUMP_NEAR and size >= 2:
                if ok_addr(bank, w(au)):
                    queue.append((bank, w(au)))
            elif name in JUMP_COND3 and size >= 3:
                if ok_addr(bank, w(au, 1)):
                    queue.append((bank, w(au, 1)))
            elif name in JUMP_FAR and size >= 3:
                if ok_addr(au[2], w(au)):
                    queue.append((au[2], w(au)))
            if name in TERMINATORS:
                break
            pc += 1 + size
    return out, st


def record(out, st, usa, br, ub, ua, bb, ba):
    if not ok_addr(ub, ua) or not ok_addr(bb, ba):
        return
    k = _k(ub, ua)
    en, ok1 = decode(usa, ub, ua, br=False)
    pt, ok2 = decode(br, bb, ba, br=True)
    if not ok1 or not ok2 or not pt:
        st["decode_falhou"] += 1
        return
    if k in out and out[k][1] != pt:
        st["conflito"] += 1
        return
    out[k] = (en, pt)
    st["texto"] += 1


if __name__ == "__main__":
    usa, br = Rom(USA_PATH), Rom(BR_PATH)
    mf = json.load(open(os.path.join(REPO, "tools/rom_manifest_gold.json"), encoding="utf-8"))
    groups = collections.defaultdict(int)
    for m in mf["maps"].values():
        groups[m["group"]] = max(groups[m["group"]], m["map"])
    starts, textos = entradas.coletar(usa, br, groups)
    print("pontos de entrada:", len(starts), "| textos diretos:", len(textos))
    out, st = walk(usa, br, starts)
    for bank, a_u, a_b in textos:
        record(out, st, usa, br, bank, a_u, bank, a_b)
    print("estatisticas:", dict(st))
    print("FALAS CASADAS:", len(out))
    same = sum(1 for en, pt in out.values() if en == pt)
    acc = sum(1 for en, pt in out.values() if any(c in pt for c in "áãçéê"))
    print(f"  traduzidas: {len(out)-same} | iguais: {same} | com acento: {acc}")
    json.dump({k: list(v) for k, v in out.items()},
              open(os.path.join(HERE, "dialogo.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=0)

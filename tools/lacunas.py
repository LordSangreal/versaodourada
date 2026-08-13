"""Mede exatamente onde o extrator perde texto, para priorizar o que falta."""
import os, sys, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import walk as W
from gen2text import decode, CHARMAP, BR_CHARMAP, key as _k

usa, br = W.Rom(W.USA_PATH), W.Rom(W.BR_PATH)
mf = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                    encoding="utf-8"))
groups = collections.defaultdict(int)
for m in mf["maps"].values():
    groups[m["group"]] = max(groups[m["group"]], m["map"])
starts, _ = W.entry_points(usa, groups)

# --- 1. quais bytes de opcode travam o percurso
desconhecidos = collections.Counter()
divergencias = collections.Counter()
seen = set()
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
        ou, ob = usa.byte(bank, pc), br.byte(bank, pc)
        if ou is None:
            break
        if ou not in W.OPS:
            desconhecidos[ou] += 1
            break
        if ou != ob:
            divergencias[W.OPS[ou][0]] += 1
            break
        name, size = W.OPS[ou]
        au = [usa.byte(bank, pc + 1 + i) for i in range(size)]
        if any(x is None for x in au):
            break
        if size >= 2:
            w = au[0] | (au[1] << 8)
            if name in W.JUMP_NEAR and W.ok_addr(bank, w):
                queue.append((bank, w))
            elif name in W.JUMP_FAR and size >= 3 and W.ok_addr(au[2], w):
                queue.append((au[2], w))
        if name in W.TERMINATORS:
            break
        pc += 1 + size

print("=== 1. bytes que travam o percurso (opcode nao reconhecido) ===")
print("   total de travadas:", sum(desconhecidos.values()))
for b, n in desconhecidos.most_common(12):
    print(f"     0x{b:02X}: {n}")
print()
print("=== 2. onde o bytecode das duas ROMs diverge ===")
print("   total:", sum(divergencias.values()))
for nome, n in divergencias.most_common(8):
    print(f"     apos {nome}: {n}")
print()

# --- 3. codigos ainda nao mapeados no charmap BR
d = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
faltam = collections.Counter()
for en, pt in d.values():
    for ch in pt:
        if 0x3000 < ord(ch) < 0xFF00:
            faltam["kana:" + ch] += 1
    import re
    for m in re.finditer(r"<[^>]+>", pt):
        faltam[m.group(0)] += 1
print("=== 3. codigos do charmap BR ainda nao decifrados ===")
print("   distintos:", len(faltam), "| ocorrencias:", sum(faltam.values()))
for c, n in faltam.most_common(10):
    print(f"     {c}: {n}")

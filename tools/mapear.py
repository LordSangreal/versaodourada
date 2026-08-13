"""Alinha texto USA <-> BR pelos sitios de ponteiro e emite o catalogo."""
import sys, json, collections
sys.path.insert(0, r"C:\Users\Usuario\AppData\Local\Temp\claude\D--pokemon-gold-tradu--o\b805f749-d98d-4c24-9526-51b7a6e1a0bb\scratchpad")
from gen2text import decode, is_texty, offset, key

USA = r"D:\pokemon gold tradução\Pokemon - Gold Version (USA, Europe) (SGB Enhanced).gbc"
BR = r"C:\Users\Usuario\AppData\Local\Temp\claude\D--pokemon-gold-tradu--o\b805f749-d98d-4c24-9526-51b7a6e1a0bb\scratchpad\br\Pokemon - Gold Version (BR) (www.romsportugues.com).gbc"

usa = open(USA, "rb").read()
br = open(BR, "rb").read()
N = len(usa)
MIN = 6
# um texto de verdade comeca logo depois de um terminador
STARTERS = {0x50, 0x57, 0x58}


def is_start(rom, tgt):
    return tgt > 0 and rom[tgt - 1] in STARTERS


def try_pair(bank, addr, p_br_addr, p_br_bank):
    """Valida um par (alvo USA, alvo BR). Devolve (chave, en, pt) ou None."""
    tgt = offset(bank, addr)
    if tgt >= N or not is_start(usa, tgt):
        return None
    en, _, ok = decode(usa, tgt, br=False)
    if not ok or len(en) < MIN or not is_texty(en):
        return None
    tgt2 = offset(p_br_bank, p_br_addr)
    if tgt2 >= N or not is_start(br, tgt2):
        return None
    pt, _, ok2 = decode(br, tgt2, br=True)
    if not ok2 or len(pt) < 2 or not is_texty(pt, 2):
        return None
    return key(bank, addr), en, pt


def scan():
    hits = {}
    conflicts = set()
    st = collections.Counter()
    for p in range(0, N - 3):
        bank = p // 0x4000
        a_u = usa[p] | (usa[p + 1] << 8)
        a_b = br[p] | (br[p + 1] << 8)
        if not (0x4000 <= a_u <= 0x7FFF) or not (0x4000 <= a_b <= 0x7FFF):
            continue
        # ponteiro curto: mesmo banco
        cand = []
        if bank:
            cand.append((bank, a_u, a_b, bank, "near"))
        # ponteiro far: terceiro byte e o banco
        fb_u, fb_b = usa[p + 2], br[p + 2]
        if fb_u == fb_b and 0 < fb_u < 128:
            cand.append((fb_u, a_u, a_b, fb_u, "far"))
        for bk, au, ab, bkb, kind in cand:
            r = try_pair(bk, au, ab, bkb)
            if not r:
                continue
            k, en, pt = r
            st[kind] += 1
            if k in hits and hits[k][1] != pt:
                conflicts.add(k)
                continue
            hits[k] = (en, pt)
    for k in conflicts:
        hits.pop(k, None)
    st["conflitos_removidos"] = len(conflicts)
    return hits, st


if __name__ == "__main__":
    hits, st = scan()
    print("sitios:", dict(st))
    print("chaves unicas:", len(hits))
    same = sum(1 for en, pt in hits.values() if en == pt)
    acc = sum(1 for en, pt in hits.values() if any(c in pt for c in "áâãàêíóôõúçéÁÍÂÊÃÕ"))
    print(f"  traduzidos: {len(hits)-same}   iguais ao ingles: {same}   com acento: {acc}")
    json.dump({k: list(v) for k, v in hits.items()},
              open("mapa.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print()
    print("--- amostras ---")
    shown = 0
    for k, (en, pt) in hits.items():
        if en != pt and 12 < len(en) < 45 and any(c in pt for c in "áãçéê"):
            print(f"  [{k}]  EN {en[:52]!r}")
            print(f"          PT {pt[:52]!r}")
            shown += 1
            if shown >= 8:
                break

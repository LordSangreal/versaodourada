"""Diz de qual mapa veio cada fala traduzida, para saber onde testar."""
import os, sys, json, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import walk as W
from gen2text import key as _k

usa, br = W.Rom(W.USA_PATH), W.Rom(W.BR_PATH)
mf = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                   encoding="utf-8"))
# nome do mapa por (grupo, indice)
byids = {(m["group"], m["map"]): name for name, m in mf["maps"].items()}
groups = collections.defaultdict(int)
for m in mf["maps"].values():
    groups[m["group"]] = max(groups[m["group"]], m["map"])

# refaz os pontos de entrada, mapa a mapa, e anda so os daquele mapa
PB, PA = 37, 0x40ED
kept = set(json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8")))
onde = collections.defaultdict(set)

for (group, mi), name in sorted(byids.items(), key=lambda x: x[1]):
    gp = usa.word(PB, PA + (group - 1) * 2)
    if gp is None:
        continue
    entry = gp + (mi - 1) * W.MAP_LENGTH
    ab, aa = usa.byte(PB, entry), usa.word(PB, entry + 3)
    if not ab or not aa or aa < 0x4000:
        continue
    eb = usa.byte(ab, aa + 6)
    sa, ea = usa.word(ab, aa + 7), usa.word(ab, aa + 9)
    if not eb:
        continue
    starts = []
    if sa and sa >= 0x4000:
        n = usa.byte(eb, sa)
        if n is not None and n < 32:
            for si in range(n):
                s = usa.word(eb, sa + 1 + si * 4)
                if W.ok_addr(eb, s):
                    starts.append((eb, s))
    if ea and ea >= 0x4000:
        c = ea + 2
        c += 1 + (usa.byte(eb, c) or 0) * W.WARP_LENGTH
        nc = usa.byte(eb, c) or 0
        c += 1
        for _ in range(nc):
            s = usa.word(eb, c + 4)
            if W.ok_addr(eb, s):
                starts.append((eb, s))
            c += W.COORD_LENGTH
        nb = usa.byte(eb, c) or 0
        c += 1
        for _ in range(nb):
            p = usa.word(eb, c + 3)
            if p and W.ok_addr(eb, p):
                starts.append((eb, p))
            c += W.BG_LENGTH
        no = usa.byte(eb, c) or 0
        c += 1
        for _ in range(no):
            s = usa.word(eb, c + 9)
            if W.ok_addr(eb, s):
                starts.append((eb, s))
            c += W.OBJECT_LENGTH
    out, _ = W.walk(usa, br, starts)
    for k in out:
        if k in kept:
            onde[name].add(k)

EARLY = ["NEW_BARK_TOWN", "ELMS_LAB", "PLAYERS_HOUSE_1F", "PLAYERS_HOUSE_2F",
         "ELMS_HOUSE", "NEW_BARK_TOWN_ELMS_LAB", "CHERRYGROVE_CITY",
         "ROUTE_29", "ROUTE_30", "CHERRYGROVE_POKECENTER_1F",
         "VIOLET_CITY", "VIOLET_POKECENTER_1F"]
print("=== mapas do inicio do jogo ===")
for name in EARLY:
    hits = onde.get(name)
    if hits:
        print(f"  {name:30s} {len(hits)} falas traduzidas")
    elif name in byids.values():
        print(f"  {name:30s} -")
print()
print("=== mapas com mais falas traduzidas ===")
for name, ks in sorted(onde.items(), key=lambda x: -len(x[1]))[:12]:
    print(f"  {name:30s} {len(ks)}")
json.dump({k: sorted(v) for k, v in onde.items()},
          open(os.path.join(HERE, "onde.json"), "w", encoding="utf-8"), indent=0)

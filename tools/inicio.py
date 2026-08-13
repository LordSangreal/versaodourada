"""Cobertura e pontos de teste nos mapas do inicio do jogo."""
import os, sys, json, collections, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import walk as W
import entradas
from gen2text import key as _k

CEDO = ["NEW_BARK_TOWN", "PLAYERS_HOUSE_1F", "ELMS_LAB", "ELMS_HOUSE",
        "ROUTE_29", "CHERRYGROVE_CITY", "ROUTE_30", "ROUTE_31",
        "CHERRYGROVE_POKECENTER_1F", "CHERRYGROVE_MART", "VIOLET_CITY"]

usa, br = W.Rom(W.USA_PATH), W.Rom(W.BR_PATH)
mf = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                    encoding="utf-8"))
maps = mf["maps"]
dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
pub = set(re.findall(r'\["([0-9a-f]{2}:[0-9a-f]{4})"\]',
                     open(os.path.join(HERE, "versaodourada", "lang", "dialogue.lua"),
                          encoding="utf-8").read()))

ACENTOS = "çÇôÔº"

for nome in CEDO:
    m = maps.get(nome)
    if not m:
        continue
    grupos = {m["group"]: m["map"]}
    starts, textos = entradas.coletar(
        usa, br, grupos, somente=(m["group"], m["map"]))
    out, _ = W.walk(usa, br, starts)
    for bank, a_u, a_b in textos:
        W.record(out, collections.Counter(), usa, br, bank, a_u, bank, a_b)
    chaves = [k for k in out if k in pub]
    corrigidas = [(k, out[k][1]) for k in chaves
                  if any(c in out[k][1] for c in ACENTOS)]
    print(f"{nome:28s} {len(chaves):3d} falas no mod"
          f"   {len(corrigidas):2d} com caractere corrigido")
    for k, pt in corrigidas[:2]:
        trecho = pt.replace("\n", " ").replace("\v", " ").replace("\f", " ")
        print(f"       [{k}] {trecho[:58]}")

# -*- coding: utf-8 -*-
"""Quais chaves traduzidas o filtro de launcher NAO conseguiu classificar."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pt

LAN = ("LauncherView", "LauncherSettings", "LauncherMods", "ManagerState",
       "src/update/")
onde = json.load(open("strings_en.json", encoding="utf-8"))["where"]
S, _ = pt.carregar()

sem_origem, so_launcher, compartilhadas, so_jogo = [], [], [], []
for k in S:
    arq = onde.get(k, [])
    if not arq:
        sem_origem.append(k)
    elif all(any(p in a for p in LAN) for a in arq):
        so_launcher.append(k)
    elif any(any(p in a for p in LAN) for a in arq):
        compartilhadas.append(k)
    else:
        so_jogo.append(k)

print("traduzidas:", len(S))
print("  so do jogo        :", len(so_jogo))
print("  so do launcher    :", len(so_launcher), "(o filtro remove)")
print("  compartilhadas    :", len(compartilhadas), "(ficam: o jogo precisa)")
print("  SEM origem no mapa:", len(sem_origem), "(o filtro nao alcanca)")
print()
if sem_origem:
    print("as sem origem:")
    for k in sorted(sem_origem):
        print("   %r" % k)
print()
if compartilhadas:
    print("compartilhadas (aparecem nas duas telas):")
    for k in sorted(compartilhadas):
        print("   %-22r -> %r" % (k, S[k]))

"""Quanto do mod ja e texto nosso, e quanto ainda e derivado.

A atribuicao so pode sair quando `derivadas` chegar a zero.  Este numero
existe para que esse momento seja um fato verificavel, e nao uma impressao.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pt

sistema, nosso_dialogo = pt.carregar()
dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
total_dialogo = len(dial)

nossas = sum(1 for v in nosso_dialogo.values() if v and v.strip())
# quantas falas derivadas sobrevivem aos filtros e nao foram substituidas
publicado = os.path.join(HERE, "versaodourada", "lang", "dialogue.lua")
import re
pub = 0
if os.path.exists(publicado):
    pub = len(re.findall(r'\["[0-9a-f]{2}:[0-9a-f]{4}"\]',
                         open(publicado, encoding="utf-8").read()))
derivadas = max(0, pub - nossas)

barra = lambda n, d: ("#" * int(20 * n / d) + "." * 20).__getitem__(slice(0, 20)) if d else "." * 20

print("=" * 52)
print("  VersaoDourada -- estado da traducao propria")
print("=" * 52)
print()
print("  Texto do motor (menus, batalha, launcher)")
print("    %s  %d traduzidas por nos" % (barra(len(sistema), 647), len(sistema)))
print("    de 647 chaves.  Todas nossas por natureza: a chave e a string")
print("    em ingles do motor, nao texto de ROM.")
print()
print("  Dialogo do jogo")
print("    %s  %d de %d falas nossas" % (barra(nossas, total_dialogo), nossas, total_dialogo))
print("    publicadas agora: %d  (nossas %d + derivadas %d)" % (pub, nossas, derivadas))
print()
if derivadas:
    print("  ATRIBUICAO: obrigatoria.  Ainda ha %d falas derivadas" % derivadas)
    print("  da traducao de R_Lopes e Night_Shadown no pacote.")
else:
    print("  ATRIBUICAO: pode virar agradecimento.  Nenhuma fala derivada")
    print("  no pacote.")
print()

# -*- coding: utf-8 -*-
"""Ultimos ajustes do lote 1: largura da ultima linha e duas concordancias.

Encurtar frase a martelo quebra gramatica: na rodada anterior eu troquei
"grande descoberta" por "grande achado" deixando o "uma" antes, e cortei
"roubado" para caber deixando "tinha roubou".  Aqui os dois saem junto com
as quatro linhas que ainda colidiam com a seta.
"""
import io, re

P = "pt/dialogo_01.py"

FIX = {
    # ultima linha de pagina: 17 colunas, a seta ocupa a 18a
    "60:43f7": "ELM: {PLAYER}!\nAí está você!\fPreciso lhe pedir\num favor.\fTenho um conhecido\nchamado MR.\vPOKéMON.\fEle vive achando\ncoisas estranhas\fe se gabando das\ndescobertas.\fEnfim, recebi um\ne-mail dele agora\fdizendo que desta\nvez é de verdade.\fÉ intrigante, mas\nestamos ocupados\fcom nossa pesquisa\nde POKéMON.\fVocê poderia ir\nver isso por nós?\fVou lhe dar um\nPOKéMON de\vparceiro.\fSão todos POKéMON\nraros que acabamos\vde encontrar.\fEscolha um deles!",
    "60:4590": "Se um POKéMON\nselvagem aparecer,\vdeixe o seu lutar",
    "60:463a": "ELM: Então gosta\nda CHIKORITA, a\vPOKéMON planta?",
    # concordancia: "um achado", nao "uma achado"
    "60:48fb": "Mas… Será um OVO\nde POKéMON?\fSe for, é um\ngrande achado!",
    # concordancia: "tinha roubou" nao existe
    "60:5146": "Houve um barulho\nalto lá fora…\fQuando fomos ver,\nroubaram um\vPOKéMON daqui.\fÉ inacreditável\nque alguém faça\visso!\f…ai… Aquele\nPOKéMON roubado.\fFico pensando como\nele está.\fDizem que POKéMON\ncriado por gente\fruim fica ruim\ntambém.",
}


def lua(t):
    return ('"' + t.replace("\\", "\\\\").replace('"', '\\"')
                   .replace("\n", "\\n").replace("\v", "\\v")
                   .replace("\f", "\\f") + '"')


s = io.open(P, encoding="utf-8").read()
n = 0
for k, novo in FIX.items():
    pat = re.compile(r'^(\s*)"%s": ".*",$' % re.escape(k), re.M)
    if not pat.search(s):
        print("NAO ACHOU", k)
        continue
    s = pat.sub(lambda m, kk=k, nn=novo: '%s"%s": %s,' % (m.group(1), kk, lua(nn)), s)
    n += 1
io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("corrigidas:", n, "de", len(FIX))

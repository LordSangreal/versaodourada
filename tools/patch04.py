# -*- coding: utf-8 -*-
"""Correcoes do lote 4: largura da ultima linha e sequencias de controle.

Foram 32 problemas contra 0 nos lotes 2 e 3.  A diferenca nao foi a
ferramenta, foi eu ter escrito rapido demais tentando cobrir mais chao.
"""
import io, re

P = "pt/dialogo_04.py"

FIX = {
 "44:5b06": "KURT: Olá aí,\n{PLAYER}!\fOs guardas lá em\ncima fugiram\vquando eu gritei.\fMas aí eu caí\npoço abaixo\vaqui.\fBati as costas\ncom força e agora\vnão consigo andar\fDroga! Se eu\nestivesse bem, o\fPOKéMON teria dado\no troco…\fAh, não tem\njeito.\f{PLAYER}, mostre a\neles a sua coragem\vno meu lugar!",
 "45:6b81": "Ah! O FARFETCH'D!\fVocê achou ele\npara nós, garoto?\fSem ele, a gente\nnão conseguiria\fusar CUT para\nfazer carvão.\fObrigado, garoto!\fComo posso\nagradecer…\fJá sei! Tome,\nfique com isto.",
 "45:6c29": "É o HM de CUT.\nEnsine a um\fPOKéMON para\ncortar arvoretas.\fClaro, você\nprecisa da BADGE\fdo GINÁSIO de\nAZALEA para usar.",
 "45:6ca8": "Quer virar meu\naprendiz\fde carvoeiro\ncomigo?\fEm dez anos você\nestará craque!",
 "45:6d03": "O que eu faço?\fSacudo árvores\ncom HEADBUTT.\fÉ divertido. Tente\nvocê também!",
 "48:51e7": "…Me diga uma\ncoisa.\fÉ verdade que a\nTEAM ROCKET\vvoltou?\fO quê? Você\nvenceu? Hah! Pare\vde mentir.\fNão brinca?\nEntão vamos ver o\vquanto você vale.",
 "48:52cd": "Odeio os fracos.\fPOKéMON, treinado-\nres. Não importa\vquem nem o quê.\fVou ficar forte e\nvarrer os fracos\vdo mapa.\fIsso vale para\na TEAM ROCKET.\fEles se acham em\nbando.\fMas sozinhos,\neles são\vfracos.\fOdeio todos eles.\fFique fora do meu\ncaminho. Um fraco\fcomo você só\natrapalha.",
 "48:5461": "Conhece a\nSLOWPOKETAIL?\vDizem que é boa!\fNão está feliz de\neu ter contado?",
 "48:54b5": "Os SLOWPOKE\nsumiram da\vcidade…\fOuvi que as TAILS\ndeles estão à\vvenda por aí.",
 "48:55b4": "Corte por AZALEA\ne você chega à\vILEX FOREST.\fMas essas árvores\nfinas tornam\fimpossível\npassar.\fO POKéMON do\nCARVOEIRO usa CUT\vnas árvores.",
 "48:5706": "SLOWPOKE WELL\fTambém chamado de\nPOÇO DA CHUVA.\fO povo daqui crê\nque o bocejo do\vSLOWPOKE dá chuva\fConsta que um\nbocejo dele\fpôs fim a uma seca\nhá 400 anos.",
 "55:4092": "Você conhece os\nAPRICORNS?\fAbra um, esvazie\npor dentro e põe\fum aparelho\nespecial.\fAí dá para pegar\nPOKéMON com ele.\fAntes das POKé\nBALLS existirem,\ftodo mundo usava\nAPRICORNS.",
 "55:47ee": "Hm? Quem é você?\f{PLAYER}, é? Quer\nque eu faça umas\vBALLS?\fDesculpe, mas isso\nvai esperar.\fConhece a TEAM\nROCKET? Ah, não\fimporta. Eu conto\nde qualquer forma\fA TEAM ROCKET é\numa gangue má que\fusa POKéMON para\no trabalho sujo.\fEra para eles\nterem se desfeito\vhá três anos.\fEnfim, estão no\nPOÇO, cortando\fSLOWPOKETAILS para\nvender!\fEntão eu vou lá\ndar uma lição\vdolorosa neles!\fAguente firme,\nSLOWPOKE! O velho\vKURT está indo!",
 "55:4990": "KURT: Oi!\fVocê se saiu\ncomo um herói\vno POÇO.\fGostei do estilo!\fSeria uma honra\nfazer BALLS\fpara um treinador\ncomo você.\fÉ tudo que tenho\nagora, mas leve.",
 "55:4a44": "KURT: Eu faço\nBALLS de APRICORN\fColha eles das\nárvores e traga\vaqui.\fEu faço BALLS\ncom eles.",
 "55:4ab1": "KURT: Tem um\nAPRICORN para mim\fÓtimo! Vou virar\nele numa BALL.",
 "55:4af4": "KURT: Vai levar um\ndia para a BALL.\fVolte depois\npara pegar.",
 "55:4b53": "KURT: Trabalhando!\nNão me amole!",
 "55:4c1a": "O vovô saiu…\nQue solidão…",
 "55:4c38": "O SLOWPOKE que meu\npai deu voltou!\fA TAIL dele está\ncrescendo!",
 "55:4c7e": "Meu pai trabalha\nna SILPH, onde ele\vestuda POKé BALL.\fEu fico em casa\ncom o vovô e o\vSLOWPOKE.",
 "55:53fc": "Ei, desafiante!\fO BUGSY é jovem,\nmas sabe muito\fde POKéMON inseto\nde verdade.\fVai ser difícil\nsem o meu\vconselho.\fVejamos… POKéMON\ninseto não gostam\vde fogo.\fGolpes voadores\ntambém são super\vefetivos.",
 "55:54bf": "Muito bem! Foi um\nbelo confronto\fentre jovens\ntalentosos.\fCom gente como\nvocê, o futuro dos\vPOKéMON é lindo!",
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

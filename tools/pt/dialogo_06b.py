# -*- coding: utf-8 -*-
"""Lote 6b -- OLIVINE CITY, o GINASIO da JASMINE, o LIGHTHOUSE, CIANWOOD
CITY e o GINASIO do CHUCK.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Escrito contra a saida de tools/esqueleto.py, que imprime pagina, linha,
separador e limite de coluna do ingles.  Foi o que eliminou o erro de ler
um \\f como \\v, unico defeito do lote 6a.

Ficam de fora kana solto, fragmentos de TX_FAR e a chave "Object event.",
que e sobra de depuracao.

Ficam no original: JASMINE, CHUCK, LIGHTHOUSE, GLITTER, FAST SHIP,
MINERALBADGE, STORMBADGE, IRON TAIL, DYNAMICPUNCH, ROCK SMASH, FLY,
LEAGUE, POKéGEAR, POKéDEX, DEFENSE, e os nomes de cidade.
"""

DIALOGO = {
    # ---------------- Olivine City ----------------
    "49:40d7": "…\fVocê de novo?\fNão precisa entrar\nem pânico. Eu não\fperco tempo com\nbananas como você\fFalando em fracos,\na LÍDER daqui\fdo GINÁSIO não\nestá aqui.\fDizem que está\ncuidando de um\fPOKéMON doente no\nLIGHTHOUSE.\fHunf! Bu-hu-hu!\nÉ só largar os\vPOKéMON doentes!\fUm POKéMON que não\npode batalhar não\vvale nada!\fPor que você não\nvai treinar no\vLIGHTHOUSE?\fVai que. Talvez te\ndeixe um pouco\vmenos fraco!",
    "49:4235": "Estradas escuras\nsão perigosas\vde noite.\fMas na escuridão\ntotal da noite,\fo mar é ainda\nmais traiçoeiro!\fSem a luz do farol\ndo LIGHTHOUSE\fpara guiar, navio\nnenhum navega.",
    "49:42e1": "Essa coisa que\nvocê tem, é uma\vPOKéGEAR, né? Uau,\vque legal.",
    "49:431e": "Uau, você tem uma\nPOKéDEX!\fIsso é simplesmen-\nte demais.",
    "49:434e": "Olá, rapazinho!\nO mar é doce!\fCante comigo!\nEi-ô! Puxa a corda\vcom força!…",
    "49:439a": "OLIVINE CITY\fO Porto Mais Perto\nde Outras Terras",
    "49:43ca": "OLIVINE PORT\nPÍER DO FAST SHIP",
    "49:43e7": "OLIVINE CITY\nGINÁSIO POKéMON\vLÍDER: JASMINE\fA Garota Blindada\nda Defesa",
    "49:442a": "OLIVINE LIGHTHOUSE\nTambém Conhecido\vpor GLITTER",

    # ---------------- Ginasio da JASMINE ----------------
    "51:419a": "…Obrigada pela\nsua ajuda no\vLIGHTHOUSE…\fMas isto é dife-\nrente. Por favor,\fpermita que eu me\napresente.\fSou JASMINE, LÍDER\nde GINÁSIO. Eu uso\vo tipo aço.\f…Você conhece o\ntipo aço?\fÉ um tipo que foi\ndescoberto há\vbem pouco tempo.\f…Hum… Começamos?",
    "51:429c": "…Você é melhor\ntreinador que eu,\ftanto em técnica\nquanto em bondade\fDe acordo com as\nregras da LEAGUE,\feu lhe concedo\nesta BADGE.",
    "51:431b": "{PLAYER} recebeu\na MINERALBADGE.",
    "51:4335": "A MINERALBADGE\naumenta a DEFENSE\vdo POKéMON.\f…Hum… Pegue isto\ntambém…",
    "51:4386": "…Você pode usar\nessa TM para\vensinar IRON TAIL",
    "51:43b2": "Hum… Não sei bem\ncomo dizer isto,\vmas boa sorte…",
    "51:43e3": "A JASMINE usa o\ntipo aço, que é\vbem recente.\fEu não sei quase\nnada sobre ele.",
    "51:4432": "Aquilo foi demais\fEntão o tipo aço,\nhein?\fFoi um encontro\nimediato de tipo\vdesconhecido!",
    "51:4489": "A JASMINE, LÍDER\ndo GINÁSIO, está\vno LIGHTHOUSE.\fEla cuida de um\nPOKéMON doente.\fUm treinador forte\nprecisa ter com-\vpaixão.",

    # ---------------- Olivine Lighthouse ----------------
    "44:62c5": "As pessoas treinam\nneste LIGHTHOUSE.\fNão é fácil subir\npor causa de todos\vos treinadores.",
    "44:631a": "Antigamente, POKé-\nMON iluminavam\fo mar em volta de\nOLIVINE à noite.\fO LIGHTHOUSE foi\nfeito em honra a\vesses POKéMON.",

    # ---------------- Cianwood City ----------------
    "48:5936": "Você atravessou o\nmar para chegar?\fDeve ter sido\nbem difícil.\fSeria bem mais\nfácil se o seu\fPOKéMON soubesse\nusar FLY…",
    "48:59a8": "Mas não dá para\nusar FLY sem a\vBADGE daqui.\fSe vencer o LÍDER\ndo GINÁSIO daqui,\vvenha me ver.\fVou ter um belo\npresente pra você",
    "48:5a28": "Essa é a BADGE do\nGINÁSIO daqui!\fEntão você deve\nlevar este HM.",
    "48:5a62": "Ensine FLY ao seu\nPOKéMON.\fVocê vai poder\nvoar na hora\fpara qualquer lu-\ngar já visitado.",
    "48:5abc": "Meu marido perdeu\npara você, então\vtem que treinar.\fAinda bem, porque\nele estava ficando\vmeio gordinho.",
    "48:5b24": "Se usar o FLY,\ndá para voltar\fpara OLIVINE na\nhora.",
    "48:5b5e": "As pedras ao norte\nda cidade podem\vser quebradas.\fElas podem estar\nescondendo algo.\fSeu POKéMON pode\nusar ROCK SMASH\vpara quebrar.",
    "48:5bd9": "O CHUCK, LÍDER do\nGINÁSIO, treina\fcom os POKéMON\nlutadores dele.",
    "48:5c78": "CIANWOOD CITY\fUm Porto Cercado\npor Mares Bravios",
    "48:5ca7": "CIANWOOD CITY\nGINÁSIO POKéMON\fLÍDER: CHUCK\fQuem Fala São os\nPunhos Dele",
    "48:5cee": "500 Anos de\nTradição\fCIANWOOD CITY\nFARMÁCIA\fTire Suas Dúvidas\nsobre Remédios",
    "48:5d3d": "CIANWOOD CITY\nESTÚDIO DE FOTO\fTire um Retrato\nde Lembrança!",

    # ---------------- Ginasio do CHUCK ----------------
    "5d:53ee": "UAHAHAH!\fEntão você chegou\naté aqui!\fVou te avisar:\neu sou durão!\fMeus POKéMON vão\nesmagar pedras e\vquebrar ossos!\fOlhe só isto!",
    "5d:5464": "CHUCK: Urggh!\n…\fOoooarrgh!",
    "5d:547f": "Pronto! Com medo\nagora, hein?\fO quê?\nNão tem nada\fa ver com POKéMON?\nÉ verdade!\fVamos lá. Nós dois\nvamos batalhar!",
    "5d:54eb": "Hã? Quê?\nEu perdi?\fVeja só isso!\nVocê merece a\vSTORMBADGE!",
    "5d:552a": "{PLAYER} recebeu\na STORMBADGE.",
    "5d:5542": "A STORMBADGE faz\ntodo POKéMON até\fo L70 obedecer,\naté os trocados.\fEla também deixa\nseu POKéMON usar\fFLY fora da\nbatalha.\fTome, fique com\nisto também!",
    "5d:55cf": "Isso é o DYNAMIC-\nPUNCH.\fEle nem sempre\nacerta, mas quan-\fdo acerta, causa\nconfusão!",
    "5d:5625": "UAHAHAH! Adorei\nbatalhar com você\fMas derrota é\nderrota!\fDe agora em diante\nvou treinar 24\vhoras por dia!",
}

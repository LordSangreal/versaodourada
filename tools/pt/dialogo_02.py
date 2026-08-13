# -*- coding: utf-8 -*-
"""Lote 2 -- Rota 29, Cherrygrove City, Rota 30.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Regras verificadas por tools/conferir.py:
  1. `\\n`, `\\v` e `\\f` na MESMA ordem e quantidade que o ingles.
  2. Tokens idem.
  3. 18 colunas por linha -- e 17 na ULTIMA linha de cada pagina, porque a
     seta de "aperte A" ocupa a coluna 18.

Cinco chaves deste trecho ficaram de fora: sao lixo do extrator (kana solto
ou fragmento que comeca no meio de outra fala), nao texto de jogo.

Ficam no original: TUSCANY, MONICA, WESLEY, FALKNER, RATTATA, os nomes de
cidade e rota, PINK BOW, MYSTIC WATER, ANTIDOTE, POKé BALLS.
"""

DIALOGO = {
    # ---------------- Cherrygrove City ----------------
    "48:45ae": "Você é um\ntreinador novato,\vné? Dá para ver!\fTudo bem! Todo\nmundo já foi\vnovato um dia!\fSe quiser, posso\nte ensinar umas\vcoisas.",
    "48:463a": "Certo, então!\nMe siga!",
    "48:4650": "Este é um CENTRO\nPOKéMON. Curam\fseu POKéMON num\ninstante.\fVocê vai depender\nmuito deles,\fé bom aprender\nsobre eles.",
    "48:46cf": "Esta é uma LOJA\nPOKéMON.\fVendem BALLS para\npegar POKéMON\fselvagens e outros\nitens úteis.",
    "48:4724": "A ROUTE 30 fica\npor aqui.\fTreinadores lutam\ncom seus POKéMON\fpreferidos lá.\nVale ver.",
    "48:4772": "Este é o mar,\ncomo você vê.\fAlguns POKéMON só\nsão achados\vna água.",
    "48:47b7": "Aqui…\fÉ a minha casa!\nObrigado pela\vcompanhia.\fDeixe eu lhe dar\num presentinho.",
    "48:4803": "A POKéGEAR de\n{PLAYER} tem MAPA!",
    "48:481c": "A POKéGEAR fica\nmais útil quando\vvocê põe CARDS.\fBoa sorte na sua\njornada!",
    "48:48ad": "…\fVocê pegou um\nPOKéMON no LAB.\fQue desperdício.\nUm fraco desses.\f…\fNão entendeu o\nque eu disse?\fPois eu tenho um\nPOKéMON bom.\fVou te mostrar\no que eu digo!",
    "48:4942": "Hunf. Feliz por\nter ganhado?",
    "48:4961": "…\fMeu nome é ???.\fEu vou ser o\nmelhor treinador\vPOKéMON do\vmundo.",
    "48:49a5": "Hunf. Isso foi\nperda de tempo.",
    "48:49c7": "…\fMeu nome é ???.\fEu vou ser o\nmelhor treinador\vPOKéMON do\vmundo.",
    "48:4a0b": "Você falou com o\nvelho perto do\vCENTRO POKéMON?\fEle põe um MAPA de\nJOHTO na sua\vPOKéGEAR.",
    "48:4a63": "Com POKéMON por\nperto, qualquer\vlugar é bom.",
    "48:4a91": "A casa do\nMR.POKéMON fica\vmais adiante.",
    "48:4abc": "Eu lutei com os\ntreinadores da\vestrada.\fMeus POKéMON\nperderam feio!\fPreciso levar eles\nao CENTRO POKéMON",
    "48:4b21": "Um POKéMON que eu\npeguei tinha algo\fAcho que é\nMYSTIC WATER.\fNão preciso dele,\nvocê quer?",
    "48:4b7c": "Volto a pescar,\nentão.",
    "48:4b9b": "CHERRYGROVE CITY\fA cidade das\nflores perfumadas",
    "48:4bd0": "CASA DO GUIA",

    # ---------------- Rota 29 ----------------
    "4a:4ed2": "POKéMON se\nescondem no mato.\fNunca se sabe\nquando saltam…",
    "4a:4f0a": "Já te vi umas\nvezes. Quantos\fPOKéMON você já\npegou?\fQuer que eu mostre\ncomo pegar\vPOKéMON?",
    "4a:4f78": "É assim que se\nfaz.\fSe enfraquecer\nantes, o POKéMON\vé mais fácil.",
    "4a:4fc2": "Ah. Tudo bem.\fEnfim, se quer\npegar POKéMON,\fvocê tem que\nandar bastante.",
    "4a:500e": "Hã? Quer que eu\nmostre como\vpegar POKéMON?",
    "4a:503f": "E aí. Como estão\nseus POKéMON?\fSe estão fracos\ne sem preparo,\ffique fora do\nmato.",
    "4a:5097": "Viu aqueles\nbarrancos? Dá medo\vpular deles.\fMas dá para ir a\nNEW BARK sem\fpassar pelo\nmato.",
    "4a:5104": "Quis dar uma\npausa, e salvei\fpara guardar meu\nprogresso.",
    "4a:5177": "Estou esperando\nPOKéMON que\fsó aparecem à\nnoite.",
    "4a:51a7": "Estou esperando\nPOKéMON que\fsó aparecem de\nmanhã.",
    "4a:51dd": "TUSCANY: Creio eu\nque esta é a\fprimeira vez que\nnos vemos?\fPermita-me que eu\nme apresente.\fSou TUSCANY, de\nterça-feira.",
    "4a:525a": "Como apresentação,\naceite este\fpresente, um\nPINK BOW.",
    "4a:529a": "TUSCANY: Não acha\nque ele é mesmo\vadorável?\fEle fortalece\nataques normais.\fTenho certeza que\nserá útil.",
    "4a:5312": "TUSCANY: Conhece\nMONICA, minha\virmã mais velha?\fOu meu irmão\ncaçula, WESLEY?\fSou a segunda de\nsete filhos.",
    "4a:5384": "TUSCANY: Hoje não\né terça-feira.\vQue pena…",
    "4a:53b9": "ROUTE 29\fCHERRYGROVE CITY -\nNEW BARK TOWN",
    "4a:53e4": "ROUTE 29\fCHERRYGROVE CITY -\nNEW BARK TOWN",

    # ---------------- Rota 30 ----------------
    "4a:4955": " Eu só\nqueria falar\valgo legal.",
    "4a:55ad": "Vai, RATTATA!\fTACKLE!",
    "4a:55c3": "O quê? Esta é uma\nbatalha séria!\vMe deixe em paz!",
    "4a:57f0": "A casa do\nMR.POKéMON? Fica\vum pouco adiante.",
    "4a:581a": "Todo mundo se\ndiverte lutando!\vFaça o mesmo!",
    "4a:584a": "Não sou treinador\fMas se olhar nos\nolhos de um,\vprepare-se.",
    "4a:5891": "ROUTE 30\fVIOLET CITY -\nCHERRYGROVE CITY",
    "4a:58ba": "CASA DO MR.POKéMON\nEm frente!",
    "4a:58db": "LAR DE MR.POKéMON",
    "4a:58ec": "DICA AO TREINADOR\fNão roube POKéMON\ndos outros!\fPOKé BALLS só se\njogam em POKéMON\vselvagens!",

    # ---------------- Loja de Cherrygrove ----------------
    "62:402c": "Acabaram as\nPOKé BALLS!\fQuando será que\nchegam mais?",
    "62:406b": "Tem POKé BALLS em\nestoque! Agora\vposso pegar!",
    "62:4098": "Quando eu andava\nno mato, um\fPOKéMON inseto\nenvenenou o meu!\fEu segui andando,\nmas aí o meu\vPOKéMON desmaiou.\fÉ bom andar com um\nANTIDOTE.",

    # ---------------- Centro Pokemon de Cherrygrove ----------------
    "62:4182": "É ótimo. Dá para\nguardar quantos\fPOKéMON quiser, e\ntudo de graça.",
    "62:41c0": "Aquele PC é livre\npara qualquer\vtreinador usar.",
    "62:41e9": "O CENTRO DE\nCOMUNICAÇÃO lá em\vcima é novinho.\fMas ainda estão\nterminando ele.",
    "62:423e": "O CENTRO DE\nCOMUNICAÇÃO lá em\vcima é novinho.\fJá troquei POKéMON\nlá!",
}

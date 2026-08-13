# -*- coding: utf-8 -*-
"""Lote 6a -- ECRUTEAK CITY, o GINASIO do MORTY, BURNED TOWER, TIN TOWER
e as rotas 38 e 39.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Ficam de fora as chaves de kana solto, os fragmentos de TX_FAR e as falas
que sao so nome proprio ("ROUTE 38 / OLIVINE CITY - ECRUTEAK CITY",
"MILTANK: Mooo!", "ECRUTEAK DANCE THEATER"): traduzi-las daria o mesmo
texto e so infla o catalogo.

Regras verificadas por tools/conferir.py: sequencia de \\n \\v \\f identica,
tokens preservados, 18 colunas -- 17 na ultima linha de cada pagina.

Ficam no original: MORTY, KIMONO GIRLS, DANCE THEATER, TIN TOWER, BURNED
TOWER, OLIVINE LIGHTHOUSE, LAKE OF RAGE, FOGBADGE, SURF, SHADOW BALL,
SPCL.DEF, RAINBOW WING, HEADBUTT, MOOMOO FARM, TRAINER TIPS.
"""

DIALOGO = {
    # ---------------- Ecruteak City ----------------
    "49:4604": "ECRUTEAK já teve\nduas torres:\fuma a leste e\noutra a oeste.",
    "49:4646": "Ah, jovem.\nVocê aprendeu\fa dançar como as\nKIMONO GIRLS?\fSe for ao DANCE\nTHEATER delas, um\fvelhinho esquisito\ndá algo bacana\vpara você, ouvi.",
    "49:46de": "Vou treinar lá no\nDANCE THEATER.\fQuer vir junto\ncomigo?",
    "49:471d": "Aquela torre era\nbem mais alta,\fmas pegou fogo e\nacabou queimada.",
    "49:4761": "Três POKéMON gran-\ndes fugiram cada\vum para um lado.\vO que eram eles?",
    "49:47a4": "Ouvi um boato\nsobre o OLIVINE\vLIGHTHOUSE.\fO POKéMON que\nserve de farol\fficou doente.\nParece que estão\vcom problemas.",
    "49:481d": "O POKéMON do\nOLIVINE LIGHTHOUSE\vfoi curado.\fOs barcos já podem\nsair ao mar de\vnoite em paz.",
    "49:487e": "Ouvi que POKéMON\nestão em fúria no\fLAKE OF RAGE. Eu\nqueria ver isso.",
    "49:48c3": "ECRUTEAK CITY\nCidade Histórica\fOnde o Passado\nEncontra o Hoje",
    "49:4905": "TIN TOWER\fDizem que um POKé-\nMON lendário pousa\vaqui.",
    "49:493a": "ECRUTEAK CITY\nGINÁSIO POKéMON\vLÍDER: MORTY\fO Vidente Místico\ndo Futuro",
    "49:4996": "BURNED TOWER\fFoi destruída por\num incêndio\vmisterioso.\fFique longe, pois\nnão é seguro.",

    # ---------------- Ginasio do MORTY ----------------
    "52:516b": "Que bom que você\nveio.\fAqui em ECRUTEAK,\nos POKéMON sempre\vforam venerados.\fDizem que POKéMON\nlendários surgem\fpara os treinado-\nres realmente\vpoderosos.\fEu acreditei\nnisso, e por isso\ftreinei aqui em\nsegredo sempre.\fCom isso, hoje eu\nvejo o que outros\vnão veem.\fSó mais um pouco…\fCom um pouco mais,\neu poderia ver\fum futuro em que\neu encontro o\vPOKéMON lendário.\fVocê vai me ajudar\na chegar nesse\vnível!",
    "52:52f4": "Ainda não sou bom\no bastante…\fTudo bem. Esta\nBADGE é sua.",
    "52:532d": "{PLAYER} recebeu\na FOGBADGE.",
    "52:5343": "Com a FOGBADGE,\nPOKéMON até o L50\fvão obedecer\nvocê.\fPOKéMON que sabem\nSURF também podem\fusar o golpe a\nqualquer hora.\fQuero que fique\ncom isto também.",
    "52:53d6": "É o SHADOW BALL.\nCausa dano e pode\freduzir a\nSPCL.DEF.\fUse se ele te\nagradar.",
    "52:542f": "Entendo…\fSua jornada levou\nvocê a lugares\vbem distantes.\fE você testemunhou\nmuito mais coisas\vdo que eu.\fEu invejo você\npor isso…",
    "52:56d2": "Os treinadores\ndaqui têm motivos\vsecretos.\fSe você vencer,\neles podem contar\fsegredos profundos\nde ECRUTEAK.",
    "52:573c": "Ufa, {PLAYER}.\nVocê foi ótimo!\fEu estava encolhi-\ndo no canto de\vpuro terror!",

    # ---------------- Burned Tower ----------------
    "42:4f24": "…… …… ……\f…Ah, é você.\fVocê queria ficar\nmais forte, então\fveio atrás do\nPOKéMON lendário\fque dizem estar\naqui. É essa a sua\vhistória, né?\fPois isso não vai\nacontecer.\fPorque eu vou\npegar ele!\fEu vou ser o maior\ntreinador do mun-\vdo, então um\vPOKéMON lendário\vseria perfeito\vpara mim.\f…Enfim, tanto faz\nJá estou cansado\fde ter um banana\ncomo você sempre\vaparecendo.",
    "42:5093": "…Hunf!\fÉ por isso que eu\nodeio lutar com\fbananas. Não tem\ndesafio nenhum.",
    "42:50da": "…Ah, tanto faz.\fVocê nunca ia\nconseguir pegar\fPOKéMON lendário\nmesmo.",
    "42:5124": "…Hunf!\fÉ por isso que eu\nodeio lutar com\fbananas. É só\nperda de tempo.",
    "42:516d": "Ei, estou treinan-\ndo aqui escondido\fNão me constranja\nficando olhando!",
    "42:51ac": "Queimei até virar\ncinzas brancas…",
    "42:51cb": "Eu estava tão con-\ncentrado que\facabei caindo\nneste buraco.",

    # ---------------- Tin Tower ----------------
    "42:4b20": "Tento descobrir o\nsegredo do\fPOKéMON lendário\nque dizem pousar\vaqui.\fContam que esse\nPOKéMON voa sem\fparar desde que a\nTORRE do Oeste\vpegou fogo.\fEntão pensei: se\neu tivesse o que\fesse POKéMON tem,\nele seria atraído\vpelo item.\fAcho que esse item\ndeve ser…\fUma RAINBOW WING!\fMas onde eu acho\numa dessas?",

    # ---------------- Rota 38 ----------------
    "4c:48d9": "TRAINER TIPS\fSe um POKéMON está\ntentando evoluir,\vdá para impedir.\fAperte o Botão B\ndurante a evolu-\vção.\fIsso assusta o\nPOKéMON e para a\vevolução dele.",

    # ---------------- Rota 39 ----------------
    "4c:4d81": "MOOMOO FARM\fProve Nosso Leite\nFresco e Saboroso",
    "4c:4dad": "TRAINER TIPS\fUse HEADBUTT nas\nárvores para der-\vrubar POKéMON.\fTipos diferentes\nde POKéMON caem\vdas árvores.\fUse HEADBUTT em\ntoda árvore!",
}

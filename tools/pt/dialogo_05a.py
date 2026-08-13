# -*- coding: utf-8 -*-
"""Lote 5a -- Goldenrod City, o GINASIO da WHITNEY e a DEPT.STORE.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Goldenrod tem 126 falas ao todo, o dobro de qualquer lote anterior.  Esta
metade cobre a cidade, o ginasio e a loja; a torre de radio, as rotas e o
parque ficam para o 5b.  Dividir foi decisao deliberada: o lote 4 saiu com
32 erros justamente por eu ter tentado cobrir chao demais de uma vez.

Regras verificadas por tools/conferir.py: sequencia de \\n \\v \\f identica,
tokens preservados, 18 colunas -- 17 na ultima linha de cada pagina.

Ficam no original: WHITNEY, PLAINBADGE, ATTRACT, STRENGTH, TEAM ROCKET,
RADIO TOWER, DEPT.STORE, GAME CORNER, BIKE SHOP, NAME RATER, POKéGEAR.
"""

DIALOGO = {
    # ---------------- Goldenrod City ----------------
    "48:5ec6": "Construíram a nova\nRADIO TOWER para\ftrocar a velha,\nque rangia.",
    "48:5f06": "Sei que tem uma\nBIKE SHOP nova,\fmas não acho ela\nem lugar nenhum.",
    "48:5f43": "Aquele homem de\npreto se veste\fcomo a TEAM ROCKET\nQue bobagem!",
    "48:5f8a": "Aquele de preto\nera mesmo da\fTEAM ROCKET? Não\nacredito nisso!",
    "48:5fd0": "A RADIO TOWER de\nGOLDENROD CITY é\vum cartão-postal.\fEstão com uma\npromoção\vrolando agora.\fEles modificam\na sua POKéGEAR,\fpara ela virar\num rádio também.",
    "48:6071": "Oh, sua POKéGEAR\ntoca rádio agora!",
    "48:6093": "E-he-he-he…\fLevei bronca\npor brincar no\fsubsolo da\nDEPT.STORE.",
    "48:60e0": "O homem daquela\ncasa avalia os\vnomes que você dá\fEle até renomeia\no seu POKéMON.",
    "48:612c": "Ufa! Esta cidade\né grande. Não sei\fonde fica\nnada.",
    "48:616a": "Então esta é a\nRADIO TOWER…",
    "48:6187": "O que você quer,\npentelho? Some!",
    "48:61ab": "Saia do caminho!\nCai fora!",
    "48:61ca": "Tomar a RADIO\nTOWER…\fO quê? Não é da\nsua conta!",
    "48:6207": "POKéMON? Não são\nnada além de\fferramentas para\nganhar dinheiro!",
    "48:623f": "Nosso sonho logo\nvai se realizar…\fFoi uma luta tão\nlonga…",
    "48:627c": "Ei, pirralho! Você\nnão é daqui!\vSuma!",
    "48:62a8": "Venha provar o\nverdadeiro terror\vda TEAM ROCKET!",
    "48:62d4": "GOLDENROD CITY\nESTAÇÃO",
    "48:62ec": "GOLDENROD CITY\nRADIO TOWER",
    "48:6308": "Tudo em produtos\nPOKéMON!\fGOLDENROD CITY\nDEPT.STORE",
    "48:6341": "GOLDENROD CITY\nGINÁSIO POKéMON\vLÍDER: WHITNEY\fA garota\nlinda demais!",
    "48:6386": "GOLDENROD CITY\fA cidade festiva\nde muito charme",
    "48:63b8": "O mundo é uma\nciclovia!\vBIKE SHOP",
    "48:63de": "Seu parquinho!\fGOLDENROD CITY\nGAME CORNER",
    "48:640b": "NAME RATER\fAvalie os apelidos\ndos seus POKéMON",
    "48:6435": "ENTRADA DO\nSUBTERRÂNEO",
    "48:644b": "ENTRADA DO\nSUBTERRÂNEO",

    # ---------------- Ginasio da WHITNEY ----------------
    "57:4122": "Oi! Sou WHITNEY!\fTodo mundo curtia\nPOKéMON, então eu\ventrei também!\fPOKéMON são\nfofos demais!\fQuer batalhar?\nEstou avisando,\veu sou boa!",
    "57:41a5": "Snif…\f…Buááááá!\nVocê é mau!\fNão devia levar\ntão a sério! Você,\vvocê, criança!",
    "57:41f5": "Buááááá!\fBuááááá!\f…Funga, soluço…\n…Seu malvado!",
    "57:4223": "…Snif…\fO quê? O que você\nquer? Uma BADGE?\fAh, é. Eu tinha\nesquecido. Tome a\vPLAINBADGE.",
    "57:4278": "{PLAYER} recebeu\na PLAINBADGE.",
    "57:4290": "A PLAINBADGE deixa\nseu POKéMON usar\fSTRENGTH fora da\nbatalha.\fEla também aumenta\na VELOCIDADE do\vseu POKéMON.\fAh, pode ficar\ncom isto também!",
    "57:4307": "É o ATTRACT!\nEle usa todo o\fcharme de um\nPOKéMON.\fNão é perfeito\npara uma fofa\vcomo eu?",
    "57:4365": "Ah, chorei bem!\nQue alívio!\fVolte para visitar\nde novo! Tchau!",
    "57:44de": "Ah, não. Você fez\na WHITNEY chorar.\fTudo bem. Ela para\nlogo. Ela sempre\fchora quando\nperde.",
    "57:4644": "E aí! Futuro\nCAMPEÃO!\fEste GINÁSIO é de\ntreinadores de\vPOKéMON normais.\fRecomendo que use\nPOKéMON do tipo\vlutador.",
    "57:46b1": "Ganhou? Ótimo! Eu\nestava ocupado\volhando as moças.",

    # ---------------- DEPT.STORE ----------------
    "57:5a38": "Bem-vindo à\nDEPT.STORE!",
    "57:5a5c": "A DEPT.STORE tem\numa boa\vvariedade.\fMas alguns itens\nsó saem como\fprêmios do\nGAME CORNER.",
    "57:5abf": "Estou doida para\ncomprar hoje!",
    "57:5adf": "Mamãe é boa em\ncaçar promoção.\fEla sempre compra\nas coisas mais\vbaratas.",
    "57:5b25": "1F BALCÃO\f2F MERCADO DO\n   TREINADOR\f3F COLEÇÃO DE\n   BATALHA\f4F REMÉDIOS\f5F CANTO DAS TM\f6F TERRAÇO",
}

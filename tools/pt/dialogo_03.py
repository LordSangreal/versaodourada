# -*- coding: utf-8 -*-
"""Lote 3 -- Violet City, Sprout Tower, o GINASIO do FALKNER, rotas 31 e 32.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Regras verificadas por tools/conferir.py:
  1. `\\n`, `\\v` e `\\f` na MESMA ordem e quantidade que o ingles.
  2. Tokens idem.
  3. 18 colunas por linha -- 17 na ULTIMA linha de cada pagina, porque a
     seta de "aperte A" ocupa a coluna 18.

Quinze chaves deste trecho ficaram de fora: kana solto e fragmentos que
comecam no meio de outra fala.  Nao sao texto de jogo; seguem em ingles.

O professor da academia fala ingles quebrado de proposito no original --
a traducao mantem o jeito torto em vez de consertar a gramatica dele.

Ficam no original: FALKNER, FRIEDA, BELLSPROUT, ZEPHYRBADGE, MUD-SLAP,
NIGHTMARE, FLASH, POISON BARB, SLOWPOKETAIL, POTION, ANTIDOTE, MAIL, TM,
HM e os nomes de cidade, rota e caverna.
"""

DIALOGO = {
    # ---------------- Sprout Tower ----------------
    "42:40dc": "Só quem chega ao\ntopo é que ganha\vum HM.",
    "42:410e": "A SPROUT TOWER foi\nerguida há muito\fcomo lugar de\ntreino POKéMON.",
    "42:414d": "Um BELLSPROUT de\nmais de 30 metros\fDizem que ele\nvirou o pilar\vcentral daqui.",
    "42:41a1": "Viu o pilar\ntremendo?\fEstão treinando\nlá em cima.",
    "42:41da": "Estátua POKéMON…\fParece muito\nimponente.",

    # ---------------- Violet City ----------------
    # o professor fala torto no original; mantido torto aqui
    "48:4d29": "Olá!\nVocê treinador?\fLutar com LÍDER,\nganhar você?",
    "48:4d62": "Ooh, la la!\nMuito bom mesmo!",
    "48:4d81": "É mesmo? Então\nestudar você deve!\vMe siga!",
    "48:4daf": "Aqui, professor eu\nsou. Bom é você\vestudar aqui!",
    "48:4ddf": "Dizem que aparecem\nfantasmas na\vSPROUT TOWER.\fDiziam que ataques\nnormais não pegam\fnos fantasmas.\nNada mesmo.",
    "48:4e49": "Ei, você é\ntreinador POKéMON\fSe vencer o LÍDER\nde GINÁSIO daqui,\fvai estar pronto\npara valer!",
    "48:4ea5": "FALKNER, do\nGINÁSIO POKéMON\fde VIOLET, é um\nótimo treinador!\fEle herdou o\nginásio do pai\fe fez um belo\ntrabalho nele.",
    "48:4f1b": "Vi uma árvore que\nse mexe adiante!\fSe você tocar,\nela se contorce\ve dança! Legal!",
    "48:4f68": "VIOLET CITY\fA cidade dos\naromas de outrora",
    "48:4f92": "VIOLET CITY\nGINÁSIO POKéMON\vLÍDER: FALKNER\fO elegante mestre\ndo tipo voador",
    "48:4fda": "SPROUT TOWER\fConheça o caminho\ndos POKéMON",
    "48:5003": "ACADEMIA POKéMON\nDO EARL",

    # ---------------- Rota 31 ----------------
    "4a:5b1e": "DARK CAVE…\fSe um POKéMON\niluminasse, eu\vexploraria.",
    "4a:5bf8": "… Hnnn… Hã?\fAndei demais hoje\nprocurando\vPOKéMON.\fMeus pés doem e\nestou com sono…\fSe eu fosse um\nPOKéMON selvagem,\vseria fácil…\f…Zzzz…",
    "4a:5c80": "…Zzzz… Hã?\fO que é isso? Tem\nMAIL para mim?",
    "4a:5caf": "{PLAYER} entregou\no POKéMON que\vsegurava a MAIL.",
    "4a:5cd9": "Vejamos…\f…DARK CAVE leva\na outra estrada…\fBom saber\ndisso.\fObrigado por\ntrazer isto.\fMeu amigo é gente\nboa, e você\vtambém é!\fQuero fazer algo\nde bom em troca\vtambém!\fJá sei! Quero que\nfique com isto!",
    "4a:5dbb": "TM50 é NIGHTMARE.\fÉ um golpe cruel\nque rói devagar\fo PS de um inimigo\nadormecido.\fOoooh…\nQue medo…\fNão quero ter\npesadelos.",
    "4a:5e46": "Esta MAIL não é\npara mim.",
    "4a:5e5e": "Por que este\nPOKéMON é raro?\fEle não tem\nMAIL nenhuma.",
    "4a:5e97": "O quê? Você não\nquer nada?",
    "4a:5eb6": "Se eu levar esse\nPOKéMON de você,\fo que vai usar\nna batalha?",
    "4a:5efa": "Achei um bom\nPOKéMON na DARK\vCAVE.\fVou criar ele\npara encarar o\vFALKNER.\fEle é o líder do\nGINÁSIO de VIOLET",
    "4a:5f6a": "ROUTE 31\fVIOLET CITY -\nCHERRYGROVE CITY",
    "4a:5f93": "DARK CAVE",

    # ---------------- Rota 32 ----------------
    "4b:42a5": "Espera aí!\nQual é a pressa?",
    "4b:42c0": "{PLAYER}, né?\nUm cara de óculos\festava procurando\npor você.\fVá ver você mesmo.\nEle espera por\fvocê no CENTRO\nPOKéMON.",
    "4b:43c5": "Você já foi ao\nGINÁSIO POKéMON?\fDá para testar seu\nPOKéMON e você\vmesmo lá.\fÉ um rito de\npassagem para todo\vtreinador!",
    "4b:443a": "Você tem bons\nPOKéMON aí.\fDeve ser do treino\nque você deu\fneles por\nVIOLET CITY.\fO treino no\nGINÁSIO deve ter\fajudado bastante.\nSem dúvida.\fComo lembrança de\nVIOLET CITY, leve\visto.\fAumenta a força\ndos ataques de\vplanta.",
    "4b:452a": "O que viveu em\nVIOLET CITY\fdeve ser útil na\nsua jornada.",
    "4b:456e": "Que tal levar\nesta gostosa e\fnutritiva\nSLOWPOKETAIL?\fPara você agora,\nsó ¥1.000.000!\fVai querer!",
    "4b:45e4": "Tsc! Pensei que\na molecada de hoje\vtinha dinheiro…",
    "4b:4611": "Não quer? Então\nfora daqui. Xô!",
    "4b:4bc0": "WROOOAR!\nGENTE FOGE QUANDO\fEU RUJO! MAS VOCÊ\nVEIO ATRÁS!\fISSO ME AGRADA!\nAGORA PEGUE ISTO!",
    "4b:4c19": "WROOOAR!\nÉ O ROAR!\fATÉ POKéMON FOGEM\nDE UM BOM ROAR!",
    "4b:4c4e": "FRIEDA: Oba!\nÉ sexta-feira!\fSou a FRIEDA de\nsexta!\fPrazer!",
    "4b:4c91": "Aqui, um POISON\nBARB para você!",
    "4b:4caf": "FRIEDA: Dê a um\nPOKéMON que tenha\vataques venenosos\fOh!\fÉ cruel!\fVai se espantar\ncom o quanto\vmelhora eles!",
    "4b:4d27": "FRIEDA: Oi! Que\ndia você gosta?\fAmo sexta-feira.\nSem dúvida!\fVocê não acha\nótimo também?",
    "4b:4d8c": "FRIEDA: Hoje não\né sexta-feira?\fÉ tão sem graça\nquando não é!",
    "4b:4dc7": "ROUTE 32\fVIOLET CITY -\nAZALEA TOWN",
    "4b:4deb": "RUINS OF ALPH\nENTRADA LESTE",
    "4b:4e08": "UNION CAVE\nEm frente",
    "4b:c600": "\fSe os tipos\nforem diferentes,\fum POKéMON mais\nalto pode perder.\fSaiba quais tipos\nsão fortes e\ffracos contra o\ntipo do seu.",

    # ---------------- Loja de Violet ----------------
    "56:400f": "Quando você pega\num POKéMON novo,\vele é fraco.\fMas com o tempo\nele vai ficar\vforte.\fÉ importante\ntratar POKéMON com\vcarinho.",
    "56:4090": "POKéMON podem\nsegurar itens como\vPOTION e ANTIDOTE\fMas parece que não\nsabem usar\fitens feitos por\ngente.",

    # ---------------- Ginasio de Violet ----------------
    "56:41e0": "Sou FALKNER, líder\ndo GINÁSIO POKéMON\vde VIOLET!\fDizem que dá para\ncortar as asas de\fPOKéMON voadores\ncom um choque\velétrico…\fNão vou permitir\ntal insulto às\vaves POKéMON!\fVou lhe mostrar o\npoder de verdade\fdas magníficas\naves POKéMON!",
    "56:42b7": "…Droga! As aves\nqueridas do meu\vpai…\fTudo bem.\nPegue isto.\fÉ a ZEPHYRBADGE\noficial da LIGA\vPOKéMON.",
    "56:431c": "{PLAYER} recebeu\na ZEPHYRBADGE.",
    "56:4335": "A ZEPHYRBADGE\naumenta o ataque\vdos seus POKéMON.\fEla também deixa\no POKéMON usar\fFLASH, se souber,\na qualquer hora.\fTome, leve isto\ntambém.",
    "56:43b5": "Usando uma TM, o\nPOKéMON aprende\fna hora um golpe\nnovo.\fPense antes de\nagir: uma TM só\vserve uma vez.\fA TM31 tem\nMUD-SLAP.\fEla reduz a\nmira do inimigo\fenquanto causa\ndano.\fOu seja, é defesa\ne ataque ao mesmo\vtempo.",
    "56:44a2": "Há GINÁSIOS\nPOKéMON em cidades\vmais à frente.\fVocê devia testar\nsua habilidade\vnesses GINÁSIOS.\fVou treinar mais\nforte para virar\fo maior mestre de\naves!",
    "56:4666": "Ei! Não sou\ntreinador, mas dou\vum conselho!\fAcredite em mim!\nSe você acredita,\fo sonho de ser\ncampeão acontece.\fAcredita?\nEntão escute.\fO tipo planta é\nfraco contra o\ftipo voador. Não\nesqueça disso.",
    "56:4735": "Boa batalha!\nContinue assim e\fvocê vira CAMPEÃO\nnum piscar!",
}

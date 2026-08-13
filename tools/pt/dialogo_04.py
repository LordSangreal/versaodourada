# -*- coding: utf-8 -*-
"""Lote 4 -- Azalea Town, Slowpoke Well, Ilex Forest, KURT e o GINASIO do BUGSY.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Regras verificadas por tools/conferir.py:
  1. `\\n`, `\\v` e `\\f` na MESMA ordem e quantidade que o ingles.
  2. Tokens idem.
  3. 18 colunas -- 17 na ULTIMA linha de cada pagina, por causa da seta.

Onze chaves ficaram de fora: kana solto, fragmentos e uma vazia.

Ficam no original: KURT, BUGSY, SLOWPOKE, FARFETCH'D, TEAM ROCKET,
HIVEBADGE, FURY CUTTER, CUT, HEADBUTT, APRICORNS, as BALLS, SILPH, e os
nomes de cidade, poco e floresta.
"""

DIALOGO = {
    # ---------------- Slowpoke Well ----------------
    "44:5b06": "KURT: Olá aí,\n{PLAYER}!\fOs guardas lá em\ncima fugiram\vquando eu gritei.\fMas aí eu caí\npoço abaixo\vaqui.\fBati as costas\ncom força e agora\vnão consigo andar\fDroga! Se eu\nestivesse bem, o\fPOKéMON teria dado\no troco…\fAh, não tem\njeito.\f{PLAYER}, mostre a\neles a sua coragem\vno meu lugar!",
    "44:6023": "Um SLOWPOKE com a\nTAIL cortada…\fHã? Tem uma MAIL.\nLer?",
    "44:6061": "{PLAYER} leu a\nMAIL.\fSeja bom e cuide\nda casa com o\fvovô e o\nSLOWPOKE.\fCom amor, papai",
    "44:60b9": "Um SLOWPOKE com a\nTAIL cortada…",

    # ---------------- Ilex Forest ----------------
    "45:6a44": "Ah, cara… Meu\nchefe vai ficar\vfurioso…\fO FARFETCH'D que\nusa CUT nas\fárvores para o\ncarvão fugiu.\fNão dá para eu\nprocurar ele aqui\vna ILEX FOREST.\fÉ grande, escura\ne assustadora…",
    "45:6b01": "Nossa! Muito\nobrigado mesmo!\fO POKéMON do meu\nchefe não me obe-\vdece porque eu não\vtenho BADGE.",
    "45:6b57": "É o POKéMON que\nsumiu!",
    "45:6b6e": "FARFETCH'D: Kwaa!",
    "45:6b81": "Ah! O FARFETCH'D!\fVocê achou ele\npara nós, garoto?\fSem ele, a gente\nnão conseguiria\fusar CUT para\nfazer carvão.\fObrigado, garoto!\fComo posso\nagradecer…\fJá sei! Tome,\nfique com isto.",
    "45:6c29": "É o HM de CUT.\nEnsine a um\fPOKéMON para\ncortar arvoretas.\fClaro, você\nprecisa da BADGE\fdo GINÁSIO de\nAZALEA para usar.",
    "45:6ca8": "Quer virar meu\naprendiz\fde carvoeiro\ncomigo?\fEm dez anos você\nestará craque!",
    "45:6d03": "O que eu faço?\fSacudo árvores\ncom HEADBUTT.\fÉ divertido. Tente\nvocê também!",
    "45:6d55": "Sacuda as árvores\ncom HEADBUTT. Às\vvezes cai um\vPOKéMON dormindo.",
    "45:6d97": "A ILEX FOREST tem\ntanta árvore que\fnão dá para ver\no céu.\fFique de olho em\nitens que possam\vter caído por aí.",
    "45:6e11": "SANTUÁRIO da ILEX\nFOREST…\fÉ em honra ao\nprotetor da\vfloresta…",

    # ---------------- Azalea Town ----------------
    "48:51e7": "…Me diga uma\ncoisa.\fÉ verdade que a\nTEAM ROCKET\vvoltou?\fO quê? Você\nvenceu? Hah! Pare\vde mentir.\fNão brinca?\nEntão vamos ver o\vquanto você vale.",
    "48:5280": "… Hunf! POKéMON\ninútil!\fEscute aqui. Você\nsó ganhou porque\fmeus POKéMON\nestavam fracos.",
    "48:52cd": "Odeio os fracos.\fPOKéMON, treinado-\nres. Não importa\vquem nem o quê.\fVou ficar forte e\nvarrer os fracos\vdo mapa.\fIsso vale para\na TEAM ROCKET.\fEles se acham em\nbando.\fMas sozinhos,\neles são\vfracos.\fOdeio todos eles.\fFique fora do meu\ncaminho. Um fraco\fcomo você só\natrapalha.",
    "48:53f5": "…Hunf! Eu sabia\nque você mentia.",
    "48:5415": "Não é seguro\nentrar ali, então\vfico de guarda.\fNão sou um bom\nsamaritano?",
    "48:5461": "Conhece a\nSLOWPOKETAIL?\vDizem que é boa!\fNão está feliz de\neu ter contado?",
    "48:54b5": "Os SLOWPOKE\nsumiram da\vcidade…\fOuvi que as TAILS\ndeles estão à\vvenda por aí.",
    "48:550d": "Os SLOWPOKE\nvoltaram.\fConhecendo eles,\nsó estavam de\fbobeira em algum\ncanto.",
    "48:5568": "Veio pedir para o\nKURT fazer umas\vBALLS?\fMuita gente vem\nsó para isso.",
    "48:55b4": "Corte por AZALEA\ne você chega à\vILEX FOREST.\fMas essas árvores\nfinas tornam\fimpossível\npassar.\fO POKéMON do\nCARVOEIRO usa CUT\vnas árvores.",
    "48:564a": "SLOWPOKE: …\f…… …… ……",
    "48:565d": "…… ……Bocejo?",
    "48:5679": "AZALEA TOWN\nOnde pessoas e\fPOKéMON vivem em\nfeliz harmonia",
    "48:56b2": "CASA DO KURT",
    "48:56c0": "AZALEA TOWN\nGINÁSIO POKéMON\vLÍDER: BUGSY\fA enciclopédia\nambulante de\vPOKéMON inseto",
    "48:5706": "SLOWPOKE WELL\fTambém chamado de\nPOÇO DA CHUVA.\fO povo daqui crê\nque o bocejo do\vSLOWPOKE dá chuva\fConsta que um\nbocejo dele\fpôs fim a uma seca\nhá 400 anos.",
    "48:57ac": "FORNO DE CARVÃO",
    "48:57bb": "ILEX FOREST\fEntre pelo\nportão.",

    # ---------------- Rota 33 ----------------
    "4b:503e": "ROUTE 33",

    # ---------------- Centro Pokemon de Azalea ----------------
    "55:4013": "Seus POKéMON sabem\ngolpes de HM?\fEsses golpes podem\nser usados mesmo\fse o seu POKéMON\ndesmaiou.",
    "55:4067": "O PC do BILL\nguarda até 20\vPOKéMON por BOX.",
    "55:4092": "Você conhece os\nAPRICORNS?\fAbra um, esvazie\npor dentro e põe\fum aparelho\nespecial.\fAí dá para pegar\nPOKéMON com ele.\fAntes das POKé\nBALLS existirem,\ftodo mundo usava\nAPRICORNS.",

    # ---------------- Loja de Azalea ----------------
    "55:44c6": "Não tem GREAT BALL\naqui. As POKé\fBALLS vão ter\nque servir.\fQueria que o KURT\nme fizesse umas\vBALLS especiais.",
    "55:452f": "Uma GREAT BALL é\nmelhor para pegar\vPOKéMON que uma\vPOKé BALL.\fMas as do KURT às\nvezes são\vmelhores.",

    # ---------------- Casa do KURT ----------------
    "55:47ee": "Hm? Quem é você?\f{PLAYER}, é? Quer\nque eu faça umas\vBALLS?\fDesculpe, mas isso\nvai esperar.\fConhece a TEAM\nROCKET? Ah, não\fimporta. Eu conto\nde qualquer forma\fA TEAM ROCKET é\numa gangue má que\fusa POKéMON para\no trabalho sujo.\fEra para eles\nterem se desfeito\vhá três anos.\fEnfim, estão no\nPOÇO, cortando\fSLOWPOKETAILS para\nvender!\fEntão eu vou lá\ndar uma lição\vdolorosa neles!\fAguente firme,\nSLOWPOKE! O velho\vKURT está indo!",
    # encurtar nao pode custar o token: "KURT: Oi!" cabia mas jogava fora o
    # {PLAYER}, e o KURT deixaria de chamar o jogador pelo nome
    "55:4990": "KURT: {PLAYER}!\fVocê se saiu\ncomo um herói\vno POÇO.\fGostei do estilo!\fSeria uma honra\nfazer BALLS\fpara um treinador\ncomo você.\fÉ tudo que tenho\nagora, mas leve.",
    "55:4a44": "KURT: Eu faço\nBALLS de APRICORN\fColha eles das\nárvores e traga\vaqui.\fEu faço BALLS\ncom eles.",
    "55:4ab1": "KURT: Tem um\nAPRICORN para mim\fÓtimo! Vou virar\nele numa BALL.",
    "55:4af4": "KURT: Vai levar um\ndia para a BALL.\fVolte depois\npara pegar.",
    "55:4b37": "KURT: Ah…\nQue decepção.",
    "55:4b53": "KURT: Trabalhando!\nNão me amole!",
    "55:4b76": "KURT: Ah, {PLAYER}!\nAcabei de terminar\vsua BALL. Tome!",
    "55:4ba5": "KURT: Ficou muito\nboa.\fTente pegar\nPOKéMON com ela.",
    "55:4bde": "Os SLOWPOKE se\nforam… Será que\fgente ruim levou\neles?",
    "55:4c1a": "O vovô saiu…\nQue solidão…",
    "55:4c38": "O SLOWPOKE que meu\npai deu voltou!\fA TAIL dele está\ncrescendo!",
    "55:4c7e": "Meu pai trabalha\nna SILPH, onde ele\vestuda POKé BALL.\fEu fico em casa\ncom o vovô e o\vSLOWPOKE.",
    "55:4cdb": "SLOWPOKE: …\nBocejo?",
    "55:4cee": "…Um PROF.OAK\njovem?",
    "55:4d03": "É uma estátua do\nprotetor da\vfloresta.",

    # ---------------- Ginasio de Azalea ----------------
    "55:4e83": "Eu sou o BUGSY!\nEu nunca perco\fquando o assunto\né POKéMON inseto.\fMinha pesquisa vai\nme tornar a maior\fautoridade em\nPOKéMON inseto!\fDeixe eu mostrar o\nque aprendi nos\vmeus estudos.",
    "55:4f26": "Uau, incrível!\nVocê é um perito\vem POKéMON!\fMinha pesquisa\nainda não acabou.\fCerto, você venceu\nLeve esta BADGE.",
    "55:4f8c": "{PLAYER} recebeu\na HIVEBADGE.",
    "55:4fa3": "Conhece as vanta-\ngens da HIVE-\vBADGE?\fCom ela, POKéMON\naté o L30 vão\vobedecer você.\fPOKéMON que sabem\nCUT poderão usar\fo golpe fora da\nbatalha também.\fTome, quero que\nfique com isto.",
    "55:5060": "A TM49 contém\nFURY CUTTER.\fSe você não errar,\nele fica mais\vforte a cada vez.\fQuanto mais longa\na batalha, melhor\vele fica.\fNão é ótimo?\nEu que descobri!",
    "55:50fe": "POKéMON inseto são\nprofundos. Há\fmuitos mistérios\na explorar.\fEstude bem os\nseus preferidos.",
    "55:53fc": "Ei, desafiante!\fO BUGSY é jovem,\nmas sabe muito\fde POKéMON inseto\nde verdade.\fVai ser difícil\nsem o meu\vconselho.\fVejamos… POKéMON\ninseto não gostam\vde fogo.\fGolpes voadores\ntambém são super\vefetivos.",
    "55:54bf": "Muito bem! Foi um\nbelo confronto\fentre jovens\ntalentosos.\fCom gente como\nvocê, o futuro dos\vPOKéMON é lindo!",
}

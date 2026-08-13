# -*- coding: utf-8 -*-
"""Texto do motor: batalha, itens, PC, loja, bicicleta e a fala do OAK.

Chave = a string em ingles do motor, exatamente como o codigo a escreve.
Nao e texto de ROM: nao tem ponteiro e nao passa pelo `dialogo.json`.

Por que este arquivo existe: o usuario jogou e viu batalha em ingles.
`sistema.py` cobria menus e status, mas 279 strings de jogo tinham ficado
de fora -- entre elas `%s used\\n%s!`, que aparece em TODO turno de TODA
batalha.  Era o texto mais visto do jogo inteiro, sem traducao.

Duas regras que valem aqui e nao valem no dialogo de ROM:

1. Os `%s`/`%d` tem de sobreviver em NUMERO e ORDEM.  O motor passa os
   argumentos na ordem em que aparecem -- inverter troca o nome do
   POKéMON pelo do golpe.  `validar.py` confere.
2. Rotulo de largura fixa (HUD, aba de menu) so entra se o portugues for
   MENOR OU IGUAL ao ingles.  "MONEY" -> "DINHEIRO" cabe no dicionario e
   nao cabe na tela, entao fica em ingles de proposito.
"""

SISTEMA = {
    # ---------------------------------------------------------- batalha
    "%s used\n%s!": "%s usou\n%s!",
    "%s wants\nto battle!": "%s quer\nbatalhar!",
    "%s ran from\nthe battle!": "%s fugiu da\nbatalha!",
    "%s left the\nbattle.": "%s saiu da\nbatalha.",
    "%s is out of\nPOKéMON!\x0c%s wins!": "%s está sem\nPOKéMON!\x0c%s venceu!",
    "%s ran out of\ntime!": "%s ficou sem\ntempo!",
    "Time's up! You\nforfeit the match.": "Tempo esgotado!\nVocê perdeu.",
    "There's no will\nto fight!": "Não há vontade\nde lutar!",
    "%s's\nhits will never\nmiss!": "%s não vai\nmais errar\nnenhum golpe!",
    "%s's %s\nrose!": "%s teve %s\naumentado!",
    "%s learned\n%s!": "%s aprendeu\n%s!",
    "%s's HP\nwas restored!": "Os PS de %s\nvoltaram!",
    "It won't have\nany effect.": "Não vai ter\nefeito nenhum.",
    "Congratulations!\nYour %s\nevolved into\n%s!":
        "Parabéns!\nSeu %s\nevoluiu para\n%s!",
    "%s came\nout of its EGG!": "%s saiu\ndo EGG!",
    "REPEL's effect\nwore off.": "O efeito do REPEL\nacabou.",

    # ------------------------------------------------------------ itens
    "You can't carry\nany more items!": "Você não pode\nlevar mais itens!",
    "You can't carry\nany more items.": "Não dá para levar\nmais itens.",
    "{PLAYER} got\n%s!": "{PLAYER} pegou\n%s!",
    "{PLAYER} received\n%s.": "{PLAYER} recebeu\n%s.",
    "{PLAYER} put the\n%s in\nthe %s.": "{PLAYER} pôs o\n%s na\n%s.",
    "The %s\nis full…": "A %s\nestá cheia…",
    "Obtained\n%s!": "Obteve\n%s!",
    "It contained\n%s!": "Continha\n%s!",
    "But the PACK is\nfull…": "Mas a BOLSA está\ncheia…",
    "That's too impor-\ntant to toss!": "Importante demais\npara jogar fora!",
    "Threw away\n%s.": "Jogou fora\n%s.",
    "Threw away %s.": "Jogou %s fora.",
    "Toss %s?": "Jogar %s fora?",
    "How many?": "Quantos?",
    "Use on which one?": "Usar em qual?",
    "Move to where?": "Mover para onde?",
    "%s received\nthe %s!": "%s recebeu\no %s!",
    "%s received\n%s!": "%s recebeu\n%s!",
    "%s found\n%s!": "%s achou\n%s!",
    "%s found\n%d coins!": "%s achou\n%d fichas!",

    # ------------------------------------------------------- fora de batalha
    "A blinding FLASH\nlights the area!": "Um FLASH forte\nilumina a área!",
    "No SURFing here!": "Não dá SURF aqui!",
    "Nothing to CUT!": "Nada para cortar!",
    "{RAM:wNameBuffer} used\nSTRENGTH.": "{RAM:wNameBuffer} usou\nSTRENGTH.",
    "{RAM:wNameBuffer} can\nmove boulders.": "{RAM:wNameBuffer} pode\nmover pedras.",
    "No good! It's not\neven near water.": "Não dá! Nem tem\nágua por perto.",
    "OAK: %s!\nThis isn't the\ntime to use that!":
        "OAK: %s!\nNão é hora de\nusar isso!",
    "The TOWN MAP is\nunreadable here.": "O TOWN MAP não\nfunciona aqui.",
    "Yes! ITEMFINDER\nindicates there's\nan item nearby.":
        "Sim! O ITEMFINDER\nacusa um item\naqui perto.",
    "Nope! ITEMFINDER\nisn't responding.": "Nada! O ITEMFINDER\nnão responde.",
    "You can't get off\nhere.": "Não dá para\ndescer aqui.",
    "%s got off\nthe BICYCLE.": "%s desceu da\nBICYCLE.",
    "%s got on\nthe BICYCLE!": "%s subiu na\nBICYCLE!",
    "No cycling\nallowed here.": "Não pode pedalar\naqui.",
    "You need a\nBICYCLE for the\nCycling Road!":
        "Precisa de uma\nBICYCLE para a\nCycling Road!",
    "The boulder fell\nthrough the hole!": "A pedra caiu\nno buraco!",
    "It's a fruit-\nbearing tree.": "É uma árvore\nfrutífera.",
    "There's nothing\nhere…": "Não tem nada\naqui…",
    "Hey! It's\n%s!": "Ei! É\n%s!",
    "Crammed full of\nPOKéMON books!": "Lotado de livros\nde POKéMON!",
    "There's a slew of\nPOKéMON stuff!": "Um monte de coisa\nde POKéMON!",
    "An elevator!": "Um elevador!",
    "Nothing here.": "Nada aqui.",

    # --------------------------------------------------------- POKéMON
    "Use TM on which\nPOKéMON?": "Usar TM em qual\nPOKéMON?",
    "Bring out which\nPOKéMON?": "Chamar qual\nPOKéMON?",
    "Choose a POKéMON.": "Escolha um POKéMON",
    "No POKéMON!": "Sem POKéMON!",
    "Do you want to\ngive a nickname\nto %s?": "Quer dar um\napelido para\n%s?",
    "Give a nickname to\n%s?": "Dar um apelido a\n%s?",
    "Which move should": "Qual movimento",
    "be forgotten?": "deve ser esquecido",

    # -------------------------------------------------------------- PC
    "What? There are\nno POKéMON here!": "O quê? Não há\nPOKéMON aqui!",
    "You can't take\nany more POKéMON.\x0cDeposit POKéMON\nfirst.":
        "Não dá para levar\nmais POKéMON.\x0cGuarde algum\nprimeiro.",
    "You can't deposit\nthe last POKéMON!": "Não dá para\nguardar o último!",
    "Oops! This Box is\nfull of POKéMON.": "Opa! Esta Box\nestá cheia.",
    "You need at least\none POKéMON!": "Precisa de pelo\nmenos um POKéMON!",
    "%s was\nstored in Box %s.": "%s foi para\na Box %s.",
    "%s was\nstored via PC.": "%s foi\nguardado no PC.",
    "Once released,\n%s is\ngone forever. OK?":
        "Uma vez solto,\n%s\nse vai. Tudo bem?",
    "%s was\nreleased outside.\x0cBye %s!":
        "%s foi\nsolto lá fora.\x0cTchau %s!",
    "When you change a\nPOKéMON BOX, data\nwill be saved. OK?":
        "Ao trocar de BOX,\no jogo vai ser\nsalvo. Tudo bem?",
    "No room left to\nstore items.": "Sem espaço para\nguardar itens.",
    "There's no more\nroom for POKéMON!\x0b%s was\x0bsent to POKéMON\x0bBOX %s on PC!":
        "Sem espaço para\nPOKéMON!\x0b%s foi\x0bpara a POKéMON\x0bBOX %s do PC!",
    # Rotulos que ENCOLHEM em portugues -- por isso podem entrar
    "WITHDRAW ITEM": "RETIRAR ITEM",
    "DEPOSIT ITEM": "GUARDAR ITEM",
    "LOG OFF": "SAIR",
    "SEEN %3d  OWN %3d": "VIU %3d  TEM %3d",
    "CRY": "SOM",
    "AREA": "ÁREA",

    # ------------------------------------------------------------- loja
    "You don't have\nenough money.": "Você não tem\ndinheiro.",
    "%s?\nThat will be\n¥%d. OK?": "%s?\nSão\n¥%d. Tudo bem?",
    "Here you are!\nThank you!": "Aqui está!\nObrigado!",
    "I can't put a\nprice on that.": "Não posso dar\npreço nisso.",
    "I can pay you\n¥%d for that.": "Posso pagar\n¥%d por isso.",

    # ------------------------------------------------------ game corner
    "%s lined up!\nScored %d coins!": "%s alinhou!\nGanhou %d fichas!",
    "Darn!\nRan out of coins!": "Droga!\nFicou sem fichas!",
    "Not enough\ncoins!": "Fichas\ninsuficientes!",
    "New record!": "Novo recorde!",

    # ------------------------------------------------- salvar e centro
    "\x0cWould you like to\nSAVE the game?": "\x0cQuer SALVAR\no jogo?",
    "Now saving...": "Salvando...",
    "%s saved\nthe game!": "%s salvou\no jogo!",
    "RETURN TO MAIN\nMENU?": "VOLTAR AO MENU\nPRINCIPAL?",
    "Welcome to our\nPOKéMON CENTER!": "Bem-vindo ao nosso\nCENTRO POKéMON!",
    "Shall we heal your\nPOKéMON?": "Curamos os seus\nPOKéMON?",
    "OK. We'll need\nyour POKéMON.": "Certo. Preciso dos\nseus POKéMON.",
    "Your POKéMON are\nfighting fit!": "Seus POKéMON estão\nem forma!",
    "I like shorts!\nThey're comfy and\neasy to wear!":
        "Adoro shorts!\nSão confortáveis\ne fáceis de usar!",
    "Go right ahead!": "Pode ir!",
    "{PLAYER} used the": "{PLAYER} usou o",
    "Registered the": "Registrou o",
    "You can't register": "Não é possível",
    "that item.": "registrar o item.",

    # ------------------------------------------- a fala de abertura do OAK
    "Hello! Sorry to\nkeep you waiting!\x0cWelcome to the\nworld of POKéMON!"
    "\x0cMy name is OAK.\x0cPeople call me the\nPOKéMON PROF.":
        "Olá! Desculpe a\ndemora!\x0cBem-vindo ao mundo\ndos POKéMON!"
        "\x0cMeu nome é OAK.\x0cMe chamam de\nPROF. POKéMON.",
    "This world is in-\nhabited by crea-\x0btures that we call\x0bPOKéMON.":
        "Este mundo é\nhabitado por\x0bcriaturas que\x0bchamamos POKéMON.",
    "People and POKéMON\nlive together by\x0csupporting each\nother."
    "\x0cSome people play\nwith POKéMON, some\x0bbattle with them.":
        "Pessoas e POKéMON\nvivem juntos se\x0capoiando uns aos\noutros."
        "\x0cUns brincam com\nPOKéMON, outros\x0bbatalham com eles",
    "But we don't know\neverything about\x0bPOKéMON yet.\x0cThere are still\n"
    "many mysteries to\x0bsolve.\x0cThat's why I study\nPOKéMON every day.":
        "Mas ainda não\nsabemos tudo sobre\x0bos POKéMON.\x0cAinda há muitos\n"
        "mistérios para\x0bresolver.\x0cPor isso estudo\nPOKéMON todo dia.",
    "Now, what did you\nsay your name was?": "Agora, como você\ndisse se chamar?",
    "{PLAYER}, are you\nready?\x0cYour very own\nPOKéMON story is\x0b"
    "about to unfold.\x0cYou'll face fun\ntimes and tough\x0bchallenges.\x0c"
    "A world of dreams\nand adventures\x0cwith POKéMON\nawaits! Let's go!\x0c"
    "I'll be seeing you\nlater!":
        "{PLAYER}, você está\npronto?\x0cSua própria\nhistória POKéMON\x0b"
        "está começando.\x0cVocê vai viver\nmomentos bons e\x0bdesafios duros.\x0c"
        "Um mundo de sonhos\ne aventuras\x0ccom POKéMON\nespera! Vamos lá!\x0c"
        "A gente se vê\npor aí!",
}

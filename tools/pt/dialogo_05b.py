# -*- coding: utf-8 -*-
"""Lote 5b -- RADIO TOWER, rotas 34 e 35, NATIONAL PARK.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Das 77 chaves restantes do lote 05, 51 entram aqui.  As outras 26 sao
fragmentos de TX_FAR (comecam no meio de uma palavra), kana solto de
ponteiro mal alinhado, duas vazias, e duas iguais ao ingles ("ROUTE 35",
"FLASH!").  Traduzir fragmento nao adianta: o pedaco que aparece em tela
vem da fala inteira, e essa ja esta em outro ponteiro.

Regras verificadas por tools/conferir.py: sequencia de \\n \\v \\f identica,
tokens preservados, 18 colunas -- 17 na ultima linha de cada pagina.

Ficam no original: LUCKY NUMBER SHOW, LUCKY CHANNEL, RADIO CARD, MASTER
BALL, EXP.SHARE, PP UP, QUICK CLAW, POKéGEAR, POKéDEX, TOWN MAP, MAIL,
BERRY/BERRIES, DAY-CARE, TRAINER TIPS, START, NATIONAL PARK, ILEX FOREST,
os nomes de cidade e rota, e os nomes proprios (KURT, BEN, MARY, MARIE,
NIDORINA, MAGIKARP, PERSIAN, PROF.OAK'S POKéMON TALK).
"""

DIALOGO = {
    # ---------------- RADIO TOWER 1F ----------------
    "43:4e1f": "Bem-vindo!",
    "43:4e29": "Olá. Sinto muito,\nmas hoje não temos\vvisitas guiadas\vdisponíveis.",
    "43:4e62": "Oi, você veio pelo\nLUCKY NUMBER\vSHOW?\fQuer que eu veja\nos números de ID\vdos seus POKéMON?\fSe der sorte, você\nganha um prêmio.",
    "43:4ee2": "O ID da semana é\n{STRBUF}.",
    "43:4f02": "Vamos ver se você\nacertou algum.",
    "43:4f21": "……\n……",
    "43:4f26": "Volte semana que\nvem para o próximo\vLUCKY NUMBER.",
    "43:4f5d": "Uau! Você acertou\nos cinco números\vem cheio!\fTemos um ganhador\ndo grande prêmio!\fVocê ganhou uma\nMASTER BALL!",
    "43:4fcb": "Ei! Você acertou\nos três últimos\vnúmeros!\fGanhou o segundo\nprêmio, um EXP.\vSHARE!",
    "43:501e": "Ooh, você acertou\nos dois últimos\vnúmeros.\fGanhou o terceiro\nprêmio, um PP UP.",
    "43:5068": "Não, nenhum dos\nseus IDs combina.",
    "43:508e": "Não há espaço para\no seu prêmio.\fAbra espaço e\nvolte logo aqui.",
    "43:50d5": "Temos uma promoção\nde quiz especial\vrolando agora.\fAcerte cinco per-\nguntas e ganhe um\vRADIO CARD.\fEncaixe ele na sua\nPOKéGEAR e toque\fo rádio a qualquer\nhora e lugar.\fQuer responder ao\nquiz?",
    "43:519a": "Pergunta 1:\fO TOWN MAP pode\nser exibido em uma\vPOKéGEAR?",
    "43:51d1": "Correto!\nPergunta 2:\fNIDORINA pode ser\nsomente fêmea?",
    "43:5204": "Na mosca!\nPergunta 3:\fO KURT, artesão de\nPOKé BALLS, usa\vAPRICORNS?",
    "43:524d": "Até aqui tudo bem!\nPergunta 4:\fMAGIKARP não sabe\naprender TM?",
    "43:528b": "Uau! Certo de novo\nEsta é a última\vpergunta:\fPROF.OAK'S POKéMON\nTALK é um programa\vmuito popular.\fA MARIE é a co-\napresentadora?",
    "43:530b": "Bingo! Acertou!\nParabéns!\fEste é seu prêmio,\num RADIO CARD!",
    "43:5350": "A POKéGEAR de\n{PLAYER} agora toca\vrádio também!",
    "43:5375": "Sintonize nossos\nshows de rádio.",
    "43:5399": "Ah, que pena.\nSinto muito, mas\fvocê errou.\nTente de novo!",
    "43:53d3": "Ah. Entendo. Tente\nde novo se mudar\vde ideia.",
    "43:5403": "O BEN é um DJ\nfabuloso.\fA voz doce dele\nme derrete!",
    "43:5439": "Adoro a MARY, do\nPOKéMON TALK.\fSó conheço a voz\ndela, mas nunca\va vi.",
    "43:5574": "1F RECEPÇÃO\n2F VENDAS\f3F PESSOAL\n4F PRODUÇÃO\f5F SALA DO\n   DIRETOR",
    "43:55be": "LUCKY CHANNEL!\fGanhe com os IDs\ndos seus POKéMON!\fTroque POKéMON e\ncolecione IDs\vdiferentes!",

    # ---------------- Rota 34 ----------------
    "4b:54ea": "Quem vem lá?\nO que você está\vaprontando?",
    "4b:550f": "Você é um garoto\ndurão.",
    "4b:552a": "É, não vejo nada\nde errado hoje.\fComporte-se e não\narrume confusão.",
    "4b:5570": "Estou de ronda\natrás de gente\vsuspeita.",
    "4b:58b1": "ROUTE 34\fGOLDENROD CITY -\nAZALEA TOWN\fILEX FOREST\nEm algum ponto",
    "4b:58f6": "TRAINER TIPS\fÁrvores de BERRY\ndão BERRIES novas\vtodo dia.\fAnote que árvore\ndá qual tipo de\vBERRY.",
    "4b:595a": "DAY-CARE\fNós Criamos o Seu\nPOKéMON por Você!",

    # ---------------- Rota 35 ----------------
    "4b:6037": "O perigo espreita\nà noite!",
    "4b:6053": "Opa!",
    "4b:605c": "Sabe, a noite tem\nas diversões dela\vtambém.\fMas não exagere,\ntá bom?",
    "4b:60a3": "Seus POKéMON são\nbem fortes.\fVocê pode ir a\nqualquer lugar.",

    # ---------------- NATIONAL PARK ----------------
    "43:4196": "Olhe! Veja a minha\nbolsa!\fImprimi os meus\nfavoritos da\fPOKéDEX e colei\nna minha bolsa.",
    "43:41f1": "Esta é uma MAIL da\nminha filha.\vEla me anima.",
    "43:4228": "Atenção, por\nfavor!\f…Opa, preciso\nparar de pensar\fcomo professora o\ntempo todo.\fVocê deve ser um\ntreinador POKéMON\fJá que se esforça\ntanto, quero que\fvocê fique com\nisto.",
    "43:42d0": "Dê essa QUICK CLAW\na um POKéMON.\fÀs vezes ele ataca\nprimeiro na\vbatalha.",
    "43:4320": "Estou brincando\ncom adesivos que\vtirei da POKéDEX.",
    "43:4352": "Se eu ganhar, fico\ncom o adesivo da\vPOKéDEX dele.",
    "43:437f": "Eu passeio pelo\nPARK, mas nunca\fentro no meio do\nmato.\fTreinadores sempre\nquerem batalhar…",
    "43:43d9": "PERSIAN: Fufusha!",
    "43:43ed": "Estou imprimindo a\nminha POKéDEX.\fDá para imprimir\noutras coisas,\fcomo MAIL e suas\nBOXES do PC.",
    "43:46e4": "PRAÇA DO DESCANSO\nNATIONAL PARK",
    "43:4705": "O que diz este\naviso?\fBatalhe somente no\nmato, por favor.\fNATIONAL PARK\nSEDE DA GUARDA",
    "43:4745": "SEDE DA GUARDA\nDO PARK",
    "43:475a": "TRAINER TIPS\fPara imprimir uma\nMAIL, abra ela e\vaperte START.",
}

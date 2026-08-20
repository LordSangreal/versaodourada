-- Entradas da POKéDEX do Pokémon SILVER.  Chave = id da especie.
--
-- Arquivo separado do pokedex.lua de proposito: as 251 fichas do Silver sao
-- OUTRO texto.  A comparacao das duas extracoes deu 504 campos diferentes --
-- `text` e `text2` de todas as 251 especies -- e o registro e indexado por id
-- de especie, entao um catalogo unico mostraria a ficha do Gold para quem joga
-- Silver.  O `main.lua` pergunta em qual jogo esta e carrega um ou outro.
--
-- `kind` NAO foi retraduzido: a categoria e identica nas duas ROMs, entao e a
-- mesma linha do catalogo do Gold, palavra por palavra.
--
-- `height` e `weight` sao os mesmos do Gold, e isso e uma decisao: a ROM do
-- Silver traz ENTEI e TYRANITAR com a altura TROCADA (ENTEI 6'07", TYRANITAR
-- 6'11"), e o mod ja substitui a medida imperial do cartucho pela tabela
-- canonica da franquia desde a 0.48.0.  Manter o canone nos dois jogos e
-- coerente com essa decisao -- e de quebra conserta a troca.
--
-- O resto das regras e igual a do Gold: `<NEXT>` e quebra de LINHA (tres
-- linhas por tela, 18 colunas), a contagem tem de bater com a do ingles, e
-- so existe o alfabeto ASCII mais as 25 acentuadas da pagina do mod.
--
-- SO FUNCIONA em motor com a rota `pokedex` no registro (Schemas.GEN2).
return {
  ["ABRA"] = {
    kind = "PSI",
    text = "Se ele usa o<NEXT>TELEPORTE sem<NEXT>rumo, cria a",
    text2 = "ilusão de que fez<NEXT>cópias de si<NEXT>mesmo.",
    height = 9, weight = 195,   -- 0,9 m / 19,5 kg
  },
  ["AERODACTYL"] = {
    kind = "FÓSSIL",
    text = "Dizem que este<NEXT>POKéMON feroz voou<NEXT>nos céus antigos",
    text2 = "soltando gritos<NEXT>agudos e<NEXT>estridentes.",
    height = 108, weight = 590,   -- 1,8 m / 59,0 kg
  },
  ["AIPOM"] = {
    kind = "RABO LONGO",
    text = "Ele vive no alto<NEXT>das árvores. Ao<NEXT>pular de galho",
    text2 = "em galho, usa o<NEXT>rabo com jeito<NEXT>para se equilibrar",
    height = 8, weight = 115,   -- 0,8 m / 11,5 kg
  },
  ["ALAKAZAM"] = {
    kind = "PSI",
    text = "As células do<NEXT>cérebro dele se<NEXT>multiplicam sem",
    text2 = "parar até ele<NEXT>morrer. Por isso,<NEXT>lembra de tudo.",
    height = 105, weight = 480,   -- 1,5 m / 48,0 kg
  },
  ["AMPHAROS"] = {
    kind = "LUZ",
    text = "A luz forte do<NEXT>rabo dele é vista<NEXT>de bem longe. É",
    text2 = "guardada como um<NEXT>farol desde os<NEXT>tempos antigos.",
    height = 104, weight = 615,   -- 1,4 m / 61,5 kg
  },
  ["ARBOK"] = {
    kind = "NAJA",
    text = "Muito vingativo,<NEXT>ele não desiste<NEXT>da caçada, por",
    text2 = "mais longe que<NEXT>seja, quando mira<NEXT>uma presa.",
    height = 305, weight = 650,   -- 3,5 m / 65,0 kg
  },
  ["ARCANINE"] = {
    kind = "LENDÁRIO",
    text = "O latido magnífico<NEXT>dele passa uma<NEXT>sensação de",
    text2 = "majestade. Quem<NEXT>ouve não resiste<NEXT>e se curva.",
    height = 109, weight = 1550,   -- 1,9 m / 155,0 kg
  },
  ["ARIADOS"] = {
    kind = "PERNALONGA",
    text = "Um fio único e<NEXT>especial sai sem<NEXT>parar de trás",
    text2 = "dele. O fio leva<NEXT>de volta para o<NEXT>ninho.",
    height = 101, weight = 335,   -- 1,1 m / 33,5 kg
  },
  ["ARTICUNO"] = {
    kind = "GELO",
    text = "Uma das aves<NEXT>POKéMON lendárias,<NEXT>ela congela a",
    text2 = "umidade do ar e<NEXT>faz nevar<NEXT>enquanto voa.",
    height = 107, weight = 554,   -- 1,7 m / 55,4 kg
  },
  ["AZUMARILL"] = {
    kind = "COELHOÁGUA",
    text = "Quando brinca na<NEXT>água, ele enrola<NEXT>as orelhas longas",
    text2 = "para não deixar<NEXT>que molhem por<NEXT>dentro.",
    height = 8, weight = 285,   -- 0,8 m / 28,5 kg
  },
  ["BAYLEEF"] = {
    kind = "FOLHA",
    text = "Um cheiro picante<NEXT>sai do pescoço<NEXT>dele. O cheiro",
    text2 = "age como estímulo<NEXT>e recupera a<NEXT>saúde.",
    height = 102, weight = 158,   -- 1,2 m / 15,8 kg
  },
  ["BEEDRILL"] = {
    kind = "ABELHA",
    text = "Ele tem três<NEXT>ferrões de veneno.<NEXT>O do rabo solta",
    text2 = "o veneno mais<NEXT>forte que ele<NEXT>tem.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["BELLOSSOM"] = {
    kind = "FLOR",
    text = "Comum nos<NEXT>trópicos. Quando<NEXT>ela dança, as",
    text2 = "pétalas se roçam<NEXT>e fazem um som<NEXT>agradável.",
    height = 4, weight = 58,   -- 0,4 m / 5,8 kg
  },
  ["BELLSPROUT"] = {
    kind = "FLOR",
    text = "Ele finca os pés<NEXT>bem fundo no chão<NEXT>para repor água.",
    text2 = "Enquanto está<NEXT>enraizado, não<NEXT>foge do inimigo.",
    height = 7, weight = 40,   -- 0,7 m / 4,0 kg
  },
  ["BLASTOISE"] = {
    kind = "MARISCO",
    text = "Os canhões da<NEXT>casca dele soltam<NEXT>jatos de água que",
    text2 = "furam até uma<NEXT>chapa grossa de<NEXT>aço.",
    height = 106, weight = 855,   -- 1,6 m / 85,5 kg
  },
  ["BLISSEY"] = {
    kind = "FELICIDADE",
    text = "Ele é muito<NEXT>compassivo. Se vê<NEXT>um POKéMON doente,",
    text2 = "cuida dele até<NEXT>que fique bom de<NEXT>novo.",
    height = 105, weight = 468,   -- 1,5 m / 46,8 kg
  },
  ["BULBASAUR"] = {
    kind = "SEMENTE",
    text = "Ele carrega uma<NEXT>semente nas costas<NEXT>desde que nasce.",
    text2 = "Conforme ele<NEXT>cresce, a semente<NEXT>cresce também.",
    height = 7, weight = 69,   -- 0,7 m / 6,9 kg
  },
  ["BUTTERFREE"] = {
    kind = "BORBOLETA",
    text = "O pó que repele<NEXT>água nas asas<NEXT>dele deixa que",
    text2 = "colha mel até na<NEXT>chuva mais<NEXT>pesada.",
    height = 101, weight = 320,   -- 1,1 m / 32,0 kg
  },
  ["CATERPIE"] = {
    kind = "LAGARTA",
    text = "Os pés dele têm<NEXT>ventosas que<NEXT>grudam em qualquer",
    text2 = "superfície. Ele<NEXT>sobe em árvores<NEXT>para se alimentar",
    height = 3, weight = 29,   -- 0,3 m / 2,9 kg
  },
  ["CELEBI"] = {
    kind = "VIAJATEMPO",
    text = "Quando CELEBI some<NEXT>no fundo de uma<NEXT>floresta, dizem",
    text2 = "que ele deixa um<NEXT>ovo trazido do<NEXT>futuro.",
    height = 6, weight = 50,   -- 0,6 m / 5,0 kg
  },
  ["CHANSEY"] = {
    kind = "OVO",
    text = "Raro e difícil de<NEXT>capturar, dizem<NEXT>que ele traz",
    text2 = "felicidade para o<NEXT>treinador que<NEXT>consegue pegá-lo.",
    height = 101, weight = 346,   -- 1,1 m / 34,6 kg
  },
  ["CHARIZARD"] = {
    kind = "CHAMA",
    text = "Soltando chamas<NEXT>quentes e fortes,<NEXT>ele derrete quase",
    text2 = "tudo. O sopro<NEXT>dele causa uma dor<NEXT>terrível no rival.",
    height = 107, weight = 905,   -- 1,7 m / 90,5 kg
  },
  ["CHARMANDER"] = {
    kind = "LAGARTO",
    text = "A chama no rabo<NEXT>mostra a força<NEXT>vital dele. Se",
    text2 = "estiver saudável,<NEXT>a chama queima<NEXT>bem forte.",
    height = 6, weight = 85,   -- 0,6 m / 8,5 kg
  },
  ["CHARMELEON"] = {
    kind = "CHAMA",
    text = "Ele tem uma<NEXT>natureza selvagem.<NEXT>Na luta, chicoteia",
    text2 = "o rabo em brasa e<NEXT>corta tudo com as<NEXT>garras afiadas.",
    height = 101, weight = 190,   -- 1,1 m / 19,0 kg
  },
  ["CHIKORITA"] = {
    kind = "FOLHA",
    text = "As folhas dela têm<NEXT>um cheiro gostoso<NEXT>e conseguem medir",
    text2 = "a umidade e a<NEXT>temperatura do<NEXT>ar em volta.",
    height = 9, weight = 64,   -- 0,9 m / 6,4 kg
  },
  ["CHINCHOU"] = {
    kind = "PESCADOR",
    text = "No fundo escuro do<NEXT>mar, o único jeito<NEXT>que ele tem de se",
    text2 = "comunicar são as<NEXT>luzes que pisca<NEXT>sem parar.",
    height = 5, weight = 120,   -- 0,5 m / 12,0 kg
  },
  ["CLEFABLE"] = {
    kind = "FADA",
    text = "As orelhas bem<NEXT>sensíveis deixam<NEXT>ele ouvir sons",
    text2 = "distantes. Por<NEXT>isso, prefere<NEXT>lugares calmos.",
    height = 103, weight = 400,   -- 1,3 m / 40,0 kg
  },
  ["CLEFAIRY"] = {
    kind = "FADA",
    text = "O jeitinho e o<NEXT>grito dela fazem<NEXT>muito sucesso. Mas",
    text2 = "este POKéMON tão<NEXT>fofo é bem raro<NEXT>de se encontrar.",
    height = 6, weight = 75,   -- 0,6 m / 7,5 kg
  },
  ["CLEFFA"] = {
    kind = "ESTRELA",
    text = "Quando muitos<NEXT>meteoros iluminam<NEXT>o céu da noite,",
    text2 = "por algum motivo<NEXT>aparece mais<NEXT>CLEFFA por aí.",
    height = 3, weight = 30,   -- 0,3 m / 3,0 kg
  },
  ["CLOYSTER"] = {
    kind = "BIVALVE",
    text = "Os CLOYSTER que<NEXT>vivem em mares de<NEXT>correnteza brava",
    text2 = "criam espinhos<NEXT>grandes e afiados<NEXT>na casca.",
    height = 105, weight = 1325,   -- 1,5 m / 132,5 kg
  },
  ["CORSOLA"] = {
    kind = "CORAL",
    text = "Num país de mar do<NEXT>sul, as pessoas<NEXT>moram em vilas",
    text2 = "construídas em<NEXT>cima de grupos<NEXT>destes POKéMON.",
    height = 6, weight = 50,   -- 0,6 m / 5,0 kg
  },
  ["CROBAT"] = {
    kind = "MORCEGO",
    text = "As asas que<NEXT>nasceram nas<NEXT>pernas deixam ele",
    text2 = "voar rápido, mas<NEXT>dificultam parar<NEXT>para descansar.",
    height = 108, weight = 750,   -- 1,8 m / 75,0 kg
  },
  ["CROCONAW"] = {
    kind = "MANDÍBULA",
    text = "Ele abre bem a<NEXT>bocarra na hora de<NEXT>atacar. Se perder",
    text2 = "alguma presa na<NEXT>mordida, ela nasce<NEXT>de novo.",
    height = 101, weight = 250,   -- 1,1 m / 25,0 kg
  },
  ["CUBONE"] = {
    kind = "SOLITÁRIO",
    text = "Ele sempre usa o<NEXT>crânio da mãe<NEXT>morta, então",
    text2 = "ninguém faz ideia<NEXT>de como é o rosto<NEXT>escondido dele.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["CYNDAQUIL"] = {
    kind = "RATO FOGO",
    text = "Ele costuma ficar<NEXT>encolhido. Se leva<NEXT>um susto ou fica",
    text2 = "com raiva, solta<NEXT>chamas pelas<NEXT>costas.",
    height = 5, weight = 79,   -- 0,5 m / 7,9 kg
  },
  ["DELIBIRD"] = {
    kind = "ENTREGA",
    text = "Ele faz ninho na<NEXT>beira de penhascos<NEXT>afiados. Passa o",
    text2 = "dia todo levando<NEXT>comida para os<NEXT>filhotes.",
    height = 9, weight = 160,   -- 0,9 m / 16,0 kg
  },
  ["DEWGONG"] = {
    kind = "FOCA",
    text = "Ele adora mares<NEXT>gelados com placas<NEXT>de gelo. Usa o",
    text2 = "rabo comprido para<NEXT>mudar de direção<NEXT>bem rápido.",
    height = 107, weight = 1200,   -- 1,7 m / 120,0 kg
  },
  ["DIGLETT"] = {
    kind = "TOUPEIRA",
    text = "Se um DIGLETT cava<NEXT>por um campo, a<NEXT>terra fica",
    text2 = "revirada e ótima<NEXT>para plantar<NEXT>qualquer coisa.",
    height = 2, weight = 8,   -- 0,2 m / 0,8 kg
  },
  ["DITTO"] = {
    kind = "TRANSFORMA",
    text = "O poder de se<NEXT>transformar dele é<NEXT>perfeito. Mas se",
    text2 = "alguém faz ele<NEXT>rir, não segura o<NEXT>disfarce.",
    height = 3, weight = 40,   -- 0,3 m / 4,0 kg
  },
  ["DODRIO"] = {
    kind = "AVE TRIPLA",
    text = "Se uma das cabeças<NEXT>come, as outras<NEXT>ficam satisfeitas",
    text2 = "também, e todas<NEXT>param de brigar<NEXT>entre si.",
    height = 108, weight = 852,   -- 1,8 m / 85,2 kg
  },
  ["DODUO"] = {
    kind = "AVE GÊMEA",
    text = "Ele corre pelas<NEXT>planícies de mato<NEXT>com passadas",
    text2 = "fortes, deixando<NEXT>pegadas de até dez<NEXT>centímetros.",
    height = 104, weight = 392,   -- 1,4 m / 39,2 kg
  },
  ["DONPHAN"] = {
    kind = "ARMADURA",
    text = "Quanto maiores as<NEXT>presas dele, mais<NEXT>alto o posto no",
    text2 = "bando. As presas<NEXT>demoram muito<NEXT>para crescer.",
    height = 101, weight = 1200,   -- 1,1 m / 120,0 kg
  },
  ["DRAGONAIR"] = {
    kind = "DRAGÃO",
    text = "As esferas de<NEXT>cristal parecem<NEXT>dar a este POKéMON",
    text2 = "o poder de mudar<NEXT>o tempo como<NEXT>quiser.",
    height = 400, weight = 165,   -- 4,0 m / 16,5 kg
  },
  ["DRAGONITE"] = {
    kind = "DRAGÃO",
    text = "Este POKéMON do<NEXT>mar tem um corpo<NEXT>impressionante que",
    text2 = "deixa ele voar<NEXT>sobre mares bravos<NEXT>sem dificuldade.",
    height = 202, weight = 2100,   -- 2,2 m / 210,0 kg
  },
  ["DRATINI"] = {
    kind = "DRAGÃO",
    text = "Este POKéMON é<NEXT>cheio de energia<NEXT>vital. Ele troca",
    text2 = "de pele sem parar<NEXT>e vai crescendo<NEXT>cada vez mais.",
    height = 108, weight = 33,   -- 1,8 m / 3,3 kg
  },
  ["DROWZEE"] = {
    kind = "HIPNOSE",
    text = "Ele lembra de todo<NEXT>sonho que come.<NEXT>Quase não come os",
    text2 = "sonhos de adulto:<NEXT>os de criança são<NEXT>bem mais gostosos",
    height = 100, weight = 324,   -- 1,0 m / 32,4 kg
  },
  ["DUGTRIO"] = {
    kind = "TOUPEIRA",
    text = "Muito poderosos,<NEXT>eles cavam até no<NEXT>chão mais duro,",
    text2 = "chegando a mais de<NEXT>cem quilômetros de<NEXT>profundidade.",
    height = 7, weight = 333,   -- 0,7 m / 33,3 kg
  },
  ["DUNSPARCE"] = {
    kind = "COBRATERRA",
    text = "Se alguém o vê,<NEXT>ele foge cavando<NEXT>com o rabo. Dá",
    text2 = "para ele flutuar<NEXT>um pouquinho<NEXT>usando as asas.",
    height = 105, weight = 140,   -- 1,5 m / 14,0 kg
  },
  ["EEVEE"] = {
    kind = "EVOLUÇÃO",
    text = "O DNA irregular<NEXT>dele é afetado<NEXT>pelo ambiente. Ele",
    text2 = "evolui se o lugar<NEXT>onde vive muda de<NEXT>alguma forma.",
    height = 3, weight = 65,   -- 0,3 m / 6,5 kg
  },
  ["EKANS"] = {
    kind = "COBRA",
    text = "Ele sempre se<NEXT>esconde no mato.<NEXT>Recém-nascido, não",
    text2 = "tem veneno, então<NEXT>a mordida dói mas<NEXT>não faz mal.",
    height = 200, weight = 69,   -- 2,0 m / 6,9 kg
  },
  ["ELECTABUZZ"] = {
    kind = "ELÉTRICO",
    text = "O corpo dele solta<NEXT>eletricidade sem<NEXT>parar. Chegar",
    text2 = "perto faz o seu<NEXT>cabelo ficar todo<NEXT>arrepiado.",
    height = 101, weight = 300,   -- 1,1 m / 30,0 kg
  },
  ["ELECTRODE"] = {
    kind = "BOLA",
    text = "Ele guarda uma<NEXT>quantidade enorme<NEXT>de eletricidade",
    text2 = "no corpo. Até um<NEXT>choque pequeno faz<NEXT>ele explodir.",
    height = 102, weight = 666,   -- 1,2 m / 66,6 kg
  },
  ["ELEKID"] = {
    kind = "ELÉTRICO",
    text = "Mesmo na pior das<NEXT>tempestades, este<NEXT>POKéMON brinca",
    text2 = "feliz se o trovão<NEXT>estrondar lá no<NEXT>céu.",
    height = 6, weight = 235,   -- 0,6 m / 23,5 kg
  },
  ["ENTEI"] = {
    kind = "VULCÃO",
    text = "Um POKéMON que<NEXT>corre pela terra.<NEXT>Dizem que nasce",
    text2 = "um a cada vez que<NEXT>um vulcão novo<NEXT>aparece.",
    height = 201, weight = 1980,   -- 2,1 m / 198,0 kg
  },
  ["ESPEON"] = {
    kind = "SOL",
    text = "Lendo as correntes<NEXT>de ar, ela prevê<NEXT>coisas como o",
    text2 = "tempo ou o próximo<NEXT>movimento do<NEXT>inimigo.",
    height = 9, weight = 265,   -- 0,9 m / 26,5 kg
  },
  ["EXEGGCUTE"] = {
    kind = "OVO",
    text = "Usando telepatia<NEXT>que só eles<NEXT>captam, sempre",
    text2 = "formam um cacho de<NEXT>seis EXEGGCUTE<NEXT>juntos.",
    height = 4, weight = 25,   -- 0,4 m / 2,5 kg
  },
  ["EXEGGUTOR"] = {
    kind = "COCO",
    text = "Se uma cabeça cai,<NEXT>ela manda um<NEXT>chamado telepático",
    text2 = "atrás de outras<NEXT>para formar um<NEXT>cacho de EXEGGCUTE",
    height = 200, weight = 1200,   -- 2,0 m / 120,0 kg
  },
  ["FARFETCH_D"] = {
    kind = "PATO BRAVO",
    text = "Se come o galho<NEXT>que carrega como<NEXT>reserva, ele sai",
    text2 = "correndo atrás<NEXT>de um galho<NEXT>novo.",
    height = 8, weight = 150,   -- 0,8 m / 15,0 kg
  },
  ["FEAROW"] = {
    kind = "BICO",
    text = "Ele usa com<NEXT>esperteza o bico<NEXT>fino e comprido",
    text2 = "para tirar e comer<NEXT>insetos pequenos<NEXT>que se escondem.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["FERALIGATR"] = {
    kind = "MANDÍBULA",
    text = "É difícil para ele<NEXT>aguentar o próprio<NEXT>peso fora d'água,",
    text2 = "então anda de<NEXT>quatro. Mesmo<NEXT>assim, é rápido.",
    height = 203, weight = 888,   -- 2,3 m / 88,8 kg
  },
  ["FLAAFFY"] = {
    kind = "LÃ",
    text = "A lã fofa dele<NEXT>guarda eletrici-<NEXT>dade com folga.",
    text2 = "A pele de borracha<NEXT>impede que ele<NEXT>leve choque.",
    height = 8, weight = 133,   -- 0,8 m / 13,3 kg
  },
  ["FLAREON"] = {
    kind = "CHAMA",
    text = "Ele arrepia a gola<NEXT>de pelo para<NEXT>baixar a",
    text2 = "temperatura do<NEXT>corpo, que chega a<NEXT>900 graus.",
    height = 9, weight = 250,   -- 0,9 m / 25,0 kg
  },
  ["FORRETRESS"] = {
    kind = "BICHO-SACO",
    text = "Ele fica preso na<NEXT>árvore dele sem se<NEXT>mexer. Espalha",
    text2 = "pedaços da casca<NEXT>dura para espantar<NEXT>os inimigos.",
    height = 102, weight = 1258,   -- 1,2 m / 125,8 kg
  },
  ["FURRET"] = {
    kind = "CORPOLONGO",
    text = "Não dá para saber<NEXT>onde o rabo dele<NEXT>começa. Apesar das",
    text2 = "pernas curtas, é<NEXT>rápido para caçar<NEXT>RATTATA.",
    height = 108, weight = 325,   -- 1,8 m / 32,5 kg
  },
  ["GASTLY"] = {
    kind = "GÁS",
    text = "O corpo fino dele<NEXT>é feito de gás.<NEXT>Ele consegue",
    text2 = "envolver um rival<NEXT>de qualquer<NEXT>tamanho e sufocar.",
    height = 103, weight = 1,   -- 1,3 m / 0,1 kg
  },
  ["GENGAR"] = {
    kind = "SOMBRA",
    text = "Para roubar a vida<NEXT>do alvo, ele entra<NEXT>na sombra da presa",
    text2 = "e espera calado<NEXT>por uma chance<NEXT>de agir.",
    height = 105, weight = 405,   -- 1,5 m / 40,5 kg
  },
  ["GEODUDE"] = {
    kind = "PEDRA",
    text = "Ele usa os braços<NEXT>para subir firme<NEXT>por trilhas de",
    text2 = "montanha íngreme.<NEXT>Se ficar bravo,<NEXT>soca para tudo.",
    height = 4, weight = 200,   -- 0,4 m / 20,0 kg
  },
  ["GIRAFARIG"] = {
    kind = "PESCOÇUDO",
    text = "O rabo dele, que<NEXT>também tem um<NEXT>cérebro pequeno,",
    text2 = "pode morder<NEXT>sozinho se sentir<NEXT>um cheiro gostoso.",
    height = 105, weight = 415,   -- 1,5 m / 41,5 kg
  },
  ["GLIGAR"] = {
    kind = "ESCORPIÃO",
    text = "Ele costuma ficar<NEXT>grudado em<NEXT>penhascos. Quando",
    text2 = "vê a presa, abre<NEXT>as asas e desce<NEXT>planando.",
    height = 101, weight = 648,   -- 1,1 m / 64,8 kg
  },
  ["GLOOM"] = {
    kind = "ERVA",
    text = "Ela solta um mel<NEXT>grudento parecido<NEXT>com baba. É doce,",
    text2 = "mas o cheiro é tão<NEXT>ruim que ninguém<NEXT>chega muito perto.",
    height = 8, weight = 86,   -- 0,8 m / 8,6 kg
  },
  ["GOLBAT"] = {
    kind = "MORCEGO",
    text = "Ele bebe mais de<NEXT>300 mililitros de<NEXT>sangue de uma vez.",
    text2 = "Se exagerar, fica<NEXT>pesado e voa<NEXT>atrapalhado.",
    height = 106, weight = 550,   -- 1,6 m / 55,0 kg
  },
  ["GOLDEEN"] = {
    kind = "PEIXE OURO",
    text = "Nadador forte, ele<NEXT>sobe correntezas<NEXT>rápidas sem parar",
    text2 = "e mantém a<NEXT>velocidade de<NEXT>cinco nós.",
    height = 6, weight = 150,   -- 0,6 m / 15,0 kg
  },
  ["GOLDUCK"] = {
    kind = "PATO",
    text = "Ele aparece perto<NEXT>da água ao<NEXT>anoitecer. Pode",
    text2 = "usar poderes da<NEXT>mente quando a<NEXT>testa dele brilha.",
    height = 107, weight = 766,   -- 1,7 m / 76,6 kg
  },
  ["GOLEM"] = {
    kind = "MEGATON",
    text = "Ele consegue se<NEXT>explodir sozinho.<NEXT>Usa essa força",
    text2 = "para pular de uma<NEXT>montanha para<NEXT>outra.",
    height = 104, weight = 3000,   -- 1,4 m / 300,0 kg
  },
  ["GRANBULL"] = {
    kind = "FADA",
    text = "Como as presas são<NEXT>pesadas demais,<NEXT>ele anda sempre de",
    text2 = "cabeça baixa. Mas<NEXT>a mordida dele é<NEXT>bem forte.",
    height = 104, weight = 487,   -- 1,4 m / 48,7 kg
  },
  ["GRAVELER"] = {
    kind = "PEDRA",
    text = "Anda devagar, e<NEXT>por isso rola para<NEXT>se mexer. Não dá",
    text2 = "atenção a nada que<NEXT>esteja no caminho<NEXT>dele.",
    height = 100, weight = 1050,   -- 1,0 m / 105,0 kg
  },
  ["GRIMER"] = {
    kind = "LODO",
    text = "Por onde GRIMER<NEXT>passa, sobram<NEXT>tantos germes que",
    text2 = "planta nenhuma<NEXT>volta a crescer<NEXT>ali.",
    height = 9, weight = 300,   -- 0,9 m / 30,0 kg
  },
  ["GROWLITHE"] = {
    kind = "FILHOTE",
    text = "Muito leal, ele<NEXT>late sem medo para<NEXT>qualquer rival",
    text2 = "para proteger o<NEXT>próprio treinador<NEXT>de qualquer mal.",
    height = 7, weight = 190,   -- 0,7 m / 19,0 kg
  },
  ["GYARADOS"] = {
    kind = "ATROZ",
    text = "Assim que aparece,<NEXT>ele sai destruindo<NEXT>tudo. Fica furioso",
    text2 = "até acabar com<NEXT>tudo que estiver<NEXT>em volta.",
    height = 605, weight = 2350,   -- 6,5 m / 235,0 kg
  },
  ["HAUNTER"] = {
    kind = "GÁS",
    text = "A língua dele é<NEXT>feita de gás. Quem<NEXT>for lambido começa",
    text2 = "a tremer sem parar<NEXT>até que a morte<NEXT>acabe chegando.",
    height = 106, weight = 1,   -- 1,6 m / 0,1 kg
  },
  ["HERACROSS"] = {
    kind = "UM CHIFRE",
    text = "Em geral é manso,<NEXT>mas se atrapalham<NEXT>ele no meio do mel",
    text2 = "ele enxota o<NEXT>invasor com o<NEXT>chifre.",
    height = 105, weight = 540,   -- 1,5 m / 54,0 kg
  },
  ["HITMONCHAN"] = {
    kind = "SOCO",
    text = "Os socos dele<NEXT>cortam o ar. Saem<NEXT>tão rápidos que um",
    text2 = "roçar de leve já<NEXT>pode causar<NEXT>queimadura.",
    height = 104, weight = 502,   -- 1,4 m / 50,2 kg
  },
  ["HITMONLEE"] = {
    kind = "CHUTE",
    text = "Se ele começa a<NEXT>chutar sem parar,<NEXT>as duas pernas se",
    text2 = "esticam mais ainda<NEXT>para acertar quem<NEXT>está fugindo.",
    height = 105, weight = 498,   -- 1,5 m / 49,8 kg
  },
  ["HITMONTOP"] = {
    kind = "BANANEIRA",
    text = "Ele solta chutes<NEXT>enquanto gira. Se<NEXT>girar bem rápido,",
    text2 = "pode acabar<NEXT>furando o chão e<NEXT>entrando nele.",
    height = 104, weight = 480,   -- 1,4 m / 48,0 kg
  },
  ["HOOTHOOT"] = {
    kind = "CORUJA",
    text = "Ele tem noção<NEXT>perfeita de tempo.<NEXT>Aconteça o que",
    text2 = "acontecer, marca o<NEXT>ritmo inclinando a<NEXT>cabeça certinho.",
    height = 7, weight = 212,   -- 0,7 m / 21,2 kg
  },
  ["HOPPIP"] = {
    kind = "ALGODÃO",
    text = "O corpo dele é tão<NEXT>leve que precisa<NEXT>se firmar bem no",
    text2 = "chão com os pés<NEXT>para o vento não<NEXT>levar ele.",
    height = 4, weight = 5,   -- 0,4 m / 0,5 kg
  },
  ["HORSEA"] = {
    kind = "DRAGÃO",
    text = "As nadadeiras<NEXT>grandes dele se<NEXT>mexem bem rápido",
    text2 = "e deixam ele nadar<NEXT>de costas olhando<NEXT>para a frente.",
    height = 4, weight = 80,   -- 0,4 m / 8,0 kg
  },
  ["HOUNDOOM"] = {
    kind = "SOMBRIO",
    text = "Ao ouvir o uivo<NEXT>arrepiante dele,<NEXT>outros POKéMON",
    text2 = "sentem calafrio e<NEXT>voltam correndo<NEXT>para os ninhos.",
    height = 104, weight = 350,   -- 1,4 m / 35,0 kg
  },
  ["HOUNDOUR"] = {
    kind = "SOMBRIO",
    text = "Para encurralar a<NEXT>presa, eles se<NEXT>avisam onde estão",
    text2 = "com latidos que só<NEXT>eles conseguem<NEXT>entender.",
    height = 6, weight = 108,   -- 0,6 m / 10,8 kg
  },
  ["HO_OH"] = {
    kind = "ARCO-ÍRIS",
    text = "Uma lenda diz que<NEXT>o corpo dele<NEXT>brilha em sete",
    text2 = "cores. Dizem que<NEXT>um arco-íris se<NEXT>forma quando voa.",
    height = 308, weight = 1990,   -- 3,8 m / 199,0 kg
  },
  ["HYPNO"] = {
    kind = "HIPNOSE",
    text = "Sempre com um<NEXT>pêndulo balançando<NEXT>no mesmo ritmo,",
    text2 = "ele dá sono em<NEXT>qualquer um que<NEXT>esteja por perto.",
    height = 106, weight = 756,   -- 1,6 m / 75,6 kg
  },
  ["IGGLYBUFF"] = {
    kind = "BALÃO",
    text = "O corpo dele é tão<NEXT>flexível e mole<NEXT>que ele fica",
    text2 = "quicando sem<NEXT>parar, a qualquer<NEXT>hora e lugar.",
    height = 3, weight = 10,   -- 0,3 m / 1,0 kg
  },
  ["IVYSAUR"] = {
    kind = "SEMENTE",
    text = "Se o botão nas<NEXT>costas começa a<NEXT>cheirar doce, é",
    text2 = "sinal de que a<NEXT>flor grande vai<NEXT>abrir logo.",
    height = 100, weight = 130,   -- 1,0 m / 13,0 kg
  },
  ["JIGGLYPUFF"] = {
    kind = "BALÃO",
    text = "Olhar nos olhos<NEXT>redondos e fofos<NEXT>dela faz com que",
    text2 = "cante uma melodia<NEXT>calma que faz o<NEXT>inimigo dormir.",
    height = 5, weight = 55,   -- 0,5 m / 5,5 kg
  },
  ["JOLTEON"] = {
    kind = "RAIO",
    text = "Cada pelo do corpo<NEXT>dele fica todo<NEXT>arrepiado quando",
    text2 = "ele fica<NEXT>carregado de<NEXT>eletricidade.",
    height = 8, weight = 245,   -- 0,8 m / 24,5 kg
  },
  ["JUMPLUFF"] = {
    kind = "ALGODÃO",
    text = "Ele viaja nos<NEXT>ventos da estação<NEXT>e espalha esporos",
    text2 = "de algodão pelo<NEXT>mundo todo para<NEXT>gerar mais filhos.",
    height = 8, weight = 30,   -- 0,8 m / 3,0 kg
  },
  ["JYNX"] = {
    kind = "HUMANOIDE",
    text = "Ela fala uma<NEXT>língua parecida<NEXT>com a das pessoas.",
    text2 = "Mas parece usar a<NEXT>dança para se<NEXT>comunicar.",
    height = 104, weight = 406,   -- 1,4 m / 40,6 kg
  },
  ["KABUTO"] = {
    kind = "MARISCO",
    text = "Este POKéMON viveu<NEXT>em tempos antigos.<NEXT>Em casos raros,",
    text2 = "já foi encontrado<NEXT>como fóssil<NEXT>vivo.",
    height = 5, weight = 115,   -- 0,5 m / 11,5 kg
  },
  ["KABUTOPS"] = {
    kind = "MARISCO",
    text = "Com garras<NEXT>afiadas, este<NEXT>POKéMON antigo e",
    text2 = "feroz rasga a<NEXT>presa e suga os<NEXT>líquidos do corpo.",
    height = 103, weight = 405,   -- 1,3 m / 40,5 kg
  },
  ["KADABRA"] = {
    kind = "PSI",
    text = "Quando usa os<NEXT>poderes, ele solta<NEXT>ondas alfa",
    text2 = "especiais que<NEXT>fazem as máquinas<NEXT>darem defeito.",
    height = 103, weight = 565,   -- 1,3 m / 56,5 kg
  },
  ["KAKUNA"] = {
    kind = "CASULO",
    text = "Desta forma ele<NEXT>vai crescer e<NEXT>virar adulto.",
    text2 = "Enquanto o corpo<NEXT>amolece, a casca<NEXT>de fora endurece.",
    height = 6, weight = 100,   -- 0,6 m / 10,0 kg
  },
  ["KANGASKHAN"] = {
    kind = "MÃE",
    text = "Para proteger o<NEXT>filhote, ela nunca<NEXT>desiste da luta,",
    text2 = "por mais<NEXT>ferida que<NEXT>esteja.",
    height = 202, weight = 800,   -- 2,2 m / 80,0 kg
  },
  ["KINGDRA"] = {
    kind = "DRAGÃO",
    text = "Ele dorme no fundo<NEXT>do mar para juntar<NEXT>energia. Dizem que",
    text2 = "provoca tornados<NEXT>na hora em que<NEXT>acorda.",
    height = 108, weight = 1520,   -- 1,8 m / 152,0 kg
  },
  ["KINGLER"] = {
    kind = "PINÇA",
    text = "As pinças dele<NEXT>crescem de um<NEXT>jeito esquisito.",
    text2 = "Se levantar rápido<NEXT>demais, perde o<NEXT>equilíbrio.",
    height = 103, weight = 600,   -- 1,3 m / 60,0 kg
  },
  ["KOFFING"] = {
    kind = "GÁS TÓXICO",
    text = "Os gases venenosos<NEXT>que ele guarda são<NEXT>um pouquinho mais",
    text2 = "leves que o ar, e<NEXT>por isso ele fica<NEXT>meio flutuando.",
    height = 6, weight = 10,   -- 0,6 m / 1,0 kg
  },
  ["KRABBY"] = {
    kind = "CARANGUEJO",
    text = "As pinças quebram<NEXT>com facilidade. Se<NEXT>ele perde uma,",
    text2 = "por algum motivo<NEXT>não consegue mais<NEXT>andar de lado.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["LANTURN"] = {
    kind = "LUZ",
    text = "Ele cega a presa<NEXT>com um clarão<NEXT>forte e engole ela",
    text2 = "de uma vez só,<NEXT>parada e sem<NEXT>conseguir reagir.",
    height = 102, weight = 225,   -- 1,2 m / 22,5 kg
  },
  ["LAPRAS"] = {
    kind = "TRANSPORTE",
    text = "Ela leva pessoas<NEXT>pelo mar nas<NEXT>costas. Se estiver",
    text2 = "de bom humor, pode<NEXT>cantar um som<NEXT>encantador.",
    height = 205, weight = 2200,   -- 2,5 m / 220,0 kg
  },
  ["LARVITAR"] = {
    kind = "PELE PEDRA",
    text = "Ele nasce bem<NEXT>fundo no subsolo.<NEXT>Só consegue sair",
    text2 = "depois de comer<NEXT>toda a terra em<NEXT>volta dele.",
    height = 6, weight = 720,   -- 0,6 m / 72,0 kg
  },
  ["LEDIAN"] = {
    kind = "5 ESTRELAS",
    text = "Os desenhos de<NEXT>estrela nas costas<NEXT>dele crescem ou",
    text2 = "diminuem conforme<NEXT>o número de<NEXT>estrelas no céu.",
    height = 104, weight = 356,   -- 1,4 m / 35,6 kg
  },
  ["LEDYBA"] = {
    kind = "5 ESTRELAS",
    text = "Quando o tempo<NEXT>esfria, muitos<NEXT>LEDYBA vêm de todo",
    text2 = "lado e se juntam<NEXT>para se aquecerem<NEXT>uns aos outros.",
    height = 100, weight = 108,   -- 1,0 m / 10,8 kg
  },
  ["LICKITUNG"] = {
    kind = "LAMBIDA",
    text = "A língua comprida<NEXT>dele, cheia de uma<NEXT>saliva grudenta,",
    text2 = "gruda em qualquer<NEXT>coisa, e por isso<NEXT>é bem útil.",
    height = 102, weight = 655,   -- 1,2 m / 65,5 kg
  },
  ["LUGIA"] = {
    kind = "MERGULHO",
    text = "Dizem que ele é o<NEXT>guardião dos<NEXT>mares. Contam que",
    text2 = "foi visto numa<NEXT>noite de<NEXT>tempestade.",
    height = 502, weight = 2160,   -- 5,2 m / 216,0 kg
  },
  ["MACHAMP"] = {
    kind = "SUPERFORÇA",
    text = "Ele usa os quatro<NEXT>braços fortes para<NEXT>prender o inimigo",
    text2 = "e depois joga a<NEXT>vítima para além<NEXT>do horizonte.",
    height = 106, weight = 1300,   -- 1,6 m / 130,0 kg
  },
  ["MACHOKE"] = {
    kind = "SUPERFORÇA",
    text = "Os músculos que<NEXT>cobrem o corpo<NEXT>dele transbordam",
    text2 = "força. Mesmo<NEXT>parado, passa uma<NEXT>sensação incrível.",
    height = 105, weight = 705,   -- 1,5 m / 70,5 kg
  },
  ["MACHOP"] = {
    kind = "SUPERFORÇA",
    text = "Ele adora treinar<NEXT>e ganhar músculo.<NEXT>Nunca fica",
    text2 = "satisfeito, mesmo<NEXT>treinando pesado o<NEXT>dia inteiro.",
    height = 8, weight = 195,   -- 0,8 m / 19,5 kg
  },
  ["MAGBY"] = {
    kind = "BRASA VIVA",
    text = "Ele é achado em<NEXT>crateras de<NEXT>vulcão. O corpo",
    text2 = "passa de 600<NEXT>graus, então não<NEXT>o subestime.",
    height = 7, weight = 214,   -- 0,7 m / 21,4 kg
  },
  ["MAGCARGO"] = {
    kind = "LAVA",
    text = "A casca frágil<NEXT>dele solta de vez<NEXT>em quando chamas",
    text2 = "fortes que<NEXT>circulam pelo<NEXT>corpo todo.",
    height = 8, weight = 550,   -- 0,8 m / 55,0 kg
  },
  ["MAGIKARP"] = {
    kind = "PEIXE",
    text = "Sem motivo nenhum,<NEXT>ele pula e se<NEXT>debate, o que",
    text2 = "facilita para<NEXT>PIDGEOTTO pegar<NEXT>ele no meio do ar.",
    height = 9, weight = 100,   -- 0,9 m / 10,0 kg
  },
  ["MAGMAR"] = {
    kind = "CUSPE-FOGO",
    text = "A superfície em<NEXT>chamas do corpo<NEXT>dele solta um",
    text2 = "brilho ondulante<NEXT>parecido com o do<NEXT>sol.",
    height = 103, weight = 445,   -- 1,3 m / 44,5 kg
  },
  ["MAGNEMITE"] = {
    kind = "ÍMÃ",
    text = "As peças nos lados<NEXT>do corpo dele<NEXT>geram energia",
    text2 = "antigravidade para<NEXT>mantê-lo lá no<NEXT>ar.",
    height = 3, weight = 60,   -- 0,3 m / 6,0 kg
  },
  ["MAGNETON"] = {
    kind = "ÍMÃ",
    text = "Os MAGNEMITE ficam<NEXT>unidos por um<NEXT>magnetismo tão",
    text2 = "forte que seca<NEXT>toda a umidade<NEXT>em volta.",
    height = 100, weight = 600,   -- 1,0 m / 60,0 kg
  },
  ["MANKEY"] = {
    kind = "MACACO",
    text = "É perigoso chegar<NEXT>perto se ele fica<NEXT>furioso sem motivo",
    text2 = "e não distingue<NEXT>mais amigo de<NEXT>inimigo.",
    height = 5, weight = 280,   -- 0,5 m / 28,0 kg
  },
  ["MANTINE"] = {
    kind = "PIPA",
    text = "Nadando solto em<NEXT>mar aberto, ele<NEXT>pode sair da água",
    text2 = "e voar sobre as<NEXT>ondas se pegar<NEXT>velocidade.",
    height = 201, weight = 2200,   -- 2,1 m / 220,0 kg
  },
  ["MAREEP"] = {
    kind = "LÃ",
    text = "A lã dele cresce<NEXT>sem parar. No<NEXT>verão, cai toda,",
    text2 = "mas volta a<NEXT>crescer em uma<NEXT>semana.",
    height = 6, weight = 78,   -- 0,6 m / 7,8 kg
  },
  ["MARILL"] = {
    kind = "RATO ÁGUA",
    text = "A ponta do rabo<NEXT>dele serve de boia<NEXT>e impede que ele",
    text2 = "afunde, mesmo numa<NEXT>correnteza bem<NEXT>brava.",
    height = 4, weight = 85,   -- 0,4 m / 8,5 kg
  },
  ["MAROWAK"] = {
    kind = "GUARDAOSSO",
    text = "Ele junta ossos de<NEXT>um lugar que<NEXT>ninguém conhece.",
    text2 = "Dizem que existe<NEXT>um cemitério de<NEXT>MAROWAK no mundo.",
    height = 100, weight = 450,   -- 1,0 m / 45,0 kg
  },
  ["MEGANIUM"] = {
    kind = "ERVA",
    text = "O sopro de<NEXT>MEGANIUM tem o<NEXT>poder de reviver",
    text2 = "mato e plantas<NEXT>mortas, e deixa<NEXT>tudo saudável.",
    height = 108, weight = 1005,   -- 1,8 m / 100,5 kg
  },
  ["MEOWTH"] = {
    kind = "ARRANHADOR",
    text = "Ele adora tudo<NEXT>que brilha. Gosta<NEXT>mais ainda de",
    text2 = "moedas, que ele<NEXT>cata e guarda<NEXT>escondido.",
    height = 4, weight = 42,   -- 0,4 m / 4,2 kg
  },
  ["METAPOD"] = {
    kind = "CASULO",
    text = "Ele se prepara<NEXT>para evoluir<NEXT>endurecendo a",
    text2 = "casca o máximo que<NEXT>dá, para proteger<NEXT>o corpo mole.",
    height = 7, weight = 99,   -- 0,7 m / 9,9 kg
  },
  ["MEW"] = {
    kind = "ESPÉCIE",
    text = "Dizem que o DNA<NEXT>dele tem o código<NEXT>genético de todos",
    text2 = "os POKéMON, então<NEXT>ele usa todo tipo<NEXT>de técnica.",
    height = 4, weight = 40,   -- 0,4 m / 4,0 kg
  },
  ["MEWTWO"] = {
    kind = "GENÉTICO",
    text = "Ele costuma ficar<NEXT>parado para poupar<NEXT>energia, e assim",
    text2 = "solta toda a força<NEXT>que tem na hora<NEXT>da batalha.",
    height = 200, weight = 1220,   -- 2,0 m / 122,0 kg
  },
  ["MILTANK"] = {
    kind = "VACA LEITE",
    text = "Se ela acabou de<NEXT>ter um filhote, o<NEXT>leite que produz",
    text2 = "vem com muito mais<NEXT>nutrientes que o<NEXT>normal.",
    height = 102, weight = 755,   -- 1,2 m / 75,5 kg
  },
  ["MISDREAVUS"] = {
    kind = "GRITO",
    text = "Ela adora morder e<NEXT>puxar o cabelo das<NEXT>pessoas por trás,",
    text2 = "sem avisar, só<NEXT>para ver a cara de<NEXT>susto delas.",
    height = 7, weight = 10,   -- 0,7 m / 1,0 kg
  },
  ["MOLTRES"] = {
    kind = "CHAMA",
    text = "Dizem que esta ave<NEXT>POKéMON lendária<NEXT>traz a primavera",
    text2 = "mais cedo para as<NEXT>terras de inverno<NEXT>que visita.",
    height = 200, weight = 600,   -- 2,0 m / 60,0 kg
  },
  ["MR__MIME"] = {
    kind = "BARREIRA",
    text = "As pontas dos<NEXT>dedos dele soltam<NEXT>um campo de força",
    text2 = "esquisito que<NEXT>endurece o ar e<NEXT>forma uma parede.",
    height = 103, weight = 545,   -- 1,3 m / 54,5 kg
  },
  ["MUK"] = {
    kind = "LODO",
    text = "O corpo dele é<NEXT>feito de um veneno<NEXT>forte. Encostar",
    text2 = "sem querer dá uma<NEXT>febre que obriga a<NEXT>ficar de cama.",
    height = 102, weight = 300,   -- 1,2 m / 30,0 kg
  },
  ["MURKROW"] = {
    kind = "ESCURIDÃO",
    text = "Dizem que ele<NEXT>atrai quem o caça<NEXT>para trilhas",
    text2 = "escuras da<NEXT>montanha, onde o<NEXT>inimigo se perde.",
    height = 5, weight = 21,   -- 0,5 m / 2,1 kg
  },
  ["NATU"] = {
    kind = "PASSARINHO",
    text = "Ele costuma<NEXT>procurar comida no<NEXT>chão, mas às vezes",
    text2 = "sobe nos galhos<NEXT>para bicar os<NEXT>brotos.",
    height = 2, weight = 20,   -- 0,2 m / 2,0 kg
  },
  ["NIDOKING"] = {
    kind = "BROCA",
    text = "O rabo dele é<NEXT>grosso e forte. Se<NEXT>prender um",
    text2 = "inimigo, quebra a<NEXT>coluna da vítima<NEXT>com facilidade.",
    height = 104, weight = 620,   -- 1,4 m / 62,0 kg
  },
  ["NIDOQUEEN"] = {
    kind = "BROCA",
    text = "Ela usa o corpo<NEXT>áspero e cheio de<NEXT>escamas para tapar",
    text2 = "a entrada do ninho<NEXT>e proteger os<NEXT>filhotes.",
    height = 103, weight = 600,   -- 1,3 m / 60,0 kg
  },
  ["NIDORAN_F"] = {
    kind = "ESPINHO",
    text = "Apesar de não ser<NEXT>muito briguenta,<NEXT>ela castiga o",
    text2 = "inimigo com<NEXT>espinhos venenosos<NEXT>se for ameaçada.",
    height = 4, weight = 70,   -- 0,4 m / 7,0 kg
  },
  ["NIDORAN_M"] = {
    kind = "ESPINHO",
    text = "Ele levanta as<NEXT>orelhas grandes<NEXT>para conferir o",
    text2 = "que há em volta.<NEXT>Ataca primeiro se<NEXT>sentir perigo.",
    height = 5, weight = 90,   -- 0,5 m / 9,0 kg
  },
  ["NIDORINA"] = {
    kind = "ESPINHO",
    text = "Ela é calma e<NEXT>cuidadosa. Como o<NEXT>chifre dela cresce",
    text2 = "devagar, prefere<NEXT>não entrar em<NEXT>briga.",
    height = 8, weight = 200,   -- 0,8 m / 20,0 kg
  },
  ["NIDORINO"] = {
    kind = "ESPINHO",
    text = "Esquentado, ele<NEXT>espeta o inimigo<NEXT>com o chifre para",
    text2 = "injetar um veneno<NEXT>forte quando fica<NEXT>agitado.",
    height = 9, weight = 195,   -- 0,9 m / 19,5 kg
  },
  ["NINETALES"] = {
    kind = "RAPOSA",
    text = "Os nove rabos<NEXT>lindos dela estão<NEXT>cheios de uma",
    text2 = "energia incrível<NEXT>que a manteria<NEXT>viva por mil anos.",
    height = 101, weight = 199,   -- 1,1 m / 19,9 kg
  },
  ["NOCTOWL"] = {
    kind = "CORUJA",
    text = "Quando precisa<NEXT>pensar, ele gira a<NEXT>cabeça 180 graus",
    text2 = "para aguçar o<NEXT>poder de<NEXT>raciocínio.",
    height = 106, weight = 408,   -- 1,6 m / 40,8 kg
  },
  ["OCTILLERY"] = {
    kind = "JATO",
    text = "Por instinto, ele<NEXT>se enfia em furos<NEXT>de pedra. Com",
    text2 = "sono, ele rouba o<NEXT>ninho de outro<NEXT>OCTILLERY.",
    height = 9, weight = 285,   -- 0,9 m / 28,5 kg
  },
  ["ODDISH"] = {
    kind = "ERVA",
    text = "Se pega luz de<NEXT>lua, ela começa a<NEXT>se mexer. Anda",
    text2 = "longe à noite para<NEXT>espalhar as<NEXT>sementes dela.",
    height = 5, weight = 54,   -- 0,5 m / 5,4 kg
  },
  ["OMANYTE"] = {
    kind = "ESPIRAL",
    text = "Dizem que este<NEXT>POKéMON dos tempos<NEXT>antigos navegava",
    text2 = "o mar torcendo com<NEXT>jeito os dez<NEXT>tentáculos dele.",
    height = 4, weight = 75,   -- 0,4 m / 7,5 kg
  },
  ["OMASTAR"] = {
    kind = "ESPIRAL",
    text = "Depois que enrola<NEXT>na presa, ele não<NEXT>solta mais. Come",
    text2 = "rasgando ela com<NEXT>as presas<NEXT>afiadas.",
    height = 100, weight = 350,   -- 1,0 m / 35,0 kg
  },
  ["ONIX"] = {
    kind = "COBRAPEDRA",
    text = "Ele fura o chão<NEXT>rápido, a 80 km<NEXT>por hora, se",
    text2 = "contorcendo e<NEXT>torcendo o corpo<NEXT>enorme e áspero.",
    height = 808, weight = 2100,   -- 8,8 m / 210,0 kg
  },
  ["PARAS"] = {
    kind = "COGUMELO",
    text = "Conforme o corpo<NEXT>dele cresce, um<NEXT>cogumelo oriental",
    text2 = "chamado tochukaso<NEXT>começa a brotar<NEXT>nas costas dele.",
    height = 3, weight = 54,   -- 0,3 m / 5,4 kg
  },
  ["PARASECT"] = {
    kind = "COGUMELO",
    text = "Quanto maior fica<NEXT>o cogumelo nas<NEXT>costas dele, mais",
    text2 = "fortes são os<NEXT>esporos que ele<NEXT>espalha.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["PERSIAN"] = {
    kind = "GATO FINO",
    text = "Os músculos ágeis<NEXT>dele deixam que<NEXT>ande sem fazer",
    text2 = "barulho nenhum.<NEXT>Ele ataca num<NEXT>instante.",
    height = 100, weight = 320,   -- 1,0 m / 32,0 kg
  },
  ["PHANPY"] = {
    kind = "NARIZLONGO",
    text = "Para mostrar<NEXT>carinho, ele dá<NEXT>topadinhas com a",
    text2 = "tromba. Mas é tão<NEXT>forte que pode te<NEXT>jogar longe.",
    height = 5, weight = 335,   -- 0,5 m / 33,5 kg
  },
  ["PICHU"] = {
    kind = "RATINHO",
    text = "Apesar de pequeno,<NEXT>ele dá choque até<NEXT>em gente adulta.",
    text2 = "Mas, quando faz<NEXT>isso, ele mesmo se<NEXT>assusta.",
    height = 3, weight = 20,   -- 0,3 m / 2,0 kg
  },
  ["PIDGEOT"] = {
    kind = "PÁSSARO",
    text = "Ele abre bem as<NEXT>asas lindas dele<NEXT>para assustar os",
    text2 = "inimigos. Consegue<NEXT>voar na velocidade<NEXT>Mach 2.",
    height = 105, weight = 395,   -- 1,5 m / 39,5 kg
  },
  ["PIDGEOTTO"] = {
    kind = "PÁSSARO",
    text = "Ele imobiliza a<NEXT>presa com as<NEXT>garras bem",
    text2 = "fortes e a leva<NEXT>por mais de 100 km<NEXT>até o ninho.",
    height = 101, weight = 300,   -- 1,1 m / 30,0 kg
  },
  ["PIDGEY"] = {
    kind = "PASSARINHO",
    text = "Comum em campos e<NEXT>florestas, ele é<NEXT>bem manso e enxota",
    text2 = "os inimigos<NEXT>batendo as asas<NEXT>para jogar areia.",
    height = 3, weight = 18,   -- 0,3 m / 1,8 kg
  },
  ["PIKACHU"] = {
    kind = "RATO",
    text = "Ele levanta o<NEXT>rabo para conferir<NEXT>o que há em volta.",
    text2 = "Às vezes um raio<NEXT>cai no rabo dele<NEXT>nessa posição.",
    height = 4, weight = 60,   -- 0,4 m / 6,0 kg
  },
  ["PILOSWINE"] = {
    kind = "SUÍNO",
    text = "Se ele avança<NEXT>sobre um inimigo,<NEXT>os pelos das",
    text2 = "costas ficam em<NEXT>pé. Ele é muito<NEXT>sensível a som.",
    height = 101, weight = 558,   -- 1,1 m / 55,8 kg
  },
  ["PINECO"] = {
    kind = "BICHO-SACO",
    text = "Ele fica pendurado<NEXT>esperando um<NEXT>inseto voador",
    text2 = "chegar perto. Não<NEXT>se mexe muito por<NEXT>conta própria.",
    height = 6, weight = 72,   -- 0,6 m / 7,2 kg
  },
  ["PINSIR"] = {
    kind = "BESOURO",
    text = "Ele balança os<NEXT>chifres compridos<NEXT>com força para",
    text2 = "atacar. No frio,<NEXT>se esconde no<NEXT>fundo das matas.",
    height = 105, weight = 550,   -- 1,5 m / 55,0 kg
  },
  ["POLITOED"] = {
    kind = "SAPO",
    text = "Sempre que três ou<NEXT>mais deles se<NEXT>juntam, cantam bem",
    text2 = "alto, com uma voz<NEXT>que parece um<NEXT>berro.",
    height = 101, weight = 339,   -- 1,1 m / 33,9 kg
  },
  ["POLIWAG"] = {
    kind = "GIRINO",
    text = "A direção do<NEXT>espiral da barriga<NEXT>muda conforme a",
    text2 = "região. Acham que<NEXT>o equador tem a<NEXT>ver com isso.",
    height = 6, weight = 124,   -- 0,6 m / 12,4 kg
  },
  ["POLIWHIRL"] = {
    kind = "GIRINO",
    text = "A pele da maior<NEXT>parte do corpo<NEXT>dele é úmida. Mas",
    text2 = "a pele do espiral<NEXT>da barriga é<NEXT>lisinha.",
    height = 100, weight = 200,   -- 1,0 m / 20,0 kg
  },
  ["POLIWRATH"] = {
    kind = "GIRINO",
    text = "Apesar de ser um<NEXT>nadador hábil e<NEXT>cheio de energia,",
    text2 = "que usa todos os<NEXT>músculos, ele vive<NEXT>em terra seca.",
    height = 103, weight = 540,   -- 1,3 m / 54,0 kg
  },
  ["PONYTA"] = {
    kind = "CAVALOFOGO",
    text = "As patas de trás,<NEXT>com cascos mais<NEXT>duros que diamante",
    text2 = "coiceiam qualquer<NEXT>presença que ele<NEXT>sinta atrás.",
    height = 100, weight = 300,   -- 1,0 m / 30,0 kg
  },
  ["PORYGON"] = {
    kind = "VIRTUAL",
    text = "Um POKéMON feito<NEXT>pelo homem, fruto<NEXT>de pesquisa. Ele",
    text2 = "só tem movimentos<NEXT>básicos na<NEXT>programação.",
    height = 8, weight = 365,   -- 0,8 m / 36,5 kg
  },
  ["PORYGON2"] = {
    kind = "VIRTUAL",
    text = "Mais pesquisa<NEXT>melhorou as<NEXT>habilidades dele.",
    text2 = "Às vezes ele faz<NEXT>movimentos que<NEXT>ninguém programou.",
    height = 6, weight = 325,   -- 0,6 m / 32,5 kg
  },
  ["PRIMEAPE"] = {
    kind = "MACACO",
    text = "Ele fica furioso<NEXT>só de perceber<NEXT>alguém olhando",
    text2 = "para ele. Persegue<NEXT>quem cruzar com o<NEXT>olhar dele.",
    height = 100, weight = 320,   -- 1,0 m / 32,0 kg
  },
  ["PSYDUCK"] = {
    kind = "PATO",
    text = "Quando a dor de<NEXT>cabeça crônica<NEXT>dele aperta, pode",
    text2 = "mostrar poderes<NEXT>estranhos. Depois<NEXT>não lembra de nada",
    height = 8, weight = 196,   -- 0,8 m / 19,6 kg
  },
  ["PUPITAR"] = {
    kind = "CASCA DURA",
    text = "Mesmo lacrado na<NEXT>casca, ele se mexe<NEXT>à vontade. Duro e",
    text2 = "veloz, tem um<NEXT>poder de destruir<NEXT>impressionante.",
    height = 102, weight = 1520,   -- 1,2 m / 152,0 kg
  },
  ["QUAGSIRE"] = {
    kind = "PEIXE ÁGUA",
    text = "Por causa do jeito<NEXT>relaxado e<NEXT>despreocupado, ele",
    text2 = "vive batendo a<NEXT>cabeça em pedras e<NEXT>cascos de barco.",
    height = 104, weight = 750,   -- 1,4 m / 75,0 kg
  },
  ["QUILAVA"] = {
    kind = "VULCÃO",
    text = "Este POKéMON é<NEXT>todo coberto por<NEXT>pelos que não",
    text2 = "pegam fogo. Ele<NEXT>aguenta qualquer<NEXT>ataque de fogo.",
    height = 9, weight = 190,   -- 0,9 m / 19,0 kg
  },
  ["QWILFISH"] = {
    kind = "BALÃO",
    text = "Os espinhos<NEXT>pequenos que<NEXT>cobrem o corpo",
    text2 = "vieram das escamas<NEXT>e injetam um<NEXT>veneno que desmaia",
    height = 5, weight = 39,   -- 0,5 m / 3,9 kg
  },
  ["RAICHU"] = {
    kind = "RATO",
    text = "Se as bolsas de<NEXT>eletricidade das<NEXT>bochechas ficam",
    text2 = "cheias, as duas<NEXT>orelhas dele ficam<NEXT>em pé.",
    height = 8, weight = 300,   -- 0,8 m / 30,0 kg
  },
  ["RAIKOU"] = {
    kind = "TROVÃO",
    text = "Um POKéMON que<NEXT>corre pela terra<NEXT>soltando um grito",
    text2 = "que parece o<NEXT>estrondo de um<NEXT>trovão.",
    height = 109, weight = 1780,   -- 1,9 m / 178,0 kg
  },
  ["RAPIDASH"] = {
    kind = "CAVALOFOGO",
    text = "Com uma aceleração<NEXT>incrível, ele<NEXT>chega à velocidade",
    text2 = "máxima de 240 km<NEXT>por hora em só dez<NEXT>passadas.",
    height = 107, weight = 950,   -- 1,7 m / 95,0 kg
  },
  ["RATICATE"] = {
    kind = "RATO",
    text = "Os bigodes ajudam<NEXT>ele a manter o<NEXT>equilíbrio. Como",
    text2 = "os dentes crescem<NEXT>sem parar, ele rói<NEXT>para desgastar.",
    height = 7, weight = 185,   -- 0,7 m / 18,5 kg
  },
  ["RATTATA"] = {
    kind = "RATO",
    text = "Ele vive em<NEXT>qualquer lugar que<NEXT>tenha comida, e",
    text2 = "passa o dia todo<NEXT>catando algo para<NEXT>comer.",
    height = 3, weight = 35,   -- 0,3 m / 3,5 kg
  },
  ["REMORAID"] = {
    kind = "JATO",
    text = "Usando a nadadeira<NEXT>das costas como<NEXT>ventosa, ele gruda",
    text2 = "embaixo de um<NEXT>MANTINE para catar<NEXT>as sobras.",
    height = 6, weight = 120,   -- 0,6 m / 12,0 kg
  },
  ["RHYDON"] = {
    kind = "BROCA",
    text = "O cérebro dele se<NEXT>desenvolveu quando<NEXT>passou a andar nas",
    text2 = "patas de trás. O<NEXT>couro grosso o<NEXT>protege no magma.",
    height = 109, weight = 1200,   -- 1,9 m / 120,0 kg
  },
  ["RHYHORN"] = {
    kind = "ESPINHOS",
    text = "Ele não liga se<NEXT>tem alguma coisa<NEXT>no caminho. Só",
    text2 = "avança e destrói<NEXT>todos os<NEXT>obstáculos.",
    height = 100, weight = 1150,   -- 1,0 m / 115,0 kg
  },
  ["SANDSHREW"] = {
    kind = "RATO",
    text = "Como não gosta de<NEXT>água, ele vive em<NEXT>tocas fundas de",
    text2 = "lugares secos. Se<NEXT>enrola numa bola<NEXT>num instante.",
    height = 6, weight = 120,   -- 0,6 m / 12,0 kg
  },
  ["SANDSLASH"] = {
    kind = "RATO",
    text = "Se cava num ritmo<NEXT>incrível, ele pode<NEXT>quebrar os",
    text2 = "espinhos e as<NEXT>garras. Tudo volta<NEXT>a crescer num dia.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["SCIZOR"] = {
    kind = "TESOURA",
    text = "As asas dele não<NEXT>servem para voar.<NEXT>Ele bate elas bem",
    text2 = "rápido para<NEXT>ajustar a própria<NEXT>temperatura.",
    height = 108, weight = 1180,   -- 1,8 m / 118,0 kg
  },
  ["SCYTHER"] = {
    kind = "LOUVA-DEUS",
    text = "Quando se mexe,<NEXT>deixa só um vulto.<NEXT>Escondido no mato,",
    text2 = "as cores de<NEXT>camuflagem deixam<NEXT>ele invisível.",
    height = 105, weight = 560,   -- 1,5 m / 56,0 kg
  },
  ["SEADRA"] = {
    kind = "DRAGÃO",
    text = "As pontas das<NEXT>nadadeiras soltam<NEXT>veneno. Nadadeiras",
    text2 = "e ossos dele valem<NEXT>muito na medicina<NEXT>de ervas.",
    height = 102, weight = 250,   -- 1,2 m / 25,0 kg
  },
  ["SEAKING"] = {
    kind = "PEIXE OURO",
    text = "Com o chifre, ele<NEXT>fura pedras no<NEXT>fundo do rio e faz",
    text2 = "ninhos para a<NEXT>correnteza não<NEXT>levar os ovos.",
    height = 103, weight = 390,   -- 1,3 m / 39,0 kg
  },
  ["SEEL"] = {
    kind = "FOCA",
    text = "De dia, costuma<NEXT>ser visto dormindo<NEXT>em água rasa.",
    text2 = "As narinas dele se<NEXT>fecham enquanto<NEXT>ele nada.",
    height = 101, weight = 900,   -- 1,1 m / 90,0 kg
  },
  ["SENTRET"] = {
    kind = "VIGIA",
    text = "Ele se apoia no<NEXT>rabo para enxergar<NEXT>longe. Se vê um",
    text2 = "inimigo, grita bem<NEXT>alto para avisar<NEXT>os outros.",
    height = 8, weight = 60,   -- 0,8 m / 6,0 kg
  },
  ["SHELLDER"] = {
    kind = "BIVALVE",
    text = "Grãos de areia<NEXT>presos na casca se<NEXT>misturam com os",
    text2 = "líquidos do corpo<NEXT>e formam pérolas<NEXT>lindas.",
    height = 3, weight = 40,   -- 0,3 m / 4,0 kg
  },
  ["SHUCKLE"] = {
    kind = "MOFO",
    text = "Ele guarda FRUTAS<NEXT>dentro da casca.<NEXT>Para não ser",
    text2 = "atacado, se<NEXT>esconde sob pedras<NEXT>e fica imóvel.",
    height = 6, weight = 205,   -- 0,6 m / 20,5 kg
  },
  ["SKARMORY"] = {
    kind = "AVE DE AÇO",
    text = "Depois de nascer<NEXT>em moitas de<NEXT>espinho, as asas",
    text2 = "dos filhotes ficam<NEXT>duras por causa<NEXT>dos arranhões.",
    height = 107, weight = 505,   -- 1,7 m / 50,5 kg
  },
  ["SKIPLOOM"] = {
    kind = "ALGODÃO",
    text = "Ele abre as<NEXT>pétalas para<NEXT>absorver a luz do",
    text2 = "sol. Também flutua<NEXT>no ar para chegar<NEXT>mais perto dele.",
    height = 6, weight = 10,   -- 0,6 m / 1,0 kg
  },
  ["SLOWBRO"] = {
    kind = "ERMITÃO",
    text = "Já lerdo por<NEXT>natureza, ele<NEXT>perdeu a noção",
    text2 = "de dor por causa<NEXT>do veneno que<NEXT>SHELLDER solta.",
    height = 106, weight = 785,   -- 1,6 m / 78,5 kg
  },
  ["SLOWKING"] = {
    kind = "REAL",
    text = "Quando a cabeça<NEXT>foi mordida, o<NEXT>veneno entrou na",
    text2 = "cabeça do SLOWPOKE<NEXT>e liberou um poder<NEXT>extraordinário.",
    height = 200, weight = 795,   -- 2,0 m / 79,5 kg
  },
  ["SLOWPOKE"] = {
    kind = "LERDO",
    text = "Uma seiva doce<NEXT>escorre da ponta<NEXT>do rabo dele.",
    text2 = "Não alimenta, mas<NEXT>é gostoso de<NEXT>mastigar.",
    height = 102, weight = 360,   -- 1,2 m / 36,0 kg
  },
  ["SLUGMA"] = {
    kind = "LAVA",
    text = "Comum em áreas de<NEXT>vulcão, ele anda<NEXT>devagar por aí",
    text2 = "sempre<NEXT>procurando lugares<NEXT>quentes.",
    height = 7, weight = 350,   -- 0,7 m / 35,0 kg
  },
  ["SMEARGLE"] = {
    kind = "PINTOR",
    text = "Depois de adulto,<NEXT>ele costuma deixar<NEXT>que os colegas",
    text2 = "carimbem<NEXT>pegadas nas<NEXT>costas dele.",
    height = 102, weight = 580,   -- 1,2 m / 58,0 kg
  },
  ["SMOOCHUM"] = {
    kind = "BEIJO",
    text = "Ela vive<NEXT>balançando a<NEXT>cabeça devagar,",
    text2 = "para a frente e<NEXT>para trás, como se<NEXT>fosse dar um beijo",
    height = 4, weight = 60,   -- 0,4 m / 6,0 kg
  },
  ["SNEASEL"] = {
    kind = "GARRA",
    text = "Cruel por<NEXT>natureza, ele<NEXT>expulsa os PIDGEY",
    text2 = "dos ninhos e se<NEXT>farta com os ovos<NEXT>que ficam.",
    height = 9, weight = 280,   -- 0,9 m / 28,0 kg
  },
  ["SNORLAX"] = {
    kind = "DORMINDO",
    text = "O suco do estômago<NEXT>dele dissolve<NEXT>qualquer veneno.",
    text2 = "Ele consegue até<NEXT>comer coisas do<NEXT>chão.",
    height = 201, weight = 4600,   -- 2,1 m / 460,0 kg
  },
  ["SNUBBULL"] = {
    kind = "FADA",
    text = "Ele é ativo e<NEXT>brincalhão. Muita<NEXT>mulher gosta de",
    text2 = "brincar com ele<NEXT>por causa do jeito<NEXT>carinhoso dele.",
    height = 6, weight = 78,   -- 0,6 m / 7,8 kg
  },
  ["SPEAROW"] = {
    kind = "PASSARINHO",
    text = "Muito ciumento do<NEXT>território dele,<NEXT>bate as asas",
    text2 = "curtas sem parar<NEXT>para voar de um<NEXT>lado a outro.",
    height = 3, weight = 20,   -- 0,3 m / 2,0 kg
  },
  ["SPINARAK"] = {
    kind = "CUSPE-FIO",
    text = "Ele tece a teia<NEXT>com um fio fino<NEXT>mas resistente.",
    text2 = "Depois espera com<NEXT>paciência a presa<NEXT>cair nela.",
    height = 5, weight = 85,   -- 0,5 m / 8,5 kg
  },
  ["SQUIRTLE"] = {
    kind = "TARTARUGA",
    text = "A casca, que<NEXT>endurece logo<NEXT>depois que ele",
    text2 = "nasce, é firme. Se<NEXT>você cutucar, ela<NEXT>volta ao lugar.",
    height = 5, weight = 90,   -- 0,5 m / 9,0 kg
  },
  ["STANTLER"] = {
    kind = "CHIFRUDO",
    text = "Quem fica olhando<NEXT>os chifres dele<NEXT>vai aos poucos",
    text2 = "perdendo os<NEXT>sentidos e não<NEXT>para em pé.",
    height = 104, weight = 712,   -- 1,4 m / 71,2 kg
  },
  ["STARMIE"] = {
    kind = "MISTERIOSO",
    text = "Não importa o<NEXT>ambiente onde<NEXT>vive: o corpo dele",
    text2 = "cresce formando<NEXT>uma figura<NEXT>simétrica.",
    height = 101, weight = 800,   -- 1,1 m / 80,0 kg
  },
  ["STARYU"] = {
    kind = "ESTRELA",
    text = "Mesmo que o corpo<NEXT>seja rasgado, ele<NEXT>se regenera desde",
    text2 = "que o núcleo<NEXT>brilhante do meio<NEXT>fique inteiro.",
    height = 8, weight = 345,   -- 0,8 m / 34,5 kg
  },
  ["STEELIX"] = {
    kind = "COBRA AÇO",
    text = "Dizem que, se um<NEXT>ONIX vive mais de<NEXT>cem anos, o corpo",
    text2 = "dele muda e fica<NEXT>parecido com<NEXT>diamante.",
    height = 902, weight = 4000,   -- 9,2 m / 400,0 kg
  },
  ["SUDOWOODO"] = {
    kind = "IMITAÇÃO",
    text = "Ele se disfarça de<NEXT>árvore para não<NEXT>ser atacado. Odeia",
    text2 = "água, então some<NEXT>assim que começa a<NEXT>chover.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["SUICUNE"] = {
    kind = "AURORA",
    text = "Este POKéMON corre<NEXT>pela terra. Dizem<NEXT>que ventos do",
    text2 = "norte sopram<NEXT>sempre que ele<NEXT>aparece.",
    height = 200, weight = 1870,   -- 2,0 m / 187,0 kg
  },
  ["SUNFLORA"] = {
    kind = "SOL",
    text = "De dia, ela corre<NEXT>para tudo quanto é<NEXT>lado, agitada. Mas",
    text2 = "para de vez<NEXT>quando o sol<NEXT>se põe.",
    height = 8, weight = 85,   -- 0,8 m / 8,5 kg
  },
  ["SUNKERN"] = {
    kind = "SEMENTE",
    text = "Ele vive bebendo<NEXT>só o orvalho de<NEXT>baixo das folhas.",
    text2 = "Dizem que não come<NEXT>mais nada além<NEXT>disso.",
    height = 3, weight = 18,   -- 0,3 m / 1,8 kg
  },
  ["SWINUB"] = {
    kind = "PORCO",
    text = "Se sente um cheiro<NEXT>convidativo, ele<NEXT>dispara de cabeça",
    text2 = "para achar de onde<NEXT>vem aquele<NEXT>cheiro.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["TANGELA"] = {
    kind = "CIPÓ",
    text = "Ele enrola nos<NEXT>cipós dele tudo<NEXT>que se mexe. Se",
    text2 = "você for preso, o<NEXT>tremor leve deles<NEXT>faz cócegas.",
    height = 100, weight = 350,   -- 1,0 m / 35,0 kg
  },
  ["TAUROS"] = {
    kind = "TOUROBRAVO",
    text = "Depois de aumentar<NEXT>a vontade de lutar<NEXT>se chicoteando com",
    text2 = "os três rabos, ele<NEXT>avança a toda<NEXT>velocidade.",
    height = 104, weight = 884,   -- 1,4 m / 88,4 kg
  },
  ["TEDDIURSA"] = {
    kind = "URSINHO",
    text = "Antes que a comida<NEXT>fique escassa no<NEXT>inverno, ele tem o",
    text2 = "costume de guardar<NEXT>comida em vários<NEXT>esconderijos.",
    height = 6, weight = 88,   -- 0,6 m / 8,8 kg
  },
  ["TENTACOOL"] = {
    kind = "ÁGUA-VIVA",
    text = "Ele boia sem rumo<NEXT>nas ondas. Como é<NEXT>difícil de ver na",
    text2 = "água, ninguém<NEXT>percebe até que<NEXT>ele ferroe.",
    height = 9, weight = 455,   -- 0,9 m / 45,5 kg
  },
  ["TENTACRUEL"] = {
    kind = "ÁGUA-VIVA",
    text = "Na luta, ele<NEXT>estica os 80<NEXT>tentáculos dele",
    text2 = "para prender o<NEXT>rival dentro de<NEXT>uma rede venenosa.",
    height = 106, weight = 550,   -- 1,6 m / 55,0 kg
  },
  ["TOGEPI"] = {
    kind = "ESPINHOS",
    text = "Um ditado diz que<NEXT>a felicidade chega<NEXT>para quem fizer",
    text2 = "um TOGEPI<NEXT>dormindo ficar<NEXT>de pé.",
    height = 3, weight = 15,   -- 0,3 m / 1,5 kg
  },
  ["TOGETIC"] = {
    kind = "FELICIDADE",
    text = "Ele fica triste se<NEXT>não está perto de<NEXT>gente boa. Flutua",
    text2 = "no ar sem<NEXT>precisar mexer<NEXT>as asas.",
    height = 6, weight = 32,   -- 0,6 m / 3,2 kg
  },
  ["TOTODILE"] = {
    kind = "MANDÍBULA",
    text = "Ele é pequeno, mas<NEXT>é bruto e durão.<NEXT>Não pensa duas",
    text2 = "vezes antes de dar<NEXT>uma mordida em<NEXT>tudo que se mexe.",
    height = 6, weight = 95,   -- 0,6 m / 9,5 kg
  },
  ["TYPHLOSION"] = {
    kind = "VULCÃO",
    text = "Ele tem um golpe<NEXT>secreto e<NEXT>devastador. Ele",
    text2 = "esfrega os pelos<NEXT>em brasa e causa<NEXT>explosões enormes.",
    height = 107, weight = 795,   -- 1,7 m / 79,5 kg
  },
  ["TYRANITAR"] = {
    kind = "ARMADURA",
    text = "Muito forte, ele<NEXT>consegue mudar a<NEXT>paisagem. Tem um",
    text2 = "jeito insolente e<NEXT>não liga para<NEXT>os outros.",
    height = 200, weight = 2020,   -- 2,0 m / 202,0 kg
  },
  ["TYROGUE"] = {
    kind = "BRIGA",
    text = "Mesmo pequeno, ele<NEXT>não pode ser<NEXT>ignorado: soca",
    text2 = "qualquer alvo à<NEXT>mão, sem avisar<NEXT>ninguém.",
    height = 7, weight = 210,   -- 0,7 m / 21,0 kg
  },
  ["UMBREON"] = {
    kind = "LUAR",
    text = "Quando a noite<NEXT>cai, os anéis do<NEXT>corpo dele começam",
    text2 = "a brilhar e metem<NEXT>medo em quem<NEXT>estiver por perto.",
    height = 100, weight = 270,   -- 1,0 m / 27,0 kg
  },
  ["UNOWN"] = {
    kind = "SÍMBOLO",
    text = "O corpo chato e<NEXT>fino dele vive<NEXT>grudado na parede.",
    text2 = "O formato dele<NEXT>parece ter algum<NEXT>significado.",
    height = 5, weight = 50,   -- 0,5 m / 5,0 kg
  },
  ["URSARING"] = {
    kind = "HIBERNANTE",
    text = "Com a capacidade<NEXT>de distinguir<NEXT>qualquer cheiro,",
    text2 = "ele sempre acha<NEXT>comida enterrada<NEXT>bem no fundo.",
    height = 108, weight = 1258,   -- 1,8 m / 125,8 kg
  },
  ["VAPOREON"] = {
    kind = "JATO BOLHA",
    text = "Ela prefere praias<NEXT>bonitas. Como as<NEXT>células dela são",
    text2 = "parecidas com água<NEXT>ela poderia se<NEXT>derreter no mar.",
    height = 100, weight = 290,   -- 1,0 m / 29,0 kg
  },
  ["VENOMOTH"] = {
    kind = "MARIPOSA",
    text = "O pó das asas dele<NEXT>é venenoso quando<NEXT>tem cor escura.",
    text2 = "Se for claro,<NEXT>causa paralisia<NEXT>em quem tocar.",
    height = 105, weight = 125,   -- 1,5 m / 12,5 kg
  },
  ["VENONAT"] = {
    kind = "INSETO",
    text = "Escorre veneno do<NEXT>corpo dele todo.<NEXT>De noite ele pega",
    text2 = "e come insetos<NEXT>pequenos atraídos<NEXT>pela luz.",
    height = 100, weight = 300,   -- 1,0 m / 30,0 kg
  },
  ["VENUSAUR"] = {
    kind = "SEMENTE",
    text = "Ele consegue<NEXT>transformar luz do<NEXT>sol em energia.",
    text2 = "Por isso, fica<NEXT>mais poderoso no<NEXT>verão.",
    height = 200, weight = 1000,   -- 2,0 m / 100,0 kg
  },
  ["VICTREEBEL"] = {
    kind = "PAPA-MOSCA",
    text = "Esta planta<NEXT>POKéMON apavorante<NEXT>atrai a presa com",
    text2 = "um mel cheiroso e<NEXT>depois a derrete<NEXT>dentro da boca.",
    height = 107, weight = 155,   -- 1,7 m / 15,5 kg
  },
  ["VILEPLUME"] = {
    kind = "FLOR",
    text = "O botão se abre<NEXT>com um estouro.<NEXT>Depois começa a",
    text2 = "espalhar um pólen<NEXT>venenoso que causa<NEXT>alergia.",
    height = 102, weight = 186,   -- 1,2 m / 18,6 kg
  },
  ["VOLTORB"] = {
    kind = "BOLA",
    text = "Ele foi descoberto<NEXT>quando a POKé BOLA<NEXT>foi criada. Dizem",
    text2 = "que há alguma<NEXT>ligação entre as<NEXT>duas coisas.",
    height = 5, weight = 104,   -- 0,5 m / 10,4 kg
  },
  ["VULPIX"] = {
    kind = "RAPOSA",
    text = "Se um inimigo mais<NEXT>forte que ela<NEXT>ataca, ela finge",
    text2 = "estar machucada<NEXT>para enganar ele e<NEXT>escapar.",
    height = 6, weight = 99,   -- 0,6 m / 9,9 kg
  },
  ["WARTORTLE"] = {
    kind = "TARTARUGA",
    text = "Ele controla com<NEXT>esperteza as<NEXT>orelhas peludas e",
    text2 = "o rabo para manter<NEXT>o equilíbrio<NEXT>enquanto nada.",
    height = 100, weight = 225,   -- 1,0 m / 22,5 kg
  },
  ["WEEDLE"] = {
    kind = "PELUDINHO",
    text = "Ele ataca com um<NEXT>ferrão de veneno<NEXT>de 5 cm na cabeça.",
    text2 = "Costuma ser achado<NEXT>sob as folhas que<NEXT>ele come.",
    height = 3, weight = 32,   -- 0,3 m / 3,2 kg
  },
  ["WEEPINBELL"] = {
    kind = "PAPA-MOSCA",
    text = "Se a presa é maior<NEXT>que a boca dele,<NEXT>ele corta a vítima",
    text2 = "com folhas afiadas<NEXT>e come tudo, até o<NEXT>último pedaço.",
    height = 100, weight = 64,   -- 1,0 m / 6,4 kg
  },
  ["WEEZING"] = {
    kind = "GÁS TÓXICO",
    text = "Perfume caro é<NEXT>feito com os gases<NEXT>venenosos de",
    text2 = "dentro dele,<NEXT>diluídos ao<NEXT>máximo possível.",
    height = 102, weight = 95,   -- 1,2 m / 9,5 kg
  },
  ["WIGGLYTUFF"] = {
    kind = "BALÃO",
    text = "O pelo dele é bem<NEXT>fino. Cuidado para<NEXT>não deixar ele",
    text2 = "bravo: pode ir<NEXT>inchando e se<NEXT>jogar em cima.",
    height = 100, weight = 120,   -- 1,0 m / 12,0 kg
  },
  ["WOBBUFFET"] = {
    kind = "PACIENTE",
    text = "Para manter o rabo<NEXT>preto escondido,<NEXT>ele vive quieto",
    text2 = "no escuro. Nunca é<NEXT>o primeiro a<NEXT>atacar.",
    height = 103, weight = 285,   -- 1,3 m / 28,5 kg
  },
  ["WOOPER"] = {
    kind = "PEIXE ÁGUA",
    text = "Quando anda pelo<NEXT>chão, ele cobre o<NEXT>corpo com uma",
    text2 = "película<NEXT>viscosa e<NEXT>venenosa.",
    height = 4, weight = 85,   -- 0,4 m / 8,5 kg
  },
  ["XATU"] = {
    kind = "MÍSTICO",
    text = "Na América do Sul,<NEXT>dizem que o olho<NEXT>direito dele vê o",
    text2 = "futuro e o olho<NEXT>esquerdo enxerga<NEXT>o passado.",
    height = 105, weight = 150,   -- 1,5 m / 15,0 kg
  },
  ["YANMA"] = {
    kind = "ASA CLARA",
    text = "Os olhos grandes<NEXT>dele varrem 360<NEXT>graus. Ele olha",
    text2 = "para todo lado<NEXT>atrás de insetos<NEXT>para caçar.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["ZAPDOS"] = {
    kind = "ELÉTRICO",
    text = "Dizem que esta ave<NEXT>POKéMON lendária<NEXT>só aparece quando",
    text2 = "uma nuvem de<NEXT>trovoada se parte<NEXT>em duas metades.",
    height = 106, weight = 526,   -- 1,6 m / 52,6 kg
  },
  ["ZUBAT"] = {
    kind = "MORCEGO",
    text = "Capaz de voar em<NEXT>segurança no<NEXT>escuro, ele solta",
    text2 = "gritos ultrassôni-<NEXT>cos para checar se<NEXT>há obstáculos.",
    height = 8, weight = 75,   -- 0,8 m / 7,5 kg
  },
}

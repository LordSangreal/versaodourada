# Changelog

Este arquivo e escrito a mao e o build so o copia para dentro do pacote.

Ate a 0.14.0 ele era gerado por `build_mod.py`, e por isso toda versao
publicada dizia "Primeira versao" com a contagem de falas do dia -- o
historico se apagava sozinho a cada build. E o mesmo defeito que o README
tinha ate a 0.8.2. As entradas abaixo foram reconstruidas do git.

## 0.39.0

**Lote 40 -- as ULTIMAS derivadas traduziveis.** Com esta versao nao sobra
nenhuma fala de terceiros que se possa traduzir.

- **TRAINER HOUSE de VIRIDIAN (14)** -- a casa de batalha de treino, uma
  por dia, e o memo ilegivel que "parece rastro de ONIX".
- **A casa do SANDSTORM na ROUTE 27 (4)** -- a TM37 e a confianca do
  POKéMON: "Confianca e o laco que une POKéMON e treinadores."
- **A ESTACAO do MAGNET TRAIN (6)**, a **SILPH CO. (3)**, os **IRMAOS DOS
  DIAS DA SEMANA (3)** com a carta da MONICA e a lista dos sete, e a
  **ROUTE 5 com o CLEANSE TAG (3)**.
- Mais o FIGHTING DOJO, o NUGGET da ROUTE 2, o AIDE do PROF.OAK, o
  POKéMON CHANNEL com a DJ MARY, a casa da vizinha e a casa de cura.
- Derivadas: 191 -> 133. Falas nossas: 2775 -> 2833.

### O que sao as 133 que sobraram

**Nenhuma e traduzivel.** Todas sao ponteiro desalinhado:

    82  endereco fora da janela 4000-7FFF de um banco
    39  o ingles decodifica comecando no meio de uma frase
     6  o primeiro segmento e um pedaco de palavra ("S?", "RGE",
        "AFOAM IS-", "POKeMON")
     4  menos de 12 letras
     2  vazia

A ROM brasileira reapontou o texto, entao o mesmo endereco nas duas ROMs
nao e a mesma fala: o portugues publicado nessas chaves pode nem pertencer
aquele lugar. Nao da para traduzir meia palavra.

**A partir daqui o numero so cai por decisao, nao por traducao.** Ou essas
133 chaves saem do pacote -- e a fala cai em ingles, que e o comportamento
normal do mod para o que nao foi traduzido -- ou ficam, e o credito a
R_Lopes e Night_Shadown fica junto. `_triagem.py` faz a separacao e agora
reconhece tambem o primeiro segmento truncado.

## 0.38.0

**Lote 39 -- 57 falas**, a periferia de KANTO e as casas de fala de JOHTO.

- **A casa do MANIA (10)** -- o RIVAL rouba o POKéMON e o dono pede que voce
  cuide do que sobrou. "Um cara da sua idade, de olhar duro e cabelo
  comprido entrou."
- **O MR.FUJI e a SOUL HOUSE (6)** -- os tumulos dos POKéMON que se foram.
- **O irmao do FISHING GURU (4)** -- a SUPER ROD.
- **A SAFARI ZONE fechada (5)** -- o WARDEN que largou tudo e foi viajar.
- **A celebridade escondida da ROUTE 28 (2)**, o MT.SILVER, o vulcao de
  CINNABAR, a TIN TOWER, os SLOWPOKE sumidos, a SILPH CO. e as casas de
  fala de CHERRYGROVE e da ROUTE 30.
- Derivadas: 248 -> 191. Falas nossas: 2718 -> 2775.
- Cinco chaves ficaram de fora: a triagem as deixou passar, mas o ingles
  comeca no meio de uma palavra -- 44:5f00 ("S?"), 4a:5600, 4e:5100
  ("AFOAM IS-LANDS"), 4e:5f4d e 4f:5700 ("RGE / The Lightning American",
  pedaco de LT.SURGE).
- Oito linhas estouravam a caixa. Ao encurta-las eu quebrei tres frases
  ("REPEL e coisa que voce precisa vai explorar uma caverna", "da sua era"
  no lugar de "da sua idade", "POKeMON para ir com os do amigo" sem o verbo
  lutar). A releitura pegou as tres. E o mesmo padrao da 0.35.0: o perigo
  nao e escrever longo demais, e o conserto apressado depois.

## 0.37.0

**Lote 38 -- 48 falas, escolhidas por FREQUENCIA.** O CABLE CLUB do segundo
andar aparece em TODO CENTRO POKéMON das duas regioes: era o texto de maior
trafego que ainda vinha de terceiros.

- **CABLE CLUB (21)** -- COLOSSEUM, TRADE CENTER e TIME CAPSULE, os avisos
  de conexao ("A conexao foi fechada por falta de atividade"), as recusas
  de troca e o presente do balconista.
- **CIANWOOD (12)** -- a FARMACIA com a SECRETPOTION, que e linha
  principal: o remedio do POKéMON do LIGHTHOUSE. Mais o estudio de fotos,
  a casa que fala do LUGIA nas quatro ilhas e o CENTRO.
- **Centros de KANTO (15)** -- FUCHSIA, LAVENDER, VIRIDIAN e SAFFRON, quase
  todos comentando a POWER PLANT parada e o ROCK TUNNEL.
- Derivadas: 296 -> 248. Falas nossas: 2670 -> 2718.
- A releitura pegou uma que quebrava a frase: "da para ve-la voce tiver uma
  SILVER WING" tinha perdido o "se" ao caber nas 17 colunas.

### TRIAGEM: quanto falta de verdade

Das 296 derivadas que restavam antes deste lote, so **166 sao
traduziveis**. As outras 130 sao ponteiro desalinhado:

    82  endereco fora da janela 4000-7FFF de um banco
    39  o ingles decodifica comecando no meio de uma frase
     7  menos de 12 letras
     2  vazia

Nao da para traduzir meia palavra, e a ROM brasileira reapontou o texto, de
modo que o mesmo endereco nas duas ROMs nao e a mesma fala. **Zerar a
contagem de derivadas exige uma decisao sobre essas 130**, nao mais
traducao: ou saem do pacote (e a fala cai em ingles, que e o comportamento
normal do mod para o que nao foi traduzido), ou ficam e o credito fica
junto. `_triagem.py` faz essa separacao.

## 0.36.0

**Lote 37 -- 79 falas escolhidas por MAPA, nao por banco: so linha
principal.** Sao as falas que o jogador nao tem como pular.

- **MR.POKéMON e o PROF.OAK (14)** -- a abertura do jogo. O MYSTERY EGG, o
  OAK aparecendo na casa do MR.POKéMON, a entrega da POKéDEX, e a troca do
  GYARADOS vermelho pelo EXP.SHARE.
- **GINASIO de FUCHSIA (18)** -- a JANINE, as sosias que se passam por ela
  e a SOULBADGE.
- **GINASIO de SAFFRON (7)** -- a SABRINA, a visao de tres anos atras e a
  MARSHBADGE.
- **GINASIO de VIRIDIAN (7)** -- o BLUE e a EARTHBADGE.
- **Portao da VICTORY ROAD (5)** -- a conferencia das oito INSIGNIAS.
- **RADIO TOWER de LAVENDER (8)** -- o EXPN CARD, que so vem depois de
  resolver a POWER PLANT.
- **A COPYCAT (13)** -- a POKé DOLL trocada pelo MAGNET TRAIN PASS.
- **A ESTACAO do MAGNET TRAIN em SAFFRON (7)** -- a SILPH CO., o PASS e a
  explicacao dos imas.
- Derivadas: 374 -> 296. Falas nossas: 2591 -> 2670.
- Catorze linhas estouraram as 17 colunas da ultima linha da pagina e foram
  REESCRITAS, nao amputadas -- que e a licao da 0.35.0. Ainda assim a
  releitura pegou duas: um ponto final que cortava a frase no meio ("Muita
  gente aqui trabalha duro." e a pagina seguinte continuava com "na RADIO
  TOWER" pendurada) e uma pergunta que perdeu o ponto de interrogacao.
- Duas falas curtas ("Te enganei! Hahaha!" e "Ooh... Eu perdi...") sairam
  identicas a versao de terceiros. Nao e copia: a planilha do
  `derivadas.py` imprime SO o ingles. Em frase curta so existe uma traducao
  natural, e a convergencia e esperada.
- As sete falas da ESTACAO vieram de um lote paralelo que outra sessao
  havia escrito. Das 65 chaves daquele lote, 47 SOBRESCREVIAM traducao
  nossa ja verificada (abreviando "RADIO TOWER" para "R. TOWER",
  traduzindo o nome DIRECTOR, perdendo a palavra "senhas"), 10 repetiam
  este lote e 12 linhas estouravam a caixa; 21 falas usavam "..." em vez do
  glifo. So oito chaves eram novas, e uma delas era ponteiro desalinhado.
  As sete restantes foram RETRADUZIDAS do ingles aqui.

## 0.35.0

Dois lotes de derivadas de uma vez, 103 falas. Sobram 374.

- **Lote 35 -- banco 59 (62 falas): VERMILION e o OAK em KANTO.** A cidade
  inteira, o POKéMON FAN CLUB com o CHAIRMAN e a ladainha do RAPIDASH, o
  GINASIO do LT.SURGE com a THUNDERBADGE, a casa da DAISY que escova
  POKéMON, a casa do RED com a mae dele, e o laboratorio do OAK com o
  e-mail do ELM.
- **Lote 36 -- banco 5a (41 falas): a ELITE FOUR e o HALL OF FAME.** O
  GINASIO do BROCK em PEWTER, o INDIGO PLATEAU, os quatro (WILL, KOGA,
  BRUNO e a KAREN com o discurso sobre POKéMON forte e POKéMON fraco), o
  LANCE mestre dos dragoes, a MARY e o PROF.OAK depois da vitoria, e o
  registro no HALL OF FAME.
- Derivadas: 477 -> 374. Falas nossas: 2488 -> 2591.
- A releitura pegou onze erros que o conferidor aprovou, e a maioria foi
  criada por COMPRESSAO DE LARGURA: encurtar a linha para caber nas 17
  colunas da ultima linha da pagina apagou um pronome ("vai curvar" sem o
  "se"), um "que a gente" ("nao e sempre recebe um desafio") e um "tao"
  ("sao fortes quanto"). Quando a linha nao cabe, o certo e reescrever a
  frase, nao amputar palavra.

## 0.34.0

Primeiro lote das falas DERIVADAS. Elas ja apareciam em portugues -- so que
no portugues de R_Lopes e Night_Shadown. Reescreve-las do ingles e o unico
caminho para a atribuicao do README virar um agradecimento.

- **Lote 34 -- banco 5b (57 falas): o FAST SHIP S.S.AQUA inteiro.** Os dois
  portos (OLIVINE e VERMILION) com o S.S.TICKET, o navio de ponta a ponta
  (conves, cabines, porao, refeitorio), o marinheiro que dormia em servico
  e o colega que pede para acha-lo, o CAPTAIN, o avo que perdeu a neta e a
  neta que so queria brincar, as passagens dos portos e a placa do
  MT.MOON SQUARE.
- Derivadas: 534 -> 477. Falas nossas: 2431 -> 2488.
- Ficam de fora 10 chaves do banco 5b: sao ponteiros desalinhados, cujo
  ingles decodifica como pedaco de outra fala ("ll you dis-", "EPEL is a
  neces-") ou como nada. A ROM brasileira reapontou o texto, entao o mesmo
  endereco nas duas ROMs nao e a mesma fala, e nao da para traduzir meia
  palavra.
- A releitura pegou quatro erros que o conferidor aprovou: dois "Esta e sua
  cabine" sem o ponto final (cortado para caber nas 17 colunas da ultima
  linha), uma quebra no meio do sintagma ("a minha / neta") e um
  "alguem. Aflito..." truncado.

## 0.33.0

Com esta versao, **nenhum texto que o Gold desenha fica em ingles por falta
de traducao.** O que sobra em ingles e so o que fica no original de
proposito (golpes, POKéMON, itens, personagens, cidades) e as 109 frases
cravadas no codigo do motor, que registro de mod nenhum alcanca.

- **103 textos do motor**, o resto das chaves `Strings.source` que o
  coletor so passou a enxergar na 0.32.0: o MOVE DELETER, o NAME RATER, o
  Concurso de Insetos inteiro, o DAY-CARE, as 20 falas de avaliacao da
  #DEX pelo PROF.OAK, a MOM guardando dinheiro, o estudio de fotos, as
  trocas com NPC e a animacao delas, o aviso de esquecer golpe, o diploma
  e a impressora.
- **Lote 33 -- 14 falas dos bancos 60 e 61.** A varredura do projeto
  rodava `range(0x40, 0x60)` e parava ali, entao estas nunca entraram no
  catalogo e apareceram em ingles desde a primeira versao: o laboratorio
  do PROF.ELM, os psiquicos do GINASIO de SAFFRON e o FIGHTING DOJO ao
  lado, com o KARATE KING arrasado pela SABRINA.
- Ficam de fora, de proposito, 18 rotulos de largura fixa (os carimbos do
  estudio de fotos e as dicas de botao da impressora do UNOWN):
  "A▶IMPRIMIR" nao cabe onde "A▶PRINT" cabe, e simbolo de genero nao e
  palavra. Mesma regra que ja mantem PSN/BRN/PAR em ingles.
- Rotulos de menu e batalha: 351 -> 454. Falas: 2951 -> 2965.
- Quatro falas do lote 33 tropecaram na regra das 17 colunas na ultima
  linha da pagina (a seta ▼ ocupa a coluna 18) e foram reescritas antes de
  publicar.

## 0.32.0

- **86 textos do motor que estavam em ingles desde a 0.1.0** -- e nao por
  falta de traducao, por falta de COLHEITA. O `colher.py` procurava os
  sitios `Strings("...")` e `S("...")`; o motor marca uma segunda leva com
  `Strings.source("...")`, funcao identidade que existe so para por no
  catalogo um literal construido cedo demais para ser traduzido no lugar.
  O regex exigia parentese logo depois de `Strings`, entao `Strings.source(`
  nunca casou: 212 chaves ficaram de fora, 184 delas desenhadas por codigo
  gen2 -- ou seja, em ingles na tela durante 31 versoes.
- Entraram as de maior frequencia: os golpes de campo (CUT, SURF,
  WATERFALL, STRENGTH, DIG, WHIRLPOOL e o aviso de INSIGNIA), a pesca
  ("Fisgou!", "Nem uma mordida!"), o HEADBUTT nas arvores, o SWEET SCENT,
  **a cura do CENTRO POKéMON**, o premio em dinheiro de cada batalha, o
  dano de veneno e de queimadura, o acerto do relogio no inicio do jogo,
  as compras da MOM, as decoracoes do quarto, a bicicleta, os itens
  escondidos e os pedregulhos.
- Rotulos de menu e batalha: 265 -> 351.
- **Lote 32 resgatado.** A traducao das 158 falas do lote 32 foi ao ar na
  0.31.0 mas nunca foi salva em `tools/pt/`: existiam so `chaves32.json` e
  `trans32.json`, que sao a planilha em INGLES. Como o carregador de lotes
  nao le JSON, o catalogo nao tinha essas chaves, e o primeiro rebuild
  deixava a traducao de terceiros ganhar de novo -- 156 falas nossas
  sumiriam sem erro nenhum, so um `git diff` denunciava. O texto foi
  recuperado do proprio `lang/dialogue.lua` publicado e escrito em
  `pt/dialogo_32.py`, que e onde ele devia estar desde o inicio.
- Sem regressao: o `dialogue.lua` desta versao e identico ao da 0.31.0,
  fala por fala. So o `strings.lua` cresceu.

## 0.31.0

- **Lote 30** -- as 115 sobras dos bancos 00, 42, 43, 44, 46, 47, 49, 4a
  e 4b: a SPROUT TOWER e o ELDER, o RIVAL no caminho, os caçadores de
  insetos da rota 36, as RUINS DE ALPH e o UNOWN, o farol do AMPHY com a
  JASMINE, o RADIO TOWER e o DIRECTOR, o KARATE KING e o TYROGUE, a
  CLAIR e o RISINGBADGE, o SANTUÁRIO DRAGÃO e os sinais de KANTO/JOHTO.
- **Lote 31** -- as 153 derivadas dos bancos 4c, 4d, 4e e 4f: o SUNNY e
  a MONICA e as placas das rotas, PEWTER e VIRIDIAN e o diálogo do BLUE,
  o GINÁSIO fantasma de VIRIDIAN, o vereador, CINNABAR, a CELADON, e as
  cidades de Kanto com o LT.SURGE, a MISTY, a SABRINA e a ERIKA.
- **Lote 32** -- as 158 derivadas dos bancos 50, 53, 54, 55 e 56: falas
  de KANTO com a MISTY e o EARL, o POWER PLANT, e o Bug-Catching Contest
  com suas placas e regras.
- 2419 falas proprias; 532 derivadas.

## 0.30.0

- **Lote 29** -- as 93 derivadas do banco 57: a bicicletaria de
  GOLDENROD, a casa do BILL, a MOM do BILL, a loja da ovolo (S.S. AQUA),
  o trem e a estacao para SAFFRON, o PRESIDENTE, o MAGNET TRAIN e a
  ILEX FOREST.
- 1993 falas proprias; 957 derivadas.

## 0.29.0

- **Lote 28** -- as 101 derivadas do banco 5e: a CELADON DEPT. STORE, o
  GAME CORNER, a CELADON MANSION (GAME FREAK), o GINASIO da ERIKA, o
  EATATHON CONTEST e a CYCLING ROAD.
- 1900 falas proprias; 1050 derivadas.

## 0.28.0

- **Lote 27** -- as derivadas dos bancos 51-53 (90 falas): os
  marinheiros e o farol de OLIVINE e a MOOMOO FARM (51), ECRUTEAK com a
  TIN TOWER, a palestra do BILL sobre a TIME CAPSULE e as KIMONO GIRLS
  (52), e o GINÁSIO do BLAINE na caverna de CINNABAR (53).
- 1799 falas proprias; 2950 publicadas.

## 0.27.0

- **Lote 26** -- as ultimas varridas (76 falas): o GINÁSIO de pedra de
  BROCK (5a), os nadadores de Cianwood (54), a GOLDENROD dos
  treinadores, da bike e do SWEET HONEY (57), o GINÁSIO elétrico do
  LT.SURGE (59), as RUÍNAS DE ALPH (5b), os artistas marciais (5d), as
  meninas da ERIKA (5e) e o CONCURSO DE CAPTURA (56).
- **Marco: as varridas zeraram.** Nao sobra fala que aparecia **em
  ingles** na tela; a parte em ingles agora e so a derivada da traducao
  de terceiros, que sera reescrita lote a lote.
- 1709 falas proprias; 2948 publicadas.

## 0.26.0

- **Lote 25** -- interiores de Johto (69 falas): o GINÁSIO de PRYCE com o
  piso de gelo e as pistas de patinação, a DANCE THEATER e o GINÁSIO de
  ECRUTEAK com o piso invisível, as varridas do GINÁSIO de dragões de
  CLAIR, e AZALEA com os bug catchers e as gemias AMY e MAY.
- 1633 falas proprias; 2872 publicadas.

## 0.25.0

- **Lote 24** -- varridas dos bancos 40-4c (140 falas): TEAM ROCKET e a
  RADIO TOWER de GOLDENROD com o diretor no topo, a SPROUT TOWER com o
  ELDER e os aprendizes, a VICTORY ROAD com os guardioes, e pescadores
  e treinadores de passagem pelas rotas.
- 1564 falas proprias; 2803 publicadas.
- Revisao antes de publicar: cinco erros de sentido que o conferidor
  aprovou (ele valida forma, nao significado).  "POKéMON e seus
  treinador fica forte" sem concordancia, "Sou o conhecido como",
  "Vou ter que esforcar mais" sem o pronome, "Perdi para um {RIVAL}"
  com artigo indefinido antes de nome proprio, e "estou para qualquer
  um!" com o verbo faltando.

## 0.24.0

- **Lote 23** -- bancos 45 e 46 (49 falas): o esconderijo ninja do
  GINASIO de ECRUTEAK com os paineis de salto, os ROCKET GRUNTS que
  guardam a sala do chefe e soltam as senhas quando perdem
  (SLOWPOKETAIL e RATICATE TAIL), o cientista do sinal de radio, e o
  GOLDENROD UNDERGROUND com o quebra-cabeca das persianas.
- 1424 falas proprias; 2663 publicadas.

## 0.23.0

- **Lote 22** -- banco 44 inteiro (69 falas), que junta quatro lugares:
  as RUINS OF ALPH e o RESEARCH CENTER, a caverna do MT.MORTAR com o
  eremita que mora la, o SLOWPOKE WELL com os ROCKET GRUNTS cortando
  TAILS, e o OLIVINE LIGHTHOUSE com o POKéMON doente e a JASMINE.
- 1375 falas proprias; 2614 publicadas.

## 0.22.0

- **Lote 20** -- banco 50 (64 falas): o caminho do ROCK TUNNEL, os
  ecologistas, os seis desafiantes em fila e o trapaceiro que espera no
  fim, a KANTO POKéMON FEDERATION, o MAGNET TRAIN e a POWER PLANT.
- **Lote 21** -- banco 5b (67 falas): o FAST SHIP entre OLIVINE e
  VERMILION -- marinheiros, criancas em excursao, as senhoras e o
  cavalheiro de coracao partido.
- 1306 falas proprias; 2545 publicadas.

Nota de metodo: nestes dois lotes o `linhas()` reprovou tres falas por
contagem de linha e o conferidor pegou vinte e nove estouros de coluna.
Lote grande nao erra mais por fala -- erra a mesma proporcao, so que de
uma vez.  O que ele esconde e o erro de SENTIDO, que nenhuma das duas
ferramentas pega: "marinheiros ralam" com "nós" antes, "Meu coração
chora" cortado.  Esses so a releitura acha.

## 0.21.0

Lote maior por pedido do usuario: quatro bancos inteiros numa versao so,
em vez de publicar a cada trinta falas.

- **Lote 16** -- banco 4c (72 falas): as gemeas ANN e ANNE, os nadadores
  entre OLIVINE e CIANWOOD, os POKé FANS, e as conversas sobre as WHIRL
  ISLANDS e o POKéMON de asas prateadas.
- **Lote 17** -- banco 4d (67 falas): as rotas do norte ate BLACKTHORN,
  os HIKERS, os sabios, e quem fala de ARTICUNO, ZAPDOS e MOLTRES.
- **Lote 18** -- banco 4e (39 falas): o mar de Kanto, o casal que nada
  ate FUCHSIA, e os motoqueiros da CYCLING ROAD.
- **Lote 19** -- banco 4f (54 falas): as rotas de Kanto, os professores,
  a gangue do PIKACHU, os pescadores e os videntes.
- 1175 falas proprias; 2414 publicadas.  Passou de mil.

## 0.20.0

- **Lotes 15b e 15c** -- o banco 4b inteiro fechado (51 falas): os
  HIKERS, os colegiais que querem virar LÍDER, o pessoal do DAY-CARE, as
  tres irmas da praia, os casais, e quem caça inseto para o Concurso.
- **`tools/pendentes.py`** substitui o filtro de cauda que eu vinha
  reescrevendo a cada lote.  O antigo comparava cada fala pendente
  contra as OUTRAS PENDENTES, e por isso ia piorando: assim que a fala
  inteira era traduzida ela saia da lista e a cauda dela ficava sem par.
  Nove passaram por essa fresta no lote 14b.  Agora a comparacao e
  contra o `dialogo.json` inteiro, traduzido ou nao.
- 943 falas proprias; 2182 publicadas.

## 0.19.0

- **Lote 14b** -- o resto do telefone (33 falas): as saudacoes que cada
  treinador faz ao ligar, os convites para revanche, os avisos de
  "apareceu um monte de {POKéMON} perto de {LUGAR}", o trote da AUDREY
  procurando o KAZ, e o PROF.ELM em panico quando roubam o laboratorio.
- **Lote 15a** -- os treinadores das rotas (27 falas): pescadores, o
  pessoal do mato, a moca que atende o telefone no meio da batalha.  E o
  texto de cada batalha aleatoria do caminho.
- Nove chaves do banco 41 ficaram de fora por serem cauda de falas que o
  lote 14a ja cobria.  O filtro automatico nao as pegou: assim que a
  fala-mae e traduzida ela sai da lista de pendentes, e a cauda fica sem
  par para comparar.  Conferi a olho.
- 892 falas proprias; 2131 publicadas.

## 0.18.0

Primeira leva tirada da varredura da 0.16.0.

- **Lote 13** -- o resto do banco 40 (44 falas): GAME CORNER, telefone,
  felicidade do POKéMON, o JURAMENTO ROCKET, placas e mensagens de
  batalha.  O lote 7 tinha coberto 32 falas deste banco; a varredura
  achou mais 52.
- **Lote 14a** -- o telefone (36 falas): a MÃE perguntando onde voce
  esta e se quer guardar dinheiro, o SISTEMA DE ARMAZENAMENTO avisando
  que a BOX encheu, o BILL, e as ligacoes do PROF.ELM sobre o EGG e o
  POKéRUS.  E texto que chega pela POKéGEAR o jogo inteiro.
- Ficam de fora as chaves com `<TARGET>`, `<USER>`, `<ENEMY>`: esses
  marcadores nao sao texto, sao bytes que o motor troca em tempo de
  execucao.  O override publica o texto como esta, entao o marcador
  apareceria literal na tela.  Mesmo motivo pelo qual `build_mod.py` ja
  descartava essas chaves na traducao derivada.
- 832 falas proprias; 2071 publicadas.

## 0.17.0

- **Nome de item volta todo para o ingles.**  Decisao do usuario depois
  de ver a versao traduzida rodando: POKé BALL, POTION, BERRY, REPEL --
  todos no original.  O catalogo de itens fica vazio, e vazio significa
  "usa o nome da ROM".
- Isso desfaz a mudanca da 0.16.0, que tinha levado os itens de 68 para
  139 seguindo a localizacao oficial pt-BR.  A localizacao oficial de
  fato traduz as Balls -- mas quem decide o mod e o usuario, e a regra
  agora e uma so: item entra junto com golpe, POKéMON, TM e HM no que
  fica em ingles.
- A linha do Concurso de Insetos volta a dizer "PARK BALLS" em vez de
  "BOLAS", para a fala do NPC combinar com o nome na bolsa.
- Numeros do README atualizados: 1991 falas, 265 rotulos, 752 proprias.

## 0.16.0

O usuario jogou e mandou captura de tela.  Quase tudo desta versao saiu
disso.

- **Texto de batalha traduzido.**  114 strings do motor que tinham ficado
  de fora, entre elas `%s used\n%s!` -- a linha que aparece em todo turno
  de toda batalha.  Tambem: trocar de POKéMON, evolucao, PC, loja, GAME
  CORNER, bicicleta, salvar, e a fala de abertura do PROF.OAK.
- **As Balls agora sao traduzidas**, no padrao pt-BR oficial: POKé BOLA,
  GRANDE BOLA, ULTRA BOLA, BOLA MESTRA.  Ate aqui ficavam em ingles com a
  justificativa de "nome da franquia", o que estava errado -- a
  localizacao oficial traduz.  POKéMON MART virou LOJA POKéMON.  Mais 71
  nomes de item ao todo (68 -> 139).
- **`tools/varrer.py`**: acha falas que o percurso de scripts nao
  alcanca.  O usuario viu um treinador do ginasio do FALKNER falando
  ingles; a fala nao estava no `dialogo.json` porque `walk.py` so
  encontra o que algum script referencia, e falas de treinador ficam em
  structs.  A varredura achou **1032 falas** que faltavam: o catalogo
  conhecido foi de 2245 para 3277.
- Lote 12: as cinco falas do ginasio do FALKNER que faltavam.
- Lotes 09a-11 (RADIO TOWER, RUINS OF ALPH, rota 36, Concurso de
  Insetos), escritos em outra sessao, revisados: 300 palavras
  reacentuadas, 42 linhas que estouravam a caixa encurtadas, e um
  "Você removing aquela árvore?" que tinha ficado meio em ingles.
- Removido `dialogo_ginasio_goldenrod.py`: as 12 falas dele ja estavam no
  lote 5a, conferidas, e a copia mais nova as substituia por versoes
  piores.
- `tools/acentuar.py` e `tools/patch_lotes_09_11.py` documentam os dois
  consertos acima.
- 752 falas proprias; 1991 publicadas; 265 rotulos de menu; 139 itens.

## 0.15.0

- Lote 7: os StdScripts do banco 40 (32 falas).  Sao os scripts que todo
  mapa chama -- a enfermeira, o MART, o telefone, o PC do BILL, o
  Concurso de Insetos.  E o texto que o jogador mais le.
- Lote 8a: MAHOGANY TOWN, o ginasio do PRYCE e as rotas 42 e 43 (35).
- Lote 8b: LAKE OF RAGE, o encontro com o LANCE e a casa do MAGIKARP (27).
- Lote 8c: a base secreta da TEAM ROCKET, os tres andares (35).
- `pt/estrutura.py`: a funcao `linhas()` monta a fala com os separadores
  lidos do INGLES.  Trocar `\n` por `\v` na copia era o erro que sobrava
  depois do conferidor -- quatro no lote 6b, oito no 7.  Com ela, os tres
  lotes seguintes passaram limpos de primeira.
- `tools/fatiar.py`: corta uma planilha grande por mapa e descarta kana,
  fragmento e vazio.
- 559 falas proprias de 2245; 1981 publicadas.

## 0.14.0

- Lote 5b: RADIO TOWER, rotas 34 e 35, NATIONAL PARK (51 falas).
- Lote 6a: ECRUTEAK, ginasio do MORTY, BURNED TOWER, TIN TOWER, rotas
  38 e 39 (31 falas).
- Lote 6b: OLIVINE, ginasio da JASMINE, o LIGHTHOUSE, CIANWOOD e o
  ginasio do CHUCK (40 falas).
- `tools/esqueleto.py`: imprime pagina, linha, separador e limite de
  coluna do ingles.  Ler a sequencia de `\n` `\v` `\f` a olho na planilha
  era a fonte de erro que sobrava depois do conferidor.
- O CHANGELOG passa a ser um arquivo, como o README desde a 0.8.2.
- 430 falas proprias de 2245; 1980 publicadas.

## 0.13.0

- Lote 5a: Goldenrod, ginasio da WHITNEY e a DEPT.STORE.

## 0.12.0

- Lote 4: Azalea, Slowpoke Well, Ilex Forest, KURT e o ginasio do BUGSY.

## 0.11.0

- A interface do aplicativo volta ao ingles: as palavras em portugues
  estouravam o layout do launcher.  Filtro por diretorio em
  `build_mod.py`.

## 0.10.1

- `--` vira virgula, nao reticencias: em ingles e uma pausa, e em
  portugues "…" significa frase que morre.

## 0.10.0

- Lote 3: Violet City, Sprout Tower e o ginasio do FALKNER.

## 0.9.0

- Lote 2: Rota 29, Cherrygrove e Rota 30.

## 0.8.2

- O README sai de dentro do `build_mod.py` e vira arquivo.  Antes, todo
  build reescrevia a pagina do repositorio com a versao congelada no
  codigo.

## 0.8.1

- A seta ▼ de "aperte A" ocupa a coluna 18: na ultima linha de cada
  pagina cabem 17.  Foi o que comeu o "m" de "bem".

## 0.8.0

- Lote 1 da traducao propria: 87 falas de New Bark e do laboratorio.

## 0.7.0

- Mais 102 rotulos de menu: PC/Box, rede, gerenciador, teclas.

## 0.6.1

- Fundo transparente na pagina de glifos.  A 0.6.0 desenhou os acentos
  sobre branco opaco e o motor, que le o canal alfa, mostrou blocos
  pretos.

## 0.6.0

- Pagina de glifos: os acentos voltam.  Ate aqui tudo era dobrado para
  ASCII ("mae", "coracao").

## 0.5.0

- 68 nomes de item.  Status fica no original.

## 0.4.0

- 256 rotulos de menu, e conserta a regressao que perdeu 96 deles.

## 0.3.3

- Corrige a placa de New Bark e a precedencia do mapa BR.

## 0.3.2

- Corrige tres ligaduras reaproveitadas, achadas pelo validador.

## 0.3.1

- Decifra as ligaduras: 1689 -> 1968 falas.

## 0.3.0

- Pagina reescrita e infraestrutura da traducao propria.

## 0.2.0

- Conserta o percurso, que andava sobre dados como se fossem codigo:
  1410 -> 1689 falas.

## 0.1.7

- TM e HM voltam ao original.

## 0.1.6

- Glossario de terminologia pt-BR atual.

## 0.1.5

- Decifra as macros da traducao BR: 1002 -> 1410 falas.

## 0.1.4

- Acentos legiveis, fragmentos fora, menus traduzidos.

## 0.1.3

- Remove o TTF que quebrou a tela de mods.

## 0.1.2

- Restaura `games: ["gold"]`, que a 0.1.1 removeu por engano.  Sem ele,
  um boot de Gold pula o mod.

## 0.1.1

- Corrige `game_version`, que era `<1.0.0` e excluia o aplicativo 1.8.0
  da lista.

## 0.1.0

- Primeira versao: Pokemon Gold em portugues brasileiro.

# Changelog

Este arquivo e escrito a mao e o build so o copia para dentro do pacote.

Ate a 0.14.0 ele era gerado por `build_mod.py`, e por isso toda versao
publicada dizia "Primeira versao" com a contagem de falas do dia -- o
historico se apagava sozinho a cada build. E o mesmo defeito que o README
tinha ate a 0.8.2. As entradas abaixo foram reconstruidas do git.

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

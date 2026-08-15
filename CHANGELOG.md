# Changelog

Este arquivo e escrito a mao e o build so o copia para dentro do pacote.

Ate a 0.14.0 ele era gerado por `build_mod.py`, e por isso toda versao
publicada dizia "Primeira versao" com a contagem de falas do dia -- o
historico se apagava sozinho a cada build. E o mesmo defeito que o README
tinha ate a 0.8.2. As entradas abaixo foram reconstruidas do git.

## 0.46.0

**Gold e Crystal viram mods separados.** O Crystal sai daqui e passa a ter
repositorio proprio:
[LordSangreal/versaocristal-ptbr](https://github.com/LordSangreal/versaocristal-ptbr).

O motivo e um bug de conteudo que so aparece com os dois jogos no mesmo
catalogo. O Gen2Recomped indexa dialogo por rotulo nomeado
(`MomGivesPokegearText`), nao por endereco de ROM -- entao a mesma chave
serve Gold e Crystal. So que **582 rotulos existem nos dois jogos com texto
em ingles diferente**: o Crystal reescreveu falas inteiras reaproveitando o
mesmo nome. Como o catalogo tinha sido gerado por crosswalk em cima do
**Gold**, quem jogava Crystal via a fala do Gold traduzida em 555 lugares
(o inverso valia para as 27 escritas a mao a partir do Crystal na 0.45.0).
Nao da para resolver num arquivo so -- a chave e a mesma, o texto e que
muda.

- **`lang/dialogue_gen2recomped.lua` filtrado para o Gold**: 7614 -> 7324
  chaves. Saem as 261 que so o Crystal usa (peso morto aqui) e as 27 que
  tinham sido escritas com o texto do Crystal -- essas voltam a aparecer em
  ingles ate serem reescritas com o texto do Gold. Melhor ingles do que a
  fala do jogo errado.
- **`games` no `manifest.json` volta a ser so `gold`**, e o nome do mod
  volta a ser "Versao Dourada". Quem usava este mod para jogar Crystal deve
  instalar o `versaocristal-ptbr` no lugar; os dois convivem instalados,
  tem id diferente e cada um so ativa no jogo dele.
- Cobertura do Gold no Gen2Recomped cai de 99,4% para **98,3%** por causa
  das 27 removidas; no `gen1recomp` segue em **99,3%**, intocada.

### Corrigido: o catalogo inteiro sumia no Crystal

Um erro de sintaxe (string sem fechar, herdada de um script de lote da
0.45.0) fazia o `loadstring` do `main.lua` falhar. Como o `main.lua`
devolve tabela vazia quando o catalogo nao compila, os 7614 dialogos
sumiam de uma vez -- sobravam so os menus (`strings.lua`, que compilava
normal) e a fala de abertura do OAK (que vem do `dialogue.lua`). Era
exatamente o sintoma relatado: mae e NPCs iniciais em ingles, menus e
Prof. OAK em portugues. Corrigido ainda na 0.45.0, mas so agora
diagnosticado como causa daquele relato.

Entrou tambem um validador estrito de sintaxe no fluxo de trabalho, que le
o arquivo token a token em vez de so procurar aspas sem fechar -- um erro
desses nao passa de novo silenciosamente.

## 0.45.1

**Fecha a lacuna do `gen1recomp`/Gold que a 0.45.0 deixou** (88,0% de
cobertura -- ver seção "Estado" do README daquela versão). Todo o trabalho
da 0.45.0 foi no catálogo do Gen2Recomped; esta versão traz o mesmo
conteúdo pro catálogo próprio do `gen1recomp` (`lang/dialogue.lua`,
indexado por ponteiro de ROM).

- **259 falas novas em `lang/dialogue.lua`** (2815 -> 3074 chaves).
  Metodologia em duas etapas:
  - **156 por crosswalk** (142 comparando o `text.lua` do Gold extraído
    pelos dois motores por texto em inglês idêntico -- mesma técnica que
    gerou `dialogue_gen2recomped.lua` na 0.44.0 -- mais 14 que já tinham
    tradução em `strings.lua` mas nunca tinham sido copiadas pro ponteiro
    exato: o texto da ROM tem prioridade sobre o `Strings()` fallback no
    código do motor, então a chave por ponteiro precisa existir mesmo
    quando o texto já existia em outro catálogo).
  - **103 traduzidas do zero**: HM de campo (STRENGTH/ROCK SMASH), os
    cartazes do Celadon Mansion, telefone (números errados/fora de área),
    créditos do Hall of Fame, e o Day Care/MAILBOX/loja de ervas do
    Gold -- textos mais simples que a versão do Crystal (sem o ODD EGG),
    então não bateram no crosswalk. Também o discurso do OAK liberando o
    MT.SILVER depois das 8 BADGES de KANTO (12 páginas).
- **Cobertura do `gen1recomp`/Gold sobe de 88,0% para 99,3%** -- praticamente
  no mesmo nível do Crystal e do Gold no Gen2Recomped agora. O que resta
  é grito de espécie e o placeholder genérico "Object event.", que não
  precisam de tradução.

## 0.45.0

**O Crystal deixa de ser só "roda no mesmo motor" e passa a ter tradução
própria, completa.** Até a 0.44.1 o `lang/dialogue_gen2recomped.lua` era
majoritariamente o catálogo do Gold com o crosswalk de rótulo -- servia o
Crystal só onde o texto batia com o Gold. Esta versão percorre o Crystal
**na ordem em que o jogador realmente encontra o jogo**, mapa por mapa,
desde New Bark Town até o Hall of Fame, e resolve o conteúdo que só existe
no Crystal (ou que diverge do Gold sob o mesmo rótulo).

- **~1400 falas novas em `lang/dialogue_gen2recomped.lua`** (3217 -> 7614
  chaves), cobrindo:
  - A campanha inteira do Crystal na ordem do jogo: Cherrygrove, Violet,
    Union Cave, Azalea/Ilex Forest, Goldenrod, Ecruteak, Olivine, Cianwood,
    Mahogany/Lake of Rage, Blackthorn/Dragon's Den, Victory Road, Elite
    Four e Hall of Fame.
  - A sequência exclusiva do Crystal do BUENA/PASSWORD na Radio Tower, a
    provação da CLAIR pela RISING BADGE na Dragon Shrine (pergunta do
    ancião, DRATINI de recompensa -- no Gold ela só entrega a badge), e o
    arco da lenda do HO-OH/SUICUNE/ENTEI/RAIKOU (Burned Tower, Tin Tower,
    Wise Trios Room).
  - **Todas as 170 falas de treinador que faltavam** (antes/depois da
    batalha, derrota) -- achadas num sistema separado do diálogo por mapa
    (`trainer_headers.lua`, rótulos `_SEEN`/`_BEATEN`/`_AFTER`), incluindo
    os guardiões da Wise Trios Room e mais 4 treinadores da Dragon's Den.
  - Ruins of Alph (quebra-cabeça do UNOWN, as 4 câmaras, Research Center),
    Day Care/criação de ovos (nunca tinha sido traduzido), Battle Tower,
    a sub-trama da bola misteriosa do KURT, e o sistema Mobile
    Adapter/POKéCOM Admin Office.
  - Onde Gold e Crystal têm conteúdo **diferente** sob o mesmo rótulo
    (achado em ~4 casos, ex.: os objetos do quarto do jogador), a versão
    usada agora é sempre a do Crystal -- risco documentado: o Gold pode
    mostrar, nesses poucos rótulos específicos, texto pensado pro Crystal.
  - Uma auditoria final (cruzando todo `text_pointers.lua` +
    `trainer_headers.lua` do Crystal contra o catálogo) fechou em **99,4%
    de cobertura real** -- o resto é grito de espécie ("MACHOKE: Maaacho!"),
    texto em bytecode do motor (parte da Day Care) e onomatopeia idêntica
    em português, que não precisam de chave.
- **112 textos novos de combate e menu em `lang/strings.lua`** (530 ->
  645), achados vasculhando todo `Strings("...")` chamado no código-fonte
  dos dois motores (extraído do `.exe` fundido de cada um): efetividade de
  tipo, SUBSTITUTE, mensagens de HM de campo, Safari Zone, Slot Machine,
  Card Flip, PC/Trainer Card/Summary, criação de personagem, Hall of Fame,
  Cable Club. Ficou de fora de propósito a interface do launcher/mod
  manager/importador de ROM -- não é o jogo em si -- e nomes de golpe, que
  seguem a decisão de ficar em inglês.
- **Rótulos de atributo na tela de status agora traduzem** -- decisão
  revertida da 0.44.1 (ver seção própria no README). Sugestão de nomenclatura
  de **Hyd**: ATTACK -> ATAQUE, DEFENSE -> DEFESA, SPCL.ATK -> ESP.ATQ,
  SPCL.DEF -> ESP.DEF, SPECIAL -> ESP., SPEED -> VELOC. `EXP POINTS` (->
  PTS. EXP) e `LEVEL UP` (-> PRÓX. NV.) também encurtados: essa tela
  desenha rótulo e valor em **linhas separadas** (não na mesma linha como
  parecia à primeira vista), então a folga real é até a borda da tela --
  9 a 10 caracteres dependendo do local, não os 5-6 que o cálculo errado
  inicial sugeria. `HP` -> `PS` (sigla oficial pt-BR); `PP` fica.
- **Corrigido bug crítico de sintaxe** em `dialogue_gen2recomped.lua`:
  um script de lote anterior (`.replace("}", ...)` num marcador que tinha
  um `}` dentro de `{RAM:D099}`) deixou uma string sem fechar, quebrando a
  sintaxe Lua do arquivo a partir daquele ponto -- o motor provavelmente
  falhava ao carregar o catálogo inteiro. Corrigido e verificado com um
  validador dedicado (não deixa mais passar aspas sem fechar).
- `games` no `manifest.json` passa a listar `crystal` além de `gold`.

## 0.44.1

- `["5e:690a"]` tinha "LAVANDA" em vez de "LAVENDER" -- nome proprio
  traduzido por engano, escapou da regra de manter nome de lugar em
  ingles. Corrigido nos dois catalogos (`dialogue.lua` e o gerado
  `dialogue_gen2recomped.lua`).
- README: a secao "o que o motor nao deixa traduzir" tinha uma alegacao
  errada de que o `gen1recomp` compartilha o bug do prefixo "Enemy " com
  o Gen2Recomped. Conferido no codigo: o `gen1recomp` ja corrigiu isso
  (`Strings("Enemy %s", ...)`, comentado `-- #779` nos quatro arquivos) --
  o problema e exclusivo do Gen2Recomped, que parece ter reimplementado o
  trecho sem herdar o fix. Secao reorganizada com um bloco "so no
  Gen2Recomped" e a nota de que o rotulo curto da especie na POKéDEX
  (nao a descricao) tambem so tem gancho la.

## 0.44.0

**O mod passa a rodar em dois motores a partir de um unico download:**
o `gen1recomp` oficial e o [Gen2Recomped](https://github.com/UNDERdecoded/Gen2Recomped),
fork de UNDERdecodedHD com suporte a Gen 2 mais maduro. Nao e um mod
separado -- e o mesmo `main.lua`/`manifest.json`, so com um catalogo a mais.

- **Novo `lang/dialogue_gen2recomped.lua` (3217 chaves).** O Gen2Recomped
  indexa dialogo por rotulo nomeado (`AbraText`) ou, quando nao resolve
  rotulo, por `TEXT_S<banco>_<endereco>` -- formato diferente do ponteiro
  `"banco:endereco"` que o `gen1recomp` usa em `lang/dialogue.lua`. O
  `Registry:override` do motor (`src/mods/Registry.lua`) aceita qualquer
  chave sem validar, entao a chave que o motor rodando nao reconhece so
  fica parada, sem custo -- e o catalogo extra serve o Gen2Recomped sem
  atrapalhar o `gen1recomp`.
  Gerado cruzando os `data/generated/text.lua` reais dos dois motores para
  a mesma ROM (80,7% bate direto por `TEXT_S<banco>_<endereco>`, o resto
  por texto em ingles identico entre os dois caches). 97,4% das falas do
  `gen1recomp` tem correspondente; as que faltam sao ponteiros que ja nem
  aparecem na extracao atual da ferramenta, resíduo antigo.
- Quatro rotulos escritos a mao no fim do arquivo (comentado, fora da
  parte gerada): a saudacao e o "obrigado" da PokeMart, e as duas falas
  da arvore de fruta -- esses tres/quatro casos leem `data.text[chave]`
  direto, sem passar pelo catalogo `Strings`, entao so uma chave exata
  resolve (`ShopMenu.lua:19-21`, `Gen2Commands.lua:1810,1822`).
- **CITY, TOWN e ROUTE passam a traduzir a palavra generica, mantendo o
  nome proprio em ingles:** "VIOLET CITY" -> "CIDADE DE VIOLET"; "ROUTE 30"
  -> "ROTA 30"; "LAVENDER TOWN" -> "CIDADE DE LAVENDER". Decisao nova,
  troca a que valia ate a 0.43.1 (nome de lugar todo em ingles). Aplicado
  em 92 ocorrencias de CITY, ~32 de TOWN e 41 de ROUTE em `dialogue.lua`;
  boa parte precisou de quebra de linha nova pra caber nas 18 colunas
  depois que "CIDADE DE" (mais longo que "CITY"/"TOWN") entrou.
- **65 nomes de rota/cidade do aviso de "entrando na area"** (o quadro que
  aparece embaixo da tela ao cruzar pra uma rota ou cidade nova) agora em
  `strings.lua`. Esse aviso nao vem do `dialogue.lua` -- vem de
  `data.field.townMap.landmarks`, achatado (quebra de linha vira espaco) e
  passado pra `Strings()` (`OverworldController.lua:606-616` no
  Gen2Recomped). Ponto de interesse que nao e cidade/rota (SPROUT TOWER,
  UNION CAVE, LAKE OF RAGE...) fica no original, fora da regra.
- Corrigido acento sumindo/trocado no Gen2Recomped: `assets/font/latin.png`
  tinha 16px de altura, e o motor exige minimo de 64px pra aceitar pagina
  de fonte customizada nao-"extra" (`src/render/Font.lua`). Preenchido
  com espaco transparente ate 128x64, glifos originais no lugar -- o
  `gen1recomp` nao tem esse limite, entao o PNG maior nao muda nada la.
- `["RUN"]` e `["battle|RUN"]` viraram "FUGA" (era "FUGIR"): o menu de
  batalha desenha a caixa de acao em coordenada fixa, com 32px de sobra
  pra esse botao -- "FUGIR" estourava a borda.
- Seis falas novas em `strings.lua`: `BUY`/`SELL`/`QUIT` (loja), `SEEN`/
  `OWN`/`SEARCH`/`OPTION` (Pokedex e menu inicial), `SOMEONE'S PC`
  (versao maiuscula que o Gen2Recomped usa, além da minuscula que o
  `gen1recomp` ja tinha), `TOSS ITEM`, `Take your time.`/`Thank you!`.
- **Achado, nao corrigido:** a saudacao de abertura do OAK (`_OakText1`
  a `_OakText7`) so e traduzivel no Gen2Recomped. No `gen1recomp` ela
  carrega de `data/generated/oak_speech.lua` direto pra um campo privado
  (`Game2.lua:877`, `self.oakSpeechData`), nunca passa por `self.data` --
  que e o unico caminho que o registro de mod mescla. Fica documentado
  como limite do motor.

## 0.43.1

README refeito.  Nenhuma mudanca no texto do jogo.

- A secao "o que fica no original" agora explica o PORQUE de cada decisao,
  uma a uma: nomes de POKéMON e de golpe, nomes de item (decisao tomada em
  jogo na 0.17.0), TM e HM ("MT29 contem o PSYCHIC" mistura duas linguas no
  mesmo item), os rotulos de status de tres caracteres, os rotulos de
  atributo, e a interface do aplicativo (largura fixa de botao).
- Secao NOVA separando **decisao** de **limite**: a POKéDEX e as 109 frases
  cravadas no motor nao sao escolha nossa, sao coisas que registro de mod
  nenhum alcanca.  Com a nota de que na primeira geracao a POKéDEX E
  traduzivel, e por que.
- A lista de arquivos agora traz a contagem de cada catalogo e explica que
  **catalogo vazio nao e catalogo faltando** -- e a decisao registrada de
  deixar aquilo no original.
- Terminologia oficial pt-BR listada em bloco proprio.

## 0.43.0

**As 251 descricoes de GOLPE, todas traduzidas.**  Com as 161 de item da
0.42.0, as duas categorias de descricao estao completas.

- Aparecem na tela de resumo do POKéMON (SummaryMenu.lua:604) e na bolsa
  quando o item e uma TM ou HM -- ali o jogo mostra a descricao do GOLPE,
  nao a do item (PackMenu.lua:820).  Por isso as 57 TM/HM ficaram de fora
  do catalogo de item: ja sao cobertas por aqui.
- Rota: `mod.content.moves:patch(id, { description = ... })`, dentro de
  `pcall` com aviso no log, igual as de item.
- Onze estouraram 18 colunas ou 2 linhas e foram REESCRITAS, nao amputadas.
  "Sobe muito o SPCL.DEF de quem usa" virou "SPCL.DEF proprio"; o
  "Pode falhar" do PROTECT e do DETECT saiu, porque nao cabia em duas
  linhas e nao muda o que o jogador precisa saber.
- Os rotulos de atributo ficam no original -- ATTACK, DEFENSE, SPEED,
  SPECIAL, SPCL.ATK, SPCL.DEF -- porque e assim que aparecem na tela de
  status.  HP vira PS; PP fica.

Extracao: a tabela de ponteiros de golpe fica em 6d:4000 e a de item em
6e:4000, ambas com dois bytes por indice.  Os nomes, que viram o id, estao
em 6c:5574 (golpes) e 6c:4000 (itens).

## 0.42.0

**As descricoes de ITEM entram: 161 traduzidas.**  E a primeira categoria
nova desde os rotulos de menu -- ate aqui a bolsa e o MART mostravam tudo em
ingles.

- Rota: `mod.content.items:patch(id, { description = ... })`.  O campo
  `description` nao esta declarado no schema de `items`, mas o registro de
  topo e extensivel (Schemas.lua:177-181 preserva chave desconhecida) e quem
  desenha le `def.description` do alvo mesclado (PackMenu.lua:823,
  MartMenu.lua:880, ItemPcMenu.lua:531).
- O `main.lua` aplica cada uma dentro de `pcall` e escreve um aviso no log
  se a rota nao existir, em vez de derrubar o mod.  **Se as descricoes
  aparecerem em ingles no aparelho, o log diz por que.**
- Formato: duas linhas de ate 18 colunas, que e o limite medido no ingles
  (180 das 507 descricoes usam exatamente 18).
- TM e HM ficam de fora de proposito: na bolsa e no MART o jogo mostra a
  descricao do GOLPE que a maquina ensina, nao a do item
  (PackMenu.lua:810).
- `(HOLD)` virou `(SEGURA)` e `(1 BTL)` virou `(1 BAT)`: sao descritores,
  nao nomes.  ATTACK, DEFENSE, SPEED, SPECIAL, PP e EXP. ficam no original,
  porque e assim que aparecem na tela de status.

Extracao nova: `extrair_descricoes.py` le pela TABELA DE PONTEIROS do banco
(dois bytes por indice), como o extrator do motor faz, em vez de varrer
terminadores -- so assim da para saber de QUEM e cada descricao.
`extrair_nomes.py` traz o nome de cada golpe e item para formar o id.

## 0.41.0

**ZERO FALAS DERIVADAS.  O credito virou agradecimento.**

Todo o texto do pacote e traducao propria, escrita do ingles original da ROM
americana.  Nao ha uma unica linha de terceiros.

- **157 chaves de ponteiro desalinhado sairam do pacote.**  Nao eram
  traduziveis e nunca deveriam ter sido publicadas: 108 com endereco fora da
  janela 0x4000-0x7FFF de um banco, 39 cujo ingles decodifica comecando no
  meio de uma frase, 6 com o primeiro segmento truncado, 2 palavras soltas
  ("Inside", "HBADGE.") e 2 vazias.  Dessas, **26 eram traducao NOSSA** --
  feitas em lotes anteriores a triagem existir, e traduziam fragmento
  ("AFARI ZONE OFFICE", "OWN", "onate." -> "ssivo.").
- Publicar override num ponteiro desses e pior do que nao publicar: sem
  override o jogo mostra o texto ORIGINAL, que e o comportamento normal do
  mod para tudo que nao foi traduzido.
- **As duas ultimas falas de verdade que ainda vinham de terceiros** foram
  traduzidas: 53:5ce1 ("Obrigado, senhor!") e 5d:51a6 ("Obrigado!").
- O filtro novo (`ponteiro_ruim` em build_mod.py) aplica o teste da JANELA a
  todo mundo, mas os testes de FRAGMENTO so a fala derivada.  Numa fala
  nossa eles dao falso positivo -- "What?", "OK, then!" e "……" sao inicios
  legitimos e curtos, e a primeira versao do filtro apagou 177 traducoes
  boas antes de eu perceber.
- README e manifest reescritos: a secao "Creditos, e o que esta em
  transicao" virou "Agradecimento a R_Lopes e Night_Shadown".

Falas do pacote: 2809, todas nossas.  Rotulos de menu e batalha: 454.

## 0.40.0

**A regra da caixa de texto mudou, por decisao do usuario: a frase tem de
fazer sentido inteira, nem que a caixa role mais -- e palavra nao se parte.**

Ate aqui a traducao tinha de ter o MESMO numero de linhas do ingles.  O
`pt/estrutura.py` garantia isso, e foi ele que acabou com o erro de
separador trocado.  Mas o portugues e mais longo que o ingles, e amarrar a
contagem obrigava a espremer: foi assim que nasceram "alegrias de",
"programas de" e "CAVERNA do", frases que simplesmente pararam no meio.

O motor sempre permitiu mais: `` acrescenta uma linha na MESMA pagina e a
caixa rola esperando A/B (`src/render/TextBox.lua:152-155`).  So a quebra de
PAGINA (``) precisa continuar batendo com o ingles, porque e ela que marca
a pausa em que o script espera o jogador.

- **159 falas refeitas.**  Nenhuma palavra e mais partida no fim da linha:
  "POKé-" + "MON" virou "POKéMON", "vanta-" + "gens" virou "vantagens",
  "treinado-" + "res" virou "treinadores".  O hifen LEXICAL fica
  ("Bem-vindos" continua "Bem-vindos"), e o "--" do ingles vira virgula.
- **Palavra partida pela quebra de PAGINA tambem foi resolvida**, e a
  preposicao que a regia atravessa junto: "Estatua de POKé-" / pagina /
  "MON…" virou "Estatua" / pagina / "de POKéMON…".
- **Zero palavras partidas e zero travessoes soltos** no catalogo inteiro.
- Paginas que terminavam em preposicao caiu de 18 para 17 nas falas
  refeitas -- o refluxo melhorou o corte em vez de piorar.

O `conferir.py` foi atualizado junto: ele cobrava sequencia de controle
IDENTICA a do ingles, e agora cobra so as quebras de PAGINA.

A mudanca e reversivel: o texto novo mora em `pt/refluxo.py`, gerado por
`_gerar_refluxo.py` e carregado por ultimo.  Tirar `refluxo` da lista LOTES
devolve o texto anterior, inteiro.

## 0.39.1

Auditoria de sentido sobre as 2833 falas nossas: 22 correcoes.  Nenhuma
fala nova -- so conserto do que ja estava publicado.

**Seis frases estavam literalmente cortadas no meio**, todas no lote 31.
O `L()` do `pt/estrutura.py` garante que a CONTAGEM de linhas bata com o
ingles, entao a linha existia; faltava a palavra dentro dela:

    "hoje nao e / segunda. Que"      -> "segunda. Triste…"
    "Essas sao as / alegrias de"     -> "Essa e a alegria / de viajar."
    "KANTO tem bons / programas de"  -> "programa de radio"
    "CAVERNA do"                     -> "DIGLETT'S CAVE"
    "vindos! DOJO de"                -> "FIGHTING DOJO"
    "SILPH CO. / PREDIO da"          -> "PREDIO DA SEDE"

**Uma fala tinha seis erros de uma vez** (53:4525, o RIVAL antes da LIGA):
"INSIGNIAS", "destino e", "va para", "para le" no lugar de "leste", "A
rota la e" e "pior por ter perder".

**Acentos**: MUSICA, sabado (quatro vezes), INSIGNIAS (duas), "voce tambem
e", "esta fechado", "E por que?".

O `conferir.py` tinha aprovado todas: ele valida largura, separador, token
e glifo -- nao valida se a frase termina.  A auditoria nova
(`_erros_reais.py`) procura fala que acaba em preposicao ou artigo, que e a
assinatura da frase cortada.

### Achado que fica em aberto

**26 falas nossas estao em endereco fora da janela 4000-7FFF de um banco** e
foram publicadas assim.  Sao ponteiros desalinhados, a mesma categoria das
133 derivadas que sobraram -- so que estas nos traduzimos, em lotes
anteriores a triagem existir.  Algumas traduzem fragmento: 4d:9549 comeca em
"AFARI ZONE OFFICE" (pedaco de SAFARI), 4d:d148 e so "OWN" (de TOWN),
50:8500 traduz "onate." como "ssivo.".  Entram na mesma decisao das 133.

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

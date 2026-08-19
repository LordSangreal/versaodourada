# Versao Dourada

**Pokemon Gold em portugues brasileiro**, para dois motores a partir de um
unico download: o [gen1recomp](https://github.com/bryanthaboi/gen1recomp)
oficial e o [Gen2Recomped](https://github.com/UNDERdecoded/Gen2Recomped),
fork de UNDERdecodedHD com suporte a Gen 2 mais maduro. Os dois sao
recriacoes nativas dos jogos em Lua/LOVE2D -- nao emuladores.

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia de
Pokemon Gold para o aplicativo importar.

**Todo o texto e traducao propria, escrita a partir do ingles original.**
Nao ha uma unica linha derivada de outra traducao no pacote.

> **Joga Pokemon Crystal?** A traducao do Crystal vive noutro repositorio:
> **[LordSangreal/versaocristal-ptbr](https://github.com/LordSangreal/versaocristal-ptbr)**.
> Ate a 0.45.1 os dois jogos dividiam este mod; a 0.46.0 separou. Veja
> [Por que dois repositorios](#por-que-dois-repositorios) abaixo.

---

## Cobertura

O mod carrega **5221 entradas**. Quanto delas chega a tela depende do motor,
porque parte do texto do Gold ainda nao passa pelo catalogo de traducoes --
esta cravada no codigo.

| | sem o patch de motor | com o patch |
|---|---|---|
| **Total** | **91%** | **97%** |

| categoria | total | sem patch | com patch |
|---|---|---|---|
| Falas de NPC | 2994 | 2994 | 2994 |
| Menus e batalha | 994 | 754 | 860 |
| POKeDEX | 251 | **0** | 251 |
| Nomes de golpe | 252 | 252 | 252 |
| Descricoes de golpe | 252 | 252 | 252 |
| Nomes de item | 161 | 161 | 161 |
| Descricoes de item | 164 | 164 | 164 |
| Classes de treinador | 66 | 66 | 66 |
| Nomes de lugar | 70 | 70 | 70 |
| Nomes de tipo | 17 | 17 | 17 |

Medido por `ferramentas/cobertura.py` contra o `gen1recomp` **0.2.6** de
fabrica.

### Sem o patch: 91%

Instale so o mod e o jogo fica **jogavel e majoritariamente em portugues**.
Falas de NPC, golpes, itens, tipos, classes de treinador, nomes de lugar e
mais de tres quartos dos menus.

**Nada quebra.** Uma chave que o motor nao pede simplesmente nao e usada, e um
registro sem rota e pulado -- o `main.lua` testa antes de aplicar. O que nao
chega **aparece em ingles**, nunca em branco nem cortado.

### Com o patch: 97%

O que falta sao **a POKeDEX inteira** e cerca de 106 chaves de menu e batalha.
Essas dependem de uma alteracao no motor, nao do mod:

- a rota `pokedex` no registro de conteudo do Gold, que ainda nao existe;
- as telas e mensagens do Gold que desenham texto cravado em vez de passar
  por `Strings()`.

Isso e um **PR pendente** no gen1recomp -- ver [Sobre o PR](#sobre-o-pr).

### E os 3% restantes?

Sao **134 chaves de `lang/strings.lua`** que o `gen1recomp` remendado nunca
pede. Ate a 0.47.1 este paragrafo dizia so "sobra das primeiras versoes"; a
0.48.0 abriu a conta, e a maior parte **nao e sobra**:

| o que sao | quantas | chegam a tela? |
|---|---|---|
| chave que so o Gen2Recomped pede | 31 | sim, no outro motor |
| nome de lugar | 65 | sim, por outra rota |
| chave com contexto | 5 | sim |
| fala que na verdade e texto da ROM | 11 | nao -- catalogo errado |
| orfa: nao existe em motor nenhum | 22 | nao |

**As 31 do Gen2Recomped.** O fork poe sob `Strings()` coisas que o
`gen1recomp` deixou cravadas: as perguntas de SURF e CUT, a sala de maquinas
do GAME CORNER, "%s quer batalhar!", a escolha de menino ou menina. Uma chave
que o motor rodando nao reconhece fica parada no registro, sem custo -- e o
mesmo arranjo dos dois catalogos de dialogo. Cada uma dessas **e** um texto em
portugues na tela de quem joga no fork.

**Os 65 nomes de lugar.** ROTA 1 a ROTA 46, CIDADE DE VIOLET e companhia. No
`gen1recomp` o TOWN MAP le `row.name` direto do registro `landmarks`, sem
passar por `Strings()` -- por isso existe `lang/landmarks.lua` com as mesmas
70 entradas, e e ele que serve essa tela. No Gen2Recomped o cartaz de area
passa por `Strings()`, mas o texto-fonte vem do cache da ROM e nao de um
literal do codigo. A regua varre **codigo**; uma chave cuja fonte e **dado**
ela nao tem como ver. Aparecem na tela nos dois motores.

**As 5 com contexto.** `Strings("FIGHT", "battle")` guarda em
`battle|FIGHT`, para o mesmo "FIGHT" poder ser uma coisa na batalha e outra
noutra tela. O codigo tem `"FIGHT"` e `"battle"` como literais separados: a
chave composta nao existe em lugar nenhum para a regua achar. Sao LUTAR,
ITEM, FUG, DESL e FORA -- todas na tela.

**As 11 que sao texto da ROM.** As falas do troco de fichas e da sala de
premios do GAME CORNER. Elas existem, com essas mesmas palavras, no texto que
o extrator tira da ROM -- ou seja, o lugar delas e `lang/dialogue.lua`, com
chave de ponteiro, e nao `strings.lua`. Estao no catalogo errado; sao
trabalho perdido ate serem mudadas de arquivo.

**As 22 orfas.** Essas sim sao a sobra que o README antigo citava: a fala da
mae, o NAME RATER, o MOVE DELETER, os avisos de STRENGTH e WHIRLPOOL, quatro
linhas de batalha. Nao batem com o `gen1recomp`, nem com o Gen2Recomped, nem
com o texto da ROM -- vieram de quando o alvo ainda era a interface de
Red/Blue/Yellow, onde essas frases eram literais do motor. Nao atrapalham
nada: chave que ninguem procura fica inerte.

> **Como isto e medido.** Uma chave conta quando o literal aparece no codigo
> do motor, em qualquer posicao. Contar so `Strings("literal")` subestimaria:
> onde o desenho embrulha uma variavel -- `Chrome.print(Strings(row.label))`
> -- o literal fica cru na tabela do modulo e nenhuma das duas formas casa.
> Foi por isso que ate a 0.47.0 o README dizia 87% e 94%.
>
> A 0.47.1 corrigiu aquilo e chegou a 89% e 96%, mas com um script de sessao
> que nao ficou no projeto: o numero dela nao da para reconferir, e a regua
> desta versao nao o reproduz. A desta versao **e** um arquivo do projeto --
> `ferramentas/cobertura.py` -- e faz o que esta escrito acima: varre todo
> literal de string das tres arvores (gen1recomp de fabrica, gen1recomp
> remendado, Gen2Recomped), resolve as escapadas (`\n`, `\011`) e
> compara com a chave do catalogo. Onde os dois numeros discordam,
> vale o que da para rodar de novo.

Fora da conta, de proposito: nome de POKeMON, de personagem e de cidade (so a
palavra generica traduz -- "CIDADE DE VIOLET"), simbolos, `POKeDEX`,
`POKeMON`, `PP`, e as 50 falas que sao grito de especie e reticencias.

---

## Sobre o PR

A parte que falta esta escrita, testada e **nao enviada**.

Sao 37 arquivos no `gen1recomp`: a rota da POKeDEX, a persistencia de opcao de
mod no Gold, o texto das telas e da batalha do Gold passando a resolver pelo
catalogo, e as unidades da ficha do #DEX (ver [Altura e peso](#altura-e-peso-da-pokedex----metro-e-quilo)). Nenhuma alteracao muda o que um jogo **sem mod** imprime -- as
palavras e ate a quebra de linha ficam identicas.

**Por que ainda nao foi enviado:** o gen1recomp lanca rapido demais. So em
17/08/2026 sairam quatro versoes; em 18/08, mais duas. Cada release apaga o
motor remendado e exige rebase, e quando o teste termina ja existe versao nova
mudando alguma coisa. Enviar um PR sem ter testado direito seria pedir revisao
de um trabalho que eu mesmo nao conferi.

Entao o PR sai **quando estiver testado de verdade**, nao quando estiver
pronto.

---

## Por que dois repositorios

Ate a 0.45.1, Gold e Crystal dividiam um catalogo so. Fazia sentido no
comeco: os dois rodam no Gen2Recomped, que indexa dialogo por **rotulo
nomeado** (`MomGivesPokegearText`), nao por endereco de ROM -- entao a
mesma chave servia os dois.

O problema aparece no detalhe. **582 rotulos existem nos dois jogos com
texto em ingles diferente** -- o Crystal reescreveu falas inteiras, e o
extrator reaproveita o mesmo nome de rotulo. Com um catalogo unico, quem
jogasse Crystal via a fala do Gold traduzida, e vice-versa. Nao ha como
resolver isso dentro de um arquivo so: a chave e a mesma, o texto e que
muda.

Na 0.46.0 o catalogo do Gen2Recomped foi filtrado para conter so os rotulos
que a extracao do **Gold** usa (7614 -> 7324 chaves), e as 27 entradas que
tinham sido escritas a partir do texto do Crystal foram removidas -- voltam
a aparecer em ingles ate serem reescritas com o texto do Gold. Melhor
ingles do que a fala do jogo errado.

`lang/strings.lua` (menus e batalha, indexado pelo texto-fonte em ingles) e
as descricoes de golpe/item (indexadas por ID interno, tipo `POTION`) nao
dependem de como cada jogo numera as falas -- esses catalogos sao identicos
nos dois repositorios.

---

## Dois motores, um download

Nao existe um mod "versao gen1recomp" e outro "versao Gen2Recomped" --
e o mesmo `main.lua`, o mesmo `manifest.json`, a mesma pasta. A unica
diferenca e um catalogo extra, `lang/dialogue_gen2recomped.lua`, que
existe porque os dois motores guardam a mesma fala sob chaves diferentes.

(Isto e sobre **motores**, e vale so para o Gold. A separacao por **jogo**
-- Gold aqui, Crystal no `versaocristal-ptbr` -- e outra coisa, explicada
na secao acima.)

**Por que precisa dos dois catalogos.** O `gen1recomp` indexa cada fala
pelo ponteiro dela na ROM: `"bb:aaaa"` (banco:endereco em hex minusculo,
calculado em `src/script/gen2/Opcodes.lua`). O Gen2Recomped indexa por
rotulo nomeado, no estilo da propria desmontagem da pokecrystal
(`AbraText`, `WantsToBattleText`) ou, quando nao acha rotulo, por um
formato mecanico `TEXT_S<BANCO>_<ENDERECO>` -- o mesmo ponteiro, so
reescrito em maiusculo sem os dois-pontos.

**Por que um catalogo so nao quebra o outro motor.** O registro de
conteudo do mod (`Registry:override`, em `src/mods/Registry.lua` -- codigo
compartilhado pelos dois projetos) aceita qualquer string como chave, sem
validar contra nada. Uma chave que o motor rodando nao reconhece fica
parada na tabela, nunca lida, sem custo nem aviso. Isso significa dar pra
`lang/dialogue.lua` (ponteiros) e `lang/dialogue_gen2recomped.lua`
(rotulos) juntos pros dois motores, e cada um so "enxerga" as chaves que
fazem sentido pra ele.

**Como o catalogo do Gen2Recomped foi gerado.** Com a mesma ROM de Gold
importada nos dois motores, comparando o `data/generated/text.lua` real
que cada um extrai: 80,7% das falas bateu direto convertendo o ponteiro
pro formato `TEXT_S<banco>_<endereco>`; o resto por comparacao de texto em
ingles identico entre os dois caches (quando um endereco tem rotulo
proprio, o texto em ingles la e aqui e igual, entao da pra linkar as duas
chaves). 97,4% das 2815 falas do `gen1recomp` tem correspondente; as ~74
que faltam ja nao aparecem na extracao atual da ferramenta -- resíduo de
uma ROM ou versao anterior, nao relacionado ao Gen2Recomped.

Na 0.46.0 esse catalogo foi filtrado para so as chaves do Gold (ver "Por
que dois repositorios"), e na 0.45.1 o `lang/dialogue.lua` do `gen1recomp`
recebeu 259 falas que so existiam do lado do Gen2Recomped -- e por isso os
dois motores estao hoje praticamente no mesmo nivel.

`lang/strings.lua` (menus e batalha, indexado pelo texto-fonte em ingles
literal) e as descricoes de golpe/item (indexadas por ID interno, tipo
`POTION`) ja funcionam nos dois motores sem precisar de catalogo extra --
essas chaves nao dependem de como cada extrator numera as falas.

---

## O que fica no original -- e por que

Isto e **decisao de traducao**, nao falta dela. Cada item abaixo poderia
ser traduzido tecnicamente; escolhemos que nao fosse.

### Nomes proprios da franquia

**Nomes de POKéMON.** BULBASAUR, PIKACHU, GYARADOS. Sao os nomes oficiais
no mundo inteiro, inclusive nos jogos em portugues. Traduzi-los quebraria
a comunicacao com qualquer guia, video ou amigo.

**Nomes de personagem.** LANCE, JANINE, WHITNEY. Sao elenco -- o jogador
precisa deles pra se achar num guia.

> **Golpes saem desta lista na 0.47.0.** Ate a 0.46.2 ficavam em ingles pelo
> mesmo argumento dos nomes de POKéMON. A regra foi revertida com a
> terminologia de carta de TCG pt-BR, e o risco de inconsistencia entre telas
> e tratado por conferidor: uma entrada de POKeDEX ou descricao que cite um
> golpe tem de usar exatamente a forma de `lang/move_names.lua`, e o
> `dex_verificar.py` recusa o lote quando nao usa. Cabem 11 colunas.

### Cidade, Rota e Vila -- a palavra generica traduz, o nome nao

**VIOLET CITY** vira **CIDADE DE VIOLET**; **ROUTE 30** vira **ROTA 30**;
**LAVENDER TOWN** vira **CIDADE DE LAVENDER**. A palavra generica (CIDADE,
ROTA) vem antes do nome, que fica em ingles -- mesma logica dos nomes de
personagem: o jogador ainda reconhece "VIOLET" num guia ou video, so que
agora "cidade" e "rota" leem em portugues, que e o que da 90% do sentido
da frase pro jogador brasileiro.

Essa e uma troca da decisao anterior (ate a 0.43.1, o nome do lugar ficava
todo em ingles, "GOLDENROD CITY"). "CIDADE DE" e mais longo que "CITY"
sozinho, entao boa parte das ~165 ocorrencias (92 CITY, ~32 TOWN, 41
ROUTE) precisou de quebra de linha nova pra caber nas 18 colunas -- a
caixa aceita, mas so rola se sobrar; nao corta palavra no meio.

Pontos de interesse que nao sao cidade, vila ou rota -- SPROUT TOWER,
UNION CAVE, LAKE OF RAGE, RADIO TOWER -- ficam inteiros em ingles. A regra
e so sobre esses tres sufixos.

### Nomes de item -- traduzidos desde a 0.47.0

POKé BOLA, POÇÃO, FRUTA, REPELENTE, VARA SUPER.

Ate a 0.46.2 ficavam em ingles, junto dos golpes. A regra foi **revertida**
com a terminologia de carta de TCG pt-BR como fonte primaria -- GRANDE BOLA e
nao "Otima Bola", que e do Pokemon GO.

Cabem 12 colunas. As sete APRICORN levam a cor abreviada na frente
(PRT APRICORN, AZL APRICORN) porque e o que o ingles faz e o que mantem a
lista alinhada. As frutas que curam status usam a **mesma sigla da batalha**:
FRUTA PAR., FRUTA VEN.

**A descricao do item, essa esta em portugues.** "POTION / Restaura 20 de
PS do POKéMON." E o padrao que a franquia usa: o nome identifica, a
descricao explica.

### TM e HM

A sigla fica. E o identificador que o jogador ve no numero (TM29), e o nome
do golpe que ela ensina ja aparece traduzido na tela de uso.

### Rotulos de status na caixa de vida -- traduzidos desde a 0.47.0

VEN, QMD, PAR, SON, GEL, DES. Continuam com tres caracteres, porque a caixinha
tem tres. Elas ecoam de proposito nos nomes de fruta: FRUTA VEN. cura VEN.

O que de fato **informa** o jogador e a mensagem na caixa de texto -- "O
veneno fere BULBASAUR!" -- e essa esta em portugues.

### Rotulos de atributo

**Traduzidos a partir da 0.45.0** (decisao anterior, ate a 0.44.1, era
manter em ingles). Nomenclatura sugerida por **Hyd**: ATTACK -> ATAQUE,
DEFENSE -> DEFESA, SPCL.ATK -> ESP.ATQ, SPCL.DEF -> ESP.DEF, SPECIAL ->
ESP., SPEED -> VELOC.

A tela de status desenha o rotulo e o valor numerico em **linhas
separadas** (rotulo em cima, valor alinhado a direita 8px abaixo) -- a
folga real de um rotulo e ate a borda da caixa/tela, no geral 9 a 10
caracteres, nao os 5-6 que um primeiro calculo (errado) sugeriu. E por
isso que "VELOCIDADE" por extenso estourava a caixa mas "VELOC." cabe com
folga.

**HP e a excecao:** vira **PS**, que e a sigla oficial em portugues do
Brasil. PP fica, porque nao tem sigla consagrada em portugues.

### Altura e peso da POKeDEX -- metro e quilo

A ficha de cada especie no #DEX vem em **pe, polegada e libra**, porque a
versao americana do cartucho converteu o que o jogo japones media em metro e
quilo. Aqui volta ao metrico: `AL 0,9m` e `PS 19,5kg`.

**O numero nao sai de converter a libra de volta.** A altura ate sobreviveria
-- a polegada e mais fina que o decimo de metro, e as 251 conferem --, mas o
peso nao: o cartucho gravou 15,0 libras onde o original diz 6,9 kg, e a volta
da 6,8. Sao 196 das 251 erradas por um decimo se a fonte for a libra. Entao a
fonte e a tabela canonica da franquia, cruzada pelo numero da POKeDEX, e o
resultado bate com o que qualquer guia em portugues mostra.

**Onde isso aparece em cada motor.** No Gen2Recomped, so no mod: a tela ja
monta a linha com `Strings("%2d′%02d″", ...)` e `Strings("%4d.%dlb", ...)`,
entao trocar a pontuacao e a unidade e uma linha de catalogo cada. No
`gen1recomp` era impossivel: `lb` estava no catalogo, mas as marcas de pe e
polegada sao **tiles** da folha do #DEX, nao letras -- metade da linha em uma
unidade e metade na outra. O patch de motor poe a linha inteira sob uma forma
de catalogo e mantem o caminho dos tiles enquanto ninguem pedir outra coisa,
entao um jogo sem mod imprime o mesmo de sempre.

O `kind` -- "RATO", "CHAMA" -- e as descricoes ja estavam em portugues desde a
0.47.0; era a ficha de medidas que ficava em ingles no meio delas.

### A interface do aplicativo

Launcher, importacao de ROM, espacos de save, gerenciador de mods: tudo em
ingles, de proposito.

O motivo e largura. Na tela do jogo eu conheco a caixa (18 colunas) e
controlo onde a linha quebra. No aplicativo os botoes tem largura fixa e o
portugues, mais longo, estourava e saia cortado -- "Play Gold (Be...",
"0 insignias - 0:00 - 0 capturados" quebrando no meio.

O filtro e por **arquivo de origem**, nao por lista escrita a mao: uma
frase que aparece em qualquer tela do aplicativo sai automaticamente. Assim
uma versao futura nao reintroduz o problema por descuido.

---

## O que o motor nao deixa traduzir

Isto **nao e decisao** -- e limite. Fica documentado para ninguem gastar
tempo tentando. Alguns limites sao dos dois motores; alguns sao so de um,
porque o Gen2Recomped reescreveu a peca que travava no `gen1recomp`.

### Nos dois motores

**As entradas da POKéDEX (251), so no `gen1recomp`.** A tela le
`data.gen2Pokedex`, uma tabela carregada direto do cache do importador, e
nenhum registro de mod faz merge nela. **No Gen2Recomped isso ja nao e
limite pra descricao** -- ver secao seguinte -- **mas o rotulo curto da
especie continua sendo** ("BIG JAW", "SEED"...): o extrator grava
`kind = table.concat(...)` como string literal
(`RomExtractorGen2.lua`), e a tela desenha com
`Font.draw(e.kind or "?", ...)` (`DexEntryMenu.lua:148,214`), sem chave.
So a descricao (o paragrafo) tem registro pra sobrescrever.

**`BILL'S PC`.** Rotulo do PC depois de conhecer o BILL
(`OverworldController.lua`, os dois motores) -- concatenacao direta, sem
gancho.

### So no Gen2Recomped

**O prefixo "Enemy " antes do nome do POKéMON adversario.** Cinco lugares
fazem `"Enemy " .. nome`, concatenacao crua, sem passar pelo catalogo
`Strings`: `BattleState.lua:452,462`, `EffectRegistry.lua:31`,
`MoveEffects.lua:25`, `StatusRegistry.lua:15`. **O `gen1recomp` ja
corrigiu isso** nos quatro arquivos equivalentes -- cada um tem
`Strings("Enemy %s", b.name)` com o comentario `-- #779` apontando pra
issue que resolveu. O Gen2Recomped parece ter reimplementado esse trecho
sem herdar o fix.

**A barra de baixo da tela de POKéDEX.** `PAGE`/`AREA`/`CRY`/`PRNT`
(`DexEntryMenu.lua:105`) e uma tabela de string cru, sem `Strings()` em
volta. (`SEL`/`OPTION`/`SEARCH`, no `ListMenu.lua` da mesma tela, ja usam
`Strings()` certinho -- so essa tabela ficou de fora.)

### So no `gen1recomp`

**A saudacao de abertura do OAK** (`_OakText1` a `_OakText7`, a
primeirissima fala do jogo). Carrega de `data/generated/oak_speech.lua`
pra um campo privado, `self.oakSpeechData` (`src/core/Game2.lua:877`) --
nunca passa por `self.data`, que e o unico lugar que o registro de mod
mescla. Comparar com `self.data.font`, que o proprio codigo do motor
comenta ser "o alvo do registro `font`, entao um mod que sobrescreve um
glifo e mesclado ali": o `oakSpeechData` nao tem esse comentario porque
nao tem esse caminho.

**No Gen2Recomped essas mesmas sete falas ja traduzem** -- o
`src/ui/OakSpeech.lua` de la le de `game.data.text`, o registro normal.
`lang/dialogue.lua` ja carrega as sete (chave = rotulo, tipo `_OakText1`,
nao ponteiro); funcionam nos dois motores quando o motor deixa.

### 109 frases da batalha e dos menus (levantamento do `gen1recomp`)

"A critical hit!", "It's super effective!", as mensagens de clima, as de
captura, as de usar item. Estao escritas direto no codigo do motor, fora
de qualquer registro. Nao foi reconferido item por item contra o
Gen2Recomped -- pode ser que uma parte ja tenha gancho la, do jeito que
"sent out"/"wants to battle" tem (ver proximo paragrafo) e "Enemy " e
POKéDEX-menu nao tem.

**Achado interessante:** varias dessas 109 -- "%s sent\nout %s!", "Wild
%s\nappeared!" -- **ja funcionam no Gen2Recomped**, porque o fork unificou
o codigo de batalha de Gen 1 e Gen 2 num arquivo so
(`src/battle/BattleState.lua`), e as falas passam pelo mesmo `Strings()`
que o Gen 1 sempre teve. No `gen1recomp`, Gen 2 tem arquivo proprio
(`src/battle/gen2/Battle.lua`) com essas mensagens concatenadas cruas,
sem gancho nenhum.

Os casos documentados aqui sao assunto para o upstream de cada projeto, e
estao com os caminhos de arquivo para quem quiser abrir a issue.

---

## Terminologia

A traducao segue a localizacao oficial em portugues do Brasil, que chegou
aos jogos com Scarlet/Violet:

**Ginasio** (nao "academia") · **Lider de Ginasio** · **Treinador** ·
**Insignia** (nao "medalha") · **Centro POKéMON** · **Bolsa** (nao
"mochila") · **PS** para HP · **Cidade de**/**Rota** para CITY/TOWN e
ROUTE (nome proprio fica em ingles) · **Ataque/Defesa/Esp.Atq/Esp.Def/
Veloc.** para os atributos na tela de status

---

## Instalacao

Precisa da versao atual do `gen1recomp` **ou** do Gen2Recomped, com Gold
importado. O suporte a Gold e beta nos dois.

> **Usava este mod para jogar Crystal?** A partir da 0.46.0 ele declara so
> `gold` no manifesto e o catalogo nao tem mais as chaves do Crystal --
> instale o
> [versaocristal-ptbr](https://github.com/LordSangreal/versaocristal-ptbr)
> no lugar. Os dois podem ficar instalados ao mesmo tempo: tem id
> diferente e cada um so ativa no jogo dele.

**Pelo catalogo do aplicativo** (recomendado -- atualiza sozinho; so
funciona no `gen1recomp` por enquanto, o Gen2Recomped nao tem essa tela
ainda). Em *Ajustes -> indices de mod*, adicione:

```
https://raw.githubusercontent.com/LordSangreal/versaodourada/main/site/data/index.json
```

Depois use *Refresh all*. O indice tem cache de 24 horas, entao e o refresh
que traz uma versao nova na hora.

**Manualmente, nos dois motores:** baixe o zip do release e importe pelo
botao *Import mod .zip* no painel de MODS -- mesma tela, mesmo fluxo, nos
dois aplicativos (e no desktop e no Android).

Confira no gerenciador de mods que ele aparece habilitado. Se aparecer
`ENABLED (NOT THIS GAME)`, o boot nao e de Gold.

---

## Creditos

Todo o texto do pacote e traducao propria, escrita a partir do ingles
original da ROM americana.

### Agradecimento a R_Lopes e Night_Shadown

A traducao deles, publicada nos anos 2000 como patch de ROM, foi o ponto de
partida deste projeto: as primeiras versoes portavam aquele texto para o
formato do gen1recomp, e a ROM brasileira serviu de conferencia enquanto a
traducao propria era escrita, lote a lote.

Da 0.34.0 a 0.40.0 cada uma dessas falas foi reescrita do ingles. Na 0.41.0
saiu a ultima. O credito obrigatorio virou o que sempre quis ser: um
obrigado.

Nao foi possivel localizar os autores. Se voce e um deles e quer que este
mod saia do ar, abra uma issue -- sai.

### Os motores

`gen1recomp` e de **bryanthaboi** e dos contribuidores do projeto.
Gen2Recomped e o fork de **UNDERdecodedHD**, que trouxe o suporte a Gen 2
que torna varios dos ganchos deste mod possiveis.

### Contribuicoes

**Hyd** sugeriu a nomenclatura dos rotulos de atributo na tela de status
(ATAQUE, DEFESA, ESP.ATQ, ESP.DEF, VELOC.) que entrou na 0.45.0.

---

## Arquivos do pacote

```
main.lua                        registra os overrides quando o jogo abre
manifest.json                   quem o mod e e para qual jogo

lang/dialogue.lua               3074 falas; chave = ponteiro da ROM USA ("bb:aaaa"),
                                 le nos dois motores (gen1recomp por definicao;
                                 Gen2Recomped so nas poucas chaves nomeadas que
                                 tambem estao aqui, como as sete do OAK)
lang/dialogue_gen2recomped.lua  7459 chaves; rotulo nomeado ou TEXT_S<banco>_<endereco>
                                 do Gen2Recomped -- so as chaves que a extracao
                                 do Gold usa (o Crystal tem repositorio proprio)
lang/strings.lua                 994 textos do motor: batalha, menus, opcoes,
                                 os avisos de entrada em rota/cidade, os rotulos
                                 de atributo da tela de status e as unidades de
                                 altura e peso do #DEX
lang/pokedex.lua                 251 entradas de POKeDEX: categoria, as duas
                                 telas de descricao e as medidas em metro e quilo
lang/move_names.lua              252 nomes de golpe
lang/move_descriptions.lua       252 descricoes de golpe; chave = id do golpe
lang/item_names.lua              161 nomes de item
lang/item_descriptions.lua       164 descricoes de item; chave = id do item
lang/trainer_classes.lua          66 classes de treinador ("CACA-INSETOS BENNY")
lang/landmarks.lua                70 nomes de lugar para o TOWN MAP do POKeGEAR,
                                 que le do registro `landmarks` e nao de Strings()
lang/type_names.lua               17 nomes de tipo
lang/status_labels.lua             6 siglas de status da caixa de vida (VEN, QMD...)
lang/font.lua                        a pagina de glifos que o mod acrescenta
lang/charmap.lua                  25 que sequencia de bytes desenha qual glifo

assets/font/latin.png             os glifos acentuados, desenhados do zero;
                                   128x64 -- a altura extra e so espaco vazio,
                                   exigencia minima do Gen2Recomped
```

Um catalogo so chega a tela onde o motor tem rota para ele: `pokedex.lua`
exige o patch do `gen1recomp`, `landmarks.lua` so existe no `gen1recomp`, e as
descricoes de golpe e item so o `gen1recomp` desenha. Onde nao ha rota, o
registro e pulado e o texto sai em ingles -- ver [Cobertura](#cobertura).

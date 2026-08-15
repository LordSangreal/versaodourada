# Versao Dourada/Cristal

**Pokemon Gold e Crystal em portugues brasileiro**, para dois motores a
partir de um unico download: o
[gen1recomp](https://github.com/bryanthaboi/gen1recomp) oficial (so Gold)
e o [Gen2Recomped](https://github.com/UNDERdecoded/Gen2Recomped), fork de
UNDERdecodedHD com suporte a Gen 2 mais maduro (Gold e Crystal). Os dois
sao recriacoes nativas dos jogos em Lua/LOVE2D -- nao emuladores.

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia de
Pokemon Gold ou Crystal para o aplicativo importar.

**Todo o texto e traducao propria, escrita a partir do ingles original.**
Nao ha uma unica linha derivada de outra traducao no pacote.

---

## Estado

Cobertura real (falas com conteudo de fato -- fora placeholder generico do
motor, grito de especie e afins) por jogo e motor:

| Jogo / motor | Cobertura |
|---|---|
| Crystal, Gen2Recomped | **99,4%** |
| Gold, Gen2Recomped | **99,4%** |
| Gold, `gen1recomp` | **88,0%** |

O Crystal recebeu uma passada completa "na ordem do jogo" nesta versao
(0.45.0): do inicio em New Bark Town ate o Hall of Fame, mais Ruins of
Alph, Day Care, Battle Tower e as 170 falas de treinador que faltavam.
O `gen1recomp` fica pra tras porque usa um catalogo proprio, indexado por
ponteiro de ROM (`lang/dialogue.lua`) -- o trabalho desta versao foi todo
no catalogo do Gen2Recomped (`lang/dialogue_gen2recomped.lua`), que serve
Gold e Crystal nesse motor mas nao alimenta o `gen1recomp` de volta.

| O que | Quanto |
|---|---|
| Falas do jogo (`gen1recomp`, ponteiro de ROM) | 2815 |
| Falas do jogo (Gen2Recomped, rotulo nomeado) | 7614 |
| Rotulos de menu e batalha (inclui 65 de rota/cidade) | 645 |
| Descricoes de golpe | 251 |
| Descricoes de item | 161 |
| Glifos acentuados desenhados | 25 |

O que ainda nao foi traduzido **aparece em ingles**, nunca em branco nem
cortado: o mod so substitui o que tem traducao pronta, entao o jogo e
sempre jogavel.

---

## Dois motores, um download

Nao existe um mod "versao gen1recomp" e outro "versao Gen2Recomped" --
e o mesmo `main.lua`, o mesmo `manifest.json`, a mesma pasta. A unica
diferenca e um catalogo extra, `lang/dialogue_gen2recomped.lua`, que
existe porque os dois motores guardam a mesma fala sob chaves diferentes.

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

**Nomes de golpe.** THUNDERBOLT, SURF, EARTHQUAKE. Mesma razao, e com um
agravante: o nome do golpe aparece em dezenas de lugares (batalha, resumo,
TM, tutor), e uma traducao inconsistente entre eles seria pior que o
ingles.

**Nomes de personagem.** LANCE, JANINE, WHITNEY. Sao elenco -- o jogador
precisa deles pra se achar num guia.

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

### Nomes de item

**Todos** ficam em ingles: POKé BALL, POTION, BERRY, REPEL, SUPER ROD.

Esta foi uma decisao tomada **em jogo**, na 0.17.0. A versao anterior
traduzia os nomes, e ver aquilo funcionando mostrou o problema: item entra
na mesma categoria dos golpes e dos POKéMON -- e vocabulario compartilhado
da franquia, nao prosa.

**A descricao do item, essa esta em portugues.** "POTION / Restaura 20 de
PS do POKéMON." E o padrao que a franquia usa: o nome identifica, a
descricao explica.

### TM e HM

A sigla fica. Traduzir so ela produziria **"MT29 contem o PSYCHIC"** --
duas linguas no mesmo item, no mesmo folego. Como o nome do golpe fica em
ingles por decisao anterior, a sigla o acompanha.

### Rotulos de status na caixa de vida

PSN, BRN, PAR, SLP, FRZ ficam. Sao tres caracteres numa caixinha de tres
caracteres, e a sigla da franquia e lida sem pensar em qualquer idioma.

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

lang/dialogue.lua               2815 falas; chave = ponteiro da ROM USA ("bb:aaaa"),
                                 le nos dois motores (gen1recomp por definicao;
                                 Gen2Recomped so nas poucas chaves nomeadas que
                                 tambem estao aqui, como as sete do OAK)
lang/dialogue_gen2recomped.lua  7614 chaves; rotulo nomeado ou TEXT_S<banco>_<endereco>
                                 do Gen2Recomped -- gerado, nao editar a mao
                                 (excecao: as secoes comentadas no fim do arquivo,
                                 escritas a mao com a passada completa do Crystal)
lang/strings.lua                645 textos do motor: batalha, menus, opcoes,
                                 os avisos de entrada em rota/cidade, e os
                                 rotulos de atributo da tela de status
lang/move_descriptions.lua      251 descricoes de golpe; chave = id do golpe
lang/item_descriptions.lua      161 descricoes de item; chave = id do item
lang/font.lua                        a pagina de glifos que o mod acrescenta
lang/charmap.lua                  25 que sequencia de bytes desenha qual glifo
lang/item_names.lua                  vazio: nome de item fica em ingles
lang/status_labels.lua               vazio: PSN/BRN/PAR/SLP/FRZ ficam

assets/font/latin.png             os glifos acentuados, desenhados do zero;
                                   128x64 -- a altura extra e so espaco vazio,
                                   exigencia minima do Gen2Recomped
```

Um catalogo vazio nao e um catalogo faltando: e a decisao registrada de
deixar aquilo no original.

# Versao Dourada

**Pokemon Gold e Silver em portugues brasileiro — 90% da traducao chega a tela
sem tocar no motor, 97% com o patch — rodando no gen1recomp e no Gen2Recomped,
num unico download.**

Os dois sao recriacoes nativas dos jogos em Lua/LOVE2D, nao emuladores:
[gen1recomp](https://github.com/bryanthaboi/gen1recomp), de bryanthaboi, e
[Gen2Recomped](https://github.com/UNDERdecoded/Gen2Recomped), o fork de
UNDERdecodedHD com suporte a Gen 2 mais maduro.

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia.

**Todo o texto e traducao propria, escrita a partir do ingles original.** Nao ha
uma unica linha derivada de outra traducao no pacote.

> **Joga Pokemon Crystal?** Vive noutro repositorio:
> **[LordSangreal/versaocristal-ptbr](https://github.com/LordSangreal/versaocristal-ptbr)**.
> Ate a 0.45.1 o Crystal dividia este mod; a 0.46.0 separou, e a razao esta em
> [Por que o Crystal se separou](#por-que-o-crystal-se-separou).

---

## Cobertura

| | sem o patch de motor | com o patch |
|---|---|---|
| **Total** | **90%** | **97%** |

Sao **5312 entradas medidas por jogo** (o pacote carrega 5563, porque a POKeDEX
tem uma versao para cada jogo).

| categoria | total | sem patch | com patch |
|---|---|---|---|
| Falas de NPC | 2994 | 2994 | 2994 |
| Menus e batalha | 1085 | 787 | 929 |
| POKeDEX | 251 | **0** | 251 |
| Nomes de golpe | 252 | 252 | 252 |
| Descricoes de golpe | 252 | 252 | 252 |
| Nomes de item | 161 | 161 | 161 |
| Descricoes de item | 164 | 164 | 164 |
| Classes de treinador | 66 | 66 | 66 |
| Nomes de lugar | 70 | 70 | 70 |
| Nomes de tipo | 17 | 17 | 17 |

Medido por `ferramentas/cobertura.py` contra o `gen1recomp` **0.2.15**.

### Sem o patch: 90%

Instale so o mod e o jogo fica **jogavel e majoritariamente em portugues**:
falas de NPC, golpes, itens, tipos, classes de treinador, nomes de lugar e tres
quartos dos menus.

**Nada quebra.** Uma chave que o motor nao pede simplesmente nao e usada, e um
registro sem rota e pulado — o `main.lua` testa antes de aplicar. O que nao
chega **aparece em ingles**, nunca em branco nem cortado.

### Com o patch: 97%

Faltam a **POKeDEX inteira** e 156 chaves de menu e batalha. As duas
dependem de uma alteracao no **motor**, nao do mod:

- a rota `pokedex` no registro de conteudo do Gold, que o upstream ainda nao
  tem;
- as telas do Gold que montam a frase com concatenacao ou guardam a pagina como
  lista de linhas, em vez de perguntar ao catalogo.

Isso e um **PR pendente** — ver [Sobre o PR](#sobre-o-pr).

### E os 3% restantes?

Sao **152 chaves de `lang/strings.lua`** que o motor remendado nunca pede. A
maior parte **nao e desperdicio**: tres categorias chegam a tela e a regua e que
nao as enxerga.

| o que sao | quantas | chega a tela? |
|---|---|---|
| chave que so o Gen2Recomped pede | 38 | sim, no outro motor |
| nome de lugar | 65 | sim, por outra rota |
| texto de cache (trocas com NPC) | 12 | sim, com o patch |
| chave com contexto | 5 | sim |
| fala que e texto da ROM | 10 | **nao** — catalogo errado |
| orfa: nao existe em motor nenhum | 22 | **nao** |

**Nome de lugar** e o caso mais instrutivo: no gen1recomp o TOWN MAP le
`row.name` direto do registro `landmarks` (por isso existe `lang/landmarks.lua`),
e no Gen2Recomped o cartaz de area passa por `Strings()` — mas o texto-fonte vem
do **cache da ROM**, nao de um literal do codigo. A regua varre codigo; uma
chave cuja fonte e **dado** ela nao tem como ver.

**Texto de cache** e o caso que entrou na 0.51.0, e e o mesmo defeito de regua
visto de outro angulo: a conversa das trocas com NPC nao esta no dump de
dialogo indexado por ponteiro -- ela mora em `events.tradeTexts`, escrita pelo
extrator a partir da ROM. O patch passa o corpo por `Strings()`, entao a fala
chega traduzida a tela; mas a **fonte** dela continua sendo dado, e por isso a
varredura de codigo nao a encontra.

**Chave com contexto**: `Strings("FIGHT", "battle")` guarda sob uma chave
composta. O codigo escreve as duas metades separadas, e a chave inteira nao
existe em lugar nenhum para a regua achar. Sao LUTAR, ITEM, FUG, DESL e FORA.

So **32 de fato nao chegam**: 10 falas do GAME CORNER que estao no catalogo
errado (o lugar delas e `dialogue.lua`) e 22 orfas da epoca em que o alvo ainda
era a interface de Red/Blue/Yellow.

> **Como isto e medido.** Uma chave conta quando o literal aparece no codigo do
> motor, em qualquer posicao. Contar so `Strings("literal")` subestimaria: onde
> o desenho embrulha uma variavel, o literal fica cru na tabela do modulo. A
> regua e um arquivo do projeto (`ferramentas/cobertura.py`), entao o numero da
> para conferir. Ha tambem a regua ao contrario, `ferramentas/faltando.py`, que
> responde "o que o motor pede e o catalogo nao tem".

---

## Gold e Silver no mesmo mod

Nao existem duas versoes do pacote: e o mesmo arquivo, e o manifesto declara os
dois jogos.

Isso e possivel porque as duas ROMs dividem quase tudo. Medido catalogo por
catalogo (`ferramentas/comparar.py`, relatorio em `GOLD-x-SILVER.md`):

| catalogo | linhas | diferentes |
|---|---|---|
| dialogo | 3134 | **0** |
| itens, golpes, lugares, treinadores | 14561 | **0** |
| POKeDEX | 2261 | **504** |

O texto de NPC e **identico**, palavra por palavra. So oito falas mudam de
endereco — STRENGTH e ROCK SMASH moram dois bytes antes no Silver — e o catalogo
carrega as duas chaves. Chave que o jogo rodando nao pede fica inerte.

### A POKeDEX troca sozinha

As 251 especies tem ficha **propria** em cada versao, e o registro e indexado
por id de especie: um catalogo unico mostraria a ficha do Gold para quem joga
Silver. Entao o `main.lua` pergunta em qual jogo esta e carrega
`lang/pokedex.lua` ou `lang/pokedex_silver.lua`.

```
CYNDAQUIL / gold  : Ele e timido e sempre se enrola como uma bolinha.
CYNDAQUIL / silver: Ele costuma ficar encolhido. Se leva um susto ou fica...
```

**Quem responde e a propria ROM.** ENTEI e TYRANITAR tem a altura TROCADA entre
as versoes. E a unica diferenca **numerica** entre as duas fichas, entao a
identidade nao depende de decodificar texto. E lida ANTES de o mod escrever
qualquer coisa; depois, o valor lido seria o nosso.

As **502 descricoes do Silver** foram escritas do zero, a partir do ingles
daquela ROM. O `kind` nao foi retraduzido — a categoria e identica nas duas — e
as medidas vem do catalogo do Gold, o que de quebra desfaz a troca de ENTEI e
TYRANITAR.

---

## Tres coisas voce escolhe

Em **MODS -> Versao Dourada -> OPTIONS** ha tres linhas:

| linha | escolhas | o que muda |
|---|---|---|
| NOME DOS GOLPES | PORTUGUES / ENGLISH | so o **nome** do golpe |
| NOME DOS ITENS | PORTUGUES / ENGLISH | so o **nome** do item |
| NOME DOS NPCS | PORTUGUES / ENGLISH | a **classe** do treinador |

Sao os nomes, e so eles: a **descricao** do golpe, da TM e do item continua em
portugues nos dois modos. Ela explica o efeito, e ninguem procura guia por ela.

As tres existem porque o argumento que segurou essa traducao ate a 0.47.0 nao
evaporou quando a regra virou: **quem joga com guia aberto quer o nome que o
guia usa**. Agora e escolha em vez de discussao.

### NOME DOS NPCS e a CLASSE, nao o nome proprio

A linha troca o rotulo que vem colado no nome do treinador:
**CACADOR DE INSETOS BENNY** vira **BUG CATCHER BENNY**.

O nome proprio nao entra nisso. BENNY, LANCE, WHITNEY e JANINE ficam como
estao nos dois modos — nome de personagem **nunca** se traduz neste mod, e nao
existe catalogo para isso. Ver [O que fica no original](#o-que-fica-no-original--e-por-que).

### Precisa reiniciar — e a tela avisa

O mod decide **no carregamento** o que registrar, e registro aplicado nao se
desfaz. Mudar a linha com o jogo aberto nao teria efeito nenhum ate o proximo
boot.

O gerenciador de mods promete `B:DONE (NO RESTART)` no rodape, o que e verdade
para um mod que le a opcao em tempo real e mentira para este. O patch
acrescenta o campo opcional `requires_restart` a uma linha de esquema: com ele
a tela mostra `B:DONE - RESTART` e avisa `RESTART TO APPLY` a cada mudanca.

**Sem o patch a escolha funciona do mesmo jeito** — o campo e ignorado por um
motor que nao o conheca, como a RFC 0008 permite; o que se perde e so o aviso
na tela.

E ela **sobrevive ao reinicio no motor de fabrica**: `modOptions` e uma das
chaves compartilhadas de `options.lua` (`SHARED_KEYS`, em
`src/core/gen2/Save.lua`), gravada no topo do arquivo e nao dentro do bloco
`gold`, que e exatamente onde o carregador de mods a procura no boot
seguinte. Foi por isso que estas linhas puderam existir: um controle que
o jogador muda e que volta sozinho no reinicio seria pior do que nao ter
controle nenhum.

---

## O que fica no original — e por que

Isto e **decisao de traducao**, nao falta dela.

**Nomes de POKeMON.** BULBASAUR, PIKACHU, GYARADOS. Sao os nomes oficiais no
mundo inteiro, inclusive nos jogos em portugues. Traduzi-los quebraria a
comunicacao com qualquer guia, video ou amigo.

**Nomes de personagem.** LANCE, JANINE, WHITNEY. Sao elenco — o jogador precisa
deles para se achar num guia.

**TM e HM.** A sigla e o identificador que o jogador ve no numero (TM29), e o
golpe que ela ensina ja aparece traduzido na tela de uso.

**A interface do aplicativo.** Launcher, importacao de ROM, espacos de save,
gerenciador de mods: tudo em ingles, de proposito. O motivo e largura — no
aplicativo os botoes tem tamanho fixo e o portugues, mais longo, saia cortado.
O filtro e por **arquivo de origem**, nao por lista escrita a mao, entao uma
versao futura nao reintroduz o problema por descuido.

### Cidade, Rota e Vila: a palavra generica traduz, o nome nao

**VIOLET CITY** vira **CIDADE DE VIOLET**; **ROUTE 30** vira **ROTA 30**. O
jogador ainda reconhece "VIOLET" num guia, mas "cidade" e "rota" leem em
portugues — que e o que da o sentido da frase. Pontos de interesse que nao sao
cidade, vila ou rota (SPROUT TOWER, UNION CAVE, RADIO TOWER) ficam inteiros em
ingles: a regra e so sobre esses tres sufixos.

### O que mudou de ideia pelo caminho

| desde | o que passou a se traduzir |
|---|---|
| 0.45.0 | rotulos de atributo (ATAQUE, DEFESA, ESP.ATQ, VELOC.) |
| 0.47.0 | golpes, itens, tipos, classes de treinador e siglas de status |
| 0.48.0 | altura e peso da POKeDEX, em metro e quilo |
| 0.51.0 | a conversa das trocas com NPC |

Golpes e itens ficavam em ingles pelo mesmo argumento dos nomes de POKeMON. A
regra foi revertida com a terminologia de **carta de TCG pt-BR** como fonte
primaria (GRANDE BOLA, e nao "Otima Bola", que e do Pokemon GO). O risco de
inconsistencia entre telas e tratado por conferidor: uma entrada de POKeDEX ou
descricao que cite um golpe tem de usar exatamente a forma de
`lang/move_names.lua`, e o `dex_verificar.py` recusa o lote quando nao usa.

### Altura e peso da POKeDEX: metro e quilo

A ficha vinha em **pe, polegada e libra**, porque a versao americana do cartucho
converteu o que o jogo japones media em metrico. Aqui volta ao metrico:
`AL 0,9m` e `PS 19,5kg`.

**O numero nao sai de converter a libra de volta.** A altura ate sobreviveria —
a polegada e mais fina que o decimo de metro, e as 251 conferem —, mas o peso
nao: o cartucho gravou 15,0 libras onde o original diz 6,9 kg, e a volta da 6,8.
Seriam 196 das 251 erradas por um decimo. A fonte e a tabela canonica da
franquia.

No `gen1recomp` isso exige o patch: `lb` estava no catalogo, mas as marcas de pe
e polegada sao **tiles** da folha do #DEX, nao letras — daria metade da linha em
cada unidade.

---

## O que o motor nao deixa traduzir

Isto **nao e decisao** — e limite, e fica documentado para ninguem gastar tempo
tentando.

**O rotulo curto da especie na POKeDEX** ("BIG JAW", "SEED") no Gen2Recomped: o
extrator grava a categoria como string literal e a tela desenha sem passar por
chave.

**O rotulo do PC do BILL** nos dois motores: concatenacao direta, sem gancho.

**A saudacao de abertura do OAK**, so no `gen1recomp`: carrega de
`data/generated/oak_speech.lua` para um campo privado que o registro de mod
nunca mescla. **No Gen2Recomped essas mesmas sete falas ja traduzem.**

**O prefixo "Enemy "** e a barra de baixo da POKeDEX, so no Gen2Recomped.

### Ainda por varrer

O `ferramentas/sitios_crus.py` lista os literais de tela que nao passam pelo
catalogo num arquivo do motor. Restam bolsoes conhecidos: `Pokegear.lua` (81 —
e onde moram os **programas de radio**, ainda em ingles), `PrizeMenu.lua` (46),
`PackMenu.lua` (18) e 31 em `battle/gen2/Battle.lua`.

A conversa das **trocas com NPC** saiu dessa lista na 0.51.0, e por um caminho
diferente: ela nao era literal de codigo nenhum: as falas vinham de
`events.tradeTexts`, cache escrito a partir da ROM, sem registro de mod que as
alcancasse. O patch passa o corpo por `Strings()` em `TradeMenu.lua` e
`TradeAnim.lua`, e o catalogo faz o resto.

---

## Sobre o PR

A parte que falta esta escrita, testada e **nao enviada**.

Sao 42 arquivos no `gen1recomp`, sobre a base **0.2.11**: a rota da POKeDEX, a
conversa das trocas com NPC, o campo `requires_restart` na linha de opcao, e o
texto das telas, da batalha, do PC, do save e da evolucao passando a resolver
pelo catalogo. Nenhuma alteracao muda o que um jogo **sem mod** imprime — as
palavras e ate a quebra de linha ficam identicas.

Comparado com o `origin/dev` limpo, o patch acrescenta **+27 verificacoes e zero
falhas novas**: as 227 do `gate_gen2_mod_api` e os quatro tiers vermelhos
aparecem igual no dev puro.

**Por que ainda nao foi enviado:** o gen1recomp lanca rapido demais — quatro
versoes num unico dia, 91 commits entre 0.2.6 e 0.2.11. Cada release apaga o
motor remendado e exige rebase, e quando o teste termina ja existe versao nova.
Enviar um PR sem ter testado direito seria pedir revisao de um trabalho que eu
mesmo nao conferi. O PR sai **quando estiver testado de verdade**.

---

## Por que o Crystal se separou

Ate a 0.45.1, Gold e Crystal dividiam um catalogo so. Fazia sentido: os dois
rodam no Gen2Recomped, que indexa dialogo por **rotulo nomeado**, nao por
endereco de ROM.

O problema aparece no detalhe. **582 rotulos existem nos dois jogos com texto em
ingles diferente** — o Crystal reescreveu falas inteiras, e o extrator
reaproveita o mesmo nome de rotulo. Com um catalogo unico, quem jogasse Crystal
via a fala do Gold traduzida, e vice-versa.

**Compare com o Gold e o Silver**, que convivem no mesmo mod: la o texto de
dialogo e identico, entao a chave compartilhada e correta. A POKeDEX, que
difere, ganhou um arquivo por jogo. E a mesma pergunta com respostas diferentes,
e e por isso que o Crystal precisou de repositorio proprio e o Silver nao.

---

## Dois motores, um download

O `gen1recomp` indexa cada fala pelo **ponteiro dela na ROM**. O Gen2Recomped
indexa por **rotulo nomeado** ou, quando nao acha rotulo, por um formato
mecanico com banco e endereco.

O registro de conteudo aceita qualquer string como chave, sem validar. Uma chave
que o motor rodando nao reconhece fica parada, nunca lida, sem custo nem aviso.
Por isso da para entregar `lang/dialogue.lua` (ponteiros) e
`lang/dialogue_gen2recomped.lua` (rotulos) juntos: cada motor so enxerga as
chaves que fazem sentido para ele.

E o mesmo arranjo que faz as oito chaves do Silver conviverem com as do Gold.

---

## Terminologia

A traducao segue a localizacao oficial em portugues do Brasil, que chegou aos
jogos com Scarlet/Violet:

**Ginasio** (nao "academia") · **Lider de Ginasio** · **Treinador** ·
**Insignia** (nao "medalha") · **Centro POKeMON** · **Bolsa** (nao "mochila") ·
**PS** para HP · **Cidade de**/**Rota** para CITY/TOWN e ROUTE ·
**Ataque/Defesa/Esp.Atq/Esp.Def/Veloc.** para os atributos

---

## Instalacao

Precisa da versao atual do `gen1recomp` **ou** do Gen2Recomped, com Gold ou
Silver importado.

**Pelo catalogo do aplicativo** (recomendado — atualiza sozinho; so no
`gen1recomp` por enquanto). Em *Ajustes -> indices de mod*, adicione:

```
https://raw.githubusercontent.com/LordSangreal/versaodourada/main/site/data/index.json
```

Depois use *Refresh all*. O indice tem cache de 24 horas, entao e o refresh que
traz uma versao nova na hora.

**Manualmente, nos dois motores:** baixe o zip do release e importe pelo botao
*Import mod .zip* no painel de MODS — mesma tela nos dois aplicativos, no
desktop e no Android.

Confira no gerenciador de mods que ele aparece habilitado. Se aparecer
`ENABLED (NOT THIS GAME)`, o boot nao e de Gold nem de Silver.

> **A POKeDEX exige o motor remendado.** Sem ele o mod funciona e essa tela sai
> em ingles. E **um motor remendado ANTIGO com mod novo** e o pior dos dois
> mundos: recebe o numero metrico e desenha no molde de pe e libra. Atualize os
> dois juntos.

---

## Creditos

Todo o texto do pacote e traducao propria, escrita a partir do ingles original
das ROMs americanas.

### Agradecimento a R_Lopes e Night_Shadown

A traducao deles, publicada nos anos 2000 como patch de ROM, foi o ponto de
partida deste projeto: as primeiras versoes portavam aquele texto para o formato
do gen1recomp, e a ROM brasileira serviu de conferencia enquanto a traducao
propria era escrita, lote a lote.

Da 0.34.0 a 0.40.0 cada uma dessas falas foi reescrita do ingles. Na 0.41.0 saiu
a ultima. O credito obrigatorio virou o que sempre quis ser: um obrigado.

Nao foi possivel localizar os autores. Se voce e um deles e quer que este mod
saia do ar, abra uma issue — sai.

### Os motores

`gen1recomp` e de **bryanthaboi** e dos contribuidores do projeto.
Gen2Recomped e o fork de **UNDERdecodedHD**, que trouxe o suporte a Gen 2 que
torna varios dos ganchos deste mod possiveis.

### Contribuicoes

**Hyd** sugeriu a nomenclatura dos rotulos de atributo na tela de status
(ATAQUE, DEFESA, ESP.ATQ, ESP.DEF, VELOC.) que entrou na 0.45.0.

---

## Arquivos do pacote

```
main.lua                        registra os overrides quando o jogo abre;
                                 e onde o mod descobre se e Gold ou Silver
manifest.json                   quem o mod e e para quais jogos

lang/dialogue.lua               3082 falas; chave = ponteiro da ROM ("bb:aaaa"),
                                 inclui as 8 chaves deslocadas do Silver
lang/dialogue_gen2recomped.lua  7459 chaves; rotulo nomeado do Gen2Recomped
lang/strings.lua                1073 textos do motor: batalha, menus, opcoes,
                                 PC, save, evolucao, relogio do POKeGEAR e as
                                 unidades de altura e peso do #DEX
lang/pokedex.lua                 251 fichas do GOLD
lang/pokedex_silver.lua          251 fichas do SILVER
lang/move_names.lua              252 nomes de golpe (12 colunas)
lang/move_descriptions.lua       252 descricoes de golpe
lang/item_names.lua              161 nomes de item
lang/item_descriptions.lua       164 descricoes de item
lang/trainer_classes.lua          66 classes de treinador
lang/landmarks.lua                70 nomes de lugar para o TOWN MAP
lang/type_names.lua               17 nomes de tipo
lang/status_labels.lua             6 siglas de status (VEN, QMD, PAR...)
lang/font.lua                        a pagina de glifos que o mod acrescenta
lang/charmap.lua                  25 que sequencia de bytes desenha qual glifo

assets/font/latin.png             os glifos acentuados, desenhados do zero;
                                   128x64 — a altura extra e exigencia minima
                                   do Gen2Recomped
```

Um catalogo so chega a tela onde o motor tem rota para ele: os dois
`pokedex*.lua` exigem o patch, `landmarks.lua` so existe no `gen1recomp`, e as
descricoes de golpe e item so o `gen1recomp` desenha. Onde nao ha rota, o
registro e pulado e o texto sai em ingles.

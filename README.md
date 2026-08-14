# VersaoDourada

**Pokemon Gold em portugues brasileiro** para o
[gen1recomp](https://github.com/bryanthaboi/gen1recomp), que e uma
recriacao nativa dos jogos em Lua/LOVE2D -- nao um emulador.

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia de
Pokemon Gold para o aplicativo importar.

**Todo o texto e traducao propria, escrita a partir do ingles original.**
Nao ha uma unica linha derivada de outra traducao no pacote.

---

## Estado

| O que | Quanto |
|---|---|
| Falas do jogo | 2809 |
| Rotulos de menu e batalha | 454 |
| Descricoes de golpe | 251 |
| Descricoes de item | 161 |
| Glifos acentuados desenhados | 25 |

O que ainda nao foi traduzido **aparece em ingles**, nunca em branco nem
cortado: o mod so substitui o que tem traducao pronta, entao o jogo e
sempre jogavel.

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

**Nomes de personagem e de lugar.** LANCE, JANINE, GOLDENROD CITY,
LAKE OF RAGE. Sao topografia e elenco -- e o jogador precisa deles para se
achar num mapa ou num guia.

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

ATTACK, DEFENSE, SPEED, SPECIAL, SPCL.ATK, SPCL.DEF ficam, porque e assim
que aparecem na tela de status. Traduzir so a descricao do golpe deixaria
duas linguas na mesma tela: "Ataque que pode baixar o SPCL.DEF" ao lado de
uma tabela que diz SPCL.DEF.

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
tempo tentando.

**As entradas da POKéDEX (251).** A tela do Gold le
`data.gen2Pokedex`, uma tabela carregada direto do cache do importador, e
nenhum registro de mod faz merge nela.

Curiosamente, **na primeira geracao isso funciona**: o extrator do Gen 1
grava um *rotulo* no campo de texto e a tela o resolve contra o registro
`text`, que qualquer mod pode sobrescrever. O Gen 2 grava a *string
literal* dentro da propria tabela -- nao ha chave para sobrescrever. Ha mod
de Gen 1 que traduz a POKéDEX justamente por essa rota
([hydhyro/gen1_pt-br_mod](https://github.com/hydhyro/gen1_pt-br_mod)).

**109 frases da batalha e dos menus.** "A critical hit!", "It's super
effective!", as mensagens de clima, as de captura, as de usar item. Estao
escritas direto no codigo do motor, fora de qualquer registro.

Os dois casos sao assunto para o upstream, e estao documentados com os
caminhos de arquivo para quem quiser abrir a issue.

---

## Terminologia

A traducao segue a localizacao oficial em portugues do Brasil, que chegou
aos jogos com Scarlet/Violet:

**Ginasio** (nao "academia") · **Lider de Ginasio** · **Treinador** ·
**Insignia** (nao "medalha") · **Centro POKéMON** · **Bolsa** (nao
"mochila") · **PS** para HP

---

## Instalacao

Precisa da versao atual do gen1recomp com Gold importado. O suporte a Gold
e beta.

**Pelo catalogo do aplicativo** (recomendado -- atualiza sozinho): adicione
este indice em *Ajustes -> indices de mod*:

```
https://raw.githubusercontent.com/LordSangreal/versaodourada/main/site/data/index.json
```

Depois use *Refresh all*. O indice tem cache de 24 horas, entao e o refresh
que traz uma versao nova na hora.

**Manualmente:** baixe o zip do release e importe por *Import mod .zip*.

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

O motor e a plataforma de mods sao de **bryanthaboi** e dos contribuidores
do gen1recomp.

---

## Arquivos do pacote

```
main.lua                     registra os overrides quando o jogo abre
manifest.json                quem o mod e e para qual jogo

lang/dialogue.lua            2809 falas; chave = ponteiro da ROM USA ("bb:aaaa")
lang/strings.lua              454 textos do motor: batalha, menus, opcoes
lang/move_descriptions.lua    251 descricoes de golpe; chave = id do golpe
lang/item_descriptions.lua    161 descricoes de item; chave = id do item
lang/font.lua                     a pagina de glifos que o mod acrescenta
lang/charmap.lua               25 que sequencia de bytes desenha qual glifo
lang/item_names.lua               vazio: nome de item fica em ingles
lang/status_labels.lua            vazio: PSN/BRN/PAR/SLP/FRZ ficam

assets/font/latin.png             os glifos acentuados, desenhados do zero
```

Um catalogo vazio nao e um catalogo faltando: e a decisao registrada de
deixar aquilo no original.

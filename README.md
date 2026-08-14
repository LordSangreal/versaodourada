# VersaoDourada

Pokemon Gold em portugues brasileiro para o
[gen1recomp](https://github.com/bryanthaboi/gen1recomp).

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia de
Pokemon Gold para o aplicativo importar.

## Estado

| | |
|---|---|
| Falas do jogo | 2966 |
| Rotulos de menu e batalha | 454 |
| Nomes de item | ficam em ingles |
| Glifos acentuados | 25 |

O que ainda nao foi traduzido aparece em ingles, entao o jogo e sempre
jogavel.

## O que fica no original

Por decisao do projeto, e nao por falta de traducao:

- **Nomes de golpes** -- sao como a franquia os nomeia
- **Nomes de Pokemon** -- sao os nomes oficiais no mundo todo
- **Nomes de personagens e cidades**
- **TM e HM** -- vem colados aos nomes dos golpes que ensinam, e traduzir
  so a sigla daria "MT29 contem o PSYCHIC", misturando duas linguas no
  mesmo item
- **Rotulos de status** (PSN, BRN, PAR, SLP, FRZ) -- sigla padrao da
  franquia, lida sem pensar em qualquer idioma, numa caixinha de tres
  caracteres. O que informa de fato e a mensagem na caixa de texto, e
  essa esta em portugues
- **Todos os nomes de item** (POKe BALL, POTION, BERRY, REPEL...) --
  decisao do usuario na 0.17.0, depois de ver em jogo a versao
  traduzida. Item entra na mesma regra dos golpes e dos Pokemon
- **A interface do aplicativo** (launcher, importacao de ROM, espacos de
  save, gerenciador de mods) -- ela tem botoes de largura fixa e o
  portugues, mais longo, estourava e saia cortado. So a tela do jogo e
  traduzida, porque ali a largura e conhecida e eu controlo a quebra

A terminologia segue a localizacao oficial em portugues do Brasil: Ginasio,
Lider de Ginasio, Treinador, Insignia, Centro Pokemon.

## Creditos, e o que esta em transicao

Parte do texto vem da traducao de **R_Lopes** e **Night_Shadown**, publicada
nos anos 2000 como patch de ROM. O mod porta aquele texto para o formato do
gen1recomp, para rodar sem ROM modificada -- o importador rejeita qualquer
ROM patcheada por SHA-1.

Esse texto esta sendo **substituido por traducao propria**, feita a partir do
ingles original, lote a lote:

| | |
|---|---|
| Falas ja nossas | 2833 |
| Falas ainda derivadas | 133 |

Os rotulos de menu e os glifos ja sao 100% nossos.

Enquanto houver **uma unica** fala derivada no pacote, este credito fica.

Nao foi possivel localizar os autores. Se voce e um deles e quer que este mod
saia do ar, abra uma issue -- sai.

O motor e a plataforma de mods sao de bryanthaboi e dos contribuidores do
gen1recomp.

## Instalacao

Precisa da versao atual do gen1recomp, com Gold importado. Gold e beta.

**Pelo catalogo do aplicativo (recomendado, atualiza sozinho):**
adicione este indice em Ajustes -> indices de mod:

```
https://raw.githubusercontent.com/LordSangreal/versaodourada/main/site/data/index.json
```

Depois use *Refresh all*. O indice tem cache de 24 horas, entao e o refresh
que traz uma versao nova na hora.

**Manualmente:** baixe o zip do release e importe por "Import mod .zip".

Confira no gerenciador de mods que ele aparece habilitado. Se aparecer
`ENABLED (NOT THIS GAME)`, o boot nao e de Gold.

## Arquivos do pacote

```
main.lua             registra os overrides quando o jogo abre
manifest.json        quem o mod e e para qual jogo
lang/dialogue.lua    falas do jogo, chave = ponteiro da ROM USA ("bb:aaaa")
lang/strings.lua     texto do motor: batalha, menus, opcoes
lang/font.lua        a pagina de glifos que o mod acrescenta
lang/item_names.lua  nomes de item (vazio = usa o nome da ROM)
lang/status_labels.lua  rotulos de status
assets/font/         os glifos acentuados, desenhados do zero
```

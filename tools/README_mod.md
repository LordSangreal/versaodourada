# VersaoDourada

Pokemon Gold em portugues brasileiro para o
[gen1recomp](https://github.com/bryanthaboi/gen1recomp).

Nao acompanha nenhum byte de ROM. Voce precisa da sua propria copia de
Pokemon Gold para o aplicativo importar.

## Estado

| | |
|---|---|
| Falas do jogo | 1972 |
| Rotulos de menu, batalha e launcher | 358 de 647 |
| Nomes de item | 68 |
| Glifos acentuados | 25 |

O que ainda nao foi traduzido aparece em ingles, entao o jogo e sempre
jogavel. `python tools/progresso.py` mostra o estado atual.

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
- **As Balls** (POKe BALL, GREAT BALL, MASTER BALL...)

A terminologia segue a localizacao oficial em portugues do Brasil: Ginasio,
Lider de Ginasio, Treinador, Insignia, Centro Pokemon. Ver `GLOSSARIO.md`,
que tambem registra o que deliberadamente nao muda.

## Creditos, e o que esta em transicao

Parte do texto vem da traducao de **R_Lopes** e **Night_Shadown**, publicada
nos anos 2000 como patch de ROM. O mod porta aquele texto para o formato do
gen1recomp, para rodar sem ROM modificada -- o importador rejeita qualquer
ROM patcheada por SHA-1.

Esse texto esta sendo **substituido por traducao propria**, feita a partir do
ingles original, lote a lote:

| | |
|---|---|
| Falas ja nossas | 143 |
| Falas ainda derivadas | 1829 |

Os rotulos de menu, os nomes de item e os glifos ja sao 100% nossos.

Enquanto houver **uma unica** fala derivada no pacote, este credito fica.
`tools/progresso.py` transforma "ja da para tirar?" numa pergunta com
resposta verificavel.

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

## Para quem for mexer

```
lang/dialogue.lua   gerado; chave = ponteiro da ROM USA ("bb:aaaa")
lang/strings.lua    gerado; chave = a string em ingles do motor
lang/font.lua       a pagina de glifos que o mod acrescenta
assets/font/        os glifos acentuados, desenhados do zero

tools/pt/           traducao propria, por lote -- e aqui que se escreve
tools/glifos.py     desenha a pagina de glifos, em arte ASCII conferivel
tools/lote.py       extrai o ingles de um lote para traduzir
tools/conferir.py   compara a traducao propria com o ingles
tools/validar.py    QA do catalogo publicado
tools/glossario.py  terminologia, sem estourar as 18 colunas
tools/progresso.py  quanto ja e nosso
tools/walk.py       percorre os scripts das duas ROMs em passo travado
tools/entradas.py   pontos de entrada, respeitando o que nao e bytecode
```

Tres restricoes mandam em tudo:

**A caixa tem 18 colunas e 2 linhas.** Uma traducao mais fiel que nao cabe e
pior que uma mais curta que cabe.

**A ultima linha de cada pagina cabe 17.** A seta de "aperte A" e desenhada
no canto inferior direito e ocupa a 18a coluna.

**Os codigos de controle sao parte do texto.** `\n`, `\v` e `\f` sao quebra
de linha, rolagem e quebra de pagina; perder um embaralha a caixa sem dar
erro nenhum. `tools/conferir.py` existe por causa disso.

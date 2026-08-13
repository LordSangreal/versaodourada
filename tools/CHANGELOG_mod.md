# Changelog

Este arquivo e escrito a mao e o build so o copia para dentro do pacote.

Ate a 0.14.0 ele era gerado por `build_mod.py`, e por isso toda versao
publicada dizia "Primeira versao" com a contagem de falas do dia -- o
historico se apagava sozinho a cada build. E o mesmo defeito que o README
tinha ate a 0.8.2. As entradas abaixo foram reconstruidas do git.

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

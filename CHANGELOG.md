# Changelog

## 0.6.0

**Os acentos voltaram.** 884 `~a`, 845 `a` agudo, 1417 `e` agudo, 234 cedilha
-- antes tudo isso virava ASCII ("mae", "coracao") porque a fonte da ROM so
tem tres caracteres acentuados.

`assets/font/latin.png` acrescenta 25 glifos na base `0x100`, que e espaco
livre acima das paginas da ROM: o alfabeto e ADICIONADO, nada e substituido.
Desenhados do zero em `tools/glifos.py`, em arte ASCII legivel -- as regras
do gen1recomp proibem distribuir arte derivada de ROM, entao extrair os
tiles da traducao BR estava fora de questao.

Minusculas ocupam as linhas 3-7 e deixam as duas de cima para o acento.
Maiusculas foram comprimidas em 6 linhas, que e o unico jeito de um A com
til caber numa celula de 8 pixels.

**Se algo der errado:** se os acentuados aparecerem em branco, a pagina nao
carregou. Reponha o mapa `DOBRA` em `tools/build_mod.py` -- e uma linha, e
volta ao comportamento da 0.5.0.

## 0.6.0

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

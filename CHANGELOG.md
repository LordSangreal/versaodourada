# Changelog

## 0.6.1

Corrige os blocos pretos no lugar dos acentos, que a 0.6.0 causou.

O motor decide o que e tinta pelo **canal alfa**, nao pela luminancia. Eu
gerei a pagina com fundo branco OPACO, entao a celula inteira contava como
tinta e cada acentuado saia como um quadrado preto solido.

A documentacao diz "preto no branco", e foi o que segui. A pagina que
funciona no jogo e preto no **transparente** -- so apareceu comparando os
pixels da minha com a do versaovermelha, que ja rodava.

Fundo agora e (0,0,0,0). A distribuicao de cores da minha pagina bate com a
da referencia.

## 0.6.1

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

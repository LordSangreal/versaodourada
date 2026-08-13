# Changelog

## 0.5.0

**68 nomes de item** traduzidos: curas, pedras de evolucao, vitaminas,
itens de batalha, varas de pesca, itens-chave.

Ficam no original, de proposito: as Balls, TM e HM, e os **rotulos de
status**. PSN, BRN, PAR, SLP e FRZ sao sigla padrao da franquia, lidas sem
pensar por quem joga em qualquer idioma, e vivem numa caixinha de tres
caracteres. O que importa ali e a mensagem na caixa de texto, e essa ja
esta em portugues.

Nome de item cabe em 12 caracteres. O build reprova o que passar disso e
deixa em ingles, em vez de publicar truncado.

Corrige tambem `main.lua`, que gerava `status_labels.lua` mas nunca o
aplicava -- o catalogo sairia e seria ignorado em silencio.

Removido o bloco de diagnostico da 0.1.3: ele ja disse o que precisava e
hoje so percorre 1968 chaves no boot para encher o log.

## 0.5.0

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

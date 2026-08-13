# Changelog

## 0.11.0

**A interface do aplicativo volta ao ingles.** Eu tinha traduzido o
launcher, a importacao de ROM, os espacos de save e o gerenciador de mods
sem verificar se o layout aguentava -- e nao aguentava. Os botoes tem
largura fixa, o portugues e mais longo, e o texto saia cortado: "Play Gold
(Be...", "0 insignias - 0:00 - 0 capturados" quebrando a linha.

O filtro e por DIRETORIO DE ORIGEM, nao por lista escrita a mao: qualquer
chave que apareca em `src/import/`, `LauncherMods`, `ManagerState` ou
`src/update/` sai do catalogo. 207 removidas; sobram 151, todas da tela do
jogo, onde a largura e conhecida e eu controlo a quebra de linha.

Duas passadas foram precisas para chegar la. Filtrar so o que era
*exclusivamente* do launcher deixava 31 compartilhadas -- FPS, orientacao,
vibracao -- que o launcher tambem desenha. E listar arquivo a arquivo
deixava passar uma mensagem do RomImporter.

Nada muda dentro do jogo: as 202 falas proprias, as 1771 derivadas, os
itens e os glifos seguem iguais.

## 0.11.0

- Primeira versao: 1973 falas em portugues.
- Nomes de golpes mantidos no original.

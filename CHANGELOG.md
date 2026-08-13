# Changelog

## 0.1.2

Restaura o direcionamento para Gold, que a 0.1.1 tinha removido por engano.

- `games: ["gold"]` de volta. Sem esse campo o manifest significa "Gen 1
  apenas" e um boot de Gold pula o mod (MK400). E o campo que rende o selo
  de geracao na lista de mods.
- `category: LANGUAGE` e `language: true` de volta: ambos sao validos.
- Mantida a faixa `game_version: <2.0.0` da 0.1.1, que era a correcao certa.

## 0.1.1

- `game_version` de `<1.0.0` para `<2.0.0`. O aplicativo e a versao 1.8.0 e a
  faixa antiga o excluia da lista -- o mod instalava e nunca aparecia.
- Removeu `games` e `language`. Foi um erro, desfeito na 0.1.2.

## 0.1.0

- Primeira versao: 1039 falas em portugues.
- Nomes de golpes mantidos no original.

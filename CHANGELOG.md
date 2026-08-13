# Changelog

## 0.1.4

Primeira versao que traduz de verdade -- a 0.1.3 confirmou que as chaves
casam. Esta corrige o que apareceu na tela.

- **Acentos.** A fonte do Gold so tem `é`, `ü` e `Ü`; os outros ~4.700
  acentos nao tinham glifo e sumiam ("m e" em vez de "mae"). Agora sao
  dobrados para ASCII: feio, mas legivel. Volta a ter acento de verdade
  quando a pagina de glifos entrar (0.2.0).
- **Lixo na fala da vizinha.** Havia tres chaves para a mesma fala, em
  enderecos deslocados de 3 bytes, e uma trazia sujeira no inicio. O build
  agora descarta os fragmentos que sao sufixo de outra fala.
- **Menus.** 97 rotulos de menu, batalha e opcoes traduzidos.
- Filtro mais duro: qualquer marcador `<...>` no texto agora reprova a
  entrada, em vez de so os que nao apareciam no ingles.

1002 falas (eram 1039; a diferenca sao os fragmentos removidos).

## 0.1.3

- Removido `font:register("ttf")`, que deixava a tela de mods ilegivel.
- Diagnostico das chaves.

## 0.1.2

- `games: ["gold"]` de volta; sem ele um boot de Gold pula o mod.

## 0.1.1

- `game_version` para `<2.0.0`: o aplicativo e 1.8.0 e a faixa antiga o
  excluia da lista.

## 0.1.0

- Primeira versao.

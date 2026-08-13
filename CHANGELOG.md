# Changelog

## 0.1.3

Corrige a tela de mods ilegivel e instrumenta o texto que nao trocou.

- **Removido `font:register("ttf", ...)`.** Era ele que deixava a tela de
  mods toda clara e mudava a fonte. O versaovermelha mantem a mesma chamada
  comentada, pelo mesmo motivo. Sem acentos proprios por enquanto -- entram
  depois como pagina de glifos, que e o caminho que funciona.
- Adicionado diagnostico: o mod agora registra no log quantas das suas
  chaves o jogo reconhece e uma amostra das chaves reais, para descobrir
  por que o dialogo continuou em ingles.
- `loadstring or load`, para nao depender da versao de Lua.

## 0.1.2

- `games: ["gold"]` de volta. Sem esse campo o manifest significa "Gen 1
  apenas" e um boot de Gold pula o mod (MK400).

## 0.1.1

- `game_version` de `<1.0.0` para `<2.0.0`. O aplicativo e a versao 1.8.0 e
  a faixa antiga o excluia da lista.

## 0.1.0

- Primeira versao: 1039 falas em portugues.

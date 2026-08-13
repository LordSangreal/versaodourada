# Changelog

## 0.1.5

**1410 falas** (eram 1002). O ganho veio de decifrar as macros que a
traducao BR redefiniu para caber nas 18 colunas. Nao sao glifos: cada byte
expande para varios caracteres. Cada uma foi deduzida cruzando o ingles
alinhado com o portugues:

| byte | expande | evidencia |
|---|---|---|
| `0x5B` | `AO` | GR+AO, onde o ingles diz BERRY |
| `0x5C` | `TA` | RO+TA, BICICLE+TA, FLORES+TA |
| `0x5D` | `POKeMON` | "CENTRO _", "GINASIO _", "seus _S" |
| `0x70 0x71` | `QU` | _EM, PSI_ICO, E_IPE |
| `0xCC` | `O` (acento) | LABORAT_RIO |
| `0xE1 0xE2` | `DO` | GYARA+DO+S, "LABORATORIO DO PROFESSOR" |

Descartes por codigo nao mapeado cairam de 640 para 236.

## 0.1.4

- Acentos dobrados para ASCII: a fonte do Gold so tem `é`, `ü` e `Ü`.
- Fragmentos duplicados removidos (o lixo na fala da vizinha).
- 97 rotulos de menu traduzidos.

## 0.1.3

- Removido `font:register("ttf")`, que deixava a tela de mods ilegivel.

## 0.1.2

- `games: ["gold"]` de volta; sem ele um boot de Gold pula o mod.

## 0.1.1

- `game_version` para `<2.0.0`: o aplicativo e 1.8.0.

## 0.1.0

- Primeira versao.

# Changelog

## 0.3.2

Tres codigos corrigidos, achados pelo validador depois de ele passar a medir
os tokens pelo tamanho que rendem em tela em vez do tamanho no arquivo:

| byte | era | e na verdade | evidencia |
|---|---|---|---|
| `0xD4` | `'s` | `C` cedilha | COMUNICA_OES, ESTA_AO, DAN_A |
| `0xD1` | `'l` | `O` circunflexo | M_NICA |
| `0xC5` | `ü` | `o` ordinal | 4_ ANDAR |

A traducao BR tomou tres ligaduras inglesas pouco uteis em portugues e as
reaproveitou. Palavras como PRODU_AO e CABE_ADA sairam quebradas ate agora.

Estouros de 18 colunas: 40 -> 23, e os que restam sao reais.

## 0.3.2

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

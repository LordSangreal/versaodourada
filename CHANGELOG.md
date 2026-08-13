# Changelog

## 0.3.1

**1968 falas** (eram 1689). Os codigos que faltavam eram os dois bytes de
LIGADURA do charmap original -- um byte so que ja valia dois glifos:

| byte | era | a traducao BR reusou como |
|---|---|---|
| `0x4A` | `<PK><MN>` | `DO` (GYARA+DO+S) |
| `0x24` | `<PO><KE>` | `QU` (E+QU+IPE, PSI+QU+ICO) |

Eu vinha mapeando `0xE1`/`0xE2` e `0x70`/`0x71`, que sao glifos legitimos e
distintos -- errado, e com risco de corromper texto. Revertido.

Descartes por marcador: 296 -> 12.

## 0.3.1

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

# Changelog

## 0.2.0

**1689 falas** (eram 1410). O percurso de scripts estava andando sobre dados.

O byte de funcao de um `bg_event` e o de um `object_event` decidem o que o
ponteiro e -- e nem todo ponteiro aponta para bytecode:

- `BGEVENT_ITEM` (7) aponta para `hiddenitem item, flag`. Sao 87 no jogo, e
  desmontar esses tres bytes como comandos era, nas palavras do proprio
  extrator oficial, "de onde veio a maioria das linhas de opcode
  desconhecido".
- `OBJECTTYPE_ITEMBALL` (1) aponta para dois bytes crus.
- `OBJECTTYPE_TRAINER` (2) aponta para a struct `trainer`.

Andar sobre esses tres desmontava dados como se fossem comandos e seguia o
salto que o ruido soletrava, o que travava ramos legitimos e produzia o
lixo kana que depois era descartado. Um conserto, dois problemas.

De quebra, a struct `trainer` guarda tres ponteiros de texto em +5/+7/+9
(visto / vitoria / derrota): 455 falas de treinador que nunca eram lidas.

| | antes | agora |
|---|---|---|
| opcodes desconhecidos | 318 | 6 |
| divergencias de bytecode | 130 | 5 |
| falas casadas | 2068 | 2245 |
| falas publicadas | 1410 | 1689 |

## 0.1.7

- TM e HM voltam ao original, junto com os nomes dos golpes que ensinam.

## 0.1.6

- Glossario de terminologia pt-BR atual (GLOSSARIO.md).

## 0.1.5

- Macros da traducao BR decifradas: 1002 -> 1410 falas.

## 0.1.4

- Acentos dobrados para ASCII; fragmentos duplicados removidos; 97 menus.

## 0.1.3

- Removido o TTF que deixava a tela de mods ilegivel.

## 0.1.2

- `games: ["gold"]` de volta.

## 0.1.1

- `game_version` para `<2.0.0`.

## 0.1.0

- Primeira versao.

# Changelog

## 0.3.3

Corrige a placa de New Bark, que saia "CI...... NEW BARK".

Dois problemas no mesmo ponto:

- `0x56` (era o byte das reticencias animadas) foi reaproveitado pela
  traducao BR como a ligadura `DADE` -- "CI+DADE NEW BARK". As reticencias
  de verdade no texto BR usam `0x75`, entao o byte estava mesmo livre.
- O decodificador tinha um caso especial que forcava `0x56` a virar
  reticencias **antes** de consultar o mapa BR. Qualquer byte reaproveitado
  que caisse na cadeia de casos especiais teria o mesmo destino. Agora o
  mapa BR tem precedencia sobre todos eles.

O segundo era o bug de verdade: o primeiro so aparecia por causa dele.

## 0.3.3

- Primeira versao: 1968 falas em portugues.
- Nomes de golpes mantidos no original.

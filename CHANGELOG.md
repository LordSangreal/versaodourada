# Changelog

## 0.10.1

Corrige a pontuacao dos travessoes.

O `--` do ingles marca uma **pausa** dentro da frase. Eu tinha trocado por
reticencias, mas em portugues reticencias dizem outra coisa: que a fala se
perdeu no ar. Agora vira **virgula**, que diz o mesmo que o original.

A regra entrou no `glossario.py` e vale para o texto todo, nao so para a
fala onde o problema apareceu: 17 ocorrencias no catalogo viraram 0. A
troca tem a mesma largura (dois caracteres viram dois), entao nenhuma linha
mudou de tamanho.

## 0.10.1

- Primeira versao: 1973 falas em portugues.
- Nomes de golpes mantidos no original.

# -*- coding: utf-8 -*-
"""Nomes de item: TODOS ficam no original em ingles.

Este catalogo esta vazio de proposito.  Vazio = o jogo usa o nome que a
ROM tem, em ingles.

## Como chegamos aqui

O projeto foi e voltou nesta decisao, e vale registrar o caminho para
ninguem refazer o percurso:

- **0.5.0** -- 68 itens traduzidos (POTION -> POÇÃO, REVIVE -> REVIVER).
  As Balls ficaram em ingles, com a justificativa de serem "nome padrao
  da franquia".
- **0.16.0** -- o usuario pediu o padrao pt-BR para as Balls.  Ele estava
  certo sobre o fato: a localizacao oficial em portugues traduz
  (Poke Bola, Grande Bola, Bola Mestra).  Foram para 139 itens.
- **0.17.0** -- o usuario jogou com isso e decidiu o contrario: **item
  fica em ingles**, incluindo as Balls, as pocoes e as BERRIES.

A decisao final e do usuario e e coerente com o resto do mod: golpes,
POKéMON, TM e HM ja ficavam no original.  Item entra na mesma regra.

## Se alguem quiser reverter

Nao basta repor este dicionario.  As falas ja publicadas citam os itens
pelo nome em ingles -- "Se ficar sem PARK BALLS", "Árvores de BERRY",
"ganham uma BERRY", "MIRACLEBERRY".  Traduzir so o item deixaria a bolsa
falando uma lingua e o NPC outra, que foi exatamente o motivo de BERRY e
APRICORN nunca terem sido traduzidos nem na 0.16.0.
"""

ITENS = {}

# Rotulos de status: FICAM NO ORIGINAL, por decisao do projeto.
#
# PSN, BRN, PAR, SLP e FRZ sao sigla padrao da franquia, reconhecida por
# quem joga em qualquer idioma, e vivem numa caixinha de tres caracteres ao
# lado da barra de vida.  Traduzir para ENV/QMD/CNG trocaria uma sigla que o
# jogador ja le sem pensar por outra que ele teria de aprender.
#
# O que importa traduzir e a MENSAGEM -- "%s foi atingido por %s!", "%s esta
# paralisado!" -- e essa esta em pt/sistema.py, na secao de batalha.
STATUS = {}

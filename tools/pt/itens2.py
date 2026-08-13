# -*- coding: utf-8 -*-
"""Itens, parte 2: as Balls e os itens equipaveis, no padrao pt-BR.

Chave = id do item.  Limite de **12 caracteres**: o build reprova o que
passar disso e deixa em ingles, porque nome cortado e pior que ingles.

## As Balls passam a ser traduzidas

Ate a 0.15.0 elas ficavam no original, com a justificativa de serem "nome
padrao da franquia".  Isso estava errado: a localizacao oficial em
portugues do Brasil **traduz** os nomes das Balls -- Poke Bola, Grande
Bola, Ultra Bola, Bola Mestra.  Quem fica no original sao os nomes de
GOLPES e de POKéMON, que e outra decisao, essa sim do usuario.

Os nomes aqui seguem a localizacao oficial sempre que ela cabe em 12
caracteres.  Quando nao cabe, abrevio o segundo termo em vez de trocar o
primeiro: "Pedaco Estelar" (14) vira "PEDACO ESTRE", nao "PEDRA".

O que continua no original, e por que:
  - BERRY e APRICORN: os dialogos ja publicados dizem "BERRY" e
    "APRICORNS".  Traduzir so o item deixaria a bolsa falando uma lingua
    e o NPC outra.
  - SLOWPOKETAIL e RAGECANDYBAR: sao itens de trama, citados pelo nome
    nas falas de Azalea e Mahogany.
  - MAIL: idem, os dialogos dizem "MAIL".
  - TM e HM: vem colados aos nomes dos golpes.
"""

ITENS = {
    # ------------------------------------------------------- as Balls
    "POKE_BALL": "POKé BOLA",
    "GREAT_BALL": "GRANDE BOLA",
    "ULTRA_BALL": "ULTRA BOLA",
    "MASTER_BALL": "BOLA MESTRA",
    "HEAVY_BALL": "BOLA PESADA",
    "LEVEL_BALL": "BOLA NÍVEL",
    "LURE_BALL": "BOLA ISCA",
    "FAST_BALL": "BOLA RÁPIDA",
    "FRIEND_BALL": "BOLA AMIGA",
    "MOON_BALL": "BOLA LUNAR",
    "LOVE_BALL": "BOLA AMOR",
    "PARK_BALL": "BOLA PARQUE",
    "SMOKE_BALL": "BOLA FUMAÇA",
    "LIGHT_BALL": "BOLA LUZ",

    # --------------------------------------------- itens equipaveis
    "BRIGHTPOWDER": "PÓ BRILHANTE",
    "METAL_POWDER": "PÓ METÁLICO",
    "SILVERPOWDER": "PÓ PRATEADO",
    "QUICK_CLAW": "GARRA RÁPIDA",
    "LUCKY_PUNCH": "SOCO SORTUDO",
    "SOFT_SAND": "AREIA MACIA",
    "SHARP_BEAK": "BICO AFIADO",
    "POISON_BARB": "ESPINHO TÓX",
    "KINGS_ROCK": "PEDRA DO REI",
    "MYSTIC_WATER": "ÁGUA MÍSTICA",
    "TWISTEDSPOON": "COLHER TORTA",
    "BLACKBELT_I": "FAIXA PRETA",
    "BLACKGLASSES": "ÓCULOS PRETO",
    "NEVERMELTICE": "GELO ETERNO",
    "MIRACLE_SEED": "SEMENTE MILA",
    "SPELL_TAG": "ETIQ MAGIA",
    "CLEANSE_TAG": "ETIQ PURA",
    "MAGNET": "ÍMÃ",
    "PINK_BOW": "LAÇO ROSA",
    "POLKADOT_BOW": "LAÇO POÁ",
    "STICK": "GRAVETO",
    "THICK_CLUB": "OSSO GROSSO",
    "FOCUS_BAND": "FAIXA FOCO",
    "HARD_STONE": "PEDRA DURA",
    "LUCKY_EGG": "OVO DA SORTE",
    "CHARCOAL": "CARVÃO",
    "SCOPE_LENS": "LENTE MIRA",
    "METAL_COAT": "CAPA METAL",
    "DRAGON_FANG": "PRESA DRAGÃO",
    "DRAGON_SCALE": "ESC. DRAGÃO",
    "LEFTOVERS": "RESTOS",
    "EVERSTONE": "PEDRA ETERNA",
    "UP_GRADE": "APRIMORADOR",
    "BERSERK_GENE": "GENE FÚRIA",
    "AMULET_COIN": "MOEDA AMULET",

    # ------------------------------------------------- cura e reviver
    "ENERGYPOWDER": "PÓ ENERGIA",
    "ENERGY_ROOT": "RAIZ ENERGIA",
    "HEAL_POWDER": "PÓ CURA",
    "REVIVAL_HERB": "ERVA REVIVER",
    "BERRY_JUICE": "SUCO BERRY",
    "SACRED_ASH": "CINZA SAGRAD",
    "CARBOS": "CARBOS",

    # ------------------------------------------------ tesouro e trama
    "PEARL": "PÉROLA",
    "BIG_PEARL": "PÉROLA GRAND",
    "STARDUST": "PÓ ESTELAR",
    "STAR_PIECE": "PEÇA ESTELAR",
    "TINYMUSHROOM": "COGUMELINHO",
    "BIG_MUSHROOM": "COGUMELÃO",
    "GOLD_LEAF": "FOLHA OURO",
    "SILVER_LEAF": "FOLHA PRATA",
    "BRICK_PIECE": "PEDAÇO TIJOL",
    "MACHINE_PART": "PEÇA MÁQUINA",
    "MYSTERY_EGG": "OVO MISTERIO",
    "S_S_TICKET": "BILHETE S.S.",
    "PASS": "PASSE",
    "NORMAL_BOX": "CAIXA NORMAL",
    "GORGEOUS_BOX": "CAIXA LUXO",
}

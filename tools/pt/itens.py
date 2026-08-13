# -*- coding: utf-8 -*-
"""Lote 5 -- nomes de itens e rotulos de status.

Chave = o id do registro (itemOrder / Status.lua), nao texto de ROM.
Traduzido do zero.

LIMITE: nome de item em Gen 2 cabe em **12 caracteres**.  Um nome cortado
pela metade e pior que o ingles inteiro, entao o build reprova o que passar
disso em vez de publicar truncado.

O QUE FICA NO ORIGINAL, por decisao do projeto:
  - as Balls (POKe BALL, GREAT BALL, ULTRA BALL, MASTER BALL...) sao nome
    padrao da franquia;
  - TM e HM, que vem colados aos nomes dos golpes;
  - itens cujo nome ja e o mesmo nos dois idiomas.
"""

MAX_NOME = 12

ITENS = {
    # ---- cura
    "POTION": "POÇÃO",
    "SUPER_POTION": "SUPERPOÇÃO",
    "HYPER_POTION": "HIPERPOÇÃO",
    "MAX_POTION": "POÇÃO MÁX",
    "FULL_RESTORE": "RESTAURAÇÃO",
    "FULL_HEAL": "CURA TOTAL",
    "REVIVE": "REVIVER",
    "MAX_REVIVE": "REVIVER MÁX",
    "ANTIDOTE": "ANTÍDOTO",
    "BURN_HEAL": "ANTIQUEIM",
    "ICE_HEAL": "ANTIGELO",
    "AWAKENING": "DESPERTA",
    "PARLYZ_HEAL": "ANTIPARAL",

    # ---- PP
    "ETHER": "ÉTER",
    "MAX_ETHER": "ÉTER MÁX",
    "ELIXER": "ELIXIR",
    "MAX_ELIXER": "ELIXIR MÁX",
    "PP_UP": "MAIS PP",

    # ---- vitaminas
    "HP_UP": "MAIS PS",
    "PROTEIN": "PROTEÍNA",
    "IRON": "FERRO",
    "CALCIUM": "CÁLCIO",
    "RARE_CANDY": "DOCE RARO",

    # ---- pedras de evolucao
    "MOON_STONE": "PEDRA LUA",
    "FIRE_STONE": "PEDRA FOGO",
    "THUNDERSTONE": "PEDRA TROVÃO",
    "WATER_STONE": "PEDRA ÁGUA",
    "LEAF_STONE": "PEDRA FOLHA",
    "SUN_STONE": "PEDRA SOL",

    # ---- itens de batalha
    "X_ATTACK": "X ATAQUE",
    "X_DEFEND": "X DEFESA",
    "X_SPEED": "X VELOC",
    "X_SPECIAL": "X ESPECIAL",
    "X_ACCURACY": "X PRECISÃO",
    "DIRE_HIT": "GOLPE CRÍT",
    "GUARD_SPEC": "PROTEÇÃO",

    # ---- bebidas
    "FRESH_WATER": "ÁGUA",
    "SODA_POP": "REFRIGERANTE",
    "LEMONADE": "LIMONADA",
    "MOOMOO_MILK": "LEITE MOOMOO",

    # ---- chave e utilidade
    "TOWN_MAP": "MAPA",
    "BICYCLE": "BICICLETA",
    "POKE_DOLL": "BONECO",
    "COIN_CASE": "PORTA-MOEDA",
    "ITEMFINDER": "ACHA-ITEM",
    "POKE_FLUTE": "FLAUTA POKé",
    "EXP_SHARE": "DIVIDE EXP",
    "OLD_ROD": "VARA VELHA",
    "GOOD_ROD": "VARA BOA",
    "SUPER_ROD": "VARA SUPER",
    "ESCAPE_ROPE": "CORDA FUGA",
    "REPEL": "REPELENTE",
    "SUPER_REPEL": "SUPERREPEL",
    "MAX_REPEL": "REPEL MÁX",
    "NUGGET": "PEPITA",
    "SQUIRTBOTTLE": "REGADOR",
    "BASEMENT_KEY": "CHAVE PORÃO",
    "CARD_KEY": "CARTÃO CHAVE",
    "SECRETPOTION": "POÇÃO SEC",
    "LOST_ITEM": "ITEM PERDIDO",
    "RED_SCALE": "ESCAMA VERM",
    "SILVER_WING": "ASA PRATA",
    "RAINBOW_WING": "ASA ARCO",
    "CLEAR_BELL": "SINO CLARO",
    "BLUE_CARD": "CARTÃO AZUL",
    "EGG_TICKET": "BILHETE OVO",
    "OLD_LINKCABLE": "CABO ANTIGO",
    "COIN": "MOEDA",
}

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

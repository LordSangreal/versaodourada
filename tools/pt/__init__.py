# -*- coding: utf-8 -*-
"""Catalogos de traducao proprios, por lote.

Tudo aqui e escrito a partir do ingles original do jogo. Nada e derivado da
traducao de terceiros -- e o que permite, quando o ultimo lote entrar, trocar
a atribuicao por um agradecimento.

`dialogo` e chaveado pelo ponteiro da ROM USA ("bb:aaaa"); `sistema` e
chaveado pela string em ingles do motor, exatamente como o codigo a escreve.

Escrever sempre com acentuacao correta: a dobra para ASCII acontece so na
hora de gerar o catalogo, e some quando a pagina de glifos entrar.
"""
import importlib
import pkgutil
import os

LOTES = ["sistema", "sistema2", "interface", "itens", "dialogo_01", "dialogo_02", "dialogo_03", "dialogo_04", "dialogo_05a", "dialogo_05b", "dialogo_06a", "dialogo_06b", "dialogo_07", "dialogo_08a", "dialogo_08b", "dialogo_08c", "dialogo_09a", "dialogo_09b", "dialogo_10a", "dialogo_10b", "dialogo_10c", "dialogo_11", "dialogo_12", "dialogo_13", "dialogo_14a", "dialogo_14b", "dialogo_15a", "dialogo_15b", "dialogo_15c", "dialogo_16", "dialogo_17", "dialogo_18", "dialogo_19", "dialogo_20", "dialogo_21", "dialogo_22", "dialogo_23", "dialogo_24", "dialogo_25", "dialogo_26"]


def carregar():
    """-> (sistema, dialogo) juntando todos os lotes."""
    sistema, dialogo = {}, {}
    for nome in LOTES:
        mod = importlib.import_module("pt." + nome)
        sistema.update(getattr(mod, "SISTEMA", {}))
        dialogo.update(getattr(mod, "DIALOGO", {}))
    return sistema, dialogo


def catalogos():
    """-> (itens, status) dos lotes que os definem."""
    itens, status = {}, {}
    for nome in LOTES:
        mod = importlib.import_module("pt." + nome)
        itens.update(getattr(mod, "ITENS", {}))
        status.update(getattr(mod, "STATUS", {}))
    return itens, status

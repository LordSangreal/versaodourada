# -*- coding: utf-8 -*-
"""`linhas(chave, ...)` -- monta a fala usando os separadores DO INGLES.

O erro que mais me custou neste projeto nao foi de traducao: foi copiar a
sequencia de `\\n` (quebra), `\\v` (rolagem) e `\\f` (nova pagina) errada.
Aconteceu quatro vezes no lote 6b e oito no lote 7, sempre do mesmo jeito
-- trocando um `\\n` por `\\v` porque na planilha o separador aparece
DEPOIS da linha a que pertence, e eu lia como se viesse antes.

Aqui isso deixa de ser possivel.  Eu escrevo so o texto das linhas, na
ordem, e a funcao intercala os separadores lidos do ingles original:

    "40:4615": linhas("40:4615",
        "Bom dia!",
        "Bem-vindo ao nosso",
        "CENTRO POKéMON."),

Se a contagem de linhas nao bater com a do ingles, estoura na hora de
importar, com a chave no erro -- em vez de virar uma caixa de texto
quebrada no aparelho.

O limite de coluna continua sendo assunto do conferidor: 18, e 17 na
ultima linha de cada pagina, onde a seta ▼ de "aperte A" ocupa a coluna.
"""
import json
import os
import re

_AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CTRL = re.compile(r"([\n\v\f])")
_dial = None


def _ingles(chave):
    global _dial
    if _dial is None:
        caminho = os.path.join(_AQUI, "dialogo.json")
        _dial = json.load(open(caminho, encoding="utf-8"))
    if chave not in _dial:
        raise KeyError("%s nao existe no dialogo extraido" % chave)
    return _dial[chave][0]


def linhas(chave, *minhas):
    """-> a fala montada, com os separadores na ordem exata do ingles."""
    partes = _CTRL.split(_ingles(chave))
    seps = partes[1::2]
    if len(minhas) != len(seps) + 1:
        raise ValueError(
            "%s: o ingles tem %d linhas, eu escrevi %d"
            % (chave, len(seps) + 1, len(minhas)))
    saida = [minhas[0]]
    for sep, linha in zip(seps, minhas[1:]):
        saida.append(sep)
        saida.append(linha)
    return "".join(saida)

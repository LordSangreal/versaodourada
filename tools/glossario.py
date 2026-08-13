# -*- coding: utf-8 -*-
"""Glossario de terminologia pt-BR, aplicado sobre o texto extraido.

A traducao base e dos anos 2000 e antecede a localizacao oficial de Pokemon
em portugues do Brasil (que chegou nos jogos com Scarlet/Violet, 2022).
Estes sao os termos canonicos de hoje.

REGRA DURA: uma substituicao que estoure as 18 colunas da caixa e
descartada -- o termo curto antigo fica.  Cabimento vence purismo.
"""

# (o que procurar, com o que trocar).  Ordem importa: mais especifico antes.
# Confianca alta: terminologia oficial ou consolidada.
TERMOS = [
    # TM e HM FICAM NO ORIGINAL, por decisao do projeto: eles vem colados aos
    # nomes dos golpes que ensinam, e os nomes de golpes ficam em ingles.
    # Traduzir a sigla e deixar o golpe em ingles produziria "MT29 contem o
    # PSYCHIC", que mistura as duas linguas no mesmo item.  Nao adicionar
    # regra de TM/HM aqui.

    # PS (Pontos de Saude) e a sigla oficial em pt-BR; HP e do ingles.
    (r"\bHP\b", "PS"),

    # "Movimento" e o termo oficial para move; "golpe" e do anime antigo.
    # Mais longo, entao so entra quando a linha ainda couber.
    (r"\bgolpe\b", "movimento"),
    (r"\bgolpes\b", "movimentos"),
    (r"\bGOLPE\b", "MOVIMENTO"),
    (r"\bGOLPES\b", "MOVIMENTOS"),

    # Consistencia de acentuacao e forma
    (r"\bPOKEMON\b", "POKéMON"),
    (r"\bPokemon\b", "POKéMON"),

    # O "--" do ingles e travessao: marca uma pausa dentro da frase.  Em
    # portugues nao se escreve assim -- vira virgula.  Mesma largura (dois
    # caracteres viram dois), entao nenhuma linha muda de tamanho.
    #
    # Reticencias NAO servem aqui: dizem que a fala se perdeu no ar, que e
    # outra coisa.  Foi o que eu tinha feito antes, e ficou estranho na tela.
    (r"(\w)--(\w)", r"\1, \2"),
    (r"--", ", "),
]

# Termos que a base ja acerta e que NAO devem ser mexidos, documentados aqui
# para ninguem "corrigir" por engano depois:
#   GINASIO       -- oficial (nao "academia")
#   LIDER         -- oficial ("Lider de Ginasio")
#   TREINADOR     -- oficial
#   INSIGNIA      -- oficial (nao "medalha")
#   CENTRO POKeMON-- oficial
#   BOLSA         -- oficial (nao "mochila")
#
# Nomes de golpes e de Pokemon ficam no original em ingles, por decisao do
# projeto -- nenhuma regra aqui pode toca-los.

MAX_COLS = 18


def aplicar(texto, re_mod):
    """Aplica o glossario preservando o limite de 18 colunas por linha.

    Substitui linha a linha: se a troca fizer a linha estourar, mantem o
    original daquela linha.  Assim um termo longo entra onde cabe e e
    silenciosamente dispensado onde nao cabe.
    """
    saida = []
    for linha in texto.split("\n"):
        nova = linha
        for padrao, troca in TERMOS:
            nova = re_mod.sub(padrao, troca, nova)
        # tokens de runtime nao contam como largura fixa; so mede o resto
        visivel = re_mod.sub(r"\{[A-Z_]+\}", "", nova)
        if len(visivel) <= MAX_COLS or len(nova) <= len(linha):
            saida.append(nova)
        else:
            saida.append(linha)
    return "\n".join(saida)

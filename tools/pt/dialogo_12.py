# -*- coding: utf-8 -*-
"""Lote 12 -- falas que o percurso de scripts nunca alcancou.

O usuario jogou o GINASIO do FALKNER, em VIOLET CITY, e mandou captura de
tela com um treinador falando ingles: "This is pathetic, losing to some
rookie trainer…".  O lote 3 cobria aquele ginasio inteiro -- mas essa fala
nao estava no `dialogo.json`, entao nao havia o que traduzir.

Causa: `walk.py` so encontra o que algum script referencia, e as falas de
treinador ficam em structs que o percurso nem sempre alcanca.
`tools/varrer.py` acha essas por outro caminho -- em Gen 2 um bloco de
texto termina em 0x50 ou 0x57, entao o endereco logo apos um terminador e
candidato a inicio de bloco.  A varredura achou 1032 falas que faltavam;
o `dialogo.json` foi de 2245 para 3277.

Confirmei o endereco antes de traduzir: o ponteiro 0x4634 aparece em
56:41b7, dentro do struct do treinador.  Meu primeiro palpite (0x4635)
estava um byte adiantado e a chave nao casaria com nada.

Estas cinco sao as do ginasio do FALKNER.  As outras 1027 ficam para os
proximos lotes.
"""
from pt.estrutura import linhas as L

DIALOGO = {
    # ---------------- Ginasio de VIOLET (FALKNER) ----------------
    "56:453a": L("56:453a",
                 "A palavra de",
                 "ordem é raça!",
                 "O pessoal aqui",
                 "treina noite e",
                 "dia para virar",
                 "mestre de POKéMON",
                 "voador. Venha!"),
    "56:45a4": L("56:45a4",
                 "O talento do",
                 "FALKNER é real!",
                 "Não se ache só",
                 "porque venceu",
                 "a mim!"),
    "56:45ec": L("56:45ec",
                 "Deixa eu ver se",
                 "você é bom o",
                 "bastante!"),
    "56:4620": L("56:4620",
                 "Isso não pode",
                 "ser verdade!"),
    "56:4634": L("56:4634",
                 "Que vergonha,",
                 "perder para um",
                 "novato…"),
}

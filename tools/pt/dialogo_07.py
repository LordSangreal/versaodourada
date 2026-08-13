# -*- coding: utf-8 -*-
"""Lote 7 -- StdScripts (banco 40): o texto comum a todos os mapas.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Estas 32 falas nao pertencem a mapa nenhum: sao os scripts padrao que
todo mapa chama.  A enfermeira do CENTRO POKéMON, a placa do MART, o
telefone, o PC do BILL, o Concurso de Insetos, a estante de livros.  E o
texto que o jogador mais le no jogo inteiro, e por isso vem antes das
regioes que ainda faltam.

Primeiro lote escrito com `linhas()`: eu ponho so o texto de cada linha e
os separadores vem do ingles.  A versao anterior deste arquivo, escrita a
mao, saiu com oito trocas de `\\n` por `\\v` -- ver pt/estrutura.py.

Termos conforme GLOSSARIO.md: PACK -> BOLSA, POKéMON CENTER -> CENTRO
POKéMON, POKéMON GYM -> GINÁSIO POKéMON, POKéMON MART -> LOJA POKéMON.
BOX fica no original, porque interface.py ja usa "BOX %d".

(Ate a 0.15.0 o MART ficava em ingles com a justificativa de ser nome de
estabelecimento.  O usuario pediu o padrao pt-BR, e "Loja" e o termo que
a localizacao oficial usa -- na mesma leva em que as Balls passaram a ser
traduzidas.  DEPT.STORE continua no original: e nome proprio da loja de
Goldenrod, nao a categoria.)
"""
from pt.estrutura import linhas as L

DIALOGO = {
    # ---------------- Centro Pokemon: a enfermeira ----------------
    "40:4615": L("40:4615",
                 "Bom dia!",
                 "Bem-vindo ao nosso",
                 "CENTRO POKéMON."),
    "40:4640": L("40:4640",
                 "Olá!",
                 "Bem-vindo ao nosso",
                 "CENTRO POKéMON."),
    "40:4664": L("40:4664",
                 "Boa noite!",
                 "Saiu tarde, hein?",
                 "Bem-vindo ao nosso",
                 "CENTRO POKéMON."),
    "40:469f": L("40:469f",
                 "Podemos curar seus",
                 "POKéMON até a",
                 "saúde perfeita.",
                 "Curamos os seus",
                 "POKéMON?"),
    "40:46e2": L("40:46e2",
                 "Certo, posso ver",
                 "seus POKéMON?"),
    "40:46fc": L("40:46fc",
                 "Obrigada por",
                 "esperar.",
                 "Seus POKéMON estão",
                 "curados."),
    "40:4730": L("40:4730",
                 "Esperamos ver você",
                 "de novo."),
    "40:4766": L("40:4766",
                 "Seus POKéMON pare-",
                 "cem ter formas de",
                 "vida minúsculas",
                 "grudadas neles.",
                 "Seus POKéMON estão",
                 "saudáveis e bem",
                 "de modo geral.",
                 "Mas não podemos",
                 "dizer mais nada",
                 "num CENTRO",
                 "POKéMON."),

    # ---------------- Moveis e placas ----------------
    "40:4801": L("40:4801",
                 "Está cheia de",
                 "livros difíceis."),
    "40:484a": L("40:484a",
                 "Revistas de POKé-",
                 "MON… POKéMON PAL,",
                 "POKéMON HANDBOOK,",
                 "POKéMON GRAPH…"),
    "40:48ef": L("40:48ef",
                 "O que é isto?",
                 "Ah, é um",
                 "incensário!"),
    "40:4934": L("40:4934", "É o TOWN MAP."),
    "40:4965": L("40:4965", "É uma TV."),
    "40:49cd": L("40:49cd",
                 "Não tem nada",
                 "aqui dentro…"),
    "40:4a43": L("40:4a43",
                 "Tudo Que Seu",
                 "POKéMON Precisa",
                 "LOJA POKéMON"),
    "40:4e96": L("40:4e96",
                 "{STRBUF}",
                 "GINÁSIO POKéMON"),

    # ---------------- Concurso de Insetos ----------------
    "40:4a66": L("40:4a66",
                 "Vamos agora julgar",
                 "os POKéMON que",
                 "você pegou.",
                 "……",
                 "……",
                 "Já escolhemos os",
                 "vencedores!",
                 "Você está pronto",
                 "para isto?"),
    "40:4d6a": L("40:4d6a",
                 "{PLAYER} ganha o",
                 "prêmio {STRBUF},",
                 "um {STRBUF}!"),
    "40:4d90": L("40:4d90",
                 "{PLAYER} recebeu",
                 "{STRBUF}."),
    "40:4da3": L("40:4da3",
                 "Volte para o",
                 "próximo Concurso!"),
    "40:4dc9": L("40:4dc9",
                 "Todos os outros",
                 "ganham uma BERRY",
                 "de consolação!"),
    "40:4dff": L("40:4dff",
                 "Esperamos que vá",
                 "melhor na próxima"),
    "40:4e21": L("40:4e21",
                 "Vamos devolver o",
                 "POKéMON que",
                 "guardamos.",
                 "Aqui está!"),

    # ---------------- Telefone ----------------
    "40:4ac8": L("40:4ac8",
                 "Uau! Você é bem",
                 "durão.",
                 "Me dá o seu número",
                 "de telefone?",
                 "Eu ligo para você",
                 "para a revanche."),
    "40:4b39": L("40:4b39",
                 "{PLAYER} registrou",
                 "{STRBUF}."),
    "40:4b7a": L("40:4b7a",
                 "Ah, tá…",
                 "Fale comigo se",
                 "quiser o meu",
                 "número."),
    "40:4bef": L("40:4bef",
                 "Eu estava esperan-",
                 "do. Vamos lutar!"),
    "40:4c77": L("40:4c77",
                 "Registrar o número",
                 "de telefone?"),
    "40:4cb0": L("40:4cb0",
                 "Eu ligo se rolar",
                 "alguma coisa."),
    "40:4d12": L("40:4d12",
                 "O seu telefone não",
                 "tem memória para",
                 "mais números."),

    # ---------------- BOX cheia, BOLSA cheia ----------------
    "40:4e55": L("40:4e55",
                 "Seu grupo está",
                 "cheio, então o",
                 "POKéMON foi para",
                 "a BOX do BILL."),
    "40:5014": L("40:5014",
                 "Ué? Sua BOLSA está",
                 "cheia.",
                 "Vamos guardar isto",
                 "por hoje, então",
                 "volte quando tiver",
                 "espaço para ele."),
}

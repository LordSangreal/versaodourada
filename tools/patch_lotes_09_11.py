# -*- coding: utf-8 -*-
"""Conserta os lotes 09a-11, escritos por outra sessao.

Tres classes de defeito, todas achadas por `conferir.py` e pela leitura:

1. **Largura** -- 42 linhas passando de 18 colunas (ou de 17, na ultima
   linha de cada pagina, onde a seta ▼ ocupa a coluna).  Na tela isso
   corta a palavra no meio.
2. **Ingles solto** -- "Você removing aquela árvore?" ficou meio
   traduzido.
3. **Acento com homografo** -- `acentuar.py` nao mexe em "e"/"é" nem em
   "esta"/"está", porque as duas formas existem.  Aqui vao a mao, uma a
   uma, olhando a frase.

Cada linha e um argumento separado de `linhas()`, entao trocar o literal
inteiro e seguro: nao ha `\\n` embutido para corromper.
"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ARQUIVOS = ["dialogo_09a", "dialogo_09b", "dialogo_10a", "dialogo_10b",
            "dialogo_10c", "dialogo_11"]

TROCAS = [
    # ---- RUINS OF ALPH: placas e pesquisadores
    ("Bem-vindos Visitantes", "Bem-vindos!"),
    ("CENTRO DE PESQUISA", "CENTRO PESQUISA"),
    ("cerca de 1500 anos.", "cerca de 1500 anos"),
    ("Quantas especies de", "Quantas espécies"),
    ("Quantas espécies de", "Quantas espécies"),
    ("Ha padroes estranhos", "Há padrões"),
    ("Há padrões estranhos", "Há padrões"),
    ("Devem ser as chaves", "Devem ser a chave"),
    ("Os POKéMON estranhos", "Os POKéMON"),
    ("Isso significa que", "Isso quer dizer"),
    ("de pedra que deslizam!", "de pedra!"),
    ("Você esta estudando", "Está estudando"),
    ("Você está estudando", "Está estudando"),
    ("as RUÍNAS DE ALPH.", "as RUÍNAS."),

    # ---- rota 36 e a arvore
    ("Você removing", "Você tirou"),
    ("Estou impressionado!", "Impressionado!"),
    ("Uma arvore estranha", "Uma árvore"),
    ("Uma árvore estranha", "Uma árvore"),
    ("esta bloqueando", "está bloqueando"),
    ("Esta me impedindo", "Está me impedindo"),

    # ---- ARTHUR, o irmao de quinta
    ("Sou o segundo filho", "Sou o segundo"),
    ("Que decepcionante.", "Que decepção."),
    ("e quinta-feira.", "é quinta-feira."),

    # ---- TRAINER TIPS
    ("parecidos inicio.", "ser parecidos."),
    ("Mas diferencas vão", "Mas as diferenças"),
    ("Mas diferenças vão", "Mas as diferenças"),
    ("conforme POKéMON.", "conforme crescem."),
    ("Use DIG para voltar", "Use DIG para ir"),
    ("a entrada de", "à entrada de"),
    ("E conveniente", "É conveniente"),
    ("pontos turisticos.", "lugares assim."),
    ("pontos turísticos.", "lugares assim."),

    # ---- Concurso de Captura de Insetos
    ("Captura de Insetos", "Captura Insetos"),
    ("e realizado na", "é realizado na"),
    ("terca, quinta e", "terça, quinta e"),
    ("sabado.", "sábado."),
    ("Hoje e {STRBUF}.", "Hoje é {STRBUF}."),
    ("esta hoje.", "é hoje."),
    ("Usando um dos seus", "Use um dos seus"),
    ("mais forte e a", "mais forte é a"),
    ("PARK BALLS, acabou.", "BOLAS, acabou."),
    ("Va e capture", "Vá e capture"),
    ("Tudo bem. Guardamos", "Tudo bem. Vamos"),
    ("seus outros POKéMON", "guardar os outros"),
    ("enquanto competir.", "durante o teste."),
    ("O primeiro POKéMON", "O 1º POKéMON"),
    ("não pode batalhar.", "não pode lutar."),
    ("equipe ou no PC BOX,", "equipe ou na BOX,"),
    ("POKéMON na equipe.", "POKéMON do grupo."),
    ("{STRBUF} minutos.", "{STRBUF} min."),
    ("terminou. Esperamos", "acabou. Esperamos"),
    ("grande parte nisso.", "muita influência."),
    ("ganhe uma pontuação", "ganhe mais pontos"),
    ("WILLIAM: Bem, estou", "WILLIAM: Estou"),
    ("capturei um POKéMON", "peguei o POKéMON"),
    ("BARRY: E mais fácil", "BARRY: É mais"),
    ("BARRY: É mais fácil", "BARRY: É mais"),
    ("consideram outros.", "olham mais coisas"),
    ("CINDY: Você venceu?", "CINDY: Venceu?"),
    ("cacar POKéMON", "caçar POKéMON"),
    ("SAMUEL: Da próxima,", "SAMUEL: Na próxima"),
    ("me dar umas dicas?", "me dar dicas?"),
    ("KIPP: Estudo muito,", "KIPP: Estudo bem,"),
    ("mas isso não e", "mas isso não é"),
]


def main():
    total = 0
    for nome in ARQUIVOS:
        caminho = os.path.join(HERE, "pt", nome + ".py")
        if not os.path.exists(caminho):
            continue
        texto = io.open(caminho, encoding="utf-8").read()
        antes = texto
        n = 0
        for velho, novo in TROCAS:
            alvo = '"%s"' % velho
            if alvo in texto:
                n += texto.count(alvo)
                texto = texto.replace(alvo, '"%s"' % novo)
        if texto != antes:
            io.open(caminho, "w", encoding="utf-8").write(texto)
            print("%-24s %d linhas" % (nome, n))
            total += n
    print("total:", total)


if __name__ == "__main__":
    main()

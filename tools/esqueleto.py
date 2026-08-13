"""Imprime o ESQUELETO do ingles: pagina, linha, separador e limite de colunas.

Ler a sequencia de \\n \\v \\f a olho na planilha e o que mais me custou erro:
no lote 6a eu li um \\f como \\v na fala do MORTY e o conferidor reprovou.
Aqui a estrutura sai explicita, entao traduzir vira preencher linha a linha.

O limite muda na ULTIMA linha de cada pagina: a seta ▼ de "aperte A" ocupa
a coluna 18, entao ali cabem 17.

Uso:  python esqueleto.py planilha-06b.py
      python esqueleto.py 52:516b        (uma chave so)
"""
import ast, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX = 18

# O console do Windows abre em cp1252 e engasga no kana que sobra de ponteiro
# mal alinhado.  Trocar por "?" e melhor do que abortar no meio da planilha.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def esqueleto(k, en, mapa=""):
    print("# %s  %s" % (k, mapa))
    paginas = en.split("\f")
    for ip, pagina in enumerate(paginas, 1):
        partes = re.split(r"([\n\v])", pagina)
        linhas = [p for p in partes if p not in ("\n", "\v")]
        seps = [p for p in partes if p in ("\n", "\v")]
        for il, linha in enumerate(linhas):
            ultima = (il == len(linhas) - 1)
            sep = "\\f" if ultima and ip < len(paginas) else (
                "  " if ultima else ("\\n" if seps[il] == "\n" else "\\v"))
            print("  P%d %s [%2d] |%s|" % (ip, sep, MAX - 1 if ultima else MAX, linha))
    print()


def main():
    alvo = sys.argv[1]
    if re.fullmatch(r"[0-9a-f]{2}:[0-9a-f]{4}", alvo):
        dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
        esqueleto(alvo, dial[alvo][0])
        return
    src = open(os.path.join(HERE, alvo), encoding="utf-8").read()
    d = ast.literal_eval("{" + src[src.index("\n"):] + "}")
    mp = dict((k, m) for m, k in
              re.findall(r"# (\w+)\n.([0-9a-f]{2}:[0-9a-f]{4}).:", src))
    for k, en in d.items():
        esqueleto(k, en, mp.get(k, ""))


if __name__ == "__main__":
    main()

"""Fatia uma planilha por mapa e joga fora o que nao da para traduzir.

Um lote de 130 falas nao se traduz bem de uma vez: o lote 4, com 65
escritas as pressas, saiu com 32 erros, enquanto os de ate ~50 sairam
limpos.  Entao a planilha grande vira fatias.

O que sai fora, e por que:
  kana      ponteiro mal alinhado; o texto decodificado e lixo
  fragmento comeca no meio de uma palavra (continuacao de TX_FAR); o
            pedaco que aparece em tela vem da fala inteira, que esta em
            outro ponteiro
  vazio     nada para traduzir
  ja feito  ja esta em pt/

Uso:  python fatiar.py 08 8a MAHOGANY_TOWN MAHOGANY_GYM ROUTE_42
"""
import ast, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def kana(s):
    return any(0x3000 < ord(c) < 0xFF00 for c in s)


def fragmento(s):
    """Comeca no meio de palavra: minuscula solta sem sinal de frase antes."""
    return bool(re.match(r"^[a-z]{1,3}[\s.,!?]", s)) or bool(
        re.match(r"^[a-z]+\n", s))


def main():
    origem, tag, mapas = sys.argv[1], sys.argv[2], set(sys.argv[3:])
    import pt
    _s, feito = pt.carregar()
    src = open(os.path.join(HERE, "planilha-%s.py" % origem), encoding="utf-8").read()
    d = ast.literal_eval("{" + src[src.index("\n"):] + "}")
    mp = dict((k, m) for m, k in
              re.findall(r"# (\w+)\n.([0-9a-f]{2}:[0-9a-f]{4}).:", src))
    fora = {"kana": 0, "fragmento": 0, "vazio": 0, "ja feito": 0}
    fica = []
    for k, en in d.items():
        if mapas and mp.get(k) not in mapas:
            continue
        if k in feito:
            fora["ja feito"] += 1
        elif not en.strip():
            fora["vazio"] += 1
        elif kana(en):
            fora["kana"] += 1
        elif fragmento(en):
            fora["fragmento"] += 1
        else:
            fica.append((mp.get(k, ""), k, en))
    destino = os.path.join(HERE, "planilha-%s.py" % tag)
    with open(destino, "w", encoding="utf-8") as f:
        f.write("# Fatia %s de planilha-%s\n\n" % (tag, origem))
        for m, k, en in fica:
            f.write("# %s\n%r: %r,\n\n" % (m, k, en))
    print("%s: %d falas -> %s" % (tag, len(fica), destino))
    print("  fora:", fora)


if __name__ == "__main__":
    main()

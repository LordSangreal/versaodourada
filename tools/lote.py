"""Extrai o ingles original de um lote de mapas, para traduzir a partir dele.

A planilha sai FORA do diretorio do mod: o ingles extraido e conteudo de ROM
e `modkit pack` zipa tudo que estiver dentro do mod, entao um arquivo assim
la dentro iria parar no release independente de .gitignore.

Uso:  python lote.py 01
"""
import os, sys, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import walk as W
import entradas
from gen2text import key as _k

LOTES = {
    "01": ("New Bark, casa do jogador, laboratorio do Elm",
           ["NEW_BARK_TOWN", "PLAYERS_HOUSE_1F", "PLAYERS_HOUSE_2F",
            "ELMS_LAB", "ELMS_HOUSE"]),
    "02": ("Rota 29-30, Cherrygrove",
           ["ROUTE_29", "CHERRYGROVE_CITY", "CHERRYGROVE_MART",
            "CHERRYGROVE_POKECENTER_1F", "ROUTE_30"]),
    "03": ("Violet e arredores",
           ["VIOLET_CITY", "VIOLET_GYM", "VIOLET_MART", "SPROUT_TOWER_1F",
            "ROUTE_31", "ROUTE_32"]),
}


def chaves_do_lote(nome):
    _titulo, mapas = LOTES[nome]
    usa, br = W.Rom(W.USA_PATH), W.Rom(W.BR_PATH)
    mf = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                        encoding="utf-8"))
    achadas = {}
    for m in mapas:
        spec = mf["maps"].get(m)
        if not spec:
            continue
        st, tx = entradas.coletar(usa, br, {spec["group"]: spec["map"]},
                                  somente=(spec["group"], spec["map"]))
        out, _ = W.walk(usa, br, st)
        for bank, a, b in tx:
            W.record(out, collections.Counter(), usa, br, bank, a, bank, b)
        for k, (en, _pt) in out.items():
            # bank 40 = StdScripts, comum a todos os mapas: nao e deste lote
            if not k.startswith("40:"):
                achadas.setdefault(k, (m, en))
    return achadas


if __name__ == "__main__":
    nome = sys.argv[1] if len(sys.argv) > 1 else "01"
    titulo, _ = LOTES[nome]
    achadas = chaves_do_lote(nome)
    dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
    # so o que o mod publica hoje (o resto foi filtrado por algum motivo)
    publicaveis = {k: v for k, v in achadas.items() if k in dial}
    destino = os.path.join(HERE, "planilha-%s.txt" % nome)
    with open(destino, "w", encoding="utf-8") as f:
        f.write("# Lote %s -- %s\n" % (nome, titulo))
        f.write("# %d falas.  Traduzir a partir do ingles.\n\n" % len(publicaveis))
        for k in sorted(publicaveis):
            mapa, en = publicaveis[k]
            f.write("[%s]  (%s)\n%s\n\n" % (k, mapa, en))
    print("lote %s: %d falas -> %s" % (nome, len(publicaveis), destino))
    por_mapa = collections.Counter(v[0] for v in publicaveis.values())
    for m, n in por_mapa.most_common():
        print("   %-22s %d" % (m, n))

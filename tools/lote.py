"""Extrai o ingles original de um lote de mapas, para traduzir a partir dele.

A planilha sai FORA do diretorio do mod: o ingles extraido e conteudo de ROM
e `modkit pack` zipa tudo que estiver dentro do mod, entao um arquivo assim
la dentro iria parar no release independente de .gitignore.

Uso:  python lote.py 04
"""
import os, sys, json, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import walk as W
import entradas

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
    "04": ("Azalea, Slowpoke Well, Ilex",
           ["AZALEA_TOWN", "AZALEA_GYM", "AZALEA_MART", "AZALEA_POKECENTER_1F",
            "SLOWPOKE_WELL_B1F", "ILEX_FOREST", "KURTS_HOUSE", "ROUTE_33"]),
    "05": ("Goldenrod e arredores",
           ["GOLDENROD_CITY", "GOLDENROD_GYM", "GOLDENROD_DEPT_STORE_1F",
            "RADIO_TOWER_1F", "ROUTE_34", "ROUTE_35", "NATIONAL_PARK"]),
    "06": ("Ecruteak, Olivine, Cianwood",
           ["ECRUTEAK_CITY", "ECRUTEAK_GYM", "BURNED_TOWER_1F", "TIN_TOWER_1F",
            "OLIVINE_CITY", "OLIVINE_GYM", "OLIVINE_LIGHTHOUSE_1F",
            "CIANWOOD_CITY", "CIANWOOD_GYM", "ROUTE_38", "ROUTE_39"]),
    "08": ("Mahogany, Lake of Rage e a base da TEAM ROCKET",
           ["MAHOGANY_TOWN", "MAHOGANY_MART_1F", "MAHOGANY_GYM",
            "MAHOGANY_RED_GYARADOS_SPEECH_HOUSE", "LAKE_OF_RAGE",
            "LAKE_OF_RAGE_MAGIKARP_HOUSE", "ROUTE_42", "ROUTE_43",
            "TEAM_ROCKET_BASE_B1F", "TEAM_ROCKET_BASE_B2F",
            "TEAM_ROCKET_BASE_B3F"]),
    "09": ("A tomada da RADIO TOWER",
           ["RADIO_TOWER_2F", "RADIO_TOWER_3F", "RADIO_TOWER_4F",
            "RADIO_TOWER_5F", "GOLDENROD_UNDERGROUND"]),
    "10": ("Blackthorn, Dragon's Den, Routes 36/44/45/46, Ruins of Alph",
           ["BLACKTHORN_CITY", "BLACKTHORN_GYM_1F", "BLACKTHORN_GYM_2F",
            "BLACKTHORN_DRAGON_SPEECH_HOUSE", "BLACKTHORN_EMYS_HOUSE",
            "BLACKTHORN_MART", "BLACKTHORN_POKECENTER_1F",
            "DRAGONS_DEN_1F", "DRAGONS_DEN_B1F",
            "ROUTE_36", "ROUTE_36_NATIONAL_PARK_GATE",
            "ROUTE_36_RUINS_OF_ALPH_GATE",
            "ROUTE_44", "ROUTE_45", "ROUTE_46",
            "RUINS_OF_ALPH_OUTSIDE", "RUINS_OF_ALPH_INNER_CHAMBER",
            "RUINS_OF_ALPH_AERODACTYL_CHAMBER", "RUINS_OF_ALPH_HO_OH_CHAMBER",
            "RUINS_OF_ALPH_KABUTO_CHAMBER", "RUINS_OF_ALPH_OMANYTE_CHAMBER",
            "RUINS_OF_ALPH_RESEARCH_CENTER"]),
    "11": ("Victory Road, Liga, Indigo Plateau",
           ["VICTORY_ROAD", "VICTORY_ROAD_GATE",
            "HALL_OF_FAME", "INDIGO_PLATEAU_POKECENTER_1F",
            "WILLS_ROOM", "KOGAS_ROOM", "BRUNOS_ROOM",
            "KARENS_ROOM", "LANCES_ROOM"]),
}


def chaves_do_lote(nome):
    """-> {chave: (mapa, ingles)} das falas proprias dos mapas do lote.

    Chaves do banco 40 ficam de fora: sao StdScripts, comuns a todos os
    mapas, e apareceriam repetidas em todo lote.
    """
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
            if not k.startswith("40:"):
                achadas.setdefault(k, (m, en))
    return achadas


def planilha(nome):
    """Escreve planilha-<nome>.py com o ingles e os codigos de controle a vista."""
    achadas = chaves_do_lote(nome)
    dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
    pub = {k: v for k, v in achadas.items() if k in dial}
    destino = os.path.join(HERE, "planilha-%s.py" % nome)
    with open(destino, "w", encoding="utf-8") as f:
        f.write("# Lote %s -- ingles original.  Nao entra no mod.\n\n" % nome)
        for k in sorted(pub):
            f.write("# %s\n%r: %r,\n\n" % (pub[k][0], k, pub[k][1]))
    return pub, destino


if __name__ == "__main__":
    nome = sys.argv[1] if len(sys.argv) > 1 else "01"
    pub, destino = planilha(nome)
    print("lote %s: %d falas -> %s" % (nome, len(pub), destino))
    for m, n in collections.Counter(v[0] for v in pub.values()).most_common():
        print("   %-26s %d" % (m, n))

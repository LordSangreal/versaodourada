"""Deduz o que cada macro redefinida da ROM BR expande, comparando EN x PT."""
import json, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
mf = json.load(open(os.path.join(HERE, "repo", "tools", "rom_manifest_gold.json"),
                    encoding="utf-8"))
cm = {int(k): v for k, v in mf["charmap"].items()}
byname = {}
for c, v in cm.items():
    byname.setdefault(v, c)

# tudo que sai como marcador ou kana no PT e candidato a macro redefinida
susp = collections.Counter()
for en, pt in d.values():
    for m in re.finditer(r"<[^>]+>", pt):
        susp[m.group(0)] += 1
    for ch in pt:
        if 0x3000 < ord(ch) < 0xFF00:
            susp[ch] += 1

print("=" * 70)
for marker, n in susp.most_common(14):
    byte = byname.get(marker)
    print(f"\n### {marker}   byte={hex(byte) if byte is not None else '?'}   {n} ocorrencias")
    # palavras que contem o marcador, com o ingles ao lado
    mostrados = 0
    for en, pt in d.values():
        if marker not in pt:
            continue
        # recorta a vizinhanca no PT e a fala inteira em EN, curtas
        for m in re.finditer(re.escape(marker), pt):
            a = max(0, m.start() - 14)
            b = min(len(pt), m.end() + 14)
            trecho = pt[a:b].replace("\n", " ").replace("\v", " ").replace("\f", " ")
            print(f"    PT ...{trecho}...")
            break
        if mostrados == 0:
            print(f"    EN {en[:70]!r}".replace("\\n", " "))
        mostrados += 1
        if mostrados >= 4:
            break

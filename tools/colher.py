"""Colhe as chaves do registro `strings` a partir dos sitios S(...) do codigo."""
import re, os, json, collections

REPO = r"C:\Users\Usuario\AppData\Local\Temp\claude\D--pokemon-gold-tradu--o\b805f749-d98d-4c24-9526-51b7a6e1a0bb\scratchpad\repo"

# S("texto")  ou  S("texto", "contexto")  ou  Strings("texto")
CALL = re.compile(
    r'\b(?:S|Strings)\(\s*"((?:[^"\\]|\\.)*)"\s*(?:,\s*"((?:[^"\\]|\\.)*)"\s*)?[,)]'
)


def unescape(s):
    return (s.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')
             .replace('\\v', '\v').replace('\\f', '\f').replace('\\\\', '\\'))


def harvest():
    found = collections.OrderedDict()
    where = collections.defaultdict(list)
    for root, dirs, files in os.walk(os.path.join(REPO, "src")):
        dirs[:] = [d for d in dirs if d not in (".git",)]
        for fn in sorted(files):
            if not fn.endswith(".lua"):
                continue
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, REPO).replace("\\", "/")
            try:
                src = open(p, encoding="utf-8").read()
            except Exception:
                continue
            for m in CALL.finditer(src):
                text, ctx = m.group(1), m.group(2)
                if not text:
                    continue
                text = unescape(text)
                # o segundo argumento so e contexto se nao for formatacao
                key = text
                if ctx and re.fullmatch(r"[a-z][\w.]*", ctx):
                    key = ctx + "|" + text
                if key not in found:
                    found[key] = text
                where[key].append(rel)
    return found, where


if __name__ == "__main__":
    found, where = harvest()
    print("chaves de `strings` encontradas:", len(found))
    gen2 = [k for k in found if any("gen2" in w for w in where[k])]
    print("  citadas em codigo gen2:", len(gen2))
    lens = [len(v) for v in found.values()]
    print("  comprimento medio:", round(sum(lens) / len(lens), 1), "| max:", max(lens))
    multiline = sum(1 for v in found.values() if "\n" in v)
    print("  com quebra de linha:", multiline)
    fmt = sum(1 for v in found.values() if "%" in v)
    print("  com formatacao %s/%d:", fmt)
    json.dump({"keys": list(found.keys()), "text": found,
               "where": {k: v[:3] for k, v in where.items()}},
              open("strings_en.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print()
    print("--- amostra ---")
    for k in list(found)[:15]:
        print("   ", repr(k))

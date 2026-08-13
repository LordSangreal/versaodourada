"""QA do catalogo: sintaxe, largura de 18 colunas, tokens."""
import re, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
MOD = os.path.join(HERE, "versaodourada")

src = open(os.path.join(MOD, "lang", "dialogue.lua"), encoding="utf-8").read()
ENTRY = re.compile(r'\["([0-9a-f]{2}:[0-9a-f]{4})"\] = "((?:[^"\\]|\\.)*)"')
entries = ENTRY.findall(src)
print("tamanho do catalogo:", len(src), "bytes")
print("entradas parseadas:", len(entries))

UNESC = {"\\n": "\n", "\\v": "\n", "\\f": "\n", '\\"': '"', "\\\\": "\\"}


def unescape(s):
    out, i = [], 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            out.append(UNESC.get(s[i:i + 2], s[i + 1]))
            i += 2
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


# Um token nao ocupa em tela o tamanho que ocupa no arquivo: "{PLAYER}" sao
# 8 caracteres no texto e rende o nome do jogador, ate 7.  Medir pelo literal
# acusava 40 estouros que nao existem, e um validador que grita errado deixa
# de ser lido -- e ai o estouro de verdade passa.  Cada token conta pelo
# maior tamanho que pode render.
LARGURA_TOKEN = {
    "{PLAYER}": 7,    # nome do jogador, limite da tela de nomes
    "{RIVAL}": 7,
    "{MOM}": 4,
    "{STRBUF}": 10,   # nome de POKeMON / item posto em runtime
    "{TRAINER}": 8,
    "{NUM}": 5,
}
TOKEN = re.compile(r"\{[A-Z_]+\}")


def largura(linha):
    """Quantas colunas a linha ocupa em tela, no pior caso."""
    def troca(m):
        return "#" * LARGURA_TOKEN.get(m.group(0), 8)
    return len(TOKEN.sub(troca, linha))


over, empty = [], 0
widths = []
for k, v in entries:
    txt = unescape(v)
    if not txt.strip():
        empty += 1
    for line in txt.split("\n"):
        w = largura(line)
        widths.append(w)
        if w > 18:
            over.append((k, line))

print("linhas de texto:", len(widths))
print("  largura maxima:", max(widths) if widths else 0)
print("  acima de 18 colunas:", len(over))
for k, l in over[:8]:
    print("     ", k, repr(l), len(l))
print("  entradas vazias:", empty)

# tokens de runtime
TOK = re.compile(r"\{[A-Z_]+\}")
toks = {}
for k, v in entries:
    for t in TOK.findall(unescape(v)):
        toks[t] = toks.get(t, 0) + 1
print("tokens de runtime:", toks)

# balanceamento basico de aspas / sintaxe
opens = src.count("[\"")
print("chaves abertas:", opens, "| entradas:", len(entries),
      "| casa:", opens == len(entries))
print()
print("--- amostra ---")
for k, v in entries[:4]:
    print(" [%s] %s" % (k, unescape(v).replace("\n", " | ")[:76]))

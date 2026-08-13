"""Monta o mod versaodourada a partir do dialogo extraido."""
import json, os, re, shutil, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "versaodourada")
VERSION = "0.1.0"

dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))

TOKENS = re.compile(r"\{[A-Z_]+\}")


BOXCHARS = set("┌─┐│└┘")


def boxy(s):
    return any(c in BOXCHARS for c in s)


def kana(s):
    return any(0x3000 < ord(c) < 0xFF00 for c in s)


def suspect_marker(en, pt):
    """Marcador <...> que aparece no PT mas nao no EN = codigo nao mapeado."""
    a = set(re.findall(r"<[^>]+>", pt))
    b = set(re.findall(r"<[^>]+>", en))
    return bool(a - b)


def clean(pt):
    # a ROM BR enche de espaco a direita para preencher a caixa; sobra visual
    return "\n".join(line.rstrip() for line in pt.split("\n"))


kept, dropped = {}, {"kana": 0, "marcador": 0, "vazio": 0, "token": 0, "igual": 0}
for k, (en, pt) in dial.items():
    if not pt.strip():
        dropped["vazio"] += 1
        continue
    if kana(pt):
        dropped["kana"] += 1
        continue
    if boxy(pt):
        dropped["moldura"] = dropped.get("moldura", 0) + 1
        continue
    if suspect_marker(en, pt):
        dropped["marcador"] += 1
        continue
    # os tokens de runtime tem que sobreviver identicos
    if sorted(TOKENS.findall(en)) != sorted(TOKENS.findall(pt)):
        dropped["token"] += 1
        continue
    if en == pt:
        dropped["igual"] += 1
        continue
    kept[k] = clean(pt)

print("falas mantidas:", len(kept))
print("descartadas:", dropped)

# ------------------------------------------------------------ arquivos
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(os.path.join(OUT, "lang"), exist_ok=True)


def lua_str(s):
    return ('"' + s.replace("\\", "\\\\").replace('"', '\\"')
            .replace("\n", "\\n").replace("\v", "\\v").replace("\f", "\\f") + '"')


with open(os.path.join(OUT, "lang", "dialogue.lua"), "w", encoding="utf-8") as f:
    f.write("-- Falas de Pokemon Gold em portugues brasileiro.\n")
    f.write("-- Chave = ponteiro da ROM USA, no formato que o gen1recomp usa.\n")
    f.write("-- Vazio ou ausente = cai em ingles.\n")
    f.write("return {\n")
    for k in sorted(kept):
        f.write("  [%s] = %s,\n" % (lua_str(k), lua_str(kept[k])))
    f.write("}\n")

MANIFEST = {
    "id": "versaodourada",
    "name": "VersaoDourada",
    "version": VERSION,
    "api": 2,
    "entry": "main.lua",
    "profile": "content",
    "category": "LANGUAGE",
    "language": True,
    "games": ["gold"],
    "game_version": ">=0.0.0-dev <1.0.0",
    "priority": 100,
    "dependencies": [],
    "optional_dependencies": [],
    "conflicts": [],
    "description": ("Portugues brasileiro para Pokemon Gold. Texto extraido da "
                    "traducao de R_Lopes e Night_Shadown. Nomes de golpes ficam "
                    "no original."),
}
json.dump(MANIFEST, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

MAIN = '''-- VersaoDourada: Pokemon Gold em portugues brasileiro.
--
-- Os catalogos em lang/ sao tabelas Lua simples.  Valor vazio significa
-- "ainda nao traduzido" e cai em ingles, entao uma traducao parcial e
-- sempre jogavel.
--
-- Nomes de golpes ficam no original em ingles, de proposito: nao ha
-- lang/move_names.lua neste mod.

return function(mod)
  local function catalog(name)
    local rel = "lang/" .. name .. ".lua"
    local body = mod:read(rel)
    if not body then return {} end
    local chunk, err = loadstring(body, rel)
    if not chunk then
      mod.log:warn("%s tem erro de sintaxe: %s", rel, tostring(err))
      return {}
    end
    local ok, t = pcall(chunk)
    if not ok or type(t) ~= "table" then
      mod.log:warn("%s nao devolveu uma tabela", rel)
      return {}
    end
    return t
  end

  local function each(name, apply)
    local n = 0
    for k, v in pairs(catalog(name)) do
      if type(v) == "string" and v ~= "" then
        apply(k, v)
        n = n + 1
      end
    end
    return n
  end

  -- A fonte da ROM nao tem os acentos do portugues.  O modo TTF do motor
  -- usa a Plain Pixel embutida, que cobre todos eles.  Os digitos ficam
  -- nos tiles da ROM para as colunas numericas seguirem alinhadas.
  mod.content.font:register("ttf", { tiles = "0123456789" })

  local n = each("dialogue", function(id, value)
    mod.content.text:override(id, value)
  end)
  n = n + each("strings", function(src, value)
    mod.content.strings:override(src, value)
  end)
  n = n + each("item_names", function(id, value)
    mod.content.items:patch(id, { name = value })
  end)
  n = n + each("status_labels", function(id, value)
    mod.content.statuses:patch(id, { label = value })
  end)

  mod.events:on("game.ready", function()
    mod.log:info("VersaoDourada: %d textos em portugues", n)
  end)
end
'''
open(os.path.join(OUT, "main.lua"), "w", encoding="utf-8").write(MAIN)

# catalogos vazios, prontos para preencher
for name, note in (("strings", "Texto do motor: batalha, menus, opcoes. Chave = o ingles original."),
                   ("item_names", "Nomes de itens. Chave = id do item."),
                   ("status_labels", "Rotulos de status (PAR, SLP...).")):
    with open(os.path.join(OUT, "lang", name + ".lua"), "w", encoding="utf-8") as f:
        f.write("-- %s\n-- Vazio = cai em ingles.\nreturn {\n}\n" % note)

README = '''# VersaoDourada

Pokemon Gold em portugues brasileiro para o [gen1recomp](https://github.com/bryanthaboi/gen1recomp).

## Creditos

A traducao do texto e trabalho de **R_Lopes** e **Night_Shadown**, publicada
originalmente como patch de ROM no PO.B.R.E / romhackers.org. Este mod nao
traduz nada por conta propria: ele porta aquele texto para o formato de mod do
gen1recomp, para que rode sem precisar de ROM modificada.

Se voce e um dos autores e quer que este mod saia do ar, e so abrir uma issue.

O motor e a plataforma de mods sao de bryanthaboi e dos contribuidores do
gen1recomp.

## O que este mod faz

- Traduz as falas do jogo para portugues, com acentuacao completa.
- **Nomes de golpes ficam no original em ingles**, de proposito.
- Nomes de Pokemon ficam no original (sao os nomes oficiais).

Cobertura e parcial e cresce a cada versao. O que ainda nao foi traduzido
aparece em ingles, entao o jogo e sempre jogavel.

## Instalacao

O mod precisa da versao atual do gen1recomp com Gold importado (Gold e beta).
Instale pelo gerenciador de mods do proprio aplicativo, ou solte a pasta em:

- Windows: `%APPDATA%\\LOVE\\pokemon-love2d\\mods\\versaodourada\\`
- Linux: `~/.local/share/love/pokemon-love2d/mods/versaodourada/`
- macOS: `~/Library/Application Support/LOVE/pokemon-love2d/mods/versaodourada/`

Abra o gerenciador de mods (F10) e confirme que aparece habilitado. Se
aparecer `ENABLED (NOT THIS GAME)`, voce nao esta num boot de Gold.

## Aviso

Nenhum byte de ROM acompanha este mod. Voce precisa da sua propria copia
legitima de Pokemon Gold para o gen1recomp importar.
'''
open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(README)

open(os.path.join(OUT, "CHANGELOG.md"), "w", encoding="utf-8").write(
    "# Changelog\n\n## %s\n\n- Primeira versao: %d falas em portugues.\n"
    "- Nomes de golpes mantidos no original.\n" % (VERSION, len(kept)))

# zip para o release
zp = os.path.join(HERE, "versaodourada-%s.zip" % VERSION)
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(OUT):
        for fn in files:
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, OUT))
print("mod em:", OUT)
print("zip:", zp, os.path.getsize(zp), "bytes")

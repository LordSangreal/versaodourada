"""Monta o mod versaodourada a partir do dialogo extraido."""
import json, os, re, shutil, zipfile, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "versaodourada")
VERSION = "0.3.2"

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


# A fonte do Gold so tem é, ü e Ü.  Todo o resto vira ASCII, senao o
# caractere simplesmente nao desenha e a palavra sai com um buraco
# ("mae" em vez de "m e").  Quando a pagina de glifos entrar, e so
# esvaziar este mapa e os acentos voltam sozinhos.
DOBRA = {
    "á": "a", "â": "a", "ã": "a", "à": "a",
    "ê": "e", "í": "i", "ó": "o", "ô": "o", "õ": "o", "ú": "u", "ç": "c",
    "Á": "A", "Â": "A", "Ã": "A", "À": "A", "É": "E", "Ê": "E",
    "Í": "I", "Ó": "O", "Ô": "O", "Õ": "O", "Ú": "U", "Ç": "C",
}


def dobrar(s):
    return "".join(DOBRA.get(c, c) for c in s)


import glossario


def clean(pt):
    # 1) glossario: terminologia pt-BR atual, sem estourar as 18 colunas
    # 2) dobra de acentos, ate a pagina de glifos entrar
    # 3) a ROM BR enche de espaco a direita para preencher a caixa
    pt = glossario.aplicar(pt, re)
    return "\n".join(line.rstrip() for line in dobrar(pt).split("\n"))


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
    if "<" in pt or "<" in en:
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

# Varias chaves caem dentro da MESMA string, em enderecos deslocados (a fala
# da vizinha aparecia em 60:5eb2/5eb5/5eb8).  A mais longa e a string inteira;
# as outras comecam no meio dela.  Fica so a inteira.
porbanco = collections.defaultdict(list)
for k in kept:
    b, a = k.split(":")
    porbanco[b].append((int(a, 16), k))
frag = set()
for b, rows in porbanco.items():
    rows.sort()
    for i, (a, k) in enumerate(rows):
        for a2, k2 in rows[max(0, i - 4):i]:
            if a - a2 <= 24 and kept[k] and kept[k2].endswith(kept[k]):
                frag.add(k)
                break
for k in frag:
    kept.pop(k, None)
dropped["fragmento"] = len(frag)

# Precedencia: traducao nossa na frente da derivada.  Enquanto os lotes nao
# cobrem tudo, o mod mistura as duas -- e por isso a atribuicao continua.
# Quando `derivadas` chegar a zero, ela pode sair.
import pt as _pt
_, _NOSSAS = _pt.carregar()
nossas = 0
for k, v in _NOSSAS.items():
    if v and v.strip():
        kept[k] = clean(v)
        nossas += 1
derivadas = len(kept) - nossas

print("falas mantidas:", len(kept))
print("  nossas   :", nossas)
print("  derivadas:", derivadas)
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
    # Sem `games`, o manifest significa "Gen 1 apenas" e um boot de Gold pula
    # o mod (MK400).  E o campo que rende o selo de geracao na lista.
    "games": ["gold"],
    # O aplicativo e a versao 1.8.0.  A faixa "<1.0.0", herdada do
    # versaovermelha, o excluia da lista -- instalava e nunca aparecia.
    "game_version": ">=0.0.0-0 <2.0.0",
    "language": True,
    "priority": 100,
    "dependencies": [],
    "optional_dependencies": [],
    "conflicts": [],
    "github": "LordSangreal/versaodourada",
    "description": ("Portugues brasileiro para Pokemon Gold. Traducao propria em "
                    "construcao; parte do texto ainda vem da traducao de R_Lopes e "
                    "Night_Shadown. Golpes, Pokemon, TM e HM ficam no original."),
}
json.dump(MANIFEST, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

MAIN = '''-- VersaoDourada: Pokemon Gold em portugues brasileiro.
--
-- Nomes de golpes e de Pokemon ficam no original em ingles, de proposito:
-- nao ha lang/move_names.lua nem lang/species_names.lua neste mod.

return function(mod)
  local function catalog(name)
    local rel = "lang/" .. name .. ".lua"
    local body = mod:read(rel)
    if not body then return {} end
    local loader = loadstring or load
    local chunk, err = loader(body, rel)
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

  -- NAO registrar a fonte TTF aqui.  Na 0.1.2 isso deixou a tela de mods
  -- ilegivel (tudo claro), e o versaovermelha mantem a mesma chamada
  -- comentada pelo mesmo motivo.  Sem acentos proprios por enquanto: o
  -- texto usa a fonte da ROM ate a pagina de glifos entrar.

  local dialogue = catalog("dialogue")

  -- ---- diagnostico ---------------------------------------------------
  -- O texto continuou em ingles na 0.1.2, entao antes de aplicar seja la o
  -- que for, medir: quantas das minhas chaves o jogo realmente conhece.
  local reg = mod.content.text
  local mine, hit = 0, 0
  for _ in pairs(dialogue) do mine = mine + 1 end
  if reg and reg.has then
    for k in pairs(dialogue) do
      local ok, yes = pcall(function() return reg:has(k) end)
      if ok and yes then hit = hit + 1 end
    end
  end
  mod.log:info("DIAG chaves minhas=%d  reconhecidas=%d", mine, hit)

  -- Uma amostra das chaves que o jogo tem de verdade, para comparar com o
  -- formato das minhas.
  if reg and reg.each then
    local shown = 0
    pcall(function()
      for id in reg:each() do
        mod.log:info("DIAG chave real: %s", tostring(id))
        shown = shown + 1
        if shown >= 8 then break end
      end
    end)
    if shown == 0 then mod.log:info("DIAG registro text vazio ou nao iteravel") end
  else
    mod.log:info("DIAG registro text sem :each()")
  end
  for _, path in ipairs({ "gen2Text", "text" }) do
    pcall(function()
      local d = mod.game and mod.game.data and mod.game.data[path]
      if type(d) == "table" then
        local c, sample = 0, nil
        for id in pairs(d) do c = c + 1; sample = sample or id end
        mod.log:info("DIAG data.%s tem %d chaves, ex: %s", path, c, tostring(sample))
      end
    end)
  end

  -- ---- aplicacao -----------------------------------------------------
  local n = 0
  for k, v in pairs(dialogue) do
    if type(v) == "string" and v ~= "" then
      reg:override(k, v)
      n = n + 1
    end
  end
  n = n + each("strings", function(src, value)
    mod.content.strings:override(src, value)
  end)
  n = n + each("item_names", function(id, value)
    mod.content.items:patch(id, { name = value })
  end)

  mod.events:on("game.ready", function()
    mod.log:info("VersaoDourada: %d textos aplicados", n)
  end)
end
'''
open(os.path.join(OUT, "main.lua"), "w", encoding="utf-8").write(MAIN)

# catalogos vazios, prontos para preencher
import pt
STRINGS, _NOSSO_DIALOGO = pt.carregar()
with open(os.path.join(OUT, "lang", "strings.lua"), "w", encoding="utf-8") as f:
    f.write("-- Texto do motor: batalha, menus, opcoes.\n")
    f.write("-- Chave = a string em ingles exatamente como o codigo a escreve.\n")
    f.write("return {\n")
    for k in sorted(STRINGS):
        f.write("  [%s] = %s,\n" % (lua_str(k), lua_str(dobrar(STRINGS[k]))))
    f.write("}\n")
print("strings de menu:", len(STRINGS))

for name, note in (("item_names", "Nomes de itens. Chave = id do item."),
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

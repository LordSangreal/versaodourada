"""Monta o mod versaodourada a partir do dialogo extraido."""
import json, os, re, shutil, zipfile, collections

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "versaodourada")
VERSION = "0.18.0"

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


# A fonte da ROM so tem é, ü e Ü.  Ate a 0.5.0 todo o resto era dobrado para
# ASCII ("mae", "coracao"), porque um caractere sem glifo nao desenha nada.
#
# A pagina em assets/font/latin.png cobre os acentos desde a 0.6.0, entao a
# dobra esta desligada: DOBRA vazio faz `dobrar` virar identidade.
#
# Para reverter, se a pagina der problema: reponha aqui o mapa de dobra
# (á->a, ã->a, ç->c, ...) e o comportamento volta ao da 0.5.0.
DOBRA = {}


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

  -- ---- glifos -------------------------------------------------------
  -- Registrar ANTES de qualquer coisa pedir um glifo.  O caminho da imagem
  -- vai direto para love.graphics.newImage, que resolve contra a raiz do
  -- jogo e nao contra o mod -- sem `mod.assets:path` a pagina carrega vazia
  -- e todo acentuado desenha em branco.
  for id, page in pairs(catalog("font")) do
    if type(page) == "table" and type(page.image) == "string"
        and mod:read(page.image) then
      page.image = mod.assets:path(page.image)
    end
    mod.content.font:register(id, page)
  end
  for seq, code in pairs(catalog("charmap")) do
    mod.content.font:register("charmap:" .. seq, { seq = seq, code = code })
  end

  -- ---- aplicacao -----------------------------------------------------
  local n = 0
  for k, v in pairs(catalog("dialogue")) do
    if type(v) == "string" and v ~= "" then
      mod.content.text:override(k, v)
      n = n + 1
    end
  end
  n = n + each("strings", function(src, value)
    mod.content.strings:override(src, value)
  end)
  n = n + each("item_names", function(id, value)
    mod.content.items:patch(id, { name = value })
  end)
  -- O status tem dois rotulos: o do texto e o de tres letras que cabe na
  -- caixinha ao lado da barra de vida.  Trocar so o primeiro deixaria o HUD
  -- em ingles, que e justamente onde o rotulo mais aparece.
  n = n + each("status_labels", function(id, value)
    mod.content.statuses:patch(id, { label = value, hudLabel = value })
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

# ---- o launcher NAO e traduzido, de proposito -------------------------
#
# A tela do jogo tem 18 colunas e eu controlo a quebra de linha.  O launcher
# nao: e a interface do aplicativo, com botoes de largura fixa.  O portugues
# e mais longo que o ingles, entao rotulo traduzido estoura e sai cortado --
# "Play Gold (Be...", "0 insignias - 0:00 - 0 capturados" quebrando a linha.
#
# O filtro e por ARQUIVO DE ORIGEM, nao por lista de chaves escrita a mao:
# uma chave que so aparece em LauncherView / LauncherSettings / LauncherMods
# / ManagerState / update e do aplicativo, e sai.  Assim um lote futuro nao
# reintroduz isto por descuido.
# `src/import/` INTEIRO, nao arquivo a arquivo: e a camada do aplicativo,
# do launcher ao importador de ROM.  Listar arquivo a arquivo deixou passar
# uma mensagem do RomImporter, que aparece na tela do aplicativo do mesmo
# jeito.  Diretorio inteiro nao tem esse buraco.
_LAUNCHER = ("src/import/", "src/mods/LauncherMods", "src/mods/ManagerState",
             "src/update/")
_onde = {}
_f = os.path.join(HERE, "strings_en.json")
if os.path.exists(_f):
    _onde = json.load(open(_f, encoding="utf-8")).get("where", {})


def _so_do_launcher(chave):
    """BASTA aparecer numa tela do aplicativo para a chave sair.

    A primeira versao disto so removia a chave se TODAS as origens fossem do
    launcher.  Sobravam 31 compartilhadas -- FPS, orientacao, vibracao,
    toque -- que sao ajuste de aparelho e o launcher desenha em botao de
    largura fixa.  Traduzidas, estouravam la.

    Perder essas no jogo custa pouco: o Gold desenha as proprias telas em
    src/ui/gen2/, entao boa parte nem aparece num boot de Gold.
    """
    return any(any(p in a for p in _LAUNCHER) for a in _onde.get(chave, []))


_fora = [k for k in STRINGS if _so_do_launcher(k)]
for k in _fora:
    STRINGS.pop(k)
print("strings do launcher removidas:", len(_fora))
with open(os.path.join(OUT, "lang", "strings.lua"), "w", encoding="utf-8") as f:
    f.write("-- Texto do motor: batalha, menus, opcoes.\n")
    f.write("-- Chave = a string em ingles exatamente como o codigo a escreve.\n")
    f.write("return {\n")
    for k in sorted(STRINGS):
        f.write("  [%s] = %s,\n" % (lua_str(k), lua_str(dobrar(STRINGS[k]))))
    f.write("}\n")
print("strings de menu:", len(STRINGS))

# ---- pagina de glifos acentuados -------------------------------------
import glifos
_w, _h = glifos.gerar(os.path.join(OUT, "assets", "font", "latin.png"))
with open(os.path.join(OUT, "lang", "font.lua"), "w", encoding="utf-8") as f:
    f.write("-- Pagina de glifos que este mod acrescenta.\n")
    f.write("-- base 0x100 e espaco livre acima das paginas $60/$80 da ROM,\n")
    f.write("-- entao isto ADICIONA um alfabeto em vez de trocar o existente.\n")
    f.write("return {\n  latin = {\n")
    f.write('    image = "assets/font/latin.png",\n')
    f.write("    base = 0x100,\n    glyphsPerRow = 16,\n  },\n}\n")
with open(os.path.join(OUT, "lang", "charmap.lua"), "w", encoding="utf-8") as f:
    f.write("-- Que sequencia de bytes desenha qual glifo da pagina acima.\n")
    f.write("return {\n")
    for _ch, _code in sorted(glifos.charmap().items(), key=lambda x: x[1]):
        f.write("  [%s] = 0x%X,\n" % (lua_str(_ch), _code))
    f.write("}\n")
print("glifos:", len(glifos.PAGINA), "(%dx%d)" % (_w, _h))

ITENS, STATUS = pt.catalogos()

# Nome de item em Gen 2 cabe em 12 caracteres.  Publicar truncado poria lixo
# na bolsa, entao o que passa disso e reprovado e fica em ingles.
MAX_NOME = 12
for _k, _v in [(k, v) for k, v in ITENS.items() if len(dobrar(v)) > MAX_NOME]:
    print("  item longo demais, fica em ingles: %s = %r (%d)"
          % (_k, _v, len(dobrar(_v))))
    ITENS.pop(_k)

with open(os.path.join(OUT, "lang", "item_names.lua"), "w", encoding="utf-8") as f:
    f.write("-- Nomes de itens.  Chave = id do item.\n")
    f.write("-- TODO nome de item fica no original em ingles, por decisao do\n")
    f.write("-- usuario na 0.17.0.  Tabela vazia = o jogo usa o nome da ROM.\n")
    f.write("return {\n")
    for k in sorted(ITENS):
        f.write("  [%s] = %s,\n" % (lua_str(k), lua_str(dobrar(ITENS[k]))))
    f.write("}\n")

with open(os.path.join(OUT, "lang", "status_labels.lua"), "w", encoding="utf-8") as f:
    f.write("-- Rotulos de status.  Tres caracteres: e o que a caixinha ao\n")
    f.write("-- lado da barra de vida comporta.\n")
    f.write("return {\n")
    for k in sorted(STATUS):
        f.write("  [%s] = %s,\n" % (lua_str(k), lua_str(dobrar(STATUS[k]))))
    f.write("}\n")
print("itens:", len(ITENS), "| status:", len(STATUS))

# O README e um ARQUIVO, nao um texto embutido aqui.
#
# Ele morava dentro deste script como uma string gigante, e por isso todo
# build reescrevia o README do repositorio com a versao congelada no codigo.
# Foi assim que a pagina atualizada na 0.8.0 voltou sozinha para o texto da
# 0.3.0 quando publiquei a 0.8.1.  Agora o arquivo manda, e o build so o
# copia para dentro do pacote.
_readme = os.path.join(HERE, "README_mod.md")
if os.path.exists(_readme):
    shutil.copyfile(_readme, os.path.join(OUT, "README.md"))
else:
    print("  AVISO: README_mod.md nao encontrado; o mod vai sem README")

# O CHANGELOG tinha o mesmo defeito que o README ate a 0.8.2: era gerado
# aqui, entao toda versao publicada dizia "Primeira versao" e o historico
# se apagava a cada build.  Agora e arquivo, e o build so copia.
_chlog = os.path.join(HERE, "CHANGELOG_mod.md")
if os.path.exists(_chlog):
    shutil.copyfile(_chlog, os.path.join(OUT, "CHANGELOG.md"))
else:
    print("  AVISO: CHANGELOG_mod.md nao encontrado; o mod vai sem changelog")

# zip para o release
zp = os.path.join(HERE, "versaodourada-%s.zip" % VERSION)
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(OUT):
        for fn in files:
            p = os.path.join(root, fn)
            z.write(p, os.path.relpath(p, OUT))
print("mod em:", OUT)
print("zip:", zp, os.path.getsize(zp), "bytes")

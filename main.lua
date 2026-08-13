-- VersaoDourada: Pokemon Gold em portugues brasileiro.
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

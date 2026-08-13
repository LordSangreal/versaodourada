-- VersaoDourada: Pokemon Gold em portugues brasileiro.
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

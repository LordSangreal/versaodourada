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
  -- Descricao de item.  `description` nao esta declarado no schema, mas o
  -- registro de topo e extensivel e quem desenha le `def.description`
  -- (ui/gen2/PackMenu.lua:823).  O pcall isola: se a rota nao existir, o
  -- mod segue funcionando e o aviso aparece no log em vez de derrubar tudo.
  local descOk, descErro = 0, nil
  each("item_descriptions", function(id, value)
    local ok, err = pcall(function()
      mod.content.items:patch(id, { description = value })
    end)
    if ok then descOk = descOk + 1 elseif not descErro then descErro = err end
  end)
  n = n + descOk
  if descErro then
    mod.log:warn("descricao de item nao aplicada: %s", tostring(descErro))
  end

  mod.events:on("game.ready", function()
    mod.log:info("VersaoDourada: %d textos aplicados", n)
  end)
end

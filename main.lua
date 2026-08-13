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

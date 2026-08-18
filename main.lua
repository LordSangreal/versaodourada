-- VersaoDourada: Pokemon Gold em portugues brasileiro.
--
-- Nomes de golpes e de Pokemon ficam no original em ingles, de proposito:
-- nao ha lang/move_names.lua nem lang/species_names.lua neste mod.

-- Ligar quando o conserto de persistencia de opcao entrar no gen1recomp.
--
-- A linha IDIOMA funciona, mas depende de o motor GRAVAR a escolha: no Gold,
-- `ManagerState:persistOptions` chama `game:writeOptions()`, que o `Game2`
-- nao define -- a guarda passa reto em silencio e o valor se perde no
-- reinicio.  (Pior: `save.options` no Game2 e o sub-bloco "gold", nao a
-- tabela de topo de onde o Loader le `modOptions`.)  Num motor sem o
-- conserto o jogador VE a opcao, muda, e ela volta sozinha -- controle morto,
-- pior que nao ter.
--
-- Enquanto isso, o botao documentado e MODS -> desligar o mod ->
-- APPLY & RESTART, que persiste em `modsByVersion` e funciona em build
-- qualquer.  Quando o conserto sair, ligar isto e exigir a versao pelo
-- `game_version` do manifest.
local OPCAO_IDIOMA = false

return function(mod)
  -- ---- idioma ---------------------------------------------------------
  -- O motor e o jogo sao em ingles; este mod e uma camada por cima.  Quem
  -- instala pode querer o original de volta sem desinstalar nada, entao a
  -- escolha vira uma linha no menu MODS em vez de exigir remover o mod.
  --
  -- `mod.options:define` registra o esquema e `:get` le o valor guardado
  -- (ou o `default`, quando o jogador nunca mexeu).  A linha de `choice`
  -- e um par { rotulo mostrado, valor gravado }.
  if OPCAO_IDIOMA then
    mod.options:define({
      {
        key = "idioma",
        type = "choice",
        label = "IDIOMA",
        choices = { { "PORTUGUES", "pt" }, { "ENGLISH", "en" } },
        default = "pt",
      },
    })
  end
  if OPCAO_IDIOMA and mod.options:get("idioma") == "en" then
    -- Nada e registrado: sem override no catalogo, `Strings.lookup` devolve
    -- a propria fonte e `data.text` fica com o texto da ROM.  O jogo roda
    -- byte a byte igual ao de quem nunca instalou o mod.
    mod.events:on("game.ready", function()
      mod.log:info("VersaoDourada: idioma ENGLISH, nada aplicado")
    end)
    return
  end

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
  -- Mesmas falas de dialogue.lua, sob as chaves que o Gen2Recomped usa
  -- (rotulo nomeado ou TEXT_S<banco>_<endereco>) em vez do ponteiro
  -- "banco:endereco" do gen1recomp.  Chave que o motor rodando nao
  -- reconhece fica parada no registro, sem custo -- por isso um catalogo
  -- so serve os dois motores sem precisar de mod separado.
  n = n + each("dialogue_gen2recomped", function(k, v)
    mod.content.text:override(k, v)
  end)
  n = n + each("strings", function(src, value)
    mod.content.strings:override(src, value)
  end)
  n = n + each("item_names", function(id, value)
    mod.content.items:patch(id, { name = value })
  end)
  -- Nome de golpe.  A regra antiga do projeto era manter em ingles; o
  -- usuario inverteu em 16/08/2026, pedindo a terminologia das cartas de TCG
  -- pt-BR (com o Pokemon GO como desempate).  Doze colunas -- ver o cabecalho
  -- de lang/move_names.lua para a medida dos dois layouts de batalha.
  local mnOk, mnErro = 0, nil
  each("move_names", function(id, value)
    local ok, err = pcall(function()
      mod.content.moves:patch(id, { name = value })
    end)
    if ok then mnOk = mnOk + 1 elseif not mnErro then mnErro = err end
  end)
  n = n + mnOk
  if mnErro then
    mod.log:warn("nome de golpe nao aplicado: %s", tostring(mnErro))
  end
  -- Nome de lugar: o TOWN MAP do POKéGEAR e o banner de area leem
  -- `row.name` direto de gen2Landmarks.landmarks (src/world/gen2/World.lua,
  -- src/ui/gen2/Pokegear.lua) -- nao passa por Strings(), entao traduzir no
  -- strings.lua nao alcanca essa tela.  Este e o registro que alcanca.
  -- So existe no gen1recomp; no Gen2Recomped o nome vem por getlandmarkname
  -- da ROM e o catalogo fica inerte, sem custo.
  n = n + each("landmarks", function(id, value)
    mod.content.landmarks:patch(id, { name = value })
  end)
  -- Classe de treinador.  A tela de batalha monta "BUG CATCHER BENNY" com
  -- `className .. " " .. name` (src/world/gen2/World.lua:6058), e `className`
  -- e o campo `name` do registro `trainers` -- que ja tem rota
  -- (`trainers = "gen2Trainers"` em Schemas.GEN2, com os callbacks gen2* que
  -- entram no `.classes`).  Nada disso passa por Strings(), entao e aqui ou
  -- em lugar nenhum.
  -- Dentro de pcall como os outros: com `api = 2` um id que o motor nao
  -- tenha e erro duro e derrubaria o mod inteiro.
  local tcOk, tcErro = 0, nil
  each("trainer_classes", function(id, value)
    local ok, err = pcall(function()
      mod.content.trainers:patch(id, { name = value })
    end)
    if ok then tcOk = tcOk + 1 elseif not tcErro then tcErro = err end
  end)
  n = n + tcOk
  if tcErro then
    mod.log:warn("classe de treinador nao aplicada: %s", tostring(tcErro))
  end
  -- O status tem dois rotulos: o do texto e o de tres letras que cabe na
  -- caixinha ao lado da barra de vida.  Trocar so o primeiro deixaria o HUD
  -- em ingles, que e justamente onde o rotulo mais aparece.
  -- Dentro de pcall: um id que o motor nao tenha derrubaria o mod inteiro
  -- (`api = 2` faz erro de registro ser erro duro, nao aviso), e ja custou
  -- uma sessao descobrir isso.  Assim um id errado some sozinho e o resto
  -- do catalogo continua valendo.
  local stOk, stErro = 0, nil
  each("status_labels", function(id, value)
    local ok, err = pcall(function()
      mod.content.statuses:patch(id, { label = value, hudLabel = value })
    end)
    if ok then stOk = stOk + 1 elseif not stErro then stErro = err end
  end)
  n = n + stOk
  if stErro then
    mod.log:warn("rotulo de status nao aplicado: %s", tostring(stErro))
  end
  -- Nome de tipo.  `TypeChart.displayName` le `record.name` de
  -- `data.type_chart.types`, e o registro type_chart aceita `name`.
  -- Dentro de pcall pelo mesmo motivo dos outros: id que o motor nao tenha
  -- derrubaria o mod inteiro com `api = 2`.
  local tpOk, tpErro = 0, nil
  each("type_names", function(id, value)
    local ok, err = pcall(function()
      mod.content.type_chart:patch(id, { name = value })
    end)
    if ok then tpOk = tpOk + 1 elseif not tpErro then tpErro = err end
  end)
  n = n + tpOk
  if tpErro then
    mod.log:warn("nome de tipo nao aplicado: %s", tostring(tpErro))
  end

  -- POKéDEX.  O registro `pokedex` so existe em motor que tenha a rota
  -- `pokedex = "gen2Pokedex.entries"` em Schemas.GEN2 -- no gen1recomp de
  -- hoje `data.gen2Pokedex` e um loadGenerated cru, sem merge.  Por isso o
  -- teste de existencia antes: num motor sem a rota, `mod.content.pokedex`
  -- e nil e o catalogo fica inerte em vez de derrubar o mod inteiro (com
  -- `api = 2` um erro de registro e erro duro, nao aviso).
  if mod.content.pokedex then
    local dexOk, dexErro = 0, nil
    for id, entrada in pairs(catalog("pokedex")) do
      if type(entrada) == "table" then
        local ok, err = pcall(function()
          mod.content.pokedex:patch(id, entrada)
        end)
        if ok then dexOk = dexOk + 1 elseif not dexErro then dexErro = err end
      end
    end
    n = n + dexOk
    if dexErro then
      mod.log:warn("POKéDEX nao aplicada: %s", tostring(dexErro))
    end
  end

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
  -- Descricao de golpe.  Aparece na tela de resumo do POKéMON
  -- (ui/gen2/SummaryMenu.lua:604) e na bolsa quando o item e uma TM ou HM
  -- (ui/gen2/PackMenu.lua:820) -- ali o jogo mostra a descricao do GOLPE.
  local mvOk, mvErro = 0, nil
  each("move_descriptions", function(id, value)
    local ok, err = pcall(function()
      mod.content.moves:patch(id, { description = value })
    end)
    if ok then mvOk = mvOk + 1 elseif not mvErro then mvErro = err end
  end)
  n = n + mvOk
  if mvErro then
    mod.log:warn("descricao de golpe nao aplicada: %s", tostring(mvErro))
  end

  mod.events:on("game.ready", function()
    mod.log:info("VersaoDourada: %d textos aplicados", n)
  end)
end

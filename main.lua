-- VersaoDourada: Pokemon Gold em portugues brasileiro.
--
-- Nome de POKeMON, de personagem e de cidade ficam no original em ingles, de
-- proposito -- so a palavra generica de lugar traduz ("CIDADE DE VIOLET").
-- Golpe, item, tipo e classe de treinador SE traduzem desde a 0.47.0, com a
-- terminologia das cartas de TCG pt-BR; por isso existem lang/move_names.lua
-- e lang/item_names.lua, que a regra anterior proibia.  Nao ha
-- lang/species_names.lua e nao deve haver.

-- Opcao de mod SOBREVIVE ao reinicio no Gold: `modOptions` esta em
-- SHARED_KEYS (src/core/gen2/Save.lua), entao `Save.saveOptions` a grava no
-- TOPO do options.lua -- nao dentro do bloco `gold` --, que e de onde o
-- carregador de mods a le no boot seguinte.  Por isso as duas linhas de
-- idioma abaixo (GOLPES e ITENS) existem: um controle que volta sozinho no
-- reinicio seria pior do que nao ter controle nenhum.
--
-- Esta aqui continua desligada, e nao por defeito: um interruptor "IDIOMA:
-- ENGLISH" que apaga o mod inteiro repete o que MODS -> desligar o mod ->
-- APPLY & RESTART ja faz, e em duplicidade a segunda copia so cria pergunta
-- sobre qual manda.
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

  -- ---- idioma de GOLPE e de ITEM --------------------------------------
  -- Nome de golpe e nome de item so passaram a traduzir na 0.47.0; ate ali a
  -- regra do projeto era a mesma dos nomes de POKeMON -- o jogador procura
  -- "THUNDERBOLT" num guia, nao "CHOQUE DO TROVAO".  A regra virou, mas o
  -- argumento nao evaporou: quem joga com guia aberto ainda quer o nome que
  -- o guia usa.  Entao vira escolha, em vez de virar discussao.
  --
  -- Sao NOMES, nao as descricoes: a descricao do golpe e da TM continua em
  -- portugues nos dois modos, porque ela explica o efeito e ninguem procura
  -- guia por ela.
  --
  -- PRECISA REINICIAR.  O mod decide no CARREGAMENTO o que registrar, e
  -- registro aplicado nao se desfaz -- entao mudar a linha com o jogo aberto
  -- nao teria efeito nenhum ate o proximo boot.  `requires_restart` faz o
  -- gerenciador dizer isso na tela (o rodape dele promete "(NO RESTART)",
  -- que aqui seria mentira); num motor que nao conheca o campo ele e
  -- ignorado sem erro, e o aviso fica por conta do README.
  local idioma = { golpes = "pt", itens = "pt" }
  local temOpcoes = pcall(function()
    mod.options:define({
      {
        key = "golpes",
        type = "choice",
        label = "NOME DOS GOLPES",
        choices = { { "PORTUGUES", "pt" }, { "ENGLISH", "en" } },
        default = "pt",
        requires_restart = true,
      },
      {
        key = "itens",
        type = "choice",
        label = "NOME DOS ITENS",
        choices = { { "PORTUGUES", "pt" }, { "ENGLISH", "en" } },
        default = "pt",
        requires_restart = true,
      },
    })
  end)
  if temOpcoes then
    for chave in pairs(idioma) do
      -- `:get` devolve o default quando o jogador nunca mexeu, e nil num
      -- motor sem a rota; qualquer coisa fora do par conhecido cai no
      -- portugues, que e o motivo de o mod existir.
      local ok, valor = pcall(function() return mod.options:get(chave) end)
      if ok and valor == "en" then idioma[chave] = "en" end
    end
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
  if idioma.itens == "pt" then
    n = n + each("item_names", function(id, value)
      mod.content.items:patch(id, { name = value })
    end)
  end
  -- Nome de golpe.  A regra antiga do projeto era manter em ingles; o
  -- usuario inverteu em 16/08/2026, pedindo a terminologia das cartas de TCG
  -- pt-BR (com o Pokemon GO como desempate).  Doze colunas -- ver o cabecalho
  -- de lang/move_names.lua para a medida dos dois layouts de batalha.
  local mnOk, mnErro = 0, nil
  if idioma.golpes == "pt" then
    each("move_names", function(id, value)
      local ok, err = pcall(function()
        mod.content.moves:patch(id, { name = value })
      end)
      if ok then mnOk = mnOk + 1 elseif not mnErro then mnErro = err end
    end)
  end
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
  -- QUAL JOGO ESTA RODANDO.  Onze dos doze catalogos servem Gold e Silver sem
  -- tocar em nada: o texto de dialogo e IDENTICO nas duas ROMs -- 3134 falas,
  -- zero diferentes -- e itens, golpes, lugares e treinadores tambem.  Ver
  -- GOLD-x-SILVER.md.
  --
  -- A POKeDEX e a excecao, e e a grande: as 251 especies tem ficha propria em
  -- cada versao, e o registro e indexado por ID DE ESPECIE, nao por endereco.
  -- Um catalogo so mostraria a ficha do Gold para quem joga Silver -- que e o
  -- mesmo defeito que separou o Crystal em repositorio proprio na 0.46.0.
  --
  -- Quem responde qual jogo e a propria ROM: ENTEI e TYRANITAR tem a altura
  -- TROCADA entre as versoes (ENTEI 6'11" no Gold, 6'07" no Silver).  E a
  -- unica diferenca NUMERICA que serve de identidade, e por isso nao depende
  -- de decodificar texto.  Lida ANTES de qualquer patch nosso: depois, o valor
  -- lido seria o que nos mesmos escrevemos.
  --
  -- Sem a rota `pokedex` (motor de fabrica) a pergunta nao tem resposta -- e
  -- nem precisa ter, porque ali nenhuma ficha e escrita de qualquer jeito.
  local jogo
  if mod.content.pokedex then
    local ok, entei = pcall(function()
      return mod.content.pokedex:get("ENTEI")
    end)
    if ok and type(entei) == "table" and entei.height then
      jogo = entei.height == 607 and "silver" or "gold"
    end
  end

  -- No Silver o arquivo ainda nao existe, e `catalog` devolve {} em silencio:
  -- a POKeDEX sai em ingles, como saia no Gold antes da 0.47.0, e nada quebra.
  local dex = catalog(jogo == "silver" and "pokedex_silver" or "pokedex")
  if mod.content.pokedex then
    local dexOk, dexErro = 0, nil
    for id, entrada in pairs(dex) do
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

  -- As mesmas medidas, pelo caminho do Gen2Recomped.  La a POKéDEX nao tem
  -- registro proprio: categoria, altura e peso moram no campo `dexEntry` do
  -- registro `pokemon`, e a altura vem repartida em dois numeros em vez do
  -- inteiro unico do gen1recomp -- `heightFt` e `heightIn`, que aqui levam
  -- metro e decimo de metro.  A virgula e a unidade nao saem daqui: a tela
  -- monta a linha com Strings("%2d′%02d″", ...) e Strings("%4d.%dlb", ...),
  -- entao quem troca pe por metro e libra por quilo e lang/strings.lua.
  --
  -- No gen1recomp o campo `dexEntry` nao existe no esquema do Gen 2
  -- (gen2Fields, src/mods/Schemas.lua): a chave passa como campo extra,
  -- ninguem a le e fica inerte -- mesmo arranjo dos dois catalogos de
  -- dialogo.  Dentro de pcall como os outros: com `api = 2` um registro
  -- recusado derrubaria o mod inteiro.
  local medidas = 0
  if mod.content.pokemon then
    local medErro = nil
    for id, entrada in pairs(dex) do
      if type(entrada) == "table" and entrada.height and entrada.weight then
        local ok, err = pcall(function()
          mod.content.pokemon:patch(id, {
            dexEntry = {
              heightFt = math.floor(entrada.height / 100),
              heightIn = entrada.height % 100,
              weight = entrada.weight,
            },
          })
        end)
        if ok then medidas = medidas + 1 elseif not medErro then medErro = err end
      end
    end
    if medErro then
      mod.log:warn("medida metrica nao aplicada: %s", tostring(medErro))
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
    mod.log:info("VersaoDourada: %d textos aplicados, %d medidas metricas"
      .. " (jogo: %s, golpes: %s, itens: %s)", n, medidas,
      jogo or "nao identificado", idioma.golpes, idioma.itens)
  end)
end

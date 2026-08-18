-- Nomes de tipo.  Chave = id do registro type_chart.
--
-- `TypeChart.displayName` (src/battle/TypeChart.lua:30) le `record.name` da
-- tabela `data.type_chart.types`, e o registro `type_chart` (Schemas.lua:1246)
-- aceita `name` -- entao o mod alcanca.  Aparece no resumo do POKéMON, no
-- painel de tipo do golpe e na POKéDEX.
--
-- OITO COLUNAS: e o tamanho do maior nome em ingles (ELECTRIC, FIGHTING),
-- entao o que couber em 8 cabe onde o original cabia.
--
-- A roda de tipos da tela de BUSCA da POKéDEX NAO passa por aqui: ela tem
-- lista propria (`PokedexMenu.SEARCH_TYPES`), usada tambem como valor de
-- filtro.  Traduzir aquela tabela exigiria separar rotulo de id no motor --
-- fica para uma passada com medicao, nao entra nesta.
--
-- BIRD e CURSE_TYPE sao tipos internos que o jogo nao mostra; ficam de fora.
return {
  ["NORMAL"] = "NORMAL",
  ["FIGHTING"] = "LUTADOR",
  ["FLYING"] = "VOADOR",
  ["POISON"] = "VENENO",
  ["GROUND"] = "TERRA",
  ["ROCK"] = "PEDRA",
  ["BUG"] = "INSETO",
  ["GHOST"] = "FANTASMA",
  ["STEEL"] = "AÇO",
  ["FIRE"] = "FOGO",
  ["WATER"] = "ÁGUA",
  ["GRASS"] = "PLANTA",
  ["ELECTRIC"] = "ELÉTRICO",
  ["PSYCHIC_TYPE"] = "PSÍQUICO",
  ["ICE"] = "GELO",
  ["DRAGON"] = "DRAGÃO",
  ["DARK"] = "SOMBRIO",
}

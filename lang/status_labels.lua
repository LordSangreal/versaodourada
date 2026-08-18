-- Rotulos de status.  Chave = id do registro gen2Statuses
-- (src/battle/gen2/Battle.lua:2800+: sleep, poison, paralyze, burn, freeze).
--
-- TRES CARACTERES.  E o que a caixa comporta: a tela POKéMON desenha o status
-- em `Chrome.print(row.status, 5, dataY)` com o nivel na coluna 8
-- (src/ui/gen2/PartyMenu.lua:760), entao sobram 3 colunas -- o mesmo espaco
-- que segurava SLP/PSN no original.  O HUD da batalha e mais folgado
-- (BattleState.lua:5823 desenha em x=120, 5 colunas), mas quem manda e a
-- menor das duas.
--
-- O TCG e o Pokemon GO escrevem por extenso ("Envenenado", "Queimado"), entao
-- a sigla e nossa.  A regra e derivar do SUBSTANTIVO, nao do adjetivo: as
-- tres primeiras letras do adjetivo davam "QUE" e "CON", que sao palavras
-- comuns em portugues e, ao lado da barra de vida, liam como conjuncao.
-- Sono -> SON, veneno -> VEN, gelo -> GEL.  "QMD" e a excecao feia: nenhuma
-- forma de "queimadura" cabe em tres letras sem virar outra palavra.
--
-- ATENCAO: este arquivo e INERTE no Gold.  As telas do gen1recomp nao leem o
-- registro `statuses` -- cada uma tem tabela propria (STATUS_STRING em
-- PartyMenu/SummaryMenu, STATUS_TAGS em BattleState).  No Gold quem manda sao
-- as chaves SLP/PSN/BRN/FRZ/PAR/FNT do lang/strings.lua.  Aqui fica pelo
-- Gen2Recomped, que usa o registro.
return {
  ["burn"] = "QMD",
  ["freeze"] = "GEL",
  ["paralyze"] = "PAR",
  ["poison"] = "VEN",
  ["sleep"] = "SON",
  ["toxic"] = "VEN",
}

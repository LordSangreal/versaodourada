-- Nome de CLASSE de treinador.  Chave = id da classe
-- (o `trainers` do cache gerado, tabela `classes`).
--
-- E o que a tela de batalha junta com o nome proprio para formar
-- "BUG CATCHER BENNY": `World:startScriptedBattle` monta
-- `className .. " " .. name` (src/world/gen2/World.lua), e `className` vem do
-- campo `name` do registro `trainers`.  Nao passa por Strings() em lugar
-- nenhum -- traduzir no strings.lua nao alcanca.
--
-- 66 classes, 41 nomes distintos: os oito lideres de ginasio compartilham
-- "LEADER", os quatro da Elite compartilham "ELITE FOUR", e os quatro Rocket
-- compartilham "ROCKET".  Cada id leva o seu, porque o registro e por id.
--
-- LARGURA: a caixa quebra sozinha (`TextBox.paginate` corta na ultima folga
-- que couber no orcamento de pixels), entao nome longo nao estoura -- vira
-- linha a mais.  Mesmo assim vale ficar perto do ingles: o proprio cartucho
-- ja passa de 18 com "<PK><MN> TRAINER RED" (20), e cada linha extra empurra
-- o resto da fala.
--
-- Nome proprio fica em ingles (regra do projeto): ROCKET e time, RIVAL e
-- papel.  `<PK><MN>` sao duas sequencias do charmap da ROM, mantidas como
-- estao; em portugues o substantivo vem antes.
return {
  ["BEAUTY"] = "BELDADE",
  ["BIKER"] = "MOTOQUEIRO",
  ["BIRD_KEEPER"] = "CRIADOR AVES",
  ["BLACKBELT_T"] = "FAIXA PRETA",
  ["BLAINE"] = "LÍDER",
  ["BLUE"] = "LÍDER",
  ["BOARDER"] = "SNOWBOARD",
  ["BROCK"] = "LÍDER",
  ["BRUNO"] = "ELITE DOS 4",
  ["BUGSY"] = "LÍDER",
  ["BUG_CATCHER"] = "CAÇA-INSETOS",
  ["BURGLAR"] = "LADRÃO",
  ["CAL"] = "TREINADOR <PK><MN>",
  ["CAMPER"] = "CAMPISTA",
  ["CHAMPION"] = "CAMPEÃO",
  ["CHUCK"] = "LÍDER",
  ["CLAIR"] = "LÍDER",
  ["COOLTRAINERF"] = "TREINADOR ÁS",
  ["COOLTRAINERM"] = "TREINADOR ÁS",
  ["ERIKA"] = "LÍDER",
  ["EXECUTIVEF"] = "ROCKET",
  ["EXECUTIVEM"] = "ROCKET",
  ["FALKNER"] = "LÍDER",
  ["FIREBREATHER"] = "CUSPE-FOGO",
  ["FISHER"] = "PESCADOR",
  ["GENTLEMAN"] = "CAVALHEIRO",
  ["GRUNTF"] = "ROCKET",
  ["GRUNTM"] = "ROCKET",
  ["GUITARIST"] = "ROQUEIRO",
  ["HIKER"] = "ALPINISTA",
  ["JANINE"] = "LÍDER",
  ["JASMINE"] = "LÍDER",
  ["JUGGLER"] = "MALABARISTA",
  ["KAREN"] = "ELITE DOS 4",
  ["KIMONO_GIRL"] = "MOÇA QUIMONO",
  ["KOGA"] = "ELITE DOS 4",
  ["LASS"] = "GAROTA",
  ["LT_SURGE"] = "LÍDER",
  ["MEDIUM"] = "MÉDIUM",
  ["MISTY"] = "LÍDER",
  ["MORTY"] = "LÍDER",
  ["OFFICER"] = "POLICIAL",
  ["PICNICKER"] = "PIQUENIQUE",
  ["POKEFANF"] = "POKéFÃ",
  ["POKEFANM"] = "POKéFÃ",
  ["POKEMANIAC"] = "POKéMANÍACO",
  ["POKEMON_PROF"] = "PROF. POKéMON",
  ["PRYCE"] = "LÍDER",
  ["PSYCHIC_T"] = "PSÍQUICO",
  ["RED"] = "TREINADOR <PK><MN>",
  ["RIVAL1"] = "RIVAL",
  ["RIVAL2"] = "RIVAL",
  ["SABRINA"] = "LÍDER",
  ["SAGE"] = "SÁBIO",
  ["SAILOR"] = "MARINHEIRO",
  ["SCHOOLBOY"] = "ESTUDANTE",
  ["SCIENTIST"] = "CIENTISTA",
  ["SKIER"] = "ESQUIADOR",
  ["SUPER_NERD"] = "SUPERNERD",
  ["SWIMMERF"] = "NADADORA♀",
  ["SWIMMERM"] = "NADADOR♂",
  ["TEACHER"] = "PROFESSORA",
  ["TWINS"] = "GÊMEAS",
  ["WHITNEY"] = "LÍDER",
  ["WILL"] = "ELITE DOS 4",
  ["YOUNGSTER"] = "GAROTO",
}

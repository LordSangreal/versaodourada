-- Entradas da POKéDEX.  Chave = id da especie.  251 de 251.
--
-- `kind` e a categoria impressa acima da entrada; `text` e `text2` sao as
-- duas telas da descricao, e `<NEXT>` e a quebra de LINHA dentro de cada uma
-- (tres linhas por tela, ~18 colunas).  A contagem de <NEXT> tem de bater com
-- a do ingles: e ela que monta a tela.
--
-- `height` e `weight` sao as medidas em METRO e QUILO, no lugar do pe,
-- polegada e libra do cartucho americano.  A forma do numero e a mesma que o
-- cartucho usa, porque e ela que a tela reparte em duas metades: `height` e
-- metro * 100 + decimo (902 = 9,2 m), no encaixe do pe * 100 + polegada, e
-- `weight` e o decimo de quilo (4600 = 460,0 kg), no do decimo de libra.  As
-- virgulas e as unidades vem do catalogo de texto -- ver lang/strings.lua.
--
-- O numero NAO sai de converter o que o cartucho guarda.  A altura ate
-- sobreviveria (a polegada e mais fina que o decimo de metro, e as 251
-- batem), mas o peso nao: o cartucho arredondou 6,9 kg para 15 libras
-- redondas, e a volta da 6,8 kg -- 196 das 251 erradas por um decimo.  A
-- fonte e a tabela canonica da franquia; ver ferramentas/dex_medidas.py.
--
-- SO FUNCIONA em motor com a rota `pokedex` no registro (Schemas.GEN2).  No
-- gen1recomp de hoje `data.gen2Pokedex` e um loadGenerated cru e nada faz
-- merge nele, entao `main.lua` so aplica se `mod.content.pokedex` existir --
-- num motor sem a rota este arquivo fica inerte, sem quebrar nada.  No
-- Gen2Recomped as medidas chegam por outro caminho (o registro `pokemon`,
-- campo `dexEntry`), montado no proprio main.lua a partir destes numeros.
--
-- A ROM brasileira tambem nao traduziu a POKeDEX: o texto e escrita do zero.
return {
  ["ABRA"] = {
    kind = "PSI",
    text = "Ele sente ataques<NEXT>que estão para<NEXT>vir e usa",
    text2 = "TELEPORTE para se<NEXT>salvar antes que<NEXT>eles cheguem.",
    height = 9, weight = 195,   -- 0,9 m / 19,5 kg
  },
  ["AERODACTYL"] = {
    kind = "FÓSSIL",
    text = "POKéMON feroz de<NEXT>um passado bem<NEXT>distante, parece",
    text2 = "que ele voava<NEXT>abrindo as asas e<NEXT>planando.",
    height = 108, weight = 590,   -- 1,8 m / 59,0 kg
  },
  ["AIPOM"] = {
    kind = "RABO LONGO",
    text = "O rabo dele é tão<NEXT>forte que ele o<NEXT>usa para agarrar",
    text2 = "um galho e se<NEXT>segurar pendurado<NEXT>lá no ar.",
    height = 8, weight = 115,   -- 0,8 m / 11,5 kg
  },
  ["ALAKAZAM"] = {
    kind = "PSI",
    text = "Fechar os dois<NEXT>olhos aguça todos<NEXT>os outros sentidos",
    text2 = "dele. Isso deixa<NEXT>ele usar tudo que<NEXT>tem ao extremo.",
    height = 105, weight = 480,   -- 1,5 m / 48,0 kg
  },
  ["AMPHAROS"] = {
    kind = "LUZ",
    text = "A ponta do rabo<NEXT>brilha muito e<NEXT>pode ser vista",
    text2 = "de bem longe. Ela<NEXT>serve de farol<NEXT>para os perdidos.",
    height = 104, weight = 615,   -- 1,4 m / 61,5 kg
  },
  ["ARBOK"] = {
    kind = "NAJA",
    text = "Ele paralisa a<NEXT>presa com o<NEXT>desenho de rosto",
    text2 = "na barriga, e<NEXT>então prende e<NEXT>envenena ela.",
    height = 305, weight = 650,   -- 3,5 m / 65,0 kg
  },
  ["ARCANINE"] = {
    kind = "LENDÁRIO",
    text = "Este POKéMON<NEXT>lendário da China<NEXT>é tido como",
    text2 = "magnífico. Muitos<NEXT>se encantam com a<NEXT>grande juba dele.",
    height = 109, weight = 1550,   -- 1,9 m / 155,0 kg
  },
  ["ARIADOS"] = {
    kind = "PERNALONGA",
    text = "Ele solta fio não<NEXT>só de trás como<NEXT>também da boca.",
    text2 = "É difícil dizer<NEXT>qual ponta é qual<NEXT>nele.",
    height = 101, weight = 335,   -- 1,1 m / 33,5 kg
  },
  ["ARTICUNO"] = {
    kind = "GELO",
    text = "As asas magníficas<NEXT>e quase<NEXT>transparentes",
    text2 = "desta ave lendária<NEXT>seriam feitas<NEXT>de gelo, dizem.",
    height = 107, weight = 554,   -- 1,7 m / 55,4 kg
  },
  ["AZUMARILL"] = {
    kind = "COELHOÁGUA",
    text = "Ficando parado e<NEXT>ouvindo com<NEXT>atenção, ele sabe",
    text2 = "o que há até<NEXT>em rios bravos e<NEXT>de água veloz.",
    height = 8, weight = 285,   -- 0,8 m / 28,5 kg
  },
  ["BAYLEEF"] = {
    kind = "FOLHA",
    text = "O cheiro de<NEXT>temperos vem da<NEXT>região do pescoço.",
    text2 = "De algum jeito,<NEXT>cheirar aquilo dá<NEXT>vontade de lutar.",
    height = 102, weight = 158,   -- 1,2 m / 15,8 kg
  },
  ["BEEDRILL"] = {
    kind = "ABELHA",
    text = "Ele derruba<NEXT>qualquer rival com<NEXT>os ferrões",
    text2 = "venenosos fortes.<NEXT>Às vezes ataca<NEXT>em enxame.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["BELLOSSOM"] = {
    kind = "FLOR",
    text = "BELLOSSOM se<NEXT>juntam às vezes e<NEXT>parecem dançar.",
    text2 = "Dizem que a dança<NEXT>é um ritual para<NEXT>chamar o sol.",
    height = 4, weight = 58,   -- 0,4 m / 5,8 kg
  },
  ["BELLSPROUT"] = {
    kind = "FLOR",
    text = "Mesmo com o corpo<NEXT>muito magrelo, ele<NEXT>é rápido de cegar",
    text2 = "na hora em que<NEXT>vai pegar a presa<NEXT>dele.",
    height = 7, weight = 40,   -- 0,7 m / 4,0 kg
  },
  ["BLASTOISE"] = {
    kind = "MARISCO",
    text = "Ele fica pesado<NEXT>de propósito para<NEXT>aguentar o recuo",
    text2 = "dos jatos de<NEXT>água que ele<NEXT>dispara.",
    height = 106, weight = 855,   -- 1,6 m / 85,5 kg
  },
  ["BLISSEY"] = {
    kind = "FELICIDADE",
    text = "Quem dá uma<NEXT>mordida que seja<NEXT>no ovo de BLISSEY",
    text2 = "vira uma pessoa<NEXT>carinhosa e<NEXT>gentil com todos.",
    height = 105, weight = 468,   -- 1,5 m / 46,8 kg
  },
  ["BULBASAUR"] = {
    kind = "SEMENTE",
    text = "A semente nas<NEXT>costas dele é<NEXT>cheia de",
    text2 = "nutrientes. Ela<NEXT>cresce junto com<NEXT>o corpo dele.",
    height = 7, weight = 69,   -- 0,7 m / 6,9 kg
  },
  ["BUTTERFREE"] = {
    kind = "BORBOLETA",
    text = "Ele colhe mel<NEXT>todo dia. Esfrega<NEXT>o mel nos pelos",
    text2 = "das pernas para<NEXT>levar tudo de<NEXT>volta ao ninho.",
    height = 101, weight = 320,   -- 1,1 m / 32,0 kg
  },
  ["CATERPIE"] = {
    kind = "LAGARTA",
    text = "Para se proteger,<NEXT>solta um cheiro<NEXT>horrível da",
    text2 = "antena da cabeça<NEXT>para espantar os<NEXT>inimigos.",
    height = 3, weight = 29,   -- 0,3 m / 2,9 kg
  },
  ["CELEBI"] = {
    kind = "VIAJATEMPO",
    text = "Este POKéMON anda<NEXT>através do tempo.<NEXT>Mato e árvores",
    text2 = "florescem nas<NEXT>matas em que ele<NEXT>apareceu.",
    height = 6, weight = 50,   -- 0,6 m / 5,0 kg
  },
  ["CHANSEY"] = {
    kind = "OVO",
    text = "Ela anda com<NEXT>cuidado para não<NEXT>quebrar o ovo.",
    text2 = "Mesmo assim, é<NEXT>extremamente<NEXT>rápida para fugir.",
    height = 101, weight = 346,   -- 1,1 m / 34,6 kg
  },
  ["CHARIZARD"] = {
    kind = "CHAMA",
    text = "Se CHARIZARD fica<NEXT>furioso, a chama<NEXT>na ponta do rabo",
    text2 = "dele arde numa<NEXT>cor azulada bem<NEXT>esbranquiçada.",
    height = 107, weight = 905,   -- 1,7 m / 90,5 kg
  },
  ["CHARMANDER"] = {
    kind = "LAGARTO",
    text = "A chama do rabo<NEXT>dele mostra a<NEXT>força da vida",
    text2 = "dele. Se estiver<NEXT>fraco, a chama<NEXT>queima fraca.",
    height = 6, weight = 85,   -- 0,6 m / 8,5 kg
  },
  ["CHARMELEON"] = {
    kind = "CHAMA",
    text = "Ele é esquentado<NEXT>por natureza, e<NEXT>por isso procura",
    text2 = "rivais o tempo<NEXT>todo. Só se acalma<NEXT>quando vence.",
    height = 101, weight = 190,   -- 1,1 m / 19,0 kg
  },
  ["CHIKORITA"] = {
    kind = "FOLHA",
    text = "Um aroma doce sai<NEXT>de leve da folha<NEXT>da cabeça dele.",
    text2 = "É dócil e adora<NEXT>se banhar nos<NEXT>raios do sol.",
    height = 9, weight = 64,   -- 0,9 m / 6,4 kg
  },
  ["CHINCHOU"] = {
    kind = "PESCADOR",
    text = "Ele dispara carga<NEXT>positiva e carga<NEXT>negativa entre as",
    text2 = "pontas das duas<NEXT>antenas dele e dá<NEXT>choque no inimigo.",
    height = 5, weight = 120,   -- 0,5 m / 12,0 kg
  },
  ["CLEFABLE"] = {
    kind = "FADA",
    text = "Com a audição<NEXT>afiada, ele capta<NEXT>sons que vêm de",
    text2 = "bem longe. Costuma<NEXT>se esconder em<NEXT>lugares quietos.",
    height = 103, weight = 400,   -- 1,3 m / 40,0 kg
  },
  ["CLEFAIRY"] = {
    kind = "FADA",
    text = "A luz da lua que<NEXT>ele guarda nas<NEXT>asas das costas",
    text2 = "parece dar a ele<NEXT>o poder de flutuar<NEXT>no ar.",
    height = 6, weight = 75,   -- 0,6 m / 7,5 kg
  },
  ["CLEFFA"] = {
    kind = "ESTRELA",
    text = "Por causa da<NEXT>silhueta esquisita<NEXT>de estrela dele,",
    text2 = "as pessoas creem<NEXT>que ele veio para<NEXT>cá num meteoro.",
    height = 3, weight = 30,   -- 0,3 m / 3,0 kg
  },
  ["CLOYSTER"] = {
    kind = "BIVALVE",
    text = "Depois que fecha a<NEXT>concha com força,<NEXT>é impossível",
    text2 = "abrir, mesmo para<NEXT>quem tem força<NEXT>acima do normal.",
    height = 105, weight = 1325,   -- 1,5 m / 132,5 kg
  },
  ["CORSOLA"] = {
    kind = "CORAL",
    text = "Ele solta e cresce<NEXT>sem parar. A ponta<NEXT>da cabeça dele é",
    text2 = "valorizada como<NEXT>tesouro pela<NEXT>beleza dela.",
    height = 6, weight = 50,   -- 0,6 m / 5,0 kg
  },
  ["CROBAT"] = {
    kind = "MORCEGO",
    text = "Ele voa tão em<NEXT>silêncio pelo<NEXT>escuro com as",
    text2 = "quatro asas que<NEXT>pode nem ser<NEXT>notado bem perto.",
    height = 108, weight = 750,   -- 1,8 m / 75,0 kg
  },
  ["CROCONAW"] = {
    kind = "MANDÍBULA",
    text = "Se ele perde uma<NEXT>presa, outra nasce<NEXT>no lugar dela.",
    text2 = "Sempre há 48<NEXT>presas na boca<NEXT>dele.",
    height = 101, weight = 250,   -- 1,1 m / 25,0 kg
  },
  ["CUBONE"] = {
    kind = "SOLITÁRIO",
    text = "Se fica triste ou<NEXT>sozinho, o crânio<NEXT>que ele usa treme",
    text2 = "e solta um som<NEXT>chorão e cheio<NEXT>de tristeza.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["CYNDAQUIL"] = {
    kind = "RATO FOGO",
    text = "Ele é tímido e<NEXT>sempre se enrola<NEXT>como uma bolinha.",
    text2 = "Se for atacado,<NEXT>acende as costas<NEXT>para se proteger.",
    height = 5, weight = 79,   -- 0,5 m / 7,9 kg
  },
  ["DELIBIRD"] = {
    kind = "ENTREGA",
    text = "Ele carrega comida<NEXT>o dia inteiro. Há<NEXT>histórias sobre",
    text2 = "gente perdida que<NEXT>foi salva pela<NEXT>comida dele.",
    height = 9, weight = 160,   -- 0,9 m / 16,0 kg
  },
  ["DEWGONG"] = {
    kind = "FOCA",
    text = "O corpo liso dele<NEXT>quase não tem<NEXT>atrito na água.",
    text2 = "Quanto mais fria<NEXT>a temperatura,<NEXT>mais animado fica.",
    height = 107, weight = 1200,   -- 1,7 m / 120,0 kg
  },
  ["DIGLETT"] = {
    kind = "TOUPEIRA",
    text = "A pele dele é bem<NEXT>fina. Se ficar<NEXT>exposto à luz, o",
    text2 = "sangue esquenta e<NEXT>isso faz ele<NEXT>ficar fraco.",
    height = 2, weight = 8,   -- 0,2 m / 0,8 kg
  },
  ["DITTO"] = {
    kind = "TRANSFORMA",
    text = "Ele pode virar<NEXT>qualquer coisa.<NEXT>Quando dorme, vira",
    text2 = "uma pedra para<NEXT>não ser<NEXT>atacado.",
    height = 3, weight = 40,   -- 0,3 m / 4,0 kg
  },
  ["DODRIO"] = {
    kind = "AVE TRIPLA",
    text = "Ele junta dados e<NEXT>planeja com três<NEXT>vezes mais juízo,",
    text2 = "mas pode pensar<NEXT>demais e acabar<NEXT>sem se mexer.",
    height = 108, weight = 852,   -- 1,8 m / 85,2 kg
  },
  ["DODUO"] = {
    kind = "AVE GÊMEA",
    text = "Levantando e<NEXT>baixando as duas<NEXT>cabeças na vez",
    text2 = "certa, ele se<NEXT>equilibra melhor<NEXT>quando corre.",
    height = 104, weight = 392,   -- 1,4 m / 39,2 kg
  },
  ["DONPHAN"] = {
    kind = "ARMADURA",
    text = "Ele tem presas<NEXT>duras e afiadas e<NEXT>couro grosso. A",
    text2 = "INVESTIDA dele<NEXT>tem força para<NEXT>derrubar uma casa.",
    height = 101, weight = 1200,   -- 1,1 m / 120,0 kg
  },
  ["DRAGONAIR"] = {
    kind = "DRAGÃO",
    text = "Dizem que se ele<NEXT>solta uma aura do<NEXT>corpo inteiro, o",
    text2 = "tempo começa a<NEXT>mudar na mesma<NEXT>hora.",
    height = 400, weight = 165,   -- 4,0 m / 16,5 kg
  },
  ["DRAGONITE"] = {
    kind = "DRAGÃO",
    text = "Dizem que este<NEXT>POKéMON voa sem<NEXT>parar sobre mares",
    text2 = "imensos e salva<NEXT>as pessoas que<NEXT>estão se afogando.",
    height = 202, weight = 2100,   -- 2,2 m / 210,0 kg
  },
  ["DRATINI"] = {
    kind = "DRAGÃO",
    text = "Ele já nasce<NEXT>grande. Troca de<NEXT>pele muitas vezes",
    text2 = "enquanto vai<NEXT>ficando cada vez<NEXT>mais comprido.",
    height = 108, weight = 33,   -- 1,8 m / 3,3 kg
  },
  ["DROWZEE"] = {
    kind = "HIPNOSE",
    text = "Se você acha que<NEXT>teve um bom sonho<NEXT>mas não consegue",
    text2 = "lembrar dele, um<NEXT>DROWZEE deve ter<NEXT>comido o sonho.",
    height = 100, weight = 324,   -- 1,0 m / 32,4 kg
  },
  ["DUGTRIO"] = {
    kind = "TOUPEIRA",
    text = "As três cabeças<NEXT>sobem e descem<NEXT>separadas para",
    text2 = "soltar a terra em<NEXT>volta e facilitar<NEXT>a escavação.",
    height = 7, weight = 333,   -- 0,7 m / 33,3 kg
  },
  ["DUNSPARCE"] = {
    kind = "COBRATERRA",
    text = "Quando é visto,<NEXT>este POKéMON foge<NEXT>de ré cavando com",
    text2 = "fúria o chão<NEXT>usando o rabo<NEXT>dele.",
    height = 105, weight = 140,   -- 1,5 m / 14,0 kg
  },
  ["EEVEE"] = {
    kind = "EVOLUÇÃO",
    text = "Ele tem o poder<NEXT>de mudar a<NEXT>composição do",
    text2 = "corpo para se<NEXT>adaptar ao<NEXT>ambiente em volta.",
    height = 3, weight = 65,   -- 0,3 m / 6,5 kg
  },
  ["EKANS"] = {
    kind = "COBRA",
    text = "Ele solta a<NEXT>própria mandíbula<NEXT>para engolir",
    text2 = "presas inteiras.<NEXT>Mas pode ficar<NEXT>pesado demais.",
    height = 200, weight = 69,   -- 2,0 m / 6,9 kg
  },
  ["ELECTABUZZ"] = {
    kind = "ELÉTRICO",
    text = "Eletricidade<NEXT>corre pela<NEXT>superfície do",
    text2 = "corpo dele. No<NEXT>escuro, o corpo<NEXT>todo brilha azul.",
    height = 101, weight = 300,   -- 1,1 m / 30,0 kg
  },
  ["ELECTRODE"] = {
    kind = "BOLA",
    text = "Ele é perigoso. Se<NEXT>tiver eletricidade<NEXT>demais e nada para",
    text2 = "fazer, se diverte<NEXT>explodindo do<NEXT>nada.",
    height = 102, weight = 666,   -- 1,2 m / 66,6 kg
  },
  ["ELEKID"] = {
    kind = "ELÉTRICO",
    text = "Ele gira os braços<NEXT>para gerar<NEXT>eletricidade, mas",
    text2 = "cansa fácil, e por<NEXT>isso carrega só<NEXT>um pouquinho.",
    height = 6, weight = 235,   -- 0,6 m / 23,5 kg
  },
  ["ENTEI"] = {
    kind = "VULCÃO",
    text = "Vulcões entram em<NEXT>erupção quando ele<NEXT>late. Sem conter",
    text2 = "o poder extremo<NEXT>dele, corre a toda<NEXT>pela terra.",
    height = 201, weight = 1980,   -- 2,1 m / 198,0 kg
  },
  ["ESPEON"] = {
    kind = "SOL",
    text = "Ele usa os pelos<NEXT>finos que cobrem<NEXT>o corpo dele para",
    text2 = "sentir o ar e<NEXT>prever o que o<NEXT>inimigo vai fazer.",
    height = 9, weight = 265,   -- 0,9 m / 26,5 kg
  },
  ["EXEGGCUTE"] = {
    kind = "OVO",
    text = "A casca é bem<NEXT>resistente. Mesmo<NEXT>que rache, ele",
    text2 = "sobrevive sem<NEXT>derramar o que<NEXT>tem dentro.",
    height = 4, weight = 25,   -- 0,4 m / 2,5 kg
  },
  ["EXEGGUTOR"] = {
    kind = "COCO",
    text = "As três cabeças<NEXT>pensam cada uma<NEXT>por si. Mesmo",
    text2 = "assim, são amigas<NEXT>e nunca parecem<NEXT>brigar.",
    height = 200, weight = 1200,   -- 2,0 m / 120,0 kg
  },
  ["FARFETCH_D"] = {
    kind = "PATO BRAVO",
    text = "Se alguém tenta<NEXT>mexer no lugar<NEXT>onde nascem os",
    text2 = "talos que ele usa,<NEXT>ele usa o próprio<NEXT>talo para impedir.",
    height = 8, weight = 150,   -- 0,8 m / 15,0 kg
  },
  ["FEAROW"] = {
    kind = "BICO",
    text = "Ele sobe de<NEXT>repente bem alto<NEXT>no céu e então",
    text2 = "despenca de uma<NEXT>só vez para<NEXT>atingir a presa.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["FERALIGATR"] = {
    kind = "MANDÍBULA",
    text = "Quando morde com<NEXT>as mandíbulas<NEXT>enormes e fortes,",
    text2 = "ele sacode a<NEXT>cabeça e rasga a<NEXT>vítima com fúria.",
    height = 203, weight = 888,   -- 2,3 m / 88,8 kg
  },
  ["FLAAFFY"] = {
    kind = "LÃ",
    text = "De tanto guardar<NEXT>eletricidade<NEXT>demais, ele criou",
    text2 = "manchas onde nem<NEXT>a lã mais fininha<NEXT>cresce.",
    height = 8, weight = 133,   -- 0,8 m / 13,3 kg
  },
  ["FLAREON"] = {
    kind = "CHAMA",
    text = "Ele guarda parte<NEXT>do ar que respira<NEXT>na bolsa de fogo",
    text2 = "de dentro dele,<NEXT>que esquenta o ar<NEXT>a 3.000 graus.",
    height = 9, weight = 250,   -- 0,9 m / 25,0 kg
  },
  ["FORRETRESS"] = {
    kind = "BICHO-SACO",
    text = "O corpo inteiro<NEXT>dele é protegido<NEXT>por uma casca",
    text2 = "dura como aço. O<NEXT>que há dentro da<NEXT>armadura é enigma.",
    height = 102, weight = 1258,   -- 1,2 m / 125,8 kg
  },
  ["FURRET"] = {
    kind = "CORPOLONGO",
    text = "Ele faz um ninho<NEXT>que serve para o<NEXT>corpo longo e",
    text2 = "magro dele. Nenhum<NEXT>outro POKéMON<NEXT>consegue entrar.",
    height = 108, weight = 325,   -- 1,8 m / 32,5 kg
  },
  ["GASTLY"] = {
    kind = "GÁS",
    text = "Com o corpo feito<NEXT>de gás, ele entra<NEXT>escondido em",
    text2 = "qualquer lugar.<NEXT>Mas o vento pode<NEXT>levar ele embora.",
    height = 103, weight = 1,   -- 1,3 m / 0,1 kg
  },
  ["GENGAR"] = {
    kind = "SOMBRA",
    text = "Ele rouba o calor<NEXT>de tudo em volta.<NEXT>Se você sentir um",
    text2 = "frio de repente, é<NEXT>certeza que um<NEXT>GENGAR apareceu.",
    height = 105, weight = 405,   -- 1,5 m / 40,5 kg
  },
  ["GEODUDE"] = {
    kind = "PEDRA",
    text = "A maioria não<NEXT>repara, mas um<NEXT>olhar mais atento",
    text2 = "revela que há<NEXT>muitos GEODUDE<NEXT>por perto.",
    height = 4, weight = 200,   -- 0,4 m / 20,0 kg
  },
  ["GIRAFARIG"] = {
    kind = "PESCOÇUDO",
    text = "O rabo dele tem um<NEXT>cérebro pequeno<NEXT>próprio. Cuidado!",
    text2 = "Se você chegar<NEXT>perto, ele pode<NEXT>sentir e morder.",
    height = 105, weight = 415,   -- 1,5 m / 41,5 kg
  },
  ["GLIGAR"] = {
    kind = "ESCORPIÃO",
    text = "Ele voa direto na<NEXT>cara do alvo dele<NEXT>e então crava os",
    text2 = "ferrões na vítima<NEXT>assustada para<NEXT>injetar veneno.",
    height = 101, weight = 648,   -- 1,1 m / 64,8 kg
  },
  ["GLOOM"] = {
    kind = "ERVA",
    text = "O que parece baba<NEXT>é na verdade mel<NEXT>doce. É bem",
    text2 = "grudento e cola<NEXT>com teimosia se<NEXT>você encostar.",
    height = 8, weight = 86,   -- 0,8 m / 8,6 kg
  },
  ["GOLBAT"] = {
    kind = "MORCEGO",
    text = "Por mais dura que<NEXT>seja a pele da<NEXT>vítima, ele fura",
    text2 = "com presas afiadas<NEXT>e se empanturra<NEXT>de sangue.",
    height = 106, weight = 550,   -- 1,6 m / 55,0 kg
  },
  ["GOLDEEN"] = {
    kind = "PEIXE OURO",
    text = "As nadadeiras<NEXT>dorsal, peitoral e<NEXT>do rabo ondulam",
    text2 = "com elegância. Por<NEXT>isso ele é o<NEXT>dançarino da água.",
    height = 6, weight = 150,   -- 0,6 m / 15,0 kg
  },
  ["GOLDUCK"] = {
    kind = "PATO",
    text = "Quando nada a toda<NEXT>velocidade com os<NEXT>membros compridos",
    text2 = "e com membrana, a<NEXT>testa dele começa<NEXT>a brilhar.",
    height = 107, weight = 766,   -- 1,7 m / 76,6 kg
  },
  ["GOLEM"] = {
    kind = "MEGATON",
    text = "Ele troca de pele<NEXT>uma vez por ano.<NEXT>A casca jogada",
    text2 = "fora endurece na<NEXT>hora e se<NEXT>esfarela.",
    height = 104, weight = 3000,   -- 1,4 m / 300,0 kg
  },
  ["GRANBULL"] = {
    kind = "FADA",
    text = "Ele é na verdade<NEXT>tímido e medroso.<NEXT>Se for atacado,",
    text2 = "sacode os braços<NEXT>para afastar quem<NEXT>o atacou.",
    height = 104, weight = 487,   -- 1,4 m / 48,7 kg
  },
  ["GRAVELER"] = {
    kind = "PEDRA",
    text = "De natureza livre<NEXT>e despreocupada,<NEXT>ele não liga se",
    text2 = "pedaços se soltam<NEXT>enquanto rola<NEXT>montanha abaixo.",
    height = 100, weight = 1050,   -- 1,0 m / 105,0 kg
  },
  ["GRIMER"] = {
    kind = "LODO",
    text = "Conforme se move,<NEXT>ele perde pedaços<NEXT>do corpo, e deles",
    text2 = "surgem GRIMER<NEXT>novos. Isso piora<NEXT>o fedor em volta.",
    height = 9, weight = 300,   -- 0,9 m / 30,0 kg
  },
  ["GROWLITHE"] = {
    kind = "FILHOTE",
    text = "Ele tem natureza<NEXT>corajosa e leal.<NEXT>Enfrenta sem medo",
    text2 = "rivais maiores e<NEXT>mais fortes que<NEXT>ele.",
    height = 7, weight = 190,   -- 0,7 m / 19,0 kg
  },
  ["GYARADOS"] = {
    kind = "ATROZ",
    text = "Dizem que nas<NEXT>guerras do passado<NEXT>GYARADOS surgia e",
    text2 = "deixava ruínas<NEXT>em chamas por<NEXT>onde passava.",
    height = 605, weight = 2350,   -- 6,5 m / 235,0 kg
  },
  ["HAUNTER"] = {
    kind = "GÁS",
    text = "Na escuridão<NEXT>total, onde nada<NEXT>se vê, HAUNTER",
    text2 = "espreita, seguindo<NEXT>em silêncio a<NEXT>próxima vítima.",
    height = 106, weight = 1,   -- 1,6 m / 0,1 kg
  },
  ["HERACROSS"] = {
    kind = "UM CHIFRE",
    text = "Este POKéMON<NEXT>poderoso enfia o<NEXT>chifre valioso",
    text2 = "por baixo da<NEXT>barriga do inimigo<NEXT>e o joga longe.",
    height = 105, weight = 540,   -- 1,5 m / 54,0 kg
  },
  ["HITMONCHAN"] = {
    kind = "SOCO",
    text = "Os socos dele<NEXT>cortam o ar. Mas<NEXT>ele parece",
    text2 = "precisar de pausa<NEXT>depois de lutar<NEXT>por três minutos.",
    height = 104, weight = 502,   -- 1,4 m / 50,2 kg
  },
  ["HITMONLEE"] = {
    kind = "CHUTE",
    text = "Este POKéMON<NEXT>incrível tem um<NEXT>equilíbrio ótimo.",
    text2 = "Ele consegue<NEXT>chutar em série de<NEXT>qualquer posição.",
    height = 105, weight = 498,   -- 1,5 m / 49,8 kg
  },
  ["HITMONTOP"] = {
    kind = "BANANEIRA",
    text = "Se você se encanta<NEXT>com os chutes<NEXT>suaves, elegantes",
    text2 = "e dançantes dele,<NEXT>pode acabar<NEXT>furado com força.",
    height = 104, weight = 480,   -- 1,4 m / 48,0 kg
  },
  ["HOOTHOOT"] = {
    kind = "CORUJA",
    text = "Ele fica sempre<NEXT>num pé só. Troca<NEXT>de pé tão rápido",
    text2 = "que quase nunca<NEXT>dá para ver o<NEXT>movimento.",
    height = 7, weight = 212,   -- 0,7 m / 21,2 kg
  },
  ["HOPPIP"] = {
    kind = "ALGODÃO",
    text = "Para o vento não<NEXT>levar eles<NEXT>embora, se juntam",
    text2 = "em cachos. Mas<NEXT>gostam mesmo é de<NEXT>brisa suave.",
    height = 4, weight = 5,   -- 0,4 m / 0,5 kg
  },
  ["HORSEA"] = {
    kind = "DRAGÃO",
    text = "Se um inimigo<NEXT>maior o ataca, ele<NEXT>nada rápido para",
    text2 = "um lugar seguro<NEXT>controlando bem a<NEXT>nadadeira dorsal.",
    height = 4, weight = 80,   -- 0,4 m / 8,0 kg
  },
  ["HOUNDOOM"] = {
    kind = "SOMBRIO",
    text = "Se você se queimar<NEXT>nas chamas que ele<NEXT>dispara pela boca,",
    text2 = "a dor nunca<NEXT>mais vai<NEXT>embora.",
    height = 104, weight = 350,   -- 1,4 m / 35,0 kg
  },
  ["HOUNDOUR"] = {
    kind = "SOMBRIO",
    text = "Ele usa tipos<NEXT>diferentes de<NEXT>grito para falar",
    text2 = "com os outros da<NEXT>espécie dele e<NEXT>para caçar presas.",
    height = 6, weight = 108,   -- 0,6 m / 10,8 kg
  },
  ["HO_OH"] = {
    kind = "ARCO-ÍRIS",
    text = "Lendas dizem que<NEXT>este POKéMON voa<NEXT>pelos céus do",
    text2 = "mundo sem parar<NEXT>com as magníficas<NEXT>asas de 7 cores.",
    height = 308, weight = 1990,   -- 3,8 m / 199,0 kg
  },
  ["HYPNO"] = {
    kind = "HIPNOSE",
    text = "Quando está com<NEXT>muita fome, ele<NEXT>faz as pessoas",
    text2 = "dormirem e então<NEXT>se banqueteia com<NEXT>os sonhos delas.",
    height = 106, weight = 756,   -- 1,6 m / 75,6 kg
  },
  ["IGGLYBUFF"] = {
    kind = "BALÃO",
    text = "Ele tem o corpo<NEXT>bem macio. Se<NEXT>começar a rolar,",
    text2 = "vai quicar por<NEXT>toda parte e será<NEXT>impossível parar.",
    height = 3, weight = 10,   -- 0,3 m / 1,0 kg
  },
  ["IVYSAUR"] = {
    kind = "SEMENTE",
    text = "Tomar sol aumenta<NEXT>a força dele. O<NEXT>sol também faz",
    text2 = "o botão nas<NEXT>costas dele<NEXT>crescer mais.",
    height = 100, weight = 130,   -- 1,0 m / 13,0 kg
  },
  ["JIGGLYPUFF"] = {
    kind = "BALÃO",
    text = "Se ele se enche<NEXT>para usar CANÇÃO<NEXT>de ninar, canta",
    text2 = "por mais tempo e<NEXT>dá sono na certa<NEXT>em quem escuta.",
    height = 5, weight = 55,   -- 0,5 m / 5,5 kg
  },
  ["JOLTEON"] = {
    kind = "RAIO",
    text = "Ele concentra as<NEXT>cargas elétricas<NEXT>fracas soltadas",
    text2 = "pelas células e<NEXT>dispara raios<NEXT>cruéis.",
    height = 8, weight = 245,   -- 0,8 m / 24,5 kg
  },
  ["JUMPLUFF"] = {
    kind = "ALGODÃO",
    text = "Assim que pega o<NEXT>vento, ele<NEXT>controla bem os",
    text2 = "esporos de algodão<NEXT>e flutua até<NEXT>em volta do mundo.",
    height = 8, weight = 30,   -- 0,8 m / 3,0 kg
  },
  ["JYNX"] = {
    kind = "HUMANOIDE",
    text = "Ele balança o<NEXT>corpo no ritmo.<NEXT>Parece mudar o",
    text2 = "ritmo conforme o<NEXT>jeito que está<NEXT>se sentindo.",
    height = 104, weight = 406,   -- 1,4 m / 40,6 kg
  },
  ["KABUTO"] = {
    kind = "MARISCO",
    text = "Em raras ocasiões,<NEXT>alguns foram<NEXT>achados virados",
    text2 = "em fóssil no fundo<NEXT>do mar, onde se<NEXT>escondiam.",
    height = 5, weight = 115,   -- 0,5 m / 11,5 kg
  },
  ["KABUTOPS"] = {
    kind = "MARISCO",
    text = "Na água, ele<NEXT>recolhe os membros<NEXT>para ficar mais",
    text2 = "compacto, e então<NEXT>sacode a concha<NEXT>para nadar rápido.",
    height = 103, weight = 405,   -- 1,3 m / 40,5 kg
  },
  ["KADABRA"] = {
    kind = "PSI",
    text = "Ele tem um forte<NEXT>poder espiritual.<NEXT>Quanto mais",
    text2 = "perigo enfrenta,<NEXT>mais forte fica o<NEXT>poder psíquico.",
    height = 103, weight = 565,   -- 1,3 m / 56,5 kg
  },
  ["KAKUNA"] = {
    kind = "CASULO",
    text = "Mesmo sendo um<NEXT>casulo, ele se<NEXT>mexe um pouco. Se",
    text2 = "for atacado, põe<NEXT>para fora o<NEXT>espinho venenoso.",
    height = 6, weight = 100,   -- 0,6 m / 10,0 kg
  },
  ["KANGASKHAN"] = {
    kind = "MÃE",
    text = "Se o lugar é<NEXT>seguro, o filhote<NEXT>sai da bolsa da",
    text2 = "barriga e brinca.<NEXT>A adulta vigia<NEXT>ele bem de perto.",
    height = 202, weight = 800,   -- 2,2 m / 80,0 kg
  },
  ["KINGDRA"] = {
    kind = "DRAGÃO",
    text = "Dizem que ele<NEXT>vive escondido em<NEXT>grutas submersas.",
    text2 = "Ele cria<NEXT>redemoinhos<NEXT>quando boceja.",
    height = 108, weight = 1520,   -- 1,8 m / 152,0 kg
  },
  ["KINGLER"] = {
    kind = "PINÇA",
    text = "Ele mal consegue<NEXT>erguer a pinça<NEXT>enorme e crescida",
    text2 = "demais. O tamanho<NEXT>dela dificulta<NEXT>mirar direito.",
    height = 103, weight = 600,   -- 1,3 m / 60,0 kg
  },
  ["KOFFING"] = {
    kind = "GÁS TÓXICO",
    text = "O corpo fino e<NEXT>leve dele é cheio<NEXT>de gases que dão",
    text2 = "coriza sem parar,<NEXT>tosse e olhos<NEXT>cheios de lágrima.",
    height = 6, weight = 10,   -- 0,6 m / 1,0 kg
  },
  ["KRABBY"] = {
    kind = "CARANGUEJO",
    text = "Se sente perigo<NEXT>chegando, ele se<NEXT>cobre de bolhas",
    text2 = "feitas com a boca<NEXT>para parecer<NEXT>maior do que é.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["LANTURN"] = {
    kind = "LUZ",
    text = "A luz que ele<NEXT>solta é tão forte<NEXT>que consegue",
    text2 = "iluminar a<NEXT>superfície do mar<NEXT>a 5 km de fundo.",
    height = 102, weight = 225,   -- 1,2 m / 22,5 kg
  },
  ["LAPRAS"] = {
    kind = "TRANSPORTE",
    text = "Eles têm coração<NEXT>gentil. Como quase<NEXT>não brigam, muitos",
    text2 = "foram capturados.<NEXT>O número deles<NEXT>diminuiu muito.",
    height = 205, weight = 2200,   -- 2,5 m / 220,0 kg
  },
  ["LARVITAR"] = {
    kind = "PELE PEDRA",
    text = "Ele se alimenta de<NEXT>terra. Depois de<NEXT>comer uma montanha",
    text2 = "grande, cai no<NEXT>sono para poder<NEXT>crescer.",
    height = 6, weight = 720,   -- 0,6 m / 72,0 kg
  },
  ["LEDIAN"] = {
    kind = "5 ESTRELAS",
    text = "Quando as estrelas<NEXT>piscam no céu da<NEXT>noite, ele voa",
    text2 = "de um lado para o<NEXT>outro espalhando<NEXT>um pó brilhante.",
    height = 104, weight = 356,   -- 1,4 m / 35,6 kg
  },
  ["LEDYBA"] = {
    kind = "5 ESTRELAS",
    text = "Ele é bem tímido.<NEXT>Fica com medo de<NEXT>se mexer se",
    text2 = "estiver sozinho.<NEXT>Mas fica ativo se<NEXT>estiver em grupo.",
    height = 100, weight = 108,   -- 1,0 m / 10,8 kg
  },
  ["LICKITUNG"] = {
    kind = "LAMBIDA",
    text = "A língua dele tem<NEXT>nervos bem<NEXT>desenvolvidos que",
    text2 = "vão até a ponta, e<NEXT>por isso ele a usa<NEXT>com destreza.",
    height = 102, weight = 655,   -- 1,2 m / 65,5 kg
  },
  ["LUGIA"] = {
    kind = "MERGULHO",
    text = "Dizem que ele<NEXT>passa o tempo em<NEXT>silêncio lá no",
    text2 = "fundo do mar<NEXT>porque os poderes<NEXT>dele são fortes.",
    height = 502, weight = 2160,   -- 5,2 m / 216,0 kg
  },
  ["MACHAMP"] = {
    kind = "SUPERFORÇA",
    text = "Ele gira rápido os<NEXT>quatro braços para<NEXT>sacudir os rivais",
    text2 = "com socos e golpes<NEXT>sem parar, vindos<NEXT>de todo lado.",
    height = 106, weight = 1300,   -- 1,6 m / 130,0 kg
  },
  ["MACHOKE"] = {
    kind = "SUPERFORÇA",
    text = "Ele sempre age com<NEXT>toda a força, mas<NEXT>este POKéMON tão",
    text2 = "duro e resistente<NEXT>nunca fica<NEXT>cansado.",
    height = 105, weight = 705,   -- 1,5 m / 70,5 kg
  },
  ["MACHOP"] = {
    kind = "SUPERFORÇA",
    text = "Cheio de força o<NEXT>tempo todo, ele<NEXT>passa as horas",
    text2 = "erguendo pedras.<NEXT>Fazer isso deixa<NEXT>ele mais forte.",
    height = 8, weight = 195,   -- 0,8 m / 19,5 kg
  },
  ["MAGBY"] = {
    kind = "BRASA VIVA",
    text = "Cada vez que ele<NEXT>puxa e solta o<NEXT>ar, brasas quentes",
    text2 = "escorrem da boca<NEXT>e das narinas<NEXT>dele.",
    height = 7, weight = 214,   -- 0,7 m / 21,4 kg
  },
  ["MAGCARGO"] = {
    kind = "LAVA",
    text = "A concha das<NEXT>costas dele é só<NEXT>pele que esfriou",
    text2 = "e endureceu. Ela<NEXT>quebra fácil com<NEXT>um toque leve.",
    height = 8, weight = 550,   -- 0,8 m / 55,0 kg
  },
  ["MAGIKARP"] = {
    kind = "PEIXE",
    text = "Um POKéMON fraco<NEXT>e patético. Pode<NEXT>pular alto em",
    text2 = "raras ocasiões,<NEXT>mas nunca mais que<NEXT>dois metros.",
    height = 9, weight = 100,   -- 0,9 m / 10,0 kg
  },
  ["MAGMAR"] = {
    kind = "CUSPE-FOGO",
    text = "Ele não gosta de<NEXT>lugares frios, e<NEXT>por isso sopra",
    text2 = "chamas ardentes<NEXT>para deixar o<NEXT>lugar bom para si.",
    height = 103, weight = 445,   -- 1,3 m / 44,5 kg
  },
  ["MAGNEMITE"] = {
    kind = "ÍMÃ",
    text = "Ele é atraído por<NEXT>ondas magnéticas.<NEXT>Pode chegar perto",
    text2 = "de treinadores se<NEXT>eles estiverem<NEXT>usando o POKéGEAR.",
    height = 3, weight = 60,   -- 0,3 m / 6,0 kg
  },
  ["MAGNETON"] = {
    kind = "ÍMÃ",
    text = "Três MAGNEMITE<NEXT>ficam ligados por<NEXT>uma força",
    text2 = "magnética forte.<NEXT>Dá dor de ouvido<NEXT>se chegar perto.",
    height = 100, weight = 600,   -- 1,0 m / 60,0 kg
  },
  ["MANKEY"] = {
    kind = "MACACO",
    text = "Ele tem um gênio<NEXT>péssimo. Grupos<NEXT>deles atacam",
    text2 = "qualquer alvo à<NEXT>mão sem motivo<NEXT>nenhum.",
    height = 5, weight = 280,   -- 0,5 m / 28,0 kg
  },
  ["MANTINE"] = {
    kind = "PIPA",
    text = "Enquanto nada com<NEXT>majestade, ele não<NEXT>liga se REMORAID",
    text2 = "grudam nele para<NEXT>catar as sobras<NEXT>dele.",
    height = 201, weight = 2200,   -- 2,1 m / 220,0 kg
  },
  ["MAREEP"] = {
    kind = "LÃ",
    text = "Se eletricidade<NEXT>estática junta no<NEXT>corpo dele, o",
    text2 = "velo dobra de<NEXT>volume. Encostar<NEXT>nele dá choque.",
    height = 6, weight = 78,   -- 0,6 m / 7,8 kg
  },
  ["MARILL"] = {
    kind = "RATO ÁGUA",
    text = "A ponta do rabo<NEXT>dele guarda um<NEXT>óleo mais leve",
    text2 = "que a água, e isso<NEXT>deixa ele nadar<NEXT>sem afundar.",
    height = 4, weight = 85,   -- 0,4 m / 8,5 kg
  },
  ["MAROWAK"] = {
    kind = "GUARDAOSSO",
    text = "Já foi visto<NEXT>batendo em pedras<NEXT>com o osso que",
    text2 = "carrega para<NEXT>mandar recados<NEXT>para os outros.",
    height = 100, weight = 450,   -- 1,0 m / 45,0 kg
  },
  ["MEGANIUM"] = {
    kind = "ERVA",
    text = "O aroma que sobe<NEXT>das pétalas dele<NEXT>tem uma substância",
    text2 = "que acalma os<NEXT>sentimentos<NEXT>agressivos.",
    height = 108, weight = 1005,   -- 1,8 m / 100,5 kg
  },
  ["MEOWTH"] = {
    kind = "ARRANHADOR",
    text = "Ele é fascinado<NEXT>por coisas<NEXT>redondas. Não",
    text2 = "consegue parar de<NEXT>brincar até cansar<NEXT>e cair no sono.",
    height = 4, weight = 42,   -- 0,4 m / 4,2 kg
  },
  ["METAPOD"] = {
    kind = "CASULO",
    text = "Dentro da casca,<NEXT>ele é mole e<NEXT>fraco enquanto se",
    text2 = "prepara para<NEXT>evoluir. Fica<NEXT>imóvel lá dentro.",
    height = 7, weight = 99,   -- 0,7 m / 9,9 kg
  },
  ["MEW"] = {
    kind = "ESPÉCIE",
    text = "Pelo visto, ele<NEXT>só aparece para<NEXT>as pessoas que",
    text2 = "têm coração puro<NEXT>e vontade forte<NEXT>de ver ele.",
    height = 4, weight = 40,   -- 0,4 m / 4,0 kg
  },
  ["MEWTWO"] = {
    kind = "GENÉTICO",
    text = "Como a capacidade<NEXT>de luta dele foi<NEXT>levada ao limite,",
    text2 = "ele só pensa em<NEXT>derrotar os<NEXT>inimigos dele.",
    height = 200, weight = 1220,   -- 2,0 m / 122,0 kg
  },
  ["MILTANK"] = {
    kind = "VACA LEITE",
    text = "O leite dela é<NEXT>cheio de nutrição,<NEXT>e isso faz dele a",
    text2 = "bebida suprema<NEXT>para os doentes<NEXT>ou cansados.",
    height = 102, weight = 755,   -- 1,2 m / 75,5 kg
  },
  ["MISDREAVUS"] = {
    kind = "GRITO",
    text = "Ele gosta de fazer<NEXT>travessuras como<NEXT>gritar e gemer",
    text2 = "para assustar as<NEXT>pessoas durante<NEXT>a noite.",
    height = 7, weight = 10,   -- 0,7 m / 1,0 kg
  },
  ["MOLTRES"] = {
    kind = "CHAMA",
    text = "Este POKéMON<NEXT>lendário espalha<NEXT>brasas a cada",
    text2 = "batida das asas.<NEXT>É uma cena<NEXT>empolgante de ver.",
    height = 200, weight = 600,   -- 2,0 m / 60,0 kg
  },
  ["MR__MIME"] = {
    kind = "BARREIRA",
    text = "Mímico habilidoso<NEXT>desde que nasce,<NEXT>ele ganha o poder",
    text2 = "de criar objetos<NEXT>invisíveis<NEXT>conforme cresce.",
    height = 103, weight = 545,   -- 1,3 m / 54,5 kg
  },
  ["MUK"] = {
    kind = "LODO",
    text = "Eles adoram se<NEXT>juntar em lugares<NEXT>fedidos onde o",
    text2 = "lodo se acumula, e<NEXT>isso piora o<NEXT>fedor em volta.",
    height = 102, weight = 300,   -- 1,2 m / 30,0 kg
  },
  ["MURKROW"] = {
    kind = "ESCURIDÃO",
    text = "Temido e odiado<NEXT>por muitos, dizem<NEXT>que ele traz",
    text2 = "azar para todos<NEXT>os que o veem<NEXT>durante a noite.",
    height = 5, weight = 21,   -- 0,5 m / 2,1 kg
  },
  ["NATU"] = {
    kind = "PASSARINHO",
    text = "Como as asas dele<NEXT>ainda não estão<NEXT>crescidas, tem de",
    text2 = "pular para andar.<NEXT>Está sempre<NEXT>encarando algo.",
    height = 2, weight = 20,   -- 0,2 m / 2,0 kg
  },
  ["NIDOKING"] = {
    kind = "BROCA",
    text = "Ele balança o<NEXT>rabão na batalha.<NEXT>Se o rival se",
    text2 = "encolher, ele<NEXT>investe com o<NEXT>corpo robusto.",
    height = 104, weight = 620,   -- 1,4 m / 62,0 kg
  },
  ["NIDOQUEEN"] = {
    kind = "BROCA",
    text = "O corpo dela é<NEXT>coberto de escamas<NEXT>que parecem",
    text2 = "agulhas. Ela nunca<NEXT>recua diante de<NEXT>ataque nenhum.",
    height = 103, weight = 600,   -- 1,3 m / 60,0 kg
  },
  ["NIDORAN_F"] = {
    kind = "ESPINHO",
    text = "O veneno escondido<NEXT>no chifrinho dela<NEXT>é muito forte.",
    text2 = "Até um arranhão<NEXT>pequeno pode ser<NEXT>fatal.",
    height = 4, weight = 70,   -- 0,4 m / 7,0 kg
  },
  ["NIDORAN_M"] = {
    kind = "ESPINHO",
    text = "Ele é pequeno, mas<NEXT>o chifre é cheio<NEXT>de veneno. Investe",
    text2 = "e então perfura<NEXT>com o chifre para<NEXT>injetar o veneno.",
    height = 5, weight = 90,   -- 0,5 m / 9,0 kg
  },
  ["NIDORINA"] = {
    kind = "ESPINHO",
    text = "Ao alimentar os<NEXT>filhotes, ela<NEXT>primeiro mastiga",
    text2 = "e amolece a<NEXT>comida, e então<NEXT>cospe para eles.",
    height = 8, weight = 200,   -- 0,8 m / 20,0 kg
  },
  ["NIDORINO"] = {
    kind = "ESPINHO",
    text = "Ele levanta as<NEXT>orelhas grandes<NEXT>para checar o que",
    text2 = "há em volta. Se<NEXT>sentir qualquer<NEXT>coisa, ataca já.",
    height = 9, weight = 195,   -- 0,9 m / 19,5 kg
  },
  ["NINETALES"] = {
    kind = "RAPOSA",
    text = "Algumas lendas<NEXT>dizem que cada um<NEXT>dos nove rabos",
    text2 = "dele tem seu<NEXT>próprio poder<NEXT>místico especial.",
    height = 101, weight = 199,   -- 1,1 m / 19,9 kg
  },
  ["NOCTOWL"] = {
    kind = "CORUJA",
    text = "Os olhos dele são<NEXT>adaptados de um<NEXT>jeito especial.",
    text2 = "Juntam até a luz<NEXT>mais fraca e dão<NEXT>a visão no escuro.",
    height = 106, weight = 408,   -- 1,6 m / 40,8 kg
  },
  ["OCTILLERY"] = {
    kind = "JATO",
    text = "Ele prende os<NEXT>inimigos com os<NEXT>tentáculos cheios",
    text2 = "de ventosas e<NEXT>então esmaga eles<NEXT>com a cabeça dura.",
    height = 9, weight = 285,   -- 0,9 m / 28,5 kg
  },
  ["ODDISH"] = {
    kind = "ERVA",
    text = "Acordado pela luz<NEXT>da lua, ele anda<NEXT>muito à noite.",
    text2 = "De dia, fica<NEXT>quietinho embaixo<NEXT>da terra.",
    height = 5, weight = 54,   -- 0,5 m / 5,4 kg
  },
  ["OMANYTE"] = {
    kind = "ESPIRAL",
    text = "Revivido de um<NEXT>fóssil antigo,<NEXT>este POKéMON usa",
    text2 = "o ar guardado na<NEXT>concha para subir<NEXT>e descer na água.",
    height = 4, weight = 75,   -- 0,4 m / 7,5 kg
  },
  ["OMASTAR"] = {
    kind = "ESPIRAL",
    text = "Pelo visto, ele<NEXT>rachava a concha<NEXT>do SHELLDER com as",
    text2 = "presas afiadas e<NEXT>chupava o que<NEXT>havia dentro.",
    height = 100, weight = 350,   -- 1,0 m / 35,0 kg
  },
  ["ONIX"] = {
    kind = "COBRAPEDRA",
    text = "Ele se retorce e<NEXT>serpenteia pelo<NEXT>chão. O estrondo",
    text2 = "do túnel dele<NEXT>ecoa por uma<NEXT>grande distância.",
    height = 808, weight = 2100,   -- 8,8 m / 210,0 kg
  },
  ["PARAS"] = {
    kind = "COGUMELO",
    text = "Ele nasce coberto<NEXT>de esporos de<NEXT>cogumelo. Conforme",
    text2 = "o corpo cresce,<NEXT>cogumelos brotam<NEXT>das costas dele.",
    height = 3, weight = 54,   -- 0,3 m / 5,4 kg
  },
  ["PARASECT"] = {
    kind = "COGUMELO",
    text = "Ele fica quase<NEXT>sempre em lugares<NEXT>escuros e úmidos,",
    text2 = "gosto não do<NEXT>inseto, mas dos<NEXT>cogumelos dele.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["PERSIAN"] = {
    kind = "GATO FINO",
    text = "Muitos o adoram<NEXT>pelo ar refinado.<NEXT>Mesmo assim, ele",
    text2 = "ataca e arranha<NEXT>por qualquer<NEXT>bobagem.",
    height = 100, weight = 320,   -- 1,0 m / 32,0 kg
  },
  ["PHANPY"] = {
    kind = "NARIZLONGO",
    text = "Ele balança a<NEXT>tromba comprida<NEXT>de brincadeira,",
    text2 = "mas como é tão<NEXT>forte, aquilo pode<NEXT>ser perigoso.",
    height = 5, weight = 335,   -- 0,5 m / 33,5 kg
  },
  ["PICHU"] = {
    kind = "RATINHO",
    text = "Ele ainda não é<NEXT>bom de guardar<NEXT>eletricidade.",
    text2 = "Pode dar choque se<NEXT>ficar animado ou<NEXT>levar um susto.",
    height = 3, weight = 20,   -- 0,3 m / 2,0 kg
  },
  ["PIDGEOT"] = {
    kind = "PÁSSARO",
    text = "Os músculos do<NEXT>peito dele são<NEXT>fortes o bastante",
    text2 = "para levantar um<NEXT>vendaval com umas<NEXT>poucas batidas.",
    height = 105, weight = 395,   -- 1,5 m / 39,5 kg
  },
  ["PIDGEOTTO"] = {
    kind = "PÁSSARO",
    text = "A visão dele é<NEXT>excelente. Por<NEXT>mais alto que",
    text2 = "voe, consegue ver<NEXT>os movimentos da<NEXT>presa dele.",
    height = 101, weight = 300,   -- 1,1 m / 30,0 kg
  },
  ["PIDGEY"] = {
    kind = "PASSARINHO",
    text = "Costuma se<NEXT>esconder no mato<NEXT>alto. Como não",
    text2 = "gosta de brigar,<NEXT>se protege<NEXT>chutando areia.",
    height = 3, weight = 18,   -- 0,3 m / 1,8 kg
  },
  ["PIKACHU"] = {
    kind = "RATO",
    text = "Este POKéMON<NEXT>esperto assa<NEXT>FRUTAS duras com",
    text2 = "eletricidade para<NEXT>deixá-las macias<NEXT>de comer.",
    height = 4, weight = 60,   -- 0,4 m / 6,0 kg
  },
  ["PILOSWINE"] = {
    kind = "SUÍNO",
    text = "Como o pelo longo<NEXT>do corpo inteiro<NEXT>atrapalha a visão",
    text2 = "dele, ele só fica<NEXT>investindo sem<NEXT>parar.",
    height = 101, weight = 558,   -- 1,1 m / 55,8 kg
  },
  ["PINECO"] = {
    kind = "BICHO-SACO",
    text = "Ele gosta de<NEXT>engrossar a casca<NEXT>juntando camadas",
    text2 = "de casca de pau.<NEXT>O peso a mais não<NEXT>incomoda ele.",
    height = 6, weight = 72,   -- 0,6 m / 7,2 kg
  },
  ["PINSIR"] = {
    kind = "BESOURO",
    text = "Com os chifres,<NEXT>ele cava tocas<NEXT>para dormir à",
    text2 = "noite. De manhã,<NEXT>terra úmida fica<NEXT>grudada nele.",
    height = 105, weight = 550,   -- 1,5 m / 55,0 kg
  },
  ["POLITOED"] = {
    kind = "SAPO",
    text = "Se POLIWAG e<NEXT>POLIWHIRL ouvem o<NEXT>grito que ecoa",
    text2 = "dele, respondem<NEXT>vindo de perto<NEXT>e de bem longe.",
    height = 101, weight = 339,   -- 1,1 m / 33,9 kg
  },
  ["POLIWAG"] = {
    kind = "GIRINO",
    text = "Como é desajeitado<NEXT>para andar com as<NEXT>pernas recém",
    text2 = "nascidas, ele vive<NEXT>nadando dentro<NEXT>da água.",
    height = 6, weight = 124,   -- 0,6 m / 12,4 kg
  },
  ["POLIWHIRL"] = {
    kind = "GIRINO",
    text = "O espiral da<NEXT>barriga dele mexe<NEXT>de leve. Ficar",
    text2 = "olhando para ele<NEXT>pode dar sono aos<NEXT>poucos.",
    height = 100, weight = 200,   -- 1,0 m / 20,0 kg
  },
  ["POLIWRATH"] = {
    kind = "GIRINO",
    text = "Este nadador forte<NEXT>e habilidoso é<NEXT>capaz até de",
    text2 = "cruzar o Oceano<NEXT>Pacífico só<NEXT>batendo as pernas.",
    height = 103, weight = 540,   -- 1,3 m / 54,0 kg
  },
  ["PONYTA"] = {
    kind = "CAVALOFOGO",
    text = "Ele corre mal logo<NEXT>depois de nascer.<NEXT>Aos poucos fica",
    text2 = "mais rápido de<NEXT>tanto correr atrás<NEXT>dos pais dele.",
    height = 100, weight = 300,   -- 1,0 m / 30,0 kg
  },
  ["PORYGON"] = {
    kind = "VIRTUAL",
    text = "Ele é um POKéMON<NEXT>feito pelo homem.<NEXT>Como não respira,",
    text2 = "as pessoas querem<NEXT>muito testar ele<NEXT>em todo ambiente.",
    height = 8, weight = 365,   -- 0,8 m / 36,5 kg
  },
  ["PORYGON2"] = {
    kind = "VIRTUAL",
    text = "Esta versão<NEXT>melhorada do<NEXT>PORYGON foi feita",
    text2 = "para explorar o<NEXT>espaço. Só que<NEXT>ele não voa.",
    height = 6, weight = 325,   -- 0,6 m / 32,5 kg
  },
  ["PRIMEAPE"] = {
    kind = "MACACO",
    text = "Se alguém chegar<NEXT>perto enquanto ele<NEXT>dorme, pode",
    text2 = "acordar e sair<NEXT>em perseguição<NEXT>furiosa e zonza.",
    height = 100, weight = 320,   -- 1,0 m / 32,0 kg
  },
  ["PSYDUCK"] = {
    kind = "PATO",
    text = "Ele tem poderes<NEXT>místicos mas não<NEXT>lembra que já os",
    text2 = "usou. É por isso<NEXT>que vive com cara<NEXT>de confuso.",
    height = 8, weight = 196,   -- 0,8 m / 19,6 kg
  },
  ["PUPITAR"] = {
    kind = "CASCA DURA",
    text = "A casca dele é<NEXT>dura como rocha, e<NEXT>ele também é bem",
    text2 = "forte. O CASTIGAR<NEXT>dele derruba uma<NEXT>montanha.",
    height = 102, weight = 1520,   -- 1,2 m / 152,0 kg
  },
  ["QUAGSIRE"] = {
    kind = "PEIXE ÁGUA",
    text = "Este POKéMON<NEXT>despreocupado tem<NEXT>um jeito calmo.",
    text2 = "Enquanto nada,<NEXT>vive batendo no<NEXT>casco dos barcos.",
    height = 104, weight = 750,   -- 1,4 m / 75,0 kg
  },
  ["QUILAVA"] = {
    kind = "VULCÃO",
    text = "Cuidado se ele<NEXT>virar as costas<NEXT>durante a luta.",
    text2 = "Significa que vai<NEXT>atacar com o fogo<NEXT>das costas dele.",
    height = 9, weight = 190,   -- 0,9 m / 19,0 kg
  },
  ["QWILFISH"] = {
    kind = "BALÃO",
    text = "Para atirar os<NEXT>espinhos com<NEXT>veneno, ele tem de",
    text2 = "inchar o corpo<NEXT>bebendo 10 litros<NEXT>de água de vez.",
    height = 5, weight = 39,   -- 0,5 m / 3,9 kg
  },
  ["RAICHU"] = {
    kind = "RATO",
    text = "Quando a<NEXT>eletricidade dele<NEXT>junta, os músculos",
    text2 = "ficam excitados e<NEXT>ele fica mais<NEXT>bravo que sempre.",
    height = 8, weight = 300,   -- 0,8 m / 30,0 kg
  },
  ["RAIKOU"] = {
    kind = "TROVÃO",
    text = "As nuvens de chuva<NEXT>que ele carrega<NEXT>deixam ele soltar",
    text2 = "raios à vontade.<NEXT>Dizem que ele<NEXT>desceu num raio.",
    height = 109, weight = 1780,   -- 1,9 m / 178,0 kg
  },
  ["RAPIDASH"] = {
    kind = "CAVALOFOGO",
    text = "A galope pleno, os<NEXT>quatro cascos dele<NEXT>quase não tocam",
    text2 = "o chão, porque ele<NEXT>se move de um<NEXT>jeito rapidíssimo.",
    height = 107, weight = 950,   -- 1,7 m / 95,0 kg
  },
  ["RATICATE"] = {
    kind = "RATO",
    text = "Rói qualquer<NEXT>coisa com as<NEXT>presas duras. Até",
    text2 = "prédios de<NEXT>concreto ele<NEXT>derruba roendo.",
    height = 7, weight = 185,   -- 0,7 m / 18,5 kg
  },
  ["RATTATA"] = {
    kind = "RATO",
    text = "Ele come de tudo.<NEXT>Onde houver<NEXT>comida, se",
    text2 = "instala e tem<NEXT>filhotes sem<NEXT>parar.",
    height = 3, weight = 35,   -- 0,3 m / 3,5 kg
  },
  ["REMORAID"] = {
    kind = "JATO",
    text = "Ele tem uma mira<NEXT>excelente. A água<NEXT>que ele dispara",
    text2 = "acerta até presa<NEXT>em movimento a<NEXT>mais de 90 metros.",
    height = 6, weight = 120,   -- 0,6 m / 12,0 kg
  },
  ["RHYDON"] = {
    kind = "BROCA",
    text = "O couro grosso<NEXT>dele protege até<NEXT>do calor da lava.",
    text2 = "Mas esse couro<NEXT>também deixa ele<NEXT>sem sensibilidade.",
    height = 109, weight = 1200,   -- 1,9 m / 120,0 kg
  },
  ["RHYHORN"] = {
    kind = "ESPINHOS",
    text = "Ele é ruim de<NEXT>virar por causa<NEXT>das quatro pernas",
    text2 = "curtas. Só<NEXT>consegue investir<NEXT>numa direção.",
    height = 100, weight = 1150,   -- 1,0 m / 115,0 kg
  },
  ["SANDSHREW"] = {
    kind = "RATO",
    text = "Se cair de bem<NEXT>alto, este POKéMON<NEXT>consegue se",
    text2 = "salvar virando<NEXT>uma bola e<NEXT>quicando no chão.",
    height = 6, weight = 120,   -- 0,6 m / 12,0 kg
  },
  ["SANDSLASH"] = {
    kind = "RATO",
    text = "Para tentar se<NEXT>esconder, ele<NEXT>corre em volta a",
    text2 = "toda velocidade<NEXT>e levanta poeira<NEXT>que cega o rival.",
    height = 100, weight = 295,   -- 1,0 m / 29,5 kg
  },
  ["SCIZOR"] = {
    kind = "TESOURA",
    text = "Ele levanta as<NEXT>pinças com desenho<NEXT>de olho para",
    text2 = "assustar rivais.<NEXT>Assim ele parece<NEXT>ter três cabeças.",
    height = 108, weight = 1180,   -- 1,8 m / 118,0 kg
  },
  ["SCYTHER"] = {
    kind = "LOUVA-DEUS",
    text = "Ele corta o mato<NEXT>com as foices<NEXT>afiadas dele, e",
    text2 = "se move rápido<NEXT>demais para o olho<NEXT>humano acompanhar.",
    height = 105, weight = 560,   -- 1,5 m / 56,0 kg
  },
  ["SEADRA"] = {
    kind = "DRAGÃO",
    text = "Um exame das<NEXT>células dele achou<NEXT>um gene que não",
    text2 = "existe no HORSEA.<NEXT>Aquilo virou um<NEXT>assunto quente.",
    height = 102, weight = 250,   -- 1,2 m / 25,0 kg
  },
  ["SEAKING"] = {
    kind = "PEIXE OURO",
    text = "Na época da<NEXT>desova, SEAKING<NEXT>se juntam de todo",
    text2 = "lugar e pintam os<NEXT>rios de um<NEXT>vermelho vivo.",
    height = 103, weight = 390,   -- 1,3 m / 39,0 kg
  },
  ["SEEL"] = {
    kind = "FOCA",
    text = "Mesmo andando mal<NEXT>em terra, ele é um<NEXT>nadador gracioso.",
    text2 = "Adora demais<NEXT>ficar em mares<NEXT>gelados.",
    height = 101, weight = 900,   -- 1,1 m / 90,0 kg
  },
  ["SENTRET"] = {
    kind = "VIGIA",
    text = "POKéMON muito<NEXT>cauteloso, ele se<NEXT>levanta usando a",
    text2 = "cauda para ver<NEXT>melhor o que há<NEXT>em volta dele.",
    height = 8, weight = 60,   -- 0,8 m / 6,0 kg
  },
  ["SHELLDER"] = {
    kind = "BIVALVE",
    text = "Ele nada de costas<NEXT>abrindo e fechando<NEXT>a concha de duas",
    text2 = "partes. É bem mais<NEXT>rápido do que<NEXT>parece.",
    height = 3, weight = 40,   -- 0,3 m / 4,0 kg
  },
  ["SHUCKLE"] = {
    kind = "MOFO",
    text = "As FRUTAS que ele<NEXT>guarda na concha<NEXT>em forma de vaso",
    text2 = "se decompõem e<NEXT>viram um líquido<NEXT>grudento.",
    height = 6, weight = 205,   -- 0,6 m / 20,5 kg
  },
  ["SKARMORY"] = {
    kind = "AVE DE AÇO",
    text = "As asas duras dele<NEXT>parecem pesadas,<NEXT>mas na verdade são",
    text2 = "ocas e leves, e<NEXT>isso deixa ele<NEXT>voar livre no céu.",
    height = 107, weight = 505,   -- 1,7 m / 50,5 kg
  },
  ["SKIPLOOM"] = {
    kind = "ALGODÃO",
    text = "A flor no alto da<NEXT>cabeça dele abre<NEXT>e fecha conforme",
    text2 = "a temperatura<NEXT>vai subindo e<NEXT>descendo.",
    height = 6, weight = 10,   -- 0,6 m / 1,0 kg
  },
  ["SLOWBRO"] = {
    kind = "ERMITÃO",
    text = "Se o SHELLDER que<NEXT>morde o rabo cair<NEXT>numa batalha",
    text2 = "dura, ele volta a<NEXT>ser um SLOWPOKE<NEXT>comum.",
    height = 106, weight = 785,   -- 1,6 m / 78,5 kg
  },
  ["SLOWKING"] = {
    kind = "REAL",
    text = "Ele tem uma<NEXT>inteligência e uma<NEXT>intuição enormes.",
    text2 = "Seja qual for a<NEXT>situação, fica<NEXT>calmo e sereno.",
    height = 200, weight = 795,   -- 2,0 m / 79,5 kg
  },
  ["SLOWPOKE"] = {
    kind = "LERDO",
    text = "Ele fica à toa<NEXT>perto da água. Se<NEXT>algo morder o",
    text2 = "rabo dele, nem<NEXT>percebe por um<NEXT>dia inteiro.",
    height = 102, weight = 360,   -- 1,2 m / 36,0 kg
  },
  ["SLUGMA"] = {
    kind = "LAVA",
    text = "Ele nunca dorme.<NEXT>Tem de ficar em<NEXT>movimento porque,",
    text2 = "se parasse, o<NEXT>corpo de magma<NEXT>esfriaria duro.",
    height = 7, weight = 350,   -- 0,7 m / 35,0 kg
  },
  ["SMEARGLE"] = {
    kind = "PINTOR",
    text = "Um fluido especial<NEXT>escorre da ponta<NEXT>do rabo dele. Ele",
    text2 = "pinta o fluido em<NEXT>tudo para marcar<NEXT>o território dele.",
    height = 102, weight = 580,   -- 1,2 m / 58,0 kg
  },
  ["SMOOCHUM"] = {
    kind = "BEIJO",
    text = "Os lábios dele são<NEXT>as partes mais<NEXT>sensíveis dele.",
    text2 = "Ele sempre usa os<NEXT>lábios primeiro<NEXT>para examinar.",
    height = 4, weight = 60,   -- 0,4 m / 6,0 kg
  },
  ["SNEASEL"] = {
    kind = "GARRA",
    text = "As patas dele<NEXT>escondem garras<NEXT>afiadas. Se for",
    text2 = "atacado, ele abre<NEXT>as garras de<NEXT>repente e assusta.",
    height = 9, weight = 280,   -- 0,9 m / 28,0 kg
  },
  ["SNORLAX"] = {
    kind = "DORMINDO",
    text = "O que parece ser<NEXT>o grito dele pode<NEXT>na verdade ser o",
    text2 = "ronco ou o roncar<NEXT>da barriga dele<NEXT>com fome.",
    height = 201, weight = 4600,   -- 2,1 m / 460,0 kg
  },
  ["SNUBBULL"] = {
    kind = "FADA",
    text = "Mesmo parecendo<NEXT>assustador, ele é<NEXT>na verdade bom e",
    text2 = "carinhoso. Faz<NEXT>muito sucesso<NEXT>entre as mulheres.",
    height = 6, weight = 78,   -- 0,6 m / 7,8 kg
  },
  ["SPEAROW"] = {
    kind = "PASSARINHO",
    text = "Ele bate as asas<NEXT>curtas para tirar<NEXT>insetos do mato",
    text2 = "alto. Depois os<NEXT>pega com o bico<NEXT>curto dele.",
    height = 3, weight = 20,   -- 0,3 m / 2,0 kg
  },
  ["SPINARAK"] = {
    kind = "CUSPE-FIO",
    text = "Ele fica parado na<NEXT>mesma posição por<NEXT>dias na teia dele,",
    text2 = "esperando a presa<NEXT>desavisada chegar<NEXT>perto.",
    height = 5, weight = 85,   -- 0,5 m / 8,5 kg
  },
  ["SQUIRTLE"] = {
    kind = "TARTARUGA",
    text = "O casco é mole<NEXT>quando ele nasce.<NEXT>Logo fica tão",
    text2 = "duro que dedos<NEXT>que o cutucam<NEXT>quicam de volta.",
    height = 5, weight = 90,   -- 0,5 m / 9,0 kg
  },
  ["STANTLER"] = {
    kind = "CHIFRUDO",
    text = "Os chifres curvos<NEXT>mudam de leve o<NEXT>fluxo do ar e",
    text2 = "criam um espaço<NEXT>estranho onde a<NEXT>realidade entorta.",
    height = 104, weight = 712,   -- 1,4 m / 71,2 kg
  },
  ["STARMIE"] = {
    kind = "MISTERIOSO",
    text = "A parte central<NEXT>do corpo dele se<NEXT>chama núcleo.",
    text2 = "Ele brilha numa<NEXT>cor diferente a<NEXT>cada vez que o vê.",
    height = 101, weight = 800,   -- 1,1 m / 80,0 kg
  },
  ["STARYU"] = {
    kind = "ESTRELA",
    text = "À noite, o centro<NEXT>do corpo dele<NEXT>pisca devagar",
    text2 = "no mesmo ritmo de<NEXT>uma batida de<NEXT>coração humano.",
    height = 8, weight = 345,   -- 0,8 m / 34,5 kg
  },
  ["STEELIX"] = {
    kind = "COBRA AÇO",
    text = "O corpo dele foi<NEXT>comprimido bem<NEXT>fundo no subsolo.",
    text2 = "Por causa disso,<NEXT>ele é mais duro<NEXT>que um diamante.",
    height = 902, weight = 4000,   -- 9,2 m / 400,0 kg
  },
  ["SUDOWOODO"] = {
    kind = "IMITAÇÃO",
    text = "Mesmo fingindo<NEXT>ser uma árvore o<NEXT>tempo todo, ele",
    text2 = "parece ser mais<NEXT>perto de pedra<NEXT>do que de planta.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["SUICUNE"] = {
    kind = "AURORA",
    text = "Tido como a<NEXT>reencarnação dos<NEXT>ventos do norte,",
    text2 = "ele purifica na<NEXT>hora a água suja<NEXT>e turva.",
    height = 200, weight = 1870,   -- 2,0 m / 187,0 kg
  },
  ["SUNFLORA"] = {
    kind = "SOL",
    text = "Ele transforma a<NEXT>luz do sol em<NEXT>energia. No escuro",
    text2 = "depois do pôr do<NEXT>sol, fecha as<NEXT>pétalas e para.",
    height = 8, weight = 85,   -- 0,8 m / 8,5 kg
  },
  ["SUNKERN"] = {
    kind = "SEMENTE",
    text = "Ele pode cair do<NEXT>céu de repente. Se<NEXT>um SPEAROW o",
    text2 = "atacar, vai<NEXT>sacudir as folhas<NEXT>com violência.",
    height = 3, weight = 18,   -- 0,3 m / 1,8 kg
  },
  ["SWINUB"] = {
    kind = "PORCO",
    text = "Ele esfrega o<NEXT>focinho no chão<NEXT>para achar e",
    text2 = "desenterrar a<NEXT>comida. Às vezes<NEXT>acha água quente.",
    height = 4, weight = 65,   -- 0,4 m / 6,5 kg
  },
  ["TANGELA"] = {
    kind = "CIPÓ",
    text = "Os cipós que<NEXT>cobrem o corpo<NEXT>inteiro dele estão",
    text2 = "sempre balançando.<NEXT>Eles deixam os<NEXT>rivais nervosos.",
    height = 100, weight = 350,   -- 1,0 m / 35,0 kg
  },
  ["TAUROS"] = {
    kind = "TOUROBRAVO",
    text = "Eles brigam entre<NEXT>si travando os<NEXT>chifres. O chefe",
    text2 = "do rebanho se<NEXT>orgulha dos<NEXT>chifres marcados.",
    height = 104, weight = 884,   -- 1,4 m / 88,4 kg
  },
  ["TEDDIURSA"] = {
    kind = "URSINHO",
    text = "Se ele acha mel,<NEXT>a marca de lua<NEXT>dele brilha. Vive",
    text2 = "lambendo as patas<NEXT>porque elas ficam<NEXT>cheias de mel.",
    height = 6, weight = 88,   -- 0,6 m / 8,8 kg
  },
  ["TENTACOOL"] = {
    kind = "ÁGUA-VIVA",
    text = "Quando a maré<NEXT>baixa, restos de<NEXT>TENTACOOL secos",
    text2 = "podem ser achados<NEXT>jogados pela água<NEXT>na praia.",
    height = 9, weight = 455,   -- 0,9 m / 45,5 kg
  },
  ["TENTACRUEL"] = {
    kind = "ÁGUA-VIVA",
    text = "Os 80 tentáculos<NEXT>dele absorvem água<NEXT>e se esticam quase",
    text2 = "sem fim para<NEXT>CONTRAIR as presas<NEXT>e os inimigos.",
    height = 106, weight = 550,   -- 1,6 m / 55,0 kg
  },
  ["TOGEPI"] = {
    kind = "ESPINHOS",
    text = "A casca parece<NEXT>estar cheia de<NEXT>alegria. Dizem",
    text2 = "que ele divide a<NEXT>boa sorte com quem<NEXT>o trata bem.",
    height = 3, weight = 15,   -- 0,3 m / 1,5 kg
  },
  ["TOGETIC"] = {
    kind = "FELICIDADE",
    text = "Dizem que ele<NEXT>aparece diante de<NEXT>gente bondosa e",
    text2 = "atenciosa e cobre<NEXT>essas pessoas de<NEXT>felicidade.",
    height = 6, weight = 32,   -- 0,6 m / 3,2 kg
  },
  ["TOTODILE"] = {
    kind = "MANDÍBULA",
    text = "As mandíbulas bem<NEXT>desenvolvidas são<NEXT>fortes e capazes",
    text2 = "de esmagar tudo.<NEXT>Até o treinador<NEXT>precisa cuidar.",
    height = 6, weight = 95,   -- 0,6 m / 9,5 kg
  },
  ["TYPHLOSION"] = {
    kind = "VULCÃO",
    text = "Se a raiva dele<NEXT>chega ao topo, ele<NEXT>fica tão quente",
    text2 = "que tudo que o<NEXT>encostar pega<NEXT>fogo na hora.",
    height = 107, weight = 795,   -- 1,7 m / 79,5 kg
  },
  ["TYRANITAR"] = {
    kind = "ARMADURA",
    text = "Nenhum tipo de<NEXT>ataque machuca o<NEXT>corpo dele, e por",
    text2 = "isso ele adora<NEXT>sair desafiando<NEXT>os inimigos.",
    height = 200, weight = 2020,   -- 2,0 m / 202,0 kg
  },
  ["TYROGUE"] = {
    kind = "BRIGA",
    text = "Ele está sempre<NEXT>transbordando de<NEXT>energia. Para",
    text2 = "ficar mais forte,<NEXT>continua lutando<NEXT>mesmo se perder.",
    height = 7, weight = 210,   -- 0,7 m / 21,0 kg
  },
  ["UMBREON"] = {
    kind = "LUAR",
    text = "Quando fica<NEXT>agitado, este<NEXT>POKéMON se protege",
    text2 = "soltando um suor<NEXT>venenoso pelos<NEXT>poros dele.",
    height = 100, weight = 270,   -- 1,0 m / 27,0 kg
  },
  ["UNOWN"] = {
    kind = "SÍMBOLO",
    text = "As formas deles<NEXT>lembram escritas<NEXT>antigas em placas",
    text2 = "de pedra. Dizem<NEXT>que as duas coisas<NEXT>têm ligação.",
    height = 5, weight = 50,   -- 0,5 m / 5,0 kg
  },
  ["URSARING"] = {
    kind = "HIBERNANTE",
    text = "Mesmo sendo bom<NEXT>de subir em<NEXT>árvore, ele",
    text2 = "prefere quebrar<NEXT>os troncos e comer<NEXT>as FRUTAS caídas.",
    height = 108, weight = 1258,   -- 1,8 m / 125,8 kg
  },
  ["VAPOREON"] = {
    kind = "JATO BOLHA",
    text = "Quando as<NEXT>nadadeiras de<NEXT>VAPOREON vibram,",
    text2 = "é sinal de que a<NEXT>chuva vem em<NEXT>poucas horas.",
    height = 100, weight = 290,   -- 1,0 m / 29,0 kg
  },
  ["VENOMOTH"] = {
    kind = "MARIPOSA",
    text = "Quando ataca, ele<NEXT>bate as asas<NEXT>grandes com força",
    text2 = "para espalhar o<NEXT>pó venenoso dele<NEXT>por toda parte.",
    height = 105, weight = 125,   -- 1,5 m / 12,5 kg
  },
  ["VENONAT"] = {
    kind = "INSETO",
    text = "Os olhos dele<NEXT>também servem de<NEXT>radar. Ele pega e",
    text2 = "come insetinhos<NEXT>que se escondem<NEXT>no escuro.",
    height = 100, weight = 300,   -- 1,0 m / 30,0 kg
  },
  ["VENUSAUR"] = {
    kind = "SEMENTE",
    text = "Abrindo as pétalas<NEXT>largas da flor<NEXT>dele e tomando",
    text2 = "os raios do sol,<NEXT>ele enche o corpo<NEXT>de poder.",
    height = 200, weight = 1000,   -- 2,0 m / 100,0 kg
  },
  ["VICTREEBEL"] = {
    kind = "PAPA-MOSCA",
    text = "O ÁCIDO que já<NEXT>dissolveu muitas<NEXT>presas fica mais",
    text2 = "doce, e assim<NEXT>atrai as presas<NEXT>com mais eficácia.",
    height = 107, weight = 155,   -- 1,7 m / 15,5 kg
  },
  ["VILEPLUME"] = {
    kind = "FLOR",
    text = "Ele tem as maiores<NEXT>pétalas do mundo.<NEXT>A cada passo, as",
    text2 = "pétalas sacodem<NEXT>nuvens pesadas de<NEXT>pólen tóxico.",
    height = 102, weight = 186,   -- 1,2 m / 18,6 kg
  },
  ["VOLTORB"] = {
    kind = "BOLA",
    text = "Ele rola para se<NEXT>mover. Se o chão<NEXT>for irregular, um",
    text2 = "tranco de bater<NEXT>numa lombada faz<NEXT>ele explodir.",
    height = 5, weight = 104,   -- 0,5 m / 10,4 kg
  },
  ["VULPIX"] = {
    kind = "RAPOSA",
    text = "Conforme cresce,<NEXT>o rabo branco<NEXT>único ganha cor",
    text2 = "e se divide em<NEXT>seis. É bem quente<NEXT>e fofinho.",
    height = 6, weight = 99,   -- 0,6 m / 9,9 kg
  },
  ["WARTORTLE"] = {
    kind = "TARTARUGA",
    text = "Ele é símbolo de<NEXT>vida longa. Se o<NEXT>casco dele tem",
    text2 = "algas, aquele<NEXT>WARTORTLE é bem<NEXT>velho.",
    height = 100, weight = 225,   -- 1,0 m / 22,5 kg
  },
  ["WEEDLE"] = {
    kind = "PELUDINHO",
    text = "O ferrão venenoso<NEXT>dele é bem forte.<NEXT>A cor viva do",
    text2 = "corpo serve para<NEXT>afastar os<NEXT>inimigos.",
    height = 3, weight = 32,   -- 0,3 m / 3,2 kg
  },
  ["WEEPINBELL"] = {
    kind = "PAPA-MOSCA",
    text = "Mesmo estando<NEXT>cheio de ÁCIDO,<NEXT>ele não derrete",
    text2 = "porque também<NEXT>escorre um fluido<NEXT>que neutraliza.",
    height = 100, weight = 64,   -- 1,0 m / 6,4 kg
  },
  ["WEEZING"] = {
    kind = "GÁS TÓXICO",
    text = "Se um dos KOFFING<NEXT>gêmeos incha, o<NEXT>outro murcha. Ele",
    text2 = "mistura os gases<NEXT>venenosos dele o<NEXT>tempo todo.",
    height = 102, weight = 95,   -- 1,2 m / 9,5 kg
  },
  ["WIGGLYTUFF"] = {
    kind = "BALÃO",
    text = "O pelo deles é tão<NEXT>gostoso que se<NEXT>dois se aconchegam",
    text2 = "juntos, não vão<NEXT>mais querer se<NEXT>separar.",
    height = 100, weight = 120,   -- 1,0 m / 12,0 kg
  },
  ["WOBBUFFET"] = {
    kind = "PACIENTE",
    text = "Ele odeia luz e<NEXT>tranco. Se for<NEXT>atacado, ele incha",
    text2 = "o corpo para dar<NEXT>mais força no<NEXT>contra-ataque.",
    height = 103, weight = 285,   -- 1,3 m / 28,5 kg
  },
  ["WOOPER"] = {
    kind = "PEIXE ÁGUA",
    text = "Este POKéMON vive<NEXT>em água fria. Sai<NEXT>da água para",
    text2 = "procurar comida<NEXT>quando esfria<NEXT>lá fora.",
    height = 4, weight = 85,   -- 0,4 m / 8,5 kg
  },
  ["XATU"] = {
    kind = "MÍSTICO",
    text = "Dizem que ele fica<NEXT>parado e quieto<NEXT>porque está vendo",
    text2 = "o passado e o<NEXT>futuro ao mesmo<NEXT>tempo.",
    height = 105, weight = 150,   -- 1,5 m / 15,0 kg
  },
  ["YANMA"] = {
    kind = "ASA CLARA",
    text = "Se ele bate as<NEXT>asas bem rápido,<NEXT>consegue criar",
    text2 = "ondas de choque<NEXT>que quebram as<NEXT>janelas da região.",
    height = 102, weight = 380,   -- 1,2 m / 38,0 kg
  },
  ["ZAPDOS"] = {
    kind = "ELÉTRICO",
    text = "Esta ave POKéMON<NEXT>lendária causa<NEXT>tempestades",
    text2 = "selvagens batendo<NEXT>as asas<NEXT>reluzentes dela.",
    height = 106, weight = 526,   -- 1,6 m / 52,6 kg
  },
  ["ZUBAT"] = {
    kind = "MORCEGO",
    text = "Enquanto voa, ele<NEXT>solta sem parar<NEXT>ondas de som pela",
    text2 = "boca para checar<NEXT>o que há em volta<NEXT>dele.",
    height = 8, weight = 75,   -- 0,8 m / 7,5 kg
  },
}

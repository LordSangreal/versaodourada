# -*- coding: utf-8 -*-
"""Lote 1 -- New Bark Town, casa do jogador, laboratorio e casa do Elm.

Traduzido a partir do ingles original.  Chave = ponteiro da ROM USA.

Tres regras, verificadas por tools/conferir.py antes de publicar:
  1. `\\n`, `\\v` e `\\f` sobrevivem na MESMA ordem e quantidade -- sao quebra
     de linha, rolagem e quebra de pagina.  Errar isso embaralha a caixa.
  2. Os tokens ({PLAYER}, {RIVAL}, {STRBUF}) idem.
  3. Cada linha cabe em 18 colunas, contando os tokens pelo que rendem.

Ficam no original: nomes de POKéMON, de personagens, de cidades e de itens
proprios (POKéGEAR, POKéDEX, EVERSTONE, S.S.TICKET, MASTER BALL).
"""

DIALOGO = {
    # ---------------- New Bark Town ----------------
    "48:4101": "Uau, sua POKéGEAR\né incrível!\fFoi sua mãe quem\nlhe deu ela?",
    "48:413e": "Espere, {PLAYER}!",
    "48:4148": "O que você pensa\nque está fazendo?",
    "48:4168": "É perigoso sair\nsem um\vPOKéMON!\fPOKéMON selvagens\npulam do mato\fno caminho para\na próxima cidade.",
    "48:41ce": "Oh! Seu POKéMON\né adorável!\vQueria ter um!",
    "48:41fc": "Oi, {PLAYER}!\nSaindo de novo?\fVocê devia avisar\nsua mãe quando\vsair.",
    "48:4240": "Ligue para sua mãe\nna POKéGEAR para\fcontar como você\nestá indo.",
    "48:427e": "Ei, {PLAYER}!\fSoube que o PROF.\nELM descobriu\vnovos POKéMON.",
    "48:42b0": "……\fEntão este é o\nfamoso LAB POKéMON\vdo ELM…",
    "48:42d7": "…O que você está\nolhando?",
    "48:42f2": "CIDADE NEW BARK\fA cidade onde\nos ventos do\vrecomeço sopram",
    "48:4332": "Casa de {PLAYER}",
    "48:433c": "LAB POKéMON ELM",
    "48:434a": "CASA DO ELM",

    # ---------------- Laboratorio do Elm ----------------
    "60:43f7": "ELM: {PLAYER}!\nAí está você!\fPreciso lhe pedir\num favor.\fTenho um conhecido\nchamado MR.\vPOKéMON.\fEle vive achando\ncoisas estranhas\fe se gabando das\ndescobertas.\fEnfim, recebi um\ne-mail dele agora\fdizendo que desta\nvez é de verdade.\fÉ intrigante, mas\nestamos ocupados\fcom nossa pesquisa\nde POKéMON.\fVocê poderia ir\nver isso por nós?\fVou lhe dar um\nPOKéMON de\vparceiro.\fSão todos POKéMON\nraros que acabamos\vde encontrar.\fEscolha um deles!",
    "60:4590": "Se um POKéMON\nselvagem aparecer,\vdeixe o seu lutar",
    "60:45c2": "ELM: Espere! Aonde\nvocê vai?",
    "60:45e3": "ELM: Vai levar o\nCYNDAQUIL, o\vPOKéMON de fogo?",
    "60:460e": "ELM: Você quer o\nTOTODILE, o\vPOKéMON de água?",
    "60:463a": "ELM: Então gosta\nda CHIKORITA, a\vPOKéMON planta?",
    "60:4668": "ELM: Pense bem\ncom calma.\fSeu parceiro é\nimportante.",
    "60:46a2": "ELM: Acho esse\num ótimo\vPOKéMON também!",
    "60:46c8": "{PLAYER} recebeu\n{STRBUF}!",
    "60:46db": "MR.POKéMON mora\nperto de\vCHERRYGROVE.\fA próxima cidade.\nÉ quase direto\vdaqui.",
    "60:472f": "Se seu POKéMON se\nmachucar, cure\fele nesta\nmáquina.",
    "60:476c": "Ah, aqui está meu\ntelefone.\fMe ligue se algo\nacontecer.",
    "60:47a9": "{PLAYER} anotou o\ntelefone do ELM.",
    "60:47c3": "MR.POKéMON vai a\ntoda parte e acha\vraridades.\fPena que sejam só\nraras e não muito\vúteis…\f{PLAYER}, conto\ncom você!",
    "60:4835": "Contém um POKéMON\ncapturado pelo\vPROF.ELM.",
    "60:485d": "Será que isto faz\no quê?",
    "60:4877": "Curar POKéMON?",
    "60:4883": "ELM: {PLAYER}, isto\né terrível…\fAh, sim, qual foi\na descoberta do\vMR.POKéMON?",
    "60:48c8": "{PLAYER} entregou\no OVO MISTERIOSO\vao PROF.ELM.",
    "60:48ef": "ELM: Isto?",
    "60:48fb": "Mas… Será um OVO\nde POKéMON?\fSe for, é um\ngrande achado!",
    "60:4936": "ELM: O quê?!?\fO PROF.OAK lhe deu\numa POKéDEX?\f{PLAYER}, é verdade\nmesmo? I-isso é\vincrível!\fEle é ótimo em ver\no potencial das\vpessoas como\vtreinadores.\fUau, {PLAYER}. Você\npode ter o que é\fpreciso para virar\nCAMPEÃO.\fParece que você se\ndá muito bem\vcom POKéMON.\fVocê devia encarar\no desafio do\vGINÁSIO POKéMON.\fO GINÁSIO mais\nperto fica em\vVIOLET CITY.",
    "60:4a85": "…{PLAYER}. O\ncaminho até o\fcampeonato vai ser\nlongo.\fAntes de partir,\nnão esqueça de\vfalar com sua mãe",
    "60:4af2": "ELM: Não desista!\nEu ligo se souber\fde algo sobre\naquele OVO!",
    "60:4b33": "ELM: {PLAYER}?\nVocê não achou meu\vassistente?\fEle devia lhe\nentregar o OVO\fno CENTRO POKéMON\nde VIOLET CITY.\fVocê deve ter\nperdido ele. Tente\vencontrá-lo lá.",
    "60:4bd1": "ELM: Ei, aquele\nOVO mudou algo?",
    "60:4bf6": "{PLAYER}? Pensei\nque o OVO chocou.\fCadê o\nPOKéMON?",
    "60:4c28": "ELM: {PLAYER}, você\nestá ótimo!",
    "60:4c41": "O quê?\nAquele POKéMON!?!",
    "60:4c55": "O OVO chocou!\nEntão POKéMON\vnascem de OVOS…\fNão, talvez não\ntodos eles.\fUau, ainda há\nmuita pesquisa\vpela frente.",
    "60:4cd2": "Obrigado, {PLAYER}!\nVocê nos ajuda a\fdesvendar os\nmistérios POKéMON\fQuero que fique\ncom isto em sinal\vda nossa gratidão",
    "60:4d43": "Isso é uma\nEVERSTONE.\fCertas espécies de\nPOKéMON evoluem\fao chegar a certos\nníveis.\fUm POKéMON segu-\nrando a EVERSTONE\vnão evolui.\fDê a um POKéMON\nque você não quer\vque evolua.",
    "60:4ded": "ELM: {PLAYER}, eu\nligo se algo\vacontecer.",
    "60:4e1b": "…ai… Aquele\nPOKéMON roubado.\fFico pensando como\nele está.\fDizem que POKéMON\ncriado por gente\fruim fica ruim\ntambém.",
    "60:4e86": "ELM: Oi, {PLAYER}!\nGraças a você,\fminha pesquisa vai\nmuito bem!\fLeve isto como\nsinal da minha\vgratidão.",
    "60:4ee7": "A MASTER BALL é a\nmelhor de todas!\fÉ a BALL suprema!\nCaptura qualquer\fPOKéMON sem\nfalhar nunca.\fSó é dada a\npesquisadores\vPOKéMON de renome\fAcho que você faz\nmelhor uso dela\fdo que eu,\n{PLAYER}!",
    "60:4fa4": "ELM: {PLAYER}!\nAí está você!\fLiguei porque\ntenho algo para\vvocê.\fViu? É um\nS.S.TICKET.\fAgora pode pegar\nPOKéMON em KANTO.",
    "60:5020": "O navio parte de\nOLIVINE CITY.\fMas isso você já\nsabia, {PLAYER}.\fAfinal, você foi\na toda parte\vcom seus POKéMON.\fMande lembranças\nao PROF.OAK!",
    "60:50e9": "{PLAYER}, quero que\nfique com isto\vpara a sua missão",
    "60:5116": "Somos só nós dois,\nentão vivemos\vsempre ocupados.",
    "60:5146": "Houve um barulho\nalto lá fora…\fQuando fomos ver,\nroubaram um\vPOKéMON daqui.\fÉ inacreditável\nque alguém faça\visso!\f…ai… Aquele\nPOKéMON roubado.\fFico pensando como\nele está.\fDizem que POKéMON\ncriado por gente\fruim fica ruim\ntambém.",
    "60:5229": "{PLAYER}!\fUse isto na sua\njornada POKéDEX!",
    "60:524b": "Para completar a\nPOKéDEX, você tem\vque pegar POKéMON\fJogue POKé BALLS\nnos POKéMON\vselvagens.",
    "60:52a1": "Soube que roubaram\num POKéMON aqui…\fEu estava colhendo\ninformações com o\vPROF.ELM.\fPelo visto era um\njovem de cabelo\vlongo e vermelho…\fO quê?\fVocê lutou com um\ntreinador assim?\fPor acaso soube\no nome dele?",
    "60:5371": "Certo! Então\n{RIVAL} é o nome.\fObrigado por\najudar na busca!",
    "60:53ae": "Janela aberta.\fUma brisa gostosa\nentra por ela.",
    "60:53e2": "Ele entrou\npor aqui!",
    "60:53fd": "{PLAYER} abriu um\nlivro.\fDica de viagem 1:\fAperte START para\nabrir o MENU.",
    "60:543b": "{PLAYER} abriu um\nlivro.\fDica de viagem 2:\fRegistre a viagem\ncom SAVE!",
    "60:5477": "{PLAYER} abriu um\nlivro.\fDica de viagem 3:\fAbra a BOLSA e\naperte SELECT para\vmover itens.",
    "60:54c6": "{PLAYER} abriu um\nlivro.\fDica de viagem 4:\fVeja os movimentos\ndo POKéMON. Use\fo botão A para\ntrocar de lugar.",
    "60:5521": "A embalagem do\nlanche que o PROF.\vELM comeu está aí",

    # ---------------- Casa do jogador ----------------
    "60:5719": "Ah, {PLAYER}! Nosso\nvizinho, o PROF.\fELM, estava\nprocurando você.\fDisse que queria\nque você fizesse\valgo para ele.\fAh! Quase esqueci!\nSua POKéMON GEAR\fvoltou do\nconserto.\fAqui está!",
    "60:57d2": "POKéMON GEAR, ou\nsó POKéGEAR.\fÉ essencial se\nvocê quer ser um\vbom treinador.\fAh, falta ajustar\no dia da semana.\fNão pode esquecer\ndisso!",
    "60:5857": "Estamos no horário\nde verão agora?",
    "60:5878": "Volte para casa\npara ajustar o\frelógio no horário\nde verão.\fA propósito, você\nsabe usar o\vTELEFONE?",
    "60:58e0": "Não é só ligar a\nPOKéGEAR e\fescolher o ícone\ndo TELEFONE?",
    "60:591c": "Vou ler as\ninstruções.\fLigue a POKéGEAR e\nescolha o ícone\vdo TELEFONE.",
    "60:5965": "Os números ficam\nsalvos na memória\fÉ só escolher o\nnome para ligar.\fQue prático,\nnão é mesmo?",
    "60:59ca": "O PROF.ELM está\nesperando você.\fVá logo, querido!",
    "60:59fa": "E aí, qual era\na missão do ELM?\f…\fIsso parece\nmesmo um desafio.\fMas orgulhe-se de\nque as pessoas\vcontam com você.",
    "60:5a6c": "{PLAYER}, vá!\fEstou com você\naté o fim!",
    "60:5a92": "Prato da mamãe!\fHAMBÚRGUER VULCÃO\nDE CINNABAR!",
    "60:5abc": "A pia está\nimpecável. A mamãe\vgosta dela limpa.",
    "60:5ae9": "Vamos ver o que há\nna geladeira…\fFRESH WATER e uma\nboa LEMONADE!",
    "60:5b28": "Passa um filme na\nTV: estrelas no\fcéu e dois\nmeninos no trem…\fÉ melhor eu ir\nandando também!",

    # ---------------- Quarto do jogador ----------------
    "60:5c5c": "POKéMON TALK DO\nPROF.OAK! Não\vperca a próxima!",
    "60:5c8d": "CANAL POKéMON!",
    "60:5c9c": "Aqui é a DJ MARY,\nsua parceira!",
    "60:5cbc": "POKéMON!\nCANAL POKéMON…",

    # ---------------- Casa do Elm ----------------
    "60:5eb8": "Oi, {PLAYER}! Meu\nmarido vive tão\focupado… espero\nque ele fique bem\fQuando mergulha na\npesquisa POKéMON,\fele até esquece\nde comer.",
    "60:5f2c": "Quando eu crescer,\nvou ajudar o meu\vpai!\fVou ser um grande\nprofessor\vPOKéMON!",
    "60:5fdc": "POKéMON. De onde\neles vêm?\fPara onde eles\nvão?\fPor que ninguém\nnunca viu um\vPOKéMON nascer?\fQuero saber! Vou\ndedicar a vida\fao estudo dos\nPOKéMON!\f…\fFaz parte dos\nartigos de\vpesquisa do ELM.",
}

# -*- coding: utf-8 -*-
"""Lote 0 -- texto do motor: batalha, menus, opcoes, launcher.

Chave = a string em ingles exatamente como o codigo-fonte a escreve.
Traduzido do ingles, do zero.

Duas regras que valem para tudo aqui:
  1. As diretivas %s / %d tem que sobreviver na MESMA quantidade.  A ordem e
     livre: o motor substitui na ordem em que aparecem.
  2. Cada linha entre \\n cabe em 18 colunas -- e a largura da caixa.  Vale
     para o texto de jogo; o launcher tem tela cheia e nao sofre disso.
"""

SISTEMA = {
    # ================= menu de batalha =================
    "battle|FIGHT": "LUTAR",
    "battle|ITEM": "ITENS",
    "battle|RUN": "FUGIR",
    "FIGHT": "LUTAR",
    "ITEM": "ITENS",
    "RUN": "FUGIR",
    "BALLx": "BOLAx",
    "BAIT": "ISCA",
    "THROW ROCK": "JOGAR PEDRA",
    "TYPE/": "TIPO/",
    "disabled!": "desabilitado!",
    "What will": "O que",
    " do?": " vai fazer?",
    "FOE": "INIMIGO",
    "OLD MAN": "VELHO",
    "POKé BALL": "POKé BALL",
    "Use next POKéMON?": "Usar outro POKéMON?",
    "NICKNAME?": "APELIDO?",
    "someone's PC": "o PC de alguém",

    # ================= atributos =================
    "ATTACK": "ATAQUE",
    "DEFENSE": "DEFESA",
    "SPEED": "VELOCIDADE",
    "SPECIAL": "ESPECIAL",

    # ================= batalha: entrada e saida =================
    "Enemy %s": "%s inimigo",
    "%s wants\nto fight!": "%s quer\nlutar!",
    "Wild %s\nappeared!": "%s selvagem\napareceu!",
    "Go! %s!": "Vai, %s!",
    "Do it! %s!": "Manda ver, %s!",
    "Get'm! %s!": "Pega ele, %s!",
    "%s sent\nout %s!": "%s mandou\n%s!",
    "%s with-\ndrew %s!": "%s chamou\n%s de volta!",
    "%s is\nalready out!": "%s já\nestá em campo!",
    "Will %s\nchange POKéMON?": "%s vai\ntrocar de POKéMON?",
    "%s is\nabout to use\x0b%s!": "%s vai\nusar %s!",

    # ================= batalha: acoes e resultado =================
    "%s\nused %s!": "%s usou\n%s!",
    "%s\nfainted!": "%s\ndesmaiou!",
    "But, it failed!": "Mas falhou!",
    "But nothing\nhappened.": "Mas nada\naconteceu.",
    "%s has no\nmoves left!": "%s não tem\nmais movimentos!",
    "%s is too\nscared to move!": "%s está com\nmedo demais!",
    "%s\nis storing energy!": "%s está\njuntando energia!",
    "%s is out of\nuseable POKéMON!": "%s não tem\nmais POKéMON!",
    "%s blacked\nout!": "%s\napagou!",
    "%s grew\nto level %d!": "%s subiu\nao nível %d!",

    # ================= batalha: atributos e status =================
    "%s's\n%s rose!": "%s teve\n%s aumentado!",
    "%s's\n%s\ngreatly rose!": "%s teve\n%s\nmuito aumentado!",
    "%s's\n%s fell!": "%s teve\n%s reduzido!",
    "%s's\n%s\ngreatly fell!": "%s teve\n%s\nmuito reduzido!",
    "%s\nwas afflicted\nby %s!": "%s foi\natingido por\n%s!",
    "%s's\nprotected against\nstat changes!": "%s está\nprotegido contra\nmudanças!",
    "%s is\nprotected by MIST!": "%s está\nprotegido pelo MIST!",

    # ================= batalha: captura =================
    "%s used\nPOKé BALL!": "%s usou\nPOKé BALL!",
    "%s used\nSAFARI BALL!": "%s usou\nSAFARI BALL!",
    "All right!\n%s was\ncaught!": "Boa!\n%s foi\ncapturado!",
    "Darn! The POKéMON\nbroke free!": "Droga! O POKéMON\nescapou!",
    "It dodged the\nthrown BALL!": "Ele desviou\nda BALL!",
    "You missed the\nPOKéMON!": "Você errou o\nPOKéMON!",
    "This POKéMON\ncan't be caught!": "Este POKéMON\nnão pode ser pego!",
    "New POKéDEX data\nwill be added for\n%s!": "Novos dados da\nPOKéDEX para\n%s!",
    "%s was\ntransferred to\n%s!": "%s foi\nenviado para\n%s!",
    "But every BOX\nis full!": "Mas todo BOX\nestá cheio!",
    "No! There's no\nrunning from a\x0btrainer battle!":
        "Não dá para fugir\nde uma batalha\x0bde treinador!",
    "PA: You're out of\nSAFARI BALLs!\nGame over!":
        "PA: Acabaram suas\nSAFARI BALLs!\nFim de jogo!",

    # ================= batalha: contextos e enredo =================
    "In battle": "Em batalha",
    "Wild battle": "Batalha selvagem",
    "Trainer battle": "Batalha de treinador",
    "Link battle": "Batalha por link",
    "Title screen": "Tela de título",
    "The GHOST\nappeared!": "O FANTASMA\napareceu!",
    "GHOST: Get out...\nGet out...": "FANTASMA: Saia...\nSaia...",
    "SILPH SCOPE\nunveiled the\x0bGHOST's identity!":
        "A SILPH SCOPE\nrevelou quem era\x0bo FANTASMA!",
    "{RIVAL}: Yeah! Am\nI great or what?": "{RIVAL}: Isso! Eu\nsou bom ou não sou?",
    "OAK: {PLAYER}!\nThis isn't the\x0btime to use that!":
        "OAK: {PLAYER}!\nNão é hora de\x0busar isso!",

    # ================= mundo e itens =================
    "{PLAYER} used the\n%s.": "{PLAYER} usou\no %s.",
    "The REPEL used\nearlier is still\x0bin effect.":
        "O REPEL de antes\nainda está\x0bfazendo efeito.",
    "You don't have a\n#MON!": "Você não tem\nnenhum POKéMON!",
    "An item in your\nPACK may be\x0cregistered for use\non SELECT Button.":
        "Um item da BOLSA\npode ser ligado\x0cao botão SELECT\npara uso rápido.",
    "There was a trophy\ninside!\x0cThe trophy was\nsent home.":
        "Havia um troféu\ndentro!\x0cO troféu foi\nmandado para casa.",

    # ================= opcoes do jogo =================
    "OPTIONS": "OPÇÕES",
    "TEXT SPEED": "VEL. DO TEXTO",
    "BATTLE ANIMATION": "ANIMAÇÃO",
    "BATTLE STYLE": "ESTILO DE LUTA",
    "BATTLE LAYOUT": "LAYOUT DE LUTA",
    "BATTLE SIZE": "TAMANHO DA LUTA",
    "BATTLE BG": "FUNDO DE LUTA",
    "BATTLE SCENE": "CENA DE LUTA",
    "UI LAYOUT": "LAYOUT DA TELA",
    "GAME SPEED": "VEL. DO JOGO",
    "OVERWORLD SPEED": "VEL. NO MAPA",
    "BATTLE SPEED": "VEL. NA LUTA",
    "MENU SPEED": "VEL. DOS MENUS",
    "SOUND": "SOM",
    "PRINT": "IMPRIMIR",
    "MENU ACCOUNT": "CONTA NO MENU",
    "FRAME": "MOLDURA",
    "COLOR": "COR",
    "COLORS": "CORES",

    # ================= audio e video =================
    "MUSIC VOL": "VOL. MÚSICA",
    "SFX VOL": "VOL. EFEITOS",
    "MUSIC FILTER": "FILTRO DE SOM",
    "options.musicFilter|OFF": "DESL",
    "PERFORMANCE": "DESEMPENHO",
    "VIDEO MODE": "MODO DE VÍDEO",
    "ORIENTATION": "ORIENTAÇÃO",
    "FAITHFUL RATIO": "PROPORÇÃO FIEL",
    "MAX FPS": "FPS MÁXIMO",
    "GBC FX": "EFEITOS GBC",
    "VOID FILL": "PREENCHIMENTO",
    "TILT": "INCLINAÇÃO",

    # ================= controles =================
    "TOUCH PAD": "TOQUE",
    "TOUCH CONTROLS": "CONTROLES DE TOQUE",
    "VIBRATION": "VIBRAÇÃO",
    "RESET REBINDS": "LIMPAR TECLAS",
    "RESET DEFAULTS": "RESTAURAR PADRÃO",
    "Edit": "Editar",
    "Reset": "Restaurar",
    "ON": "LIG",
    "OFF": "DESL",

    # ================= launcher: importar a ROM =================
    "Import ROM": "Importar ROM",
    "Re-import ROM": "Reimportar ROM",
    "Import detected ROM": "Importar ROM encontrada",
    "No ROM imported": "Nenhuma ROM importada",
    "Compatible ROM found": "ROM compatível encontrada",
    "Found in baseroms/: %s": "Encontrada em baseroms/: %s",
    "Checking baseroms...": "Verificando baseroms...",
    "Looking for compatible Red, Blue, and Yellow ROMs.":
        "Procurando ROMs compatíveis de Red, Blue e Yellow.",
    "Importing": "Importando",
    "Import failed": "Falha na importação",
    "That ROM could not be imported.": "Não foi possível importar essa ROM.",
    "Import unavailable": "Importação indisponível",
    "Copy the .gb/.gbc via MTP into imports/.":
        "Copie o .gb/.gbc por MTP para imports/.",
    "Or copy the .gb/.gbc into baseroms/.":
        "Ou copie o .gb/.gbc para baseroms/.",
    "Copy the .gb/.gbc via USB.": "Copie o .gb/.gbc por USB.",
    "Or drop the .gb/.gbc file here.": "Ou arraste o arquivo .gb/.gbc aqui.",
    "The ROM is verified before any files are created. ":
        "A ROM é verificada antes de qualquer arquivo ser criado. ",
    "The ROM for this game is imported and verified.":
        "A ROM deste jogo foi importada e verificada.",
    "Update required": "Atualização necessária",
    "This build needs a few more things from your ":
        "Esta versão precisa de mais alguns dados da sua ",
    " ROM. Re-import to continue.": " ROM. Reimporte para continuar.",
    "Not supported yet": "Ainda não suportado",
    "Support for this game is on the way.":
        "O suporte a este jogo está a caminho.",
    "Scan again": "Procurar de novo",
    "Check again": "Verificar de novo",
    "No new ROM found.": "Nenhuma ROM nova encontrada.",
    "No matching ROM found.": "Nenhuma ROM compatível encontrada.",
    "Copy your .gb/.gbc into:": "Copie seu .gb/.gbc para:",

    # ================= launcher: saves =================
    "SAVE SLOT": "ESPAÇO DE SAVE",
    "Import save": "Importar save",
    "1 slot": "1 espaço",
    "%d slots": "%d espaços",
    "No saves yet - start a new game or import one.":
        "Nenhum save ainda - comece um jogo novo ou importe um.",
    "NEW GAME": "JOGO NOVO",
    "LOADED": "CARREGADO",
    "%d badges - %s - %d caught": "%d insígnias - %s - %d capturados",
    "empty slot": "espaço vazio",
    "+ New save slot": "+ Novo espaço de save",
    "Open folder": "Abrir pasta",
    "Export": "Exportar",
    "Rename": "Renomear",
    "Name save slot": "Nomear o espaço de save",
    "Choose a .sav save file": "Escolha um arquivo .sav",
    "Imported %d saves into %s. Active: %s.":
        "%d saves importados para %s. Ativo: %s.",
    "Already imported — %d file(s) skipped. Check SAVE SLOT.":
        "Já importado — %d arquivo(s) pulado(s). Veja ESPAÇO DE SAVE.",

    # ================= launcher: estado do jogo =================
    "GOOD TO GO": "TUDO PRONTO",
    "ROM FOUND": "ROM ENCONTRADA",
    "COMING SOON": "EM BREVE",
    "ROM REQUIRED": "PRECISA DA ROM",
    "Play ": "Jogar ",
    "Run": "Executar",
    "Manage ": "Gerenciar ",
    "Settings": "Ajustes",
    "Saved to your options file; the game applies these on its next start.":
        "Salvo no seu arquivo de opções; o jogo aplica na próxima vez que abrir.",

    # ================= versoes =================
    "RED": "RED",
    "BLUE": "BLUE",
    "YELLOW": "YELLOW",
    "GOLD": "GOLD",

    # ================= gerenciador de mods =================
    "MODS": "MODS",
    "FIND MODS": "BUSCAR MODS",
    "Ready": "Pronto",
    "Conflict": "Conflito",
    "Not for this game": "Não é deste jogo",
    "Incompatible": "Incompatível",
    "Show for:": "Mostrar para:",
    "All games": "Todos os jogos",
    "All": "Todos",
    "Install": "Instalar",
    "Update": "Atualizar",
    "Reinstall": "Reinstalar",
    "Delete": "Excluir",
    "Sure?": "Tem certeza?",
    "Checking...": "Verificando...",
    "Restart to update": "Reinicie para atualizar",
    "Open releases": "Abrir releases",
    "Check for updates": "Procurar atualizações",
    "Enable all": "Ligar todos",
    "Disable all": "Desligar todos",
    "Every mod is already enabled.": "Todos os mods já estão ligados.",
    "Every mod is already disabled.": "Todos os mods já estão desligados.",
    "Enabled %d mods.": "%d mods ligados.",
    "Disabled %d mods.": "%d mods desligados.",
    "Choose a mod .zip": "Escolha um .zip de mod",
    "Sort by": "Ordenar por",
    "Filter by category": "Filtrar por categoria",
    "Versions": "Versões",
    "Details": "Detalhes",
    "Source": "Origem",
    "Loading versions": "Carregando versões",
    "Checking for updates": "Procurando atualizações",
    "Downloading %s": "Baixando %s",
    "Installing %s": "Instalando %s",
    "Working": "Trabalhando",
    "(No release notes.)": "(Sem notas de versão.)",
    " notes": " notas",
    "(No description.)": "(Sem descrição.)",

    # ================= indices de mod =================
    "No mod index added": "Nenhum índice de mod",
    "Add an index to browse mods. An index is a published list; paste its URL or its owner/repo.":
        "Adicione um índice para ver mods. Um índice é uma lista publicada; "
        "cole a URL dele ou o dono/repositório.",
    "Add an index": "Adicionar um índice",
    "Add a mod index": "Adicionar um índice de mod",
    "Paste the index URL, or its owner/repo.":
        "Cole a URL do índice, ou o dono/repositório.",
    "Indexes": "Índices",
    "Mod indexes": "Índices de mod",
    "No index added yet.": "Nenhum índice adicionado.",
    "Add index": "Adicionar índice",
    "Refresh all": "Atualizar tudo",
    "Loading mod index": "Carregando índice de mods",
    "This index lists no mods yet.": "Este índice ainda não lista mods.",
    "No mods match that search.": "Nenhum mod corresponde à busca.",
    "Not installable from this index": "Não instalável por este índice",
    "Search mods": "Buscar mods",
    "Filter": "Filtrar",
    "Sort": "Ordenar",
    "Name": "Nome",
    "Popularity": "Popularidade",
    "Release date": "Data de lançamento",
    "Last updated": "Última atualização",
    "Updating %d%%": "Atualizando %d%%",
    "Update v": "Atualizar v",
    "v%s available": "v%s disponível",
    "up to date": "atualizado",
    "Up to date": "Atualizado",
    "check failed": "falha ao verificar",
    "Other versions: ": "Outras versões: ",
    "Installed: v": "Instalado: v",
    " (installed)": " (instalado)",
    "Read more": "Ler mais",

    # ================= botoes e teclas =================
    "Save": "Salvar",
    "Cancel": "Cancelar",
    "Paste": "Colar",
    "Confirm": "Confirmar",
    "OK": "OK",
    "Close": "Fechar",
    "Remove": "Remover",
    "Add": "Adicionar",
    "Enter to save - Esc to cancel": "Enter salva - Esc cancela",
    "Enter to save - Esc to cancel - empty clears":
        "Enter salva - Esc cancela - vazio limpa",
    "Enter to add - Esc to cancel": "Enter adiciona - Esc cancela",
}

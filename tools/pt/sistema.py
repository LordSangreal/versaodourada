# -*- coding: utf-8 -*-
"""Lote 0 -- texto do motor: batalha, menus, opcoes, launcher.

Chave = a string em ingles exatamente como o codigo-fonte a escreve.
Traduzido do ingles, do zero.

Duas regras que valem para tudo aqui:
  1. As diretivas %s / %d tem que sobreviver na MESMA quantidade.  A ordem e
     livre: o motor substitui na ordem em que aparecem.
  2. Cada linha entre \\n cabe em 18 colunas -- e a largura da caixa.
"""

SISTEMA = {
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
    "All stat changes": "Todas as mudanças",

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

    # ================= mundo e itens =================
    "{PLAYER} used the\n%s.": "{PLAYER} usou\no %s.",
    "The REPEL used\nearlier is still\x0bin effect.":
        "O REPEL de antes\nainda está\x0bfazendo efeito.",
    "You don't have a\n#MON!": "Você não tem\nnenhum POKéMON!",
    "An item in your\nPACK may be\x0cregistered for use\non SELECT Button.":
        "Um item da BOLSA\npode ser ligado\x0cao botão SELECT\npara uso rápido.",
    "There was a trophy\ninside!\x0cThe trophy was\nsent home.":
        "Havia um troféu\ndentro!\x0cO troféu foi\nmandado para casa.",

    # ================= launcher: importar a ROM =================
    "Import ROM": "Importar ROM",
    "Re-import ROM": "Reimportar ROM",
    "Import detected ROM": "Importar ROM encontrada",
    "No ROM imported": "Nenhuma ROM importada",
    "Compatible ROM found": "ROM compatível encontrada",
    "Found in baseroms/: %s": "Encontrada em baseroms/: %s",
    "Checking baseroms...": "Verificando baseroms...",
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
    "Update required": "Atualização necessária",
    "This build needs a few more things from your ":
        "Esta versão precisa de mais alguns dados da sua ",
    " ROM. Re-import to continue.": " ROM. Reimporte para continuar.",
    "Not supported yet": "Ainda não suportado",
    "Support for this game is on the way.":
        "O suporte a este jogo está a caminho.",
    "Scan again": "Procurar de novo",

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

    # ================= launcher: estado do jogo =================
    "GOOD TO GO": "TUDO PRONTO",
    "ROM FOUND": "ROM ENCONTRADA",
    "COMING SOON": "EM BREVE",
    "ROM REQUIRED": "PRECISA DA ROM",
    "Play ": "Jogar ",

    # ================= catalogo de mods =================
    "No mod index added": "Nenhum índice de mod",
    "Add an index to browse mods. An index is a published list; paste its URL or its owner/repo.":
        "Adicione um índice para ver mods. Um índice é uma lista publicada; "
        "cole a URL dele ou o dono/repositório.",
    "Add an index": "Adicionar um índice",
    "Indexes": "Índices",
    "This index lists no mods yet.": "Este índice ainda não lista mods.",
    "No mods match that search.": "Nenhum mod corresponde à busca.",
    "Search mods": "Buscar mods",
    "Filter": "Filtrar",
    "Sort": "Ordenar",
    "Name": "Nome",
    "Popularity": "Popularidade",
    "Release date": "Data de lançamento",
    "Last updated": "Última atualização",
    "Not installable from this index": "Não instalável por este índice",
    "Updating %d%%": "Atualizando %d%%",
    "v%s available": "v%s disponível",
    "up to date": "atualizado",
    "Up to date": "Atualizado",
    "check failed": "falha ao verificar",
    "Other versions: ": "Outras versões: ",
    "Installed: v": "Instalado: v",
    " (installed)": " (instalado)",
    "Read more": "Ler mais",

    # ================= botoes comuns =================
    "Save": "Salvar",
    "Cancel": "Cancelar",
    "Paste": "Colar",
    "Confirm": "Confirmar",
    "OK": "OK",
}

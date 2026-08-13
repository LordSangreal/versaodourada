# -*- coding: utf-8 -*-
"""Lote 0b -- interface: link, PC/Box, gerenciador de mods, teclas.

Continuacao de pt/sistema.py.  Chave = a string em ingles como o codigo a
escreve.  Traduzido do zero.

Nomes de empresa (GAME FREAK, Nintendo, Creatures inc.) NAO entram aqui:
sao razao social, nao texto.
"""

SISTEMA = {
    # ================= PC / Box =================
    "WITHDRAW <PK><MN>": "RETIRAR <PK><MN>",
    "DEPOSIT <PK><MN>": "DEPOSITAR <PK><MN>",
    "RELEASE <PK><MN>": "SOLTAR <PK><MN>",
    "CHANGE BOX": "TROCAR BOX",
    "PRINT BOX": "IMPRIMIR BOX",
    "BOX %d (WITHDRAW)": "BOX %d (RETIRAR)",
    "BOX %d (RELEASE)": "BOX %d (SOLTAR)",
    "BOX %d is full!": "BOX %d está cheio!",
    "BOX No.": "BOX Nº",
    "BOX No.%d": "BOX Nº%d",
    "Empty.": "Vazio.",
    "What?": "O quê?",
    "SEE YA!": "ATÉ MAIS!",
    "STATS": "DADOS",
    "CANCEL": "CANCELAR",
    "Level %d": "Nível %d",

    # ================= bolsa =================
    "USE": "USAR",
    "TOSS": "DESCARTAR",
    "Click!": "Clique!",
    "Booted up a TM!": "Ligou uma TM!",

    # ================= jogo em rede =================
    "LINK CABLE (LAN)": "CABO LINK (LAN)",
    "ONLINE MATCH": "PARTIDA ONLINE",
    "TOURNAMENT": "TORNEIO",
    "HOST A GAME": "CRIAR PARTIDA",
    "JOIN A GAME": "ENTRAR NUMA PARTIDA",
    "HOST ONLINE": "CRIAR ONLINE",
    "JOIN ONLINE": "ENTRAR ONLINE",
    "HOST": "CRIAR",
    "JOIN": "ENTRAR",
    "UDP port %s": "porta UDP %s",
    "Port: %s": "Porta: %s",
    "Tell your friend": "Diga ao seu amigo",
    "the code:": "o código:",
    "Friend joins at:": "O amigo entra em:",
    "Waiting for join...": "Esperando alguém...",
    "Calling...": "Chamando...",
    "Exchanging data...": "Trocando dados...",
    "Checking the": "Verificando o",
    "other game...": "outro jogo...",
    "Waiting for the": "Esperando o",
    "host to choose...": "anfitrião escolher...",
    "Waiting for": "Esperando",
    "players to join:": "jogadores entrarem:",
    "TRADE": "TROCAR",
    "BATTLE": "BATALHAR",
    "LEVELS:": "NÍVEIS:",
    "YOURS": "SEU",
    "THEIRS": "DELE",
    "%s vs %s!": "%s vs %s!",
    "START: create": "START: criar",
    "B: cancel": "B: cancelar",
    "A: continue": "A: seguir",
    "A: join  B: back": "A: entrar  B: voltar",
    "A: connect  B: back": "A: conectar  B: voltar",
    "A: continue  B: back": "A: seguir  B: voltar",
    "A: trade  B: cancel": "A: trocar  B: cancelar",
    "A: trade anyway": "A: trocar mesmo assim",
    "X: not on theirs": "X: não está no dele",
    "A: START  B: cancel": "A: START  B: cancelar",

    # ================= torneio =================
    "TOURNAMENT %s": "TORNEIO %s",
    "ROUND %d": "RODADA %d",
    "%s (bye)": "%s (passa)",
    "%s%s vs %s%s": "%s%s vs %s%s",
    "(organizing --": "(organizando --",
    "not playing)": "não joga)",
    "%s is the": "%s é o",
    "champion!": "campeão!",

    # ================= gerenciador de mods =================
    "MOD MANAGER": "GERENCIADOR DE MODS",
    "NO MODS INSTALLED": "NENHUM MOD INSTALADO",
    "SAVE CURRENT AS..": "SALVAR ATUAL COMO..",
    "EXPORT..": "EXPORTAR..",
    "IMPORT..": "IMPORTAR..",
    "OPTIONS..": "OPÇÕES..",
    "PERMISSIONS..": "PERMISSÕES..",
    "VIEW ERROR..": "VER ERRO..",
    "APPLY & RESTART": "APLICAR E REINICIAR",
    "DISCARD CHANGES": "DESCARTAR MUDANÇAS",
    "NO CHANGES": "SEM MUDANÇAS",
    "PROFILE NAME?": "NOME DO PERFIL?",
    "RENAME?": "RENOMEAR?",
    "DON'T TRY HERE": "NÃO TENTAR AQUI",
    "TRY HERE ANYWAY": "TENTAR MESMO ASSIM",
    "DATA & API ONLY": "SÓ DADOS E API",
    "DISABLE BOTH?": "DESLIGAR OS DOIS?",
    "BACK": "VOLTAR",
    "YES": "SIM",
    "NO": "NÃO",
    "A:OK": "A:OK",
    "B:DONE (NO RESTART)": "B:PRONTO (SEM REINICIAR)",

    # ================= indice de mods =================
    "Import mod .zip": "Importar mod .zip",
    "Or copy a mod .zip via USB.": "Ou copie um .zip de mod por USB.",
    "Fetching mod index": "Buscando índice de mods",
    "%d indexes": "%d índices",
    "Refreshed - %d mods listed": "Atualizado - %d mods listados",
    "Added %s": "%s adicionado",
    "Index removed": "Índice removido",
    "Released %s  -  Updated %s": "Lançado %s  -  Atualizado %s",
    "%s (%s tab)": "%s (aba %s)",

    # ================= teclas =================
    "RESET ALL BINDINGS?": "LIMPAR TODAS AS TECLAS?",
    "PRESS A BUTTON": "APERTE UM BOTÃO",
    "RELEASE TO SET": "SOLTE PARA DEFINIR",
    "ESC/2ND CANCELS": "ESC/2º CANCELA",
}

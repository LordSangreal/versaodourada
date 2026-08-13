# -*- coding: utf-8 -*-
"""Desenha a pagina de glifos acentuados do mod.

Desenhados aqui, do zero.  As regras do gen1recomp proibem distribuir arte
derivada de ROM, entao extrair os tiles acentuados da ROM BR esta fora de
questao -- estes sao bitmaps proprios.

Cada glifo e uma celula 8x8.  Minusculas ocupam as linhas 3-7 (altura de x),
deixando as linhas 0-1 livres para o acento.  Maiusculas sao comprimidas nas
linhas 2-7 para caber o acento em cima, que e o unico jeito de um A com til
existir numa celula de 8 pixels.

A ordem desta lista E o codigo do glifo: o primeiro e 0x100, o segundo
0x101, e assim por diante.  Mexer na ordem sem mexer em lang/charmap.lua
troca as letras de lugar.
"""
import os, struct, zlib

# ---- acentos (linhas 0-1) ------------------------------------------------
AGUDO = ["....##..",
         "...##..."]
GRAVE = ["...##...",
         "....##.."]
CIRCU = ["...##...",
         "..#..#.."]
TIL   = ["..##..#.",
         ".#..##.."]
NADA  = ["........",
         "........"]

# ---- corpos minusculos (linhas 3-7) --------------------------------------
MIN = {
    "a": ["..####..",
          ".....#..",
          "..####..",
          ".#...#..",
          "..#####."],
    "e": ["..####..",
          ".#....#.",
          ".######.",
          ".#......",
          "..#####."],
    "i": ["...#....",
          "...#....",
          "...#....",
          "...#....",
          "...#...."],
    "o": ["..####..",
          ".#....#.",
          ".#....#.",
          ".#....#.",
          "..####.."],
    "u": [".#....#.",
          ".#....#.",
          ".#....#.",
          ".#...##.",
          "..###.#."],
    "c": ["..####..",
          ".#....#.",
          ".#......",
          ".#....#.",
          "..####.."],
}

# ---- corpos maiusculos (linhas 2-7, comprimidos) -------------------------
MAI = {
    "A": ["..####..",
          ".#....#.",
          ".#....#.",
          ".######.",
          ".#....#.",
          ".#....#."],
    "E": [".######.",
          ".#......",
          ".#####..",
          ".#......",
          ".#......",
          ".######."],
    "I": [".#####..",
          "...#....",
          "...#....",
          "...#....",
          "...#....",
          ".#####.."],
    "O": ["..####..",
          ".#....#.",
          ".#....#.",
          ".#....#.",
          ".#....#.",
          "..####.."],
    "U": [".#....#.",
          ".#....#.",
          ".#....#.",
          ".#....#.",
          ".#....#.",
          "..####.."],
    "C": ["..####..",
          ".#....#.",
          ".#......",
          ".#......",
          ".#....#.",
          "..####.."],
}

CEDILHA = "...##..."   # o rabinho do C, desenhado na linha 7


def minuscula(letra, acento):
    g = list(acento) + ["........"] + MIN[letra]
    return g[:8]


def maiuscula(letra, acento):
    g = list(acento) + MAI[letra]
    return g[:8]


# ---- a pagina.  A ORDEM define o codigo, comecando em 0x100 --------------
PAGINA = [
    ("á", minuscula("a", AGUDO)),
    ("â", minuscula("a", CIRCU)),
    ("ã", minuscula("a", TIL)),
    ("à", minuscula("a", GRAVE)),
    ("é", minuscula("e", AGUDO)),
    ("ê", minuscula("e", CIRCU)),
    ("í", minuscula("i", AGUDO)),
    ("ó", minuscula("o", AGUDO)),
    ("ô", minuscula("o", CIRCU)),
    ("õ", minuscula("o", TIL)),
    ("ú", minuscula("u", AGUDO)),
    ("ç", ["........", "........"] + MIN["c"] + [CEDILHA]),
    ("Á", maiuscula("A", AGUDO)),
    ("Â", maiuscula("A", CIRCU)),
    ("Ã", maiuscula("A", TIL)),
    ("À", maiuscula("A", GRAVE)),
    ("É", maiuscula("E", AGUDO)),
    ("Ê", maiuscula("E", CIRCU)),
    ("Í", maiuscula("I", AGUDO)),
    ("Ó", maiuscula("O", AGUDO)),
    ("Ô", maiuscula("O", CIRCU)),
    ("Õ", maiuscula("O", TIL)),
    ("Ú", maiuscula("U", AGUDO)),
    ("Ç", ["........"] + MAI["C"] + [CEDILHA]),
    ("º", ["..###...",
           ".#...#..",
           ".#...#..",
           "..###...",
           "........",
           "........",
           "........",
           "........"]),
]

BASE = 0x100
POR_LINHA = 16


def png(path, largura, altura, pixels):
    """PNG RGBA 8 bits, escrito na mao para nao depender de biblioteca."""
    linhas = b""
    for y in range(altura):
        linhas += b"\x00"
        for x in range(largura):
            linhas += bytes(pixels[y][x])

    def bloco(tipo, dados):
        c = struct.pack(">I", len(dados)) + tipo + dados
        return c + struct.pack(">I", zlib.crc32(tipo + dados) & 0xFFFFFFFF)

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(bloco(b"IHDR", struct.pack(">IIBBBBB", largura, altura, 8, 6, 0, 0, 0)))
        f.write(bloco(b"IDAT", zlib.compress(linhas, 9)))
        f.write(bloco(b"IEND", b""))


def gerar(destino):
    linhas_de_glifo = (len(PAGINA) + POR_LINHA - 1) // POR_LINHA
    largura, altura = POR_LINHA * 8, linhas_de_glifo * 8
    # O fundo tem de ser TRANSPARENTE, nao branco.  O motor decide o que e
    # tinta pelo canal alfa, nao pela luminancia: com fundo branco opaco a
    # celula inteira conta como tinta e a letra sai como um bloco preto
    # solido.  A documentacao fala em "preto no branco", mas a pagina que
    # funciona no jogo e preto no transparente -- foi so comparando os
    # pixels das duas que isto apareceu.
    vazio, preto = (0, 0, 0, 0), (0, 0, 0, 255)
    px = [[vazio] * largura for _ in range(altura)]
    for i, (_ch, arte) in enumerate(PAGINA):
        cx, cy = (i % POR_LINHA) * 8, (i // POR_LINHA) * 8
        assert len(arte) == 8, "%s: %d linhas" % (_ch, len(arte))
        for y, linha in enumerate(arte):
            assert len(linha) == 8, "%s linha %d: %r" % (_ch, y, linha)
            for x, c in enumerate(linha):
                if c == "#":
                    px[cy + y][cx + x] = preto
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    png(destino, largura, altura, px)
    return largura, altura


def charmap():
    return {ch: BASE + i for i, (ch, _) in enumerate(PAGINA)}


if __name__ == "__main__":
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "versaodourada", "assets", "font", "latin.png")
    w, h = gerar(d)
    print("pagina de glifos:", w, "x", h, "|", len(PAGINA), "glifos")
    for ch, code in charmap().items():
        print("   %s -> 0x%X" % (ch, code))

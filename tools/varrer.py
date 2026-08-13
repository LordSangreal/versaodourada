"""Varre a ROM atras de falas que o percurso de scripts nao alcancou.

O percurso (`walk.py`) so encontra o que algum script referencia.  Falas
de treinador ficam em structs que nem sempre sao alcancadas -- foi assim
que "This is pathetic, losing to some rookie trainer…" (56:4635), do
ginasio do FALKNER, ficou de fora das 2245 e apareceu em ingles na tela
mesmo com o lote 3 publicado.

A heuristica nao depende de ponteiro nenhum: em Gen 2 um bloco de texto
termina em 0x50 ou 0x57, entao o endereco logo depois de um terminador e
candidato a inicio de outro bloco.  Decodifica, e o que render prosa
ASCII de tamanho decente entra na lista.

Uso:  python varrer.py            # so o resumo
      python varrer.py 56         # lista o que falta no banco 56
"""
import json, os, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import walk as W
from gen2text import decode

TERMINADORES = (0x50, 0x57)
MIN_LETRAS = 12


def prosa(s):
    """Prosa de jogo: letras ASCII em maioria, sem kana, com espaco."""
    if len(s) < MIN_LETRAS or " " not in s:
        return False
    if any(0x3000 < ord(c) < 0xFF00 for c in s):
        return False
    letras = sum(c.isalpha() and ord(c) < 128 for c in s)
    return letras >= MIN_LETRAS and letras >= 0.5 * len(s)


def varrer(usa, bancos):
    achadas = {}
    for banco in bancos:
        base = banco * 0x4000
        dados = usa.d[base:base + 0x4000]
        if not dados:
            continue
        for i, b in enumerate(dados[:-1]):
            if b not in TERMINADORES:
                continue
            end = 0x4000 + i + 1
            if banco == 0:
                end = i + 1
            try:
                texto, _far = decode(usa, banco, end)
            except Exception:
                continue
            if prosa(texto):
                achadas["%02x:%04x" % (banco, end)] = texto
    return achadas


def main():
    usa = W.Rom(W.USA_PATH)
    dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
    bancos = [int(sys.argv[1], 16)] if len(sys.argv) > 1 else range(0x40, 0x60)
    achadas = varrer(usa, bancos)
    faltando = {k: v for k, v in achadas.items() if k not in dial}
    print("candidatas: %d | ja no dialogo.json: %d | FALTANDO: %d"
          % (len(achadas), len(achadas) - len(faltando), len(faltando)))
    if len(sys.argv) > 1:
        for k in sorted(faltando):
            print("%s  %r" % (k, faltando[k]))
    else:
        porbanco = collections.Counter(k.split(":")[0] for k in faltando)
        for b, n in sorted(porbanco.items()):
            print("  banco %s: %d" % (b, n))


if __name__ == "__main__":
    main()


def gravar():
    """Junta as falas achadas ao dialogo.json, com o BR vazio.

    BR vazio = "nao traduzida": o build deixa em ingles ate um lote
    nosso cobrir a chave.  Nao da para reaproveitar a traducao BR nestas:
    a ROM brasileira repontou o texto, entao o MESMO endereco nas duas
    ROMs nao e a mesma fala.  Estas so podem ser traduzidas do ingles --
    que e o rumo do projeto de qualquer forma.
    """
    usa = W.Rom(W.USA_PATH)
    caminho = os.path.join(HERE, "dialogo.json")
    dial = json.load(open(caminho, encoding="utf-8"))
    achadas = varrer(usa, range(0x40, 0x60))
    novas = 0
    for k, en in achadas.items():
        if k not in dial:
            dial[k] = [en, ""]
            novas += 1
    json.dump(dial, open(caminho, "w", encoding="utf-8"), ensure_ascii=False)
    print("acrescentadas %d falas; dialogo.json agora tem %d" % (novas, len(dial)))

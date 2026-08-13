# -*- coding: utf-8 -*-
"""Escreve a planilha das falas que faltam num banco, ja sem o lixo.

Substitui o filtro que eu vinha escrevendo a mao a cada lote.  Aquele
comparava cada fala pendente contra as OUTRAS PENDENTES -- e por isso ia
piorando: assim que a fala inteira era traduzida ela saia da lista, e a
cauda dela ficava sem par para comparar.  No lote 14b nove caudas
passaram por essa fresta.

Aqui a comparacao e contra o `dialogo.json` INTEIRO, traduzido ou nao.

O que sai fora:
  cauda      o texto e o final de outra fala do mesmo banco, num endereco
             proximo.  O jogo mostra a fala inteira a partir do ponteiro
             de cima, entao traduzir a cauda nao muda nada na tela
  marcador   tem <TARGET>, <USER>, <ENEMY> -- bytes que o motor troca em
             tempo de execucao; o override os publicaria literais
  kana       ponteiro mal alinhado, o texto decodificado e lixo
  curta      menos de 12 letras, quase sempre sobra de dado

Uso:  python pendentes.py 4b            # planilha-pend-4b.py
      python pendentes.py 4b 4c 4d      # varios bancos num arquivo so
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DISTANCIA = 400   # bytes: o quanto uma cauda pode estar longe da fala mae


def kana(s):
    return any(0x3000 < ord(c) < 0xFF00 for c in s)


def caudas(dial):
    """-> chaves cujo texto e o final de outra fala do mesmo banco."""
    porbanco = collections.defaultdict(list)
    for k, (en, _br) in dial.items():
        b, a = k.split(":")
        porbanco[b].append((int(a, 16), k, en))
    fora = set()
    for _b, linhas in porbanco.items():
        linhas.sort()
        for i, (a, k, en) in enumerate(linhas):
            for a2, _k2, en2 in linhas[max(0, i - 10):i]:
                if a - a2 <= DISTANCIA and en2.endswith(en) and en2 != en:
                    fora.add(k)
                    break
    return fora


def main():
    bancos = [b.lower() for b in sys.argv[1:]] or ["40"]
    import pt
    _sistema, nosso = pt.carregar()
    dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
    fora = caudas(dial)
    contagem = collections.Counter()
    fica = []
    for k in sorted(dial):
        if k.split(":")[0] not in bancos or k in nosso:
            continue
        en, br = dial[k]
        if br.strip():
            contagem["ja tem derivada"] += 1
            continue
        if k in fora:
            contagem["cauda"] += 1
        elif "<" in en:
            contagem["marcador"] += 1
        elif kana(en):
            contagem["kana"] += 1
        elif sum(c.isalpha() for c in en) < 12:
            contagem["curta"] += 1
        else:
            fica.append((k, en))
    destino = os.path.join(HERE, "planilha-pend-%s.py" % "-".join(bancos))
    with open(destino, "w", encoding="utf-8") as f:
        f.write("# Pendentes dos bancos %s\n\n" % ", ".join(bancos))
        for k, en in fica:
            f.write("# %s\n%r: %r,\n\n" % (k.split(":")[0], k, en))
    print("%d falas -> %s" % (len(fica), os.path.basename(destino)))
    print("  fora:", dict(contagem))


if __name__ == "__main__":
    main()

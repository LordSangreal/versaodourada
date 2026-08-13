"""Confere as traducoes proprias contra o ingles original.

Verifica o que quebra a caixa de texto de forma silenciosa:
  - a sequencia de \\n / \\v / \\f tem de ser IDENTICA (ordem e quantidade);
  - os tokens ({PLAYER}, {STRBUF}...) idem;
  - nenhuma linha acima de 18 colunas, medindo os tokens pelo que rendem;
  - nada de acento sem glifo na pagina.

Nao imprime a traducao de terceiros em lugar nenhum: o que se compara aqui
e a MINHA traducao contra o INGLES.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pt
import glifos

CTRL = re.compile(r"[\n\v\f]")
TOKEN = re.compile(r"\{[A-Z_]+\}")
LARGURA_TOKEN = {"{PLAYER}": 7, "{RIVAL}": 7, "{MOM}": 4,
                 "{STRBUF}": 10, "{TRAINER}": 8, "{NUM}": 5}
MAX_COLS = 18

# O que se pode escrever: os glifos que a pagina do mod acrescenta MAIS tudo
# que a fonte da ROM ja desenha.  Esquecer a segunda metade fazia o "…" (que
# a ROM tem em 0x75) ser acusado de nao ter glifo -- 17 alarmes falsos que
# escondiam os problemas de verdade.
import gen2text
DESENHAVEIS = set(glifos.charmap())
for _v in gen2text.CHARMAP.values():
    if _v and not _v.startswith("<"):
        DESENHAVEIS.update(_v)
ACENTOS_OK = DESENHAVEIS


def largura(linha):
    def troca(m):
        return "#" * LARGURA_TOKEN.get(m.group(0), 8)
    return len(TOKEN.sub(troca, linha))


def main():
    dial = json.load(open(os.path.join(HERE, "dialogo.json"), encoding="utf-8"))
    _sistema, nosso = pt.carregar()
    problemas = 0
    sem_fonte = 0
    for k, meu in sorted(nosso.items()):
        if k not in dial:
            print("  [%s] chave nao existe no jogo" % k)
            problemas += 1
            continue
        en = dial[k][0]
        a, b = CTRL.findall(en), CTRL.findall(meu)
        if a != b:
            print("  [%s] controle difere: ingles %r, meu %r"
                  % (k, "".join(a).replace("\n", "n").replace("\v", "v").replace("\f", "f"),
                     "".join(b).replace("\n", "n").replace("\v", "v").replace("\f", "f")))
            problemas += 1
        ta, tb = sorted(TOKEN.findall(en)), sorted(TOKEN.findall(meu))
        if ta != tb:
            print("  [%s] tokens diferem: ingles %s, meu %s" % (k, ta, tb))
            problemas += 1
        # A seta ▼ de "aperte A" e desenhada no canto inferior direito da
        # caixa e ocupa a ultima coluna.  Ela aparece quando a caixa PARA e
        # espera: no fim de cada pagina (antes de \f) e no fim do texto.
        # Nessas linhas cabem 17, nao 18 -- foi o que comeu o "m" de "bem"
        # na fala da esposa do Elm.
        paginas = meu.split("\f")
        for ip, pagina in enumerate(paginas):
            linhas = re.split(r"[\n\v]", pagina)
            for il, linha in enumerate(linhas):
                ultima = (il == len(linhas) - 1)
                limite = MAX_COLS - 1 if ultima else MAX_COLS
                if largura(linha) > limite:
                    print("  [%s] %d colunas (limite %d%s): %r"
                          % (k, largura(linha), limite,
                             ", a seta ocupa a ultima" if ultima else "", linha))
                    problemas += 1
        for c in meu:
            if ord(c) > 127 and c not in ACENTOS_OK and c != "é":
                print("  [%s] caractere sem glifo: %r" % (k, c))
                sem_fonte += 1
                break

    print()
    print("traducoes proprias:", len(nosso))
    print("problemas:", problemas, "| caracteres sem glifo:", sem_fonte)
    return 1 if (problemas or sem_fonte) else 0


if __name__ == "__main__":
    sys.exit(main())

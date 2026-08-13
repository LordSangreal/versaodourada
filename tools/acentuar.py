# -*- coding: utf-8 -*-
"""Repoe a acentuacao nos lotes escritos sem acento.

Os lotes 09a-11 e o do ginasio de Goldenrod foram escritos em ASCII puro
("nao", "voce", "POKeMON").  Isso era a regra ate a 0.5.0, quando a fonte
da ROM so tinha `é` e tudo era dobrado para ASCII.  Desde a 0.6.0 o mod
carrega uma pagina com 25 glifos acentuados e a dobra esta desligada --
escrever sem acento agora e so erro de portugues na tela.

Acentuar NAO muda a largura: um caractere continua sendo um caractere,
entao nenhuma linha passa a estourar as 18 colunas por causa disto.

O mapa abaixo so tem palavras SEM ambiguidade.  Ficam de fora, de
proposito, as que mudam de sentido com o acento e precisam de contexto:

    e / e-acento     conjuncao ou verbo ser
    esta / esta-acento   pronome ou verbo estar
    a / a-crase      artigo ou preposicao+artigo
    pode / pode-circunflexo   presente ou passado
    para / para-acento    preposicao ou verbo parar

Essas ficam para revisao a olho -- `python acentuar.py --ambiguas` lista
onde elas aparecem.
"""
import importlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ALVOS = ["dialogo_09a", "dialogo_09b", "dialogo_10a", "dialogo_10b",
         "dialogo_10c", "dialogo_11"]

# palavra sem acento -> com acento.  Só entra o que nao tem homografo.
MAPA = {
    "POKeMON": "POKéMON", "POKeDEX": "POKéDEX", "POKeGEAR": "POKéGEAR",
    "nao": "não", "Nao": "Não", "NAO": "NÃO",
    "voce": "você", "Voce": "Você", "VOCE": "VOCÊ",
    "voces": "vocês", "Voces": "Vocês",
    "tambem": "também", "Tambem": "Também",
    "entao": "então", "Entao": "Então",
    "esta e": "esta é",
    "ja": "já", "Ja": "Já",
    "so": "só", "So": "Só",
    "atras": "atrás", "Atras": "Atrás",
    "aqui e": "aqui é",
    "alguem": "alguém", "Alguem": "Alguém",
    "ninguem": "ninguém", "Ninguem": "Ninguém",
    "porem": "porém", "Porem": "Porém",
    "alem": "além", "Alem": "Além",
    "voo": "voo",
    "alias": "aliás",
    "ali": "ali",
    "alias,": "aliás,",
    "familia": "família", "Familia": "Família",
    "historia": "história", "Historia": "História",
    "memoria": "memória", "Memoria": "Memória",
    "vitoria": "vitória", "Vitoria": "Vitória",
    "gloria": "glória",
    "cencia": "ciência",
    "ciencia": "ciência", "Ciencia": "Ciência",
    "experiencia": "experiência",
    "paciencia": "paciência", "Paciencia": "Paciência",
    "existencia": "existência",
    "diferenca": "diferença", "Diferenca": "Diferença",
    "forca": "força", "Forca": "Força", "FORCA": "FORÇA",
    "comeca": "começa", "Comeca": "Começa",
    "comecar": "começar", "Comecar": "Começar",
    "comecou": "começou", "Comecou": "Começou",
    "coracao": "coração", "Coracao": "Coração",
    "atencao": "atenção", "Atencao": "Atenção", "ATENCAO": "ATENÇÃO",
    "campeao": "campeão", "Campeao": "Campeão", "CAMPEAO": "CAMPEÃO",
    "campeoes": "campeões", "Campeoes": "Campeões",
    "irmao": "irmão", "Irmao": "Irmão",
    "irmaos": "irmãos", "Irmaos": "Irmãos",
    "irma": "irmã", "Irma": "Irmã",
    "maos": "mãos", "Maos": "Mãos",
    "mae": "mãe", "Mae": "Mãe",
    "pai": "pai",
    "avo": "avô",
    "sao": "são", "Sao": "São",
    "estao": "estão", "Estao": "Estão",
    "vao": "vão", "Vao": "Vão",
    "irao": "irão",
    "serao": "serão",
    "farao": "farão",
    "razao": "razão", "Razao": "Razão",
    "licao": "lição", "Licao": "Lição",
    "questao": "questão", "Questao": "Questão",
    "regiao": "região", "Regiao": "Região", "REGIAO": "REGIÃO",
    "direcao": "direção", "Direcao": "Direção",
    "colecao": "coleção", "Colecao": "Coleção",
    "evolucao": "evolução", "Evolucao": "Evolução",
    "informacao": "informação",
    "informacoes": "informações",
    "competicao": "competição", "Competicao": "Competição",
    "pontuacao": "pontuação", "Pontuacao": "Pontuação",
    "posicao": "posição", "Posicao": "Posição",
    "condicao": "condição",
    "emocao": "emoção", "Emocao": "Emoção",
    "nocao": "noção",
    "opcao": "opção", "Opcao": "Opção",
    "acao": "ação", "Acao": "Ação",
    "cao": "cão",
    "montanha": "montanha",
    "facil": "fácil", "Facil": "Fácil",
    "dificil": "difícil", "Dificil": "Difícil",
    "possivel": "possível", "Possivel": "Possível",
    "impossivel": "impossível", "Impossivel": "Impossível",
    "incrivel": "incrível", "Incrivel": "Incrível",
    "terrivel": "terrível", "Terrivel": "Terrível",
    "horrivel": "horrível", "Horrivel": "Horrível",
    "util": "útil", "Util": "Útil",
    "nivel": "nível", "Nivel": "Nível", "NIVEL": "NÍVEL",
    "niveis": "níveis", "Niveis": "Níveis",
    "ultimo": "último", "Ultimo": "Último",
    "ultima": "última", "Ultima": "Última",
    "unico": "único", "Unico": "Único",
    "unica": "única", "Unica": "Única",
    "otimo": "ótimo", "Otimo": "Ótimo",
    "otima": "ótima", "Otima": "Ótima",
    "proximo": "próximo", "Proximo": "Próximo",
    "proxima": "próxima", "Proxima": "Próxima",
    "rapido": "rápido", "Rapido": "Rápido",
    "rapida": "rápida", "Rapida": "Rápida",
    "musica": "música", "Musica": "Música",
    "pratica": "prática", "Pratica": "Prática",
    "magica": "mágica", "Magica": "Mágica",
    "tecnica": "técnica", "Tecnica": "Técnica",
    "publico": "público", "Publico": "Público",
    "numero": "número", "Numero": "Número",
    "numeros": "números", "Numeros": "Números",
    "premio": "prêmio", "Premio": "Prêmio",
    "premios": "prêmios", "Premios": "Prêmios",
    "tres": "três", "Tres": "Três",
    "seculo": "século", "Seculo": "Século",
    "area": "área", "Area": "Área", "AREA": "ÁREA",
    "agua": "água", "Agua": "Água", "AGUA": "ÁGUA",
    "aguas": "águas", "Aguas": "Águas",
    "ideia": "ideia",
    "voltara": "voltará",
    "sera": "será", "Sera": "Será",
    "serao,": "serão,",
    "estara": "estará",
    "havera": "haverá",
    "ate": "até", "Ate": "Até",
    "apos": "após", "Apos": "Após",
    "atraves": "através", "Atraves": "Através",
    "veio": "veio",
    "ve": "vê",
    "cre": "crê",
    "le": "lê",
    "vem": "vem",
    "tem": "tem",
    "voltem": "voltem",
    "parabens": "parabéns", "Parabens": "Parabéns",
    "PARABENS": "PARABÉNS",
    "voo!": "voo!",
    "ceu": "céu", "Ceu": "Céu",
    "chao": "chão", "Chao": "Chão",
    "irmandade": "irmandade",
    "amanha": "amanhã", "Amanha": "Amanhã",
    "manha": "manhã", "Manha": "Manhã",
    "cha": "chá",
    "la": "lá", "La": "Lá",
    "ca": "cá",
    "ai": "aí", "Ai": "Aí",
    "sai": "sai",
    "pe": "pé",
    "fe": "fé",
    "avos": "avós",
    "heroi": "herói", "Heroi": "Herói",
    "herois": "heróis",
    "sozinho": "sozinho",
    "orgulho": "orgulho",
    "GINASIO": "GINÁSIO", "Ginasio": "Ginásio", "ginasio": "ginásio",
    "LIDER": "LÍDER", "Lider": "Líder", "lider": "líder",
    "INSIGNIA": "INSÍGNIA", "Insignia": "Insígnia",
    "RUINAS": "RUÍNAS", "Ruinas": "Ruínas", "ruinas": "ruínas",
    "MAGNETICO": "MAGNÉTICO", "magnetico": "magnético",
    "ELETRICO": "ELÉTRICO", "eletrico": "elétrico",
    "eletrica": "elétrica",
    "PSIQUICO": "PSÍQUICO", "psiquico": "psíquico",
    "psiquica": "psíquica",
    "dragao": "dragão", "Dragao": "Dragão", "DRAGAO": "DRAGÃO",
    "dragoes": "dragões", "Dragoes": "Dragões",
    "fantasma": "fantasma",
    "veneno": "veneno",
    "PS": "PS",
    # ---- segunda leva: o que sobrou depois de consertar o regex
    "arvore": "árvore", "Arvore": "Árvore",
    "arvores": "árvores", "Arvores": "Árvores",
    "especie": "espécie", "Especie": "Espécie",
    "especies": "espécies", "Especies": "Espécies",
    "misterio": "mistério", "Misterio": "Mistério",
    "misterios": "mistérios", "Misterios": "Mistérios",
    "misteriosa": "misteriosa", "misterioso": "misterioso",
    "crianca": "criança", "Crianca": "Criança",
    "criancas": "crianças", "Criancas": "Crianças",
    "formacao": "formação", "Formacao": "Formação",
    "paineis": "painéis", "Paineis": "Painéis",
    "painel": "painel",
    "turistico": "turístico", "turisticos": "turísticos",
    "Turistico": "Turístico", "Turisticos": "Turísticos",
    "construida": "construída", "construidas": "construídas",
    "padroes": "padrões", "Padroes": "Padrões",
    "padrao": "padrão", "Padrao": "Padrão",
    "pontuacao": "pontuação", "Pontuacao": "Pontuação",
    "respiracao": "respiração", "Respiracao": "Respiração",
    "transmissao": "transmissão", "Transmissao": "Transmissão",
    "transmissoes": "transmissões",
    "gravacao": "gravação", "Gravacao": "Gravação",
    "gravacoes": "gravações", "Gravacoes": "Gravações",
    "Cancoes": "Canções", "cancoes": "canções",
    "cancao": "canção", "Cancao": "Canção",
    "Exploracao": "Exploração", "exploracao": "exploração",
    "acoes": "ações", "Acoes": "Ações",
    "ajudarao": "ajudarão",
    "gratidao": "gratidão", "Gratidao": "Gratidão",
    "usuario": "usuário", "Usuario": "Usuário",
    "estacao": "estação", "Estacao": "Estação",
    "estacoes": "estações",
    "producao": "produção", "Producao": "Produção",
    "criacao": "criação", "Criacao": "Criação",
    "reuniao": "reunião", "Reuniao": "Reunião",
    "televisao": "televisão", "Televisao": "Televisão",
    "cabecas": "cabeças", "cabeca": "cabeça",
    "pecas": "peças", "peca": "peça",
    "danca": "dança", "Danca": "Dança",
    "dancar": "dançar", "Dancar": "Dançar",
    "espaco": "espaço", "Espaco": "Espaço",
    "comecando": "começando", "Comecando": "Começando",
    "almoco": "almoço", "Almoco": "Almoço",
    "servico": "serviço", "Servico": "Serviço",
    "precos": "preços", "preco": "preço",
    "cabelo": "cabelo",
    "japones": "japonês",
    "ingles": "inglês", "Ingles": "Inglês",
    "portugues": "português", "Portugues": "Português",
    "voces": "vocês",
    "aqui": "aqui",
    "ficara": "ficará",
    "dara": "dará",
    "vira": "virá",
    "podera": "poderá",
    "tera": "terá",
    "ninguem,": "ninguém,",
    "energia": "energia",
    "quimica": "química", "Quimica": "Química",
    "fisica": "física", "Fisica": "Física",
    "logica": "lógica",
    "maquina": "máquina", "Maquina": "Máquina",
    "maquinas": "máquinas", "Maquinas": "Máquinas",
    "automatico": "automático", "automatica": "automática",
    "eletronico": "eletrônico", "eletronica": "eletrônica",
    "telefone": "telefone",
    "antena": "antena",
    "sinal": "sinal",
    "torre": "torre",
    "andar": "andar",
    "escada": "escada",
}

AMBIGUAS = re.compile(r"\b(e|esta|estao|pode|para|a|as|so|ate|tem|vem|por)\b")


def aplicar(texto):
    def troca(m):
        p = m.group(0)
        return MAPA.get(p, p)
    return re.sub(r"[A-Za-zÀ-ÿ]+", troca, texto)


# So dentro de literais de UMA linha com aspas duplas -- que e onde moram as
# traducoes.  Rodar sobre o arquivo inteiro renomearia identificadores
# ("le", "so", "ate" estao no mapa) e reescreveria as docstrings, que por
# convencao do projeto sao ASCII.
# A barra invertida PRECISA passar: a primeira versao excluia `\\` do
# literal e por isso pulava toda fala escrita com `\n`/`\v` embutido --
# ficaram 34 palavras sem acento sem eu perceber.  Trocar letra por letra
# nao encosta em `\n`: o "n" do escape nao esta no mapa.
_LITERAL = re.compile(r'"([^"\n]*)"')

# A CHAVE tambem e um literal de aspas duplas, e "43:63ce" tem letras: a
# primeira passada trocou o "ce" e a chave deixou de existir no jogo.
# Ponteiro nao se acentua.
_PONTEIRO = re.compile(r"^[0-9a-f]{2}:[0-9a-f]{4}$")


def _uma(m):
    dentro = m.group(1)
    if _PONTEIRO.match(dentro):
        return m.group(0)
    return '"' + aplicar(dentro) + '"'


def aplicar_no_fonte(fonte):
    partes = fonte.split('"""')
    for i in range(0, len(partes), 2):   # indices pares = fora da docstring
        partes[i] = _LITERAL.sub(_uma, partes[i])
    return '"""'.join(partes)


def main():
    if "--ambiguas" in sys.argv:
        for nome in ALVOS:
            mod = importlib.import_module("pt." + nome)
            for k, v in getattr(mod, "DIALOGO", {}).items():
                if AMBIGUAS.search(v):
                    print("%s [%s] %r" % (nome, k, v[:70]))
        return
    total = 0
    for nome in ALVOS:
        caminho = os.path.join(HERE, "pt", nome + ".py")
        if not os.path.exists(caminho):
            continue
        antes = io.open(caminho, encoding="utf-8").read()
        depois = aplicar_no_fonte(antes)
        if depois != antes:
            io.open(caminho, "w", encoding="utf-8").write(depois)
            mudou = sum(1 for a, b in zip(antes.split("\n"), depois.split("\n"))
                        if a != b)
            print("%-28s %d linhas acentuadas" % (nome, mudou))
            total += mudou
    print("total:", total)


if __name__ == "__main__":
    main()

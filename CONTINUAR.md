# Como continuar este projeto

Documento de passagem de bastao.  Escrito para quem pega o projeto sem ter
acompanhado nada -- outro modelo, outra pessoa, ou eu mesmo numa sessao
nova.  Se voce leu ate o fim, sabe tudo que precisa.

---

## 1. O que e isto

`versaodourada` e um mod que poe **Pokemon Gold em portugues brasileiro**
no [gen1recomp](https://github.com/bryanthaboi/gen1recomp), que e uma
recriacao nativa dos jogos em Lua/LOVE2D -- nao um emulador.

O usuario joga no **Android**, no build "Gen1ReComp++ 1.8.0".  Ele nao tem
como rodar o projeto no PC: **nada aqui foi verificado em execucao por
quem escreve o codigo**.  Toda validacao veio de capturas de tela que ele
mandou.  Isso importa mais do que parece -- ver secao 8.

Repositorio: https://github.com/LordSangreal/versaodourada (publico)

---

## 2. As tres restricoes que mandam em tudo

Decoram estas e metade dos erros somem.

**A caixa de dialogo tem 18 colunas e 2 linhas.**  Uma traducao mais fiel
que nao cabe e pior que uma mais curta que cabe.

**A ultima linha de cada pagina cabe 17.**  A seta ▼ de "aperte A" e
desenhada no canto inferior direito quando a caixa para e espera -- fim de
pagina (antes de `\f`) e fim do texto.  Ela ocupa a coluna 18.

**Os codigos de controle sao parte do texto.**  `\n` quebra linha, `\v`
rola uma linha, `\f` quebra pagina.  Perder ou mover um embaralha a caixa
**sem gerar erro nenhum**.  Idem para os tokens `{PLAYER}`, `{RIVAL}`,
`{STRBUF}`, `{NUM}`.

`tools/conferir.py` verifica as tres.  Rode sempre antes de publicar.

---

## 3. Por que mod e nao patch de ROM

`RomImporter:startData` valida o SHA-1 da ROM contra uma allowlist de 4
hashes e recusa com "patched, trimmed or 'fixed' dumps never verify".  Nao
ha bypass, e os offsets do `RomExtractorGen2.lua` sao fixos no layout
canonico.

Traducao por patch de ROM esta fora de questao.  Tem de ser mod.

---

## 4. Como o texto chega ao jogo

O gen1recomp extrai o texto da ROM do jogador no import e o guarda com
chaves que sao **ponteiros da ROM USA**, no formato `"%02x:%04x"` --
`"55:4067"`.  Nao ha tabela de nomes como no Gen 1.

O mod sobrescreve por essa chave:

```lua
mod.content.text:override("55:4067", "...")      -- falas do jogo
mod.content.strings:override("But, it failed!", "Mas falhou!")  -- motor
mod.content.items:patch(id, { name = ... })      -- itens
```

Valor vazio = "nao traduzido" = cai em ingles.  **O mod e sempre jogavel**,
em qualquer estagio.

### O manifest tem duas armadilhas

```json
"games": ["gold"],                  // sem isto, um boot de Gold PULA o mod
"game_version": ">=0.0.0-0 <2.0.0"  // "<1.0.0" exclui o app 1.8.0 da lista
```

As duas ja custaram uma versao cada.  Nao mexa sem motivo.

---

## 5. De onde vem o texto

### Hoje: extraido de uma traducao de terceiros

O usuario tem uma ROM BR (`Pokemon - Gold Version (BR)`), traducao de
**R_Lopes e Night_Shadown** dos anos 2000.  E um patch in-place da ROM USA:
mesmo tamanho, mesma estrutura, ~87% do texto traduzido.

`tools/walk.py` percorre os scripts das **duas ROMs em passo travado**: o
bytecode e identico, so os ponteiros de texto mudam.  A USA da a chave, a
BR da a traducao.

### O rumo: substituir por traducao propria

O usuario nao conseguiu localizar os autores para pedir autorizacao, entao
o texto derivado esta sendo trocado por traducao feita **a partir do ingles
original**, lote a lote.  Cada lote e um arquivo em `tools/pt/`.

**Enquanto houver UMA fala derivada no pacote, o credito no README fica.**
`tools/progresso.py` responde "ja da para tirar?" com numero, nao com
impressao.  Nao remova a atribuicao antes de ele zerar -- tirar o credito
mantendo o texto e pior que manter os dois.

---

## 6. Decisoes de traducao (do usuario, nao negociaveis)

Ficam **no original em ingles**:

| O que | Por que |
|---|---|
| Nomes de golpes | Sao como a franquia os nomeia |
| Nomes de Pokemon | Nomes oficiais no mundo todo |
| Personagens e cidades | Idem |
| **TM e HM** | Vem colados aos nomes dos golpes: "MT29 contem o PSYCHIC" misturaria duas linguas |
| **Status** (PSN, BRN, PAR, SLP, FRZ) | Sigla padrao, lida sem pensar, em caixa de 3 caracteres.  O que informa e a mensagem na caixa de texto, e essa esta traduzida |
| **As Balls** | POKe BALL, GREAT BALL, MASTER BALL |
| **A interface do aplicativo** | Botoes de largura fixa; o portugues estoura e sai cortado.  Ver secao 7 |

Terminologia segue a localizacao oficial pt-BR: Ginasio, Lider de Ginasio,
Treinador, Insignia, Centro Pokemon.  Ver `GLOSSARIO.md`, que tambem lista
o que **nao** mudar.

---

## 7. O launcher NAO e traduzido

Traduzi a interface do aplicativo na 0.4.0 e tive de desfazer na 0.11.0: os
botoes tem largura fixa, o portugues e mais longo, e o texto saiu cortado
na tela do usuario ("Play Gold (Be...").

`build_mod.py` filtra **por diretorio de origem**: qualquer chave vinda de
`src/import/`, `LauncherMods`, `ManagerState` ou `src/update/` sai do
catalogo automaticamente.  207 removidas, 151 ficam.

Nao tente reintroduzir.  A tela do jogo tem largura conhecida; a do
aplicativo, nao.

---

## 8. O que so apareceu jogando

Cinco defeitos, nenhum detectavel por teste automatico, todos achados por
captura de tela do usuario:

1. **TTF quebrou a tela de mods** (0.1.2).  A documentacao sugere
   `font:register("ttf", {})`; o mod `versaovermelha`, que funciona, mantem
   essa linha **comentada**.  Evidencia venceu documentacao.
2. **Blocos pretos no lugar dos acentos** (0.6.0).  O motor decide o que e
   tinta pelo **canal alfa**, nao pela luminancia.  A doc diz "preto no
   branco"; a pagina que funciona e preto no **transparente**.
3. **"bem" cortado** (0.8.1).  A seta ▼ ocupa a coluna 18 -- daí a regra
   das 17.
4. **Reticencias no lugar do travessao** (0.10.1).  `--` em ingles marca
   pausa; `…` em portugues diz que a fala se perdeu.  E virgula.
5. **Launcher cortado** (0.11.0).  Secao 7.

**Licao:** quando a documentacao e o codigo que ja roda discordarem,
acredite no codigo que roda.  E peca captura de tela.

---

## 9. As ferramentas

```
tools/walk.py        percorre os scripts das duas ROMs em passo travado
tools/entradas.py    pontos de entrada, respeitando o que NAO e bytecode
tools/gen2text.py    decodificador de texto Gen 2 + charmap da traducao BR
tools/lote.py        extrai o ingles de uma regiao para traduzir
tools/fatiar.py      corta uma planilha grande por mapa e joga fora o lixo
tools/esqueleto.py   imprime pagina, linha, separador e limite de coluna
tools/pt/            a traducao propria, um arquivo por lote
tools/pt/estrutura.py  `linhas()` -- monta a fala com os separadores do ingles
tools/conferir.py    compara a traducao propria com o ingles
tools/validar.py     QA do catalogo publicado
tools/glossario.py   terminologia, sem estourar as 18 colunas
tools/glifos.py      desenha a pagina de glifos acentuados
tools/progresso.py   quanto ja e nosso, quanto ainda e derivado
tools/build_mod.py   monta o mod
tools/gerar_indice.py  gera o feed do catalogo
```

### O erro que `linhas()` existe para impedir

Copiar a sequencia de `\n` `\v` `\f` a mao **nao funciona**.  Eu errei
quatro vezes no lote 6b e oito no lote 7, sempre do mesmo jeito: na
planilha o separador aparece **depois** da linha a que pertence, e a
leitura natural e como se viesse antes.  O resultado e uma caixa que
rola quando devia virar pagina.

`pt/estrutura.py` resolve isso de vez.  Escreva so o texto:

```python
from pt.estrutura import linhas as L

DIALOGO = {
    "40:4615": L("40:4615",
                 "Bom dia!",
                 "Bem-vindo ao nosso",
                 "CENTRO POKéMON."),
}
```

Os separadores vem do ingles.  Se a contagem de linhas nao bater, estoura
no import com a chave no erro, em vez de virar bug no aparelho.  Os tres
lotes escritos assim (8a, 8b, 8c) passaram limpos **de primeira**.

**Use `linhas()` em todo lote novo.**  Os lotes 1 a 6b sao anteriores a
ela e usam string crua; nao ha motivo para converte-los, ja estao
conferidos.

### Dois detalhes que ja morderam

**`entradas.py`**: o byte de funcao de um `bg_event`/`object_event` decide
se o ponteiro e bytecode.  `BGEVENT_ITEM`, `OBJECTTYPE_ITEMBALL` e
`OBJECTTYPE_TRAINER` **nao** apontam para codigo.  Andar sobre eles
desmonta dados como comandos e gera lixo -- era a origem dos "opcodes
desconhecidos" (318 -> 6 quando corrigido).

**`gen2text.py`**: a traducao BR reaproveitou bytes livres e ligaduras.
Todos deduzidos cruzando ingles e portugues:

| byte | vale | evidencia |
|---|---|---|
| `0x4A` | `DO` | GYARA+DO+S |
| `0x24` | `QU` | E+QU+IPE |
| `0x56` | `DADE` | CI+DADE NEW BARK |
| `0x5B` | `AO` | GR+AO |
| `0x5C` | `TA` | RO+TA |
| `0x5D` | `POKeMON` | "CENTRO _" |
| `0xD4` | `C` cedilha | COMUNICA+C+OES |
| `0xD1` | `O` circunflexo | M+O+NICA |
| `0xC5` | `o` ordinal | 4+o+ ANDAR |

O mapa BR tem **precedencia** sobre a cadeia de casos especiais do
decodificador.  Sem isso, `0x56` virava reticencias antes de alguem
consultar o charmap.

---

## 10. Como fazer um lote, do zero ao release

Trabalhe **no scratchpad**, nao no repositorio.  A pasta de trabalho e a
que tem `dialogo.json`, `repo/` (o fonte do gen1recomp) e `br/` (a ROM
BR).  Nada disso esta no git -- ver secao 11.

### 10.1 Escolher o que traduzir

Dois caminhos.  Use o segundo -- e o que sobrou de trabalho.

```bash
python lote.py 08              # POR REGIAO: planilha-08.py (mapas de lote.py)
python pendentes.py 4c 4d      # POR BANCO: planilha-pend-4c-4d.py
```

`pendentes.py` e o certo hoje.  Ele lista o que falta num banco e ja
descarta cauda, marcador, kana e fala curta demais -- ver 10.5.  Rode
sem medo: ele nunca escreve no catalogo, so gera a planilha.

Para saber onde ainda ha trabalho:

```bash
python progresso.py            # quanto e nosso, quanto e derivado
python pendentes.py 42 43 47   # quantas faltam nesses bancos
```

### 10.2 Ler o esqueleto ANTES de escrever

```bash
python esqueleto.py planilha-pend-4c.py     # o lote inteiro
python esqueleto.py 56:4634                 # uma chave so
```

A saida diz, linha a linha, o separador que vem depois dela e o limite
de coluna daquela linha:

```
# 40:4664
  P1 \n [18] |Good evening!|
  P1 \f [17] |You're out late.|
  P2 \n [18] |Welcome to our|
  P2    [17] |POKéMON CENTER.|
```

Ler isso e obrigatorio.  **A saida do terminal corta linhas longas** --
se a fala for grande, o esqueleto pode aparecer truncado na tela e voce
vai contar linhas a menos.  Aconteceu comigo em `41:5484`: li 7 linhas,
o ingles tinha 21.

### 10.3 Escrever com `linhas()`

Um arquivo por lote, em `pt/dialogo_NN.py`:

```python
# -*- coding: utf-8 -*-
"""Lote NN -- descreva o escopo em uma linha.

Ficam no original: liste aqui os nomes proprios que voce nao traduziu.
"""
from pt.estrutura import linhas as L

DIALOGO = {
    "40:4664": L("40:4664",
                 "Boa noite!",
                 "Saiu tarde, hein?",
                 "Bem-vindo ao nosso",
                 "CENTRO POKéMON."),
}
```

So o texto de cada linha.  Os separadores vem do ingles.  **Nunca**
escreva `\n`, `\v` ou `\f` a mao num lote novo.

### 10.4 Conferir antes de tudo

```bash
# 1) contagem de linha -- pega o erro que quebra o import
python -c "
import json,re,io
d=json.load(open('dialogo.json',encoding='utf-8'))
src=io.open('pt/dialogo_NN.py',encoding='utf-8').read()
for m in re.finditer(r'L\(\"([0-9a-f:]+)\",(.*?)\),\n', src, re.S):
    k=m.group(1); n=len(re.findall(r'\"[^\"]*\"', m.group(2)))
    e=len(re.split(r'[\n\v\f]', d[k][0]))
    if n!=e: print('%s ingles %d, meu %d'%(k,e,n))
"

# 2) registre em pt/__init__.py, na lista LOTES
# 3) conferidor ate dar ZERO
python conferir.py
```

O passo 1 vale a pena porque `linhas()` estoura no **primeiro** erro e
voce descobre um por vez; o script acha todos de uma vez.

### 10.5 O que NAO traduzir

`pendentes.py` ja filtra, mas saiba o porque -- o filtro e heuristico e
deixa passar:

| Fica fora | Por que |
|---|---|
| **cauda** | o texto e o fim de outra fala; o jogo mostra a fala inteira a partir do ponteiro de cima, entao traduzir a cauda nao muda nada na tela |
| **`<TARGET>` `<USER>` `<ENEMY>`** | nao sao texto, sao bytes que o motor troca em execucao.  O override publica o texto como esta, entao o marcador apareceria **literal** na tela |
| **kana solto** | ponteiro mal alinhado; o texto decodificado e lixo |
| **fragmento** | comeca no meio de uma palavra (continuacao de `TX_FAR`) |
| **identico ao ingles** | placas que so tem nome proprio ("ROUTE 42 / ECRUTEAK CITY - MAHOGANY TOWN") |

Se a primeira linha do esqueleto comeca no meio de uma palavra, pule a
chave.

### 10.6 Publicar

```bash
# no scratchpad
#   suba VERSION no topo de build_mod.py
#   acrescente a entrada em CHANGELOG_mod.md
#   atualize os numeros em README_mod.md
python build_mod.py
cp -r versaodourada/. "D:/pokemon gold traducao/versaodourada/"
cp build_mod.py CHANGELOG_mod.md README_mod.md "D:/.../tools/"
cp pt/dialogo_NN.py pt/__init__.py "D:/.../tools/pt/"

# no repositorio
git add -A && git commit && git push
gh release create v0.X.0 <caminho do zip> --title "..." --notes "..."
python tools/gerar_indice.py
git add -A && git commit -m "Feed 0.X.0" && git push
```

**Cuidado com dois arquivos.**  `cp *.py tools/` **nao serve**: leva
junto as `planilha-*.py`, que sao texto de ROM em ingles e nao podem ir
para o git.  E `README_mod.md`/`CHANGELOG_mod.md` moram nos **dois**
lugares -- eu ja sobrescrevi a versao boa do README copiando a antiga do
scratchpad por cima.

### 10.7 Tamanho do lote

Ate a 0.20.0 a regra era ~50 falas.  O usuario pediu lotes maiores para
economizar tempo, e a partir da 0.21.0 os lotes sao de banco inteiro
(70-120 falas).

Isso funciona, **com uma ressalva medida**: lote grande nao erra mais
por fala -- erra a mesma proporcao, so que tudo de uma vez.  Nos lotes
20 e 21 juntos foram 3 reprovacoes de contagem e 29 estouros de coluna,
todos pegos pelas ferramentas.

O que o lote grande esconde e o **erro de sentido**, que nenhuma
ferramenta pega.  Ver 10.8.

### 10.8 Reler antes de publicar -- o passo que nao tem ferramenta

`conferir.py` valida forma: largura, codigo de controle, token, glifo.
Ele aprova frase sem sentido sem piscar.  Estes foram publicados ou
quase publicados:

| O que saiu | O que era |
|---|---|
| "Somos as estrelas destral estrada!" | erro de digitacao puro |
| "Parece que ele vai engolir." | faltou o objeto ("te engolir") |
| "Minha aula favorita e a de ed. fi" | cortada no meio |
| "cortando as cauda dos SLOWPOKE" | concordancia |
| "E aqui que nos marinheiros ralam" | concordancia |
| "Voce removing aquela arvore?" | meio traduzido (foi da outra sessao) |

Depois do conferidor dar zero, rode isto e **leia**:

```bash
python -c "
import sys,re; sys.path.insert(0,'.')
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
import pt
from pt.dialogo_NN import DIALOGO
_s,n=pt.carregar()
for k in DIALOGO: print(k,'|',' | '.join(re.split(r'[\n\v\f]', n[k])))
"
```

Procure por: palavra cortada no fim, verbo sem sujeito, concordancia,
palavra em ingles que sobrou, frase que termina em virgula.

### 10.9 Dois atalhos que NAO funcionam

**`"texto"[:18]`** para forcar largura -- corta palavra no meio e vira
"marinheiros ralamo".  Escreva a linha mais curta de verdade.

**Heredoc de bash com `\n` ou `\v` dentro** -- o shell come o escape e
corrompe o arquivo.  Ja destruiu `build_mod.py`, `dialogo_01.py` e
`lote.py`.  Use a ferramenta de escrita/edicao, ou um `.py` separado.
Se precisar de heredoc, use `<<'PY'` com aspas e sem escapes no texto.

---

## 10-A. O oficio: como traduzir para caber em 18 colunas

Esta secao e a diferenca entre uma traducao que passa no conferidor e
uma que se le bem.  Nao pule.

### O problema de fundo

O portugues ocupa cerca de **20 a 30% mais espaco** que o ingles.  Cada
linha tem 18 colunas (17 na ultima de cada pagina).  Isso significa que
traduzir palavra por palavra **nunca** cabe.  A traducao boa aqui e a
que corta o supérfluo e mantem o que a frase faz.

### Regra 1 -- traduza a INTENCAO, nao as palavras

O NPC nao precisa dizer a mesma coisa; precisa **fazer a mesma coisa**
(informar, ameacar, se gabar, se desculpar).

| Ingles | Literal (nao cabe) | Publicado |
|---|---|---|
| "I have no regrets." | "Sem arrependimentos" (19) | "Nada a lamentar." (16) |
| "You looked strong." | "Voce parecia forte" (18, ultima) | "Voce parecia bom." (17) |
| "That's my fashion policy." | "Essa e minha politica de moda" | "E a minha regra de moda." |
| "Reckless driving causes accidents!" | ... | "Direcao imprudente causa acidente!" |

### Regra 2 -- a ordem de encurtamento

Quando uma linha estoura, tente **nesta ordem**.  Pare no primeiro que
funcionar:

1. **Corte o supérfluo.**  "Eu vou ganhar" -> "Vou ganhar".  Sujeito
   pronominal em portugues quase sempre pode sair.
2. **Troque por sinonimo curto.**  "impressionante" -> "incrivel",
   "adversario" -> "rival", "consegue" -> "da".
3. **Reorganize a frase.**  "Nao ha nada aqui" -> "Nada aqui".
4. **Mova palavra para a linha seguinte** -- so se a linha seguinte tem
   folga E o sentido nao quebra.
5. **Hifenize** -- ultimo recurso, e so com as regras da Regra 3.
6. **Corte informacao secundaria** -- so quando nada mais serve, e nunca
   um nome proprio, numero ou instrucao de jogo.

O que **nunca** se corta: nome de POKéMON, de lugar, de item, de golpe,
numero, direcao ("norte", "leste"), nome de botao.  Se a fala diz "va
para o norte ate LAKE OF RAGE", o jogador precisa dos dois.

### Regra 3 -- hifenizacao

O jogo original hifeniza muito ("differ-/ent", "POKé-/MON").  Voce pode
fazer o mesmo, mas em portugues:

- **Separe por silaba.**  "impres-/sionado", "trei-/nador",
  "experi-/mento".  Nunca "impressio-/nado" cortando no meio da silaba
  se puder evitar, e **nunca** corte deixando uma letra sozinha.
- **Nao hifenize nome proprio** se puder evitar.  "SLOW-/POKETAIL" foi
  aceito porque nao cabia de outro jeito; "POKé-/MON" e o padrao do
  proprio jogo e esta ok.
- Se a hifenizacao ficar feia, **prefira reescrever**.  "Nos HIKERS
  somos melhores nas montanhas" cabe sem hifen nenhum.

### Regra 4 -- a ultima linha da pagina tem 17, nao 18

Esse e o erro mais comum de todos.  A seta ▼ de "aperte A" ocupa a
coluna 18 sempre que a caixa **para e espera**: no fim de cada pagina
(antes de `\f`) e no fim do texto.

O esqueleto ja mostra `[17]` nessas linhas.  Leia o numero, nao chute.

### Regra 5 -- registro e tom

O jogo e de 1999 e fala com crianca.  A traducao acompanha:

- **Voce**, nunca "tu".  Nunca mesoclise, nunca "vos".
- **Informal mas nao girio demais.**  "Que legal!" sim; "Que massa,
  mano!" nao.  A excecao sao personagens que ja sao girios em ingles
  (os motoqueiros da CYCLING ROAD, os ROCKET GRUNTS).
- **Interjeicao traduz-se por interjeicao equivalente**, nao pela
  transliteracao: "Whoa!" -> "Uau!", "Yikes!" -> "Eita!", "Darn!" ->
  "Droga!", "Hmmm…" -> "Hmmm…", "Wahahah!" -> "Uahahah!".
- **Ameaca de vilao soa ameacadora**, nao burocratica: "Get lost!" ->
  "Some!" e nao "Por favor retire-se".
- **NPC idoso fala como idoso**, crianca como crianca.  O KURT diz
  "Escute aqui"; o menino diz "Ei, escuta!".

### Regra 6 -- consistencia de termo

Antes de inventar uma traducao, **procure se ja existe**:

```bash
grep -rn "GINASIO\|LIDER\|CENTRO POK" pt/*.py | head
```

Termos ja fixados (ver tambem `GLOSSARIO.md`):

| Ingles | Portugues | Observacao |
|---|---|---|
| GYM | GINÁSIO | oficial pt-BR |
| GYM LEADER | LÍDER de GINÁSIO | |
| POKéMON CENTER | CENTRO POKéMON | |
| POKéMON MART | LOJA POKéMON | mudou na 0.17.0 |
| trainer | treinador | |
| BADGE | BADGE | fica em ingles |
| CHAMP | CAMPEÃO | |
| PACK | BOLSA | oficial (nao "mochila") |
| HP | PS | o glossario troca sozinho |
| move / golpe | movimento | o glossario troca **se couber** |
| MOM | MÃE | |
| BOX | BOX | interface ja usa "BOX %d" |

**Cuidado com o glossario automatico.**  `glossario.py` troca "golpe"
por "movimento" **so quando cabe** na linha.  Isso pode deixar duas
falas vizinhas usando palavras diferentes.  E o comportamento desenhado
(cabimento vence purismo), mas se incomodar, escreva "movimento" direto
quando couber.

### Regra 7 -- os tokens sao sagrados

`{PLAYER}`, `{RIVAL}`, `{STRBUF}`, `{NUM}`, `{MOM}`, `{TRAINER}` sao
substituidos em execucao.  Regras:

- **Numero e ordem** tem de bater com o ingles.  Se a fala tem dois
  `{STRBUF}`, a sua tambem tem dois, **na mesma ordem** -- o motor
  preenche pela posicao.  Inverter troca o nome do POKéMON pelo do
  lugar.
- Eles ocupam largura: `{PLAYER}`=7, `{RIVAL}`=7, `{STRBUF}`=10,
  `{NUM}`=5, `{TRAINER}`=8, `{MOM}`=4.  O conferidor ja conta assim.
- **Nunca corte um token para caber.**  Encurtar `KURT: Oi, {PLAYER}!`
  para `KURT: Oi!` faz o KURT parar de chamar o jogador pelo nome.
- Reordenar a frase em portugues e permitido **se houver so um token**:
  "{STRBUF}'s number." -> "{STRBUF}." funciona.

### Regra 8 -- quebrar a frase entre linhas

A quebra tem de cair onde a leitura respira:

- **Bom:** depois de virgula, antes de conjuncao, entre sujeito e verbo.
- **Ruim:** entre artigo e substantivo ("a / casa"), entre preposicao e
  o que ela rege ("de / POKéMON"), deixando uma palavra sozinha na
  ultima linha.
- **Pessimo:** terminar uma pagina com virgula e comecar a proxima com
  minuscula sem que a frase continue de fato.

Quando a fala cruza `\f` (pagina nova), a frase **pode** continuar -- o
ingles faz isso o tempo todo.  So confira que continua fazendo sentido.

### Regra 9 -- o que fica em ingles (decisao do usuario)

Ver secao 6 para a lista completa.  Resumo pratico: **nome proprio de
qualquer natureza fica**.  POKéMON, golpe, item, cidade, rota,
personagem, TM/HM, estabelecimento com nome proprio (DEPT.STORE, GAME
CORNER, DAY-CARE, FAST SHIP, MAGNET TRAIN).

O que **e** traduzido: tudo que e substantivo comum ou fala corrente,
mais os termos de categoria que tem forma oficial em pt-BR (GINÁSIO,
LÍDER, CENTRO POKéMON, LOJA POKéMON, CAMPEÃO).

### Regra 10 -- acentue sempre

Desde a 0.6.0 o mod carrega uma pagina com 25 glifos acentuados.
Escreva `não`, `você`, `POKéMON`, `três`, `história`.  Acento **nao**
muda a largura -- um caractere continua sendo um caractere.

Glifos disponiveis: á â ã à ê í ó ô õ ú ç é Á Í Â Ê Ã Õ É Ó Ô Ç e mais.
O conferidor acusa se voce usar um que nao existe.  `…` (reticencias
unicas) existe na fonte da ROM e deve ser usado no lugar de "...".

### Regra 11 -- o travessao do ingles

`--` no ingles e travessao, marca de pausa.  Em portugues vira
**virgula**, e o `glossario.py` ja faz isso sozinho.

Nao use reticencias no lugar: `…` em portugues significa frase que se
perde no ar, que e outra coisa.  Isso ja foi publicado errado e o
usuario reclamou (0.10.1).

---

## 10-B. O que a outra sessao errou, e como consertar

Uma sessao paralela escreveu os lotes 09a, 09b, 10a, 10b, 10c, 11 e um
`dialogo_ginasio_goldenrod.py` -- 200 falas.  Todas precisaram de
conserto.  O catalogo abaixo serve de checklist: **se voce for aquela
sessao, evite isto; se for a proxima, procure por isto.**

### Erro 1 -- escreveu tudo sem acento (200 de 200 falas)

"nao", "voce", "POKeMON", "tambem", "nivel".  Zero acentos em 200 falas.

Isso era a regra **ate a 0.5.0**, quando a fonte da ROM so tinha `é` e o
build dobrava tudo para ASCII.  Desde a **0.6.0** a pagina de glifos
entrou e `DOBRA` esta vazio.  Escrever sem acento agora e so erro de
portugues na tela.

**Conserto:** `tools/acentuar.py`.  Ele tem um mapa de ~250 palavras sem
ambiguidade e so mexe dentro de literais de aspas duplas.

```bash
python acentuar.py             # aplica
python acentuar.py --ambiguas  # lista onde estao e/esta/pode/para
```

Duas armadilhas que **ja morderam** e estao consertadas no script:

- A **chave** tambem e um literal: `"43:63ce"` tem letras, e a primeira
  versao trocou o "ce" -- a chave deixou de existir no jogo.  Ha um
  filtro `_PONTEIRO` para isso.
- O regex excluia `\\`, e por isso **pulava toda fala escrita com `\n`
  embutido**.  Ficaram 34 palavras sem acento sem eu perceber.

O que o script **nao** faz, de proposito: `e`/`é`, `esta`/`está`,
`a`/`à`, `pode`/`pôde`, `para`/`pára`.  As duas formas existem; so o
contexto decide.  Essas vao a mao.

### Erro 2 -- 42 linhas estourando a caixa

Linhas de 19 e ate 22 colunas.  Na tela isso corta a palavra no meio.
A causa foi nao ler o `[17]`/`[18]` do esqueleto.

**Conserto:** `tools/patch_lotes_09_11.py` documenta as 60 trocas que
fiz.  O metodo esta na Regra 2 acima.

### Erro 3 -- ingles solto no meio da traducao

`"Você removing aquela árvore?"` -- meio traduzido, meio nao.
Nenhuma ferramenta pega isso: a largura estava certa.

**Conserto:** so releitura (10.8).  Procure palavra em ingles no meio de
frase portuguesa.

### Erro 4 -- frase gramaticalmente quebrada

`"Seus status podem parecidos inicio."` -- sem verbo, sem sentido.
Provavelmente foi encurtamento as pressas para caber.

**Licao:** quando a linha nao cabe, **reescreva a frase inteira**, nao
arranque palavras dela.

### Erro 5 -- retraduziu o que ja estava pronto, e pior

`dialogo_ginasio_goldenrod.py` tinha 12 falas.  **Todas as 12** ja
estavam no lote 5a, conferidas e publicadas.  Como o arquivo vinha
depois na lista `LOTES`, ele **sobrescrevia** a versao boa por uma com
estouro de coluna.

**Antes de criar um lote, confira se a chave ja existe:**

```bash
python -c "
import sys; sys.path.insert(0,'.')
import pt
_s,n=pt.carregar()
print('57:4122' in n)   # True = ja traduzida, nao mexa
"
```

`pendentes.py` ja exclui o que esta traduzido -- e mais um motivo para
usa-lo em vez de montar a lista a mao.

### Erro 6 -- deixou arquivos de rascunho no repositorio

`temp_analyze.py`, `temp_check.py`, `temp_fix.py`, `temp_width.py`,
`_find_falkner.py` foram commitados.  Rascunho fica no scratchpad.
(Ja ha `temp_*.py` no `.gitignore`.)

### Resumo do conserto, em ordem

```bash
python acentuar.py                    # 1. acentos
python conferir.py                    # 2. ver o que estoura
#    corrigir as linhas uma a uma, pela Regra 2
python conferir.py                    # 3. ate dar zero
#    4. RELER tudo (10.8) procurando erro de sentido
```

---

## 11. Estado atual

Versao publicada: **0.25.0**.

| | |
|---|---|
| Falas publicadas | 2803 |
| Falas **nossas** | 1564 |
| Falas ainda derivadas | 1239 |
| Rotulos de menu e batalha | 265 |
| Nomes de item | ficam em ingles (0.17.0) |
| Glifos acentuados | 25 |

Lotes prontos:

| Lote | Escopo | Falas |
|---|---|---|
| 1 | New Bark, casa, laboratorio do ELM | 87 |
| 2 | Rota 29, Cherrygrove, rota 30 | 56 |
| 3 | Violet, Sprout Tower, ginasio do FALKNER | 59 |
| 4 | Azalea, Slowpoke Well, Ilex, KURT, BUGSY | 65 |
| 5a | Goldenrod cidade, WHITNEY, DEPT.STORE | 43 |
| 5b | RADIO TOWER, rotas 34/35, NATIONAL PARK | 51 |
| 6a | Ecruteak, MORTY, BURNED/TIN TOWER, rotas 38/39 | 31 |
| 6b | Olivine, JASMINE, LIGHTHOUSE, Cianwood, CHUCK | 40 |
| 7 | StdScripts do banco 40 (comuns a todo mapa) | 32 |
| 8a | Mahogany, PRYCE, rotas 42/43 | 35 |
| 8b | LAKE OF RAGE, o LANCE, casa do MAGIKARP | 27 |
| 8c | Base da TEAM ROCKET, tres andares | 35 |
| 09a-11 | RADIO TOWER, RUINS, rota 36, Concurso *(outra sessao, revisado)* | 200 |
| 12 | Ginasio do FALKNER -- as falas que a varredura achou | 5 |
| 13 | Resto do banco 40: GAME CORNER, telefone, batalha | 44 |
| 14a | Telefone: a MÃE, o armazenamento, o BILL, o ELM | 36 |
| 14b | Telefone: saudacoes, revanches, avistamentos | 33 |
| 15a-c | Banco 4b: pescadores, HIKERS, DAY-CARE, as irmas | 78 |
| 16 | Banco 4c: gemeas, nadadores, WHIRL ISLANDS | 72 |
| 17 | Banco 4d: rotas do norte, os passaros lendarios | 67 |
| 18 | Banco 4e: mar de Kanto, CYCLING ROAD | 39 |
| 19 | Banco 4f: rotas de Kanto, professores, videntes | 54 |
| 20 | Banco 50: ROCK TUNNEL, os seis, POWER PLANT | 64 |
| 21 | Banco 5b: o FAST SHIP inteiro | 67 |
| 22 | Banco 44: RUINS, MT.MORTAR, SLOWPOKE WELL, LIGHTHOUSE | 69 |
| 23 | Bancos 45/46: esconderijo ninja, senhas, subterraneo | 49 |
| 24 | Varridas dos bancos 40-4c: RADIO TOWER, SPROUT TOWER, VICTORY ROAD, passagem | 140 |

Alem do dialogo: `pt/sistema.py` e `pt/sistema2.py` cobrem 265 rotulos
do motor -- menus, batalha (`%s usou\n%s!`), PC, loja, GAME CORNER e a
fala de abertura do PROF.OAK.

### A pasta de trabalho nao e o repositorio

O trabalho acontece num **scratchpad**, fora do git.  Nesta maquina:

```
C:\Users\Usuario\AppData\Local\Temp\claude\D--pokemon-gold-tradu--o\<sessao>\scratchpad
```

La ficam tres coisas que **nao estao no repositorio** e sem as quais
nenhuma ferramenta roda:

- `dialogo.json` -- 2245 falas, ingles + BR, gerado por `walk.py`
- `repo/` -- o fonte do gen1recomp, de onde saem opcodes e o manifest
  de mapas (`repo/tools/rom_manifest_gold.json`)
- `br/` -- a ROM brasileira, usada so para conferencia

A ROM USA fica em `D:\pokemon gold traducao\`.  Se o scratchpad sumir,
`walk.py` reconstroi `dialogo.json` a partir das duas ROMs mais o
`repo/`.  O `tools/` do repositorio e uma **copia** do scratchpad --
edite no scratchpad e copie, nunca o contrario.

### Proximo passo

Falta trabalho de duas naturezas bem diferentes.

**1. As varridas -- 145 falas, sem traducao nenhuma hoje.**

Sao as que a varredura da 0.16.0 achou e nenhum lote cobriu.  Hoje
aparecem **em ingles** na tela.  Prioridade, portanto.

O lote 24 (0.25.0) zerou as varridas dos bancos 40-4c; resta:

```bash
python pendentes.py 52        # e assim por diante
```

| Banco | Faltam | O que e |
|---|---|---|
| 52 | 22 | interiores de Johto |
| 57 | 20 | Goldenrod: lojas, ginasio, torre |
| 51 | 17 | casas de Ecruteak e Olivine |
| 53 | 16 | casas de Mahogany e Blackthorn |
| 55 | 14 | Azalea: centro, loja, KURT |
| 5d | 13 | Cianwood e arredores |
| 5e | 13 | Blackthorn e a Liga |
| 59 | 11 | cidades |
| 54 | 8 | outros |
| 56 | 4 | outros |
| 5b | 4 | outros |
| 5a | 3 | outros |

**2. As derivadas -- 1239 falas.**

Estao **em portugues** no jogo, vindas da traducao de R_Lopes e
Night_Shadown.  Traduzi-las de novo nao muda o que o jogador ve; muda
a **procedencia**.  E o que falta para `progresso.py` zerar e a
atribuicao poder virar agradecimento (secao 5).

Para achar uma fala derivada e reescreve-la do ingles:

```bash
python -c "
import json,sys; sys.path.insert(0,'.')
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
import pt
_s,n=pt.carregar()
d=json.load(open('dialogo.json',encoding='utf-8'))
alvo=[k for k,(en,br) in d.items() if br.strip() and k not in n and k.startswith('55:')]
print(len(alvo)); print(alvo[:10])
"
```

Depois trate como lote normal: `esqueleto.py` da chave, escreva com
`linhas()`, confira.  **Traduza do ingles**, nao do portugues deles --
e o ponto inteiro do exercicio.  `conferir.py` compara so com o ingles
justamente para isso.

**Ordem sugerida:** as 145 varridas primeiro (o jogador ve ingles
agora), depois as derivadas por regiao.

---

## 12. Pendencias que nao dependem de traducao

- **Marcos do mapa** (95 nomes de local): bloqueados pela issue #976 do
  upstream, ainda aberta.  O banner de entrada de mapa nao aceita override.
- **Contatos do Pokegear** (32): o registro `phone_contacts` existe mas
  **nenhum boot de Gold o consulta** -- preencher nao surtiria efeito.  As
  *conversas* ao telefone sao texto de script normal e ja estao traduzidas;
  so a listinha de nomes fica em ingles.
- **Falas ainda descartadas pelos filtros**: 188 por kana, 12 por marcador
  nao decifrado.  Recuperaveis com mais deducao de charmap.
- **391 rotulos de `strings`** nao traduzidos, quase todos mensagens longas
  de erro do launcher -- que, por decisao, nao entram mesmo.

---

## 12-A. Um lote completo, do comeco ao fim

Exemplo real (lote 22), para copiar o ritmo.

```bash
cd <scratchpad>

# 1. o que falta no banco 44
python pendentes.py 44
#    69 falas -> planilha-pend-44.py
#    fora: {'ja tem derivada': 125}

# 2. ler a estrutura -- em DUAS partes, porque a saida e longa
python esqueleto.py planilha-pend-44.py | head -175
python esqueleto.py planilha-pend-44.py | sed -n '175,420p'

# 3. escrever pt/dialogo_22.py com linhas()

# 4. contagem de linha ANTES de registrar
python -c "...script da secao 10.4..."

# 5. registrar em pt/__init__.py
python -c "
p='pt/__init__.py'; s=open(p,encoding='utf-8').read()
s=s.replace('\"dialogo_21\"]','\"dialogo_21\", \"dialogo_22\"]')
open(p,'w',encoding='utf-8').write(s)
"

# 6. conferir ate zero
python conferir.py
#    6 problemas -> corrigir -> 0 problemas

# 7. RELER as falas corrigidas (10.8)
#    achei 'cortando as cauda' -- concordancia, o conferidor aprovou

# 8. versao, changelog, README
# 9. build, copia, commit, release, feed
```

Tempo tipico: a leitura do esqueleto e a escrita levam a maior parte.
O conferidor costuma acusar entre 5 e 30 linhas num lote de 70 -- isso
e normal, nao e sinal de que o lote esta ruim.

---

## 12-AA. PRIMEIRO DE TUDO: montar a pasta de trabalho

**Leia isto antes de qualquer coisa.**  O scratchpad e por sessao: uma
sessao nova recebe uma pasta VAZIA, e sem os arquivos abaixo nenhuma
ferramenta roda.  Nao adianta tentar traduzir antes de resolver isto.

Faltam tres coisas, nenhuma no git:

| Arquivo | O que e | Tamanho |
|---|---|---|
| `dialogo.json` | 3277 falas, ingles + BR | ~610 KB |
| `repo/` | fonte do gen1recomp (opcodes, manifest de mapas) | pasta |
| `br/*.gbc` | a ROM brasileira, so para conferencia | 2 MB |

### Caminho 1 -- copiar do scratchpad antigo (rapido)

O scratchpad da sessao anterior costuma continuar no disco.  Procure:

```bash
ls -d "C:/Users/Usuario/AppData/Local/Temp/claude/D--pokemon-gold-tradu--o"/*/scratchpad
```

Achando, copie o que importa para o scratchpad novo:

```bash
VELHO="<o caminho que apareceu>"
NOVO="<seu scratchpad>"
cp "$VELHO/dialogo.json" "$NOVO/"
cp -r "$VELHO/repo" "$VELHO/br" "$NOVO/"
cp "$VELHO"/*.py "$NOVO/"
cp -r "$VELHO/pt" "$NOVO/"
```

Se o `pt/` do scratchpad antigo estiver mais velho que o do
repositorio, prefira o do repositorio -- ele e a fonte publicada:

```bash
cp -r "D:/pokemon gold traducao/versaodourada/tools/"*.py "$NOVO/"
cp -r "D:/pokemon gold traducao/versaodourada/tools/pt" "$NOVO/"
```

### Caminho 2 -- reconstruir do zero

Se nao houver scratchpad antigo:

1. As ferramentas estao todas no repositorio, em `tools/`.  Copie
   `tools/*.py` e `tools/pt/` para o scratchpad novo.
2. Clone o gen1recomp em `<scratchpad>/repo`:
   `git clone https://github.com/bryanthaboi/gen1recomp repo`
3. A ROM BR precisa estar em `<scratchpad>/br/`.  O usuario tem o
   arquivo (`Pokemon - Gold Version (BR) (www.romsportugues.com).7z`).
   **Sem ela o `walk.py` nao roda** -- ele percorre as duas ROMs em
   passo travado.
4. Gere o `dialogo.json`:

```bash
python walk.py                              # 2245 falas
python -c "import varrer; varrer.gravar()"  # +1032 = 3277
```

A ROM USA fica em `D:\pokemon gold traducao\` e o caminho esta fixo no
topo de `walk.py` (`USA_PATH`).  Se o usuario mover a pasta, corrija
ali.

### Conferir que deu certo

```bash
python -c "
import json; d=json.load(open('dialogo.json',encoding='utf-8'))
print(len(d), 'falas')                      # esperado: 3277
print('56:4634' in d)                       # True (veio da varredura)
"
python conferir.py                          # esperado: 0 problemas
python progresso.py
```

Se `conferir.py` acusar "chave nao existe no jogo", o `dialogo.json`
esta com 2245 e falta rodar `varrer.gravar()`.

---

## 12-B. Se voce estiver retomando com o contexto zerado

Ordem de leitura:

0. **Secao 12-AA** -- montar a pasta de trabalho.  Sem isso nada roda.
1. Secao **2** (as tres restricoes que mandam em tudo).
2. Secao **10** inteira (o processo) e **10-A** (o oficio).
3. Secao **10-B** (o que ja deu errado) antes de escrever a primeira fala.
4. Secao **11** (estado) para saber onde parar.
5. `tools/CHANGELOG_mod.md` -- cada versao diz o que entrou e por que.

Comandos para se situar em um minuto:

```bash
python progresso.py            # quanto e nosso
python conferir.py             # o catalogo esta limpo?
git -C "D:/pokemon gold traducao/versaodourada" log --oneline -5
```

Se `conferir.py` acusar problema **sem voce ter mexido em nada**, e
porque o `dialogo.json` do scratchpad esta desatualizado em relacao aos
lotes -- rode `python -c "import varrer; varrer.gravar()"` para repor as
1032 falas da varredura.

---

## 13. Se algo quebrar

**Acentos aparecem em branco:** a pagina de glifos nao carregou.  Reponha o
mapa `DOBRA` em `build_mod.py` (uma linha) e tudo volta a ASCII, como na
0.5.0.

**Acentos aparecem como bloco preto:** o fundo do PNG esta opaco.  Tem de
ser `(0,0,0,0)`.

**O mod nao aparece na lista:** confira `game_version` (`<2.0.0`) e
`games: ["gold"]` no manifest.

**O mod aparece mas nao traduz:** as chaves nao estao casando.  Havia um
bloco de diagnostico no `main.lua` ate a 0.5.0 -- vale reintroduzir para
contar quantas chaves o jogo reconhece.

**O feed nao oferece atualizacao:** o `gerar_indice.py` espera a API do
GitHub alcancar o manifest e aborta se nao alcancar.  Se abortar, e porque
o release ainda nao foi publicado.  O `raw.githubusercontent` tem cache de
~5 min e o indice no app, de 24 h -- use *Refresh all*.

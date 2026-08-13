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
tools/pt/            a traducao propria, um arquivo por lote
tools/conferir.py    compara a traducao propria com o ingles
tools/validar.py     QA do catalogo publicado
tools/glossario.py   terminologia, sem estourar as 18 colunas
tools/glifos.py      desenha a pagina de glifos acentuados
tools/progresso.py   quanto ja e nosso, quanto ainda e derivado
tools/build_mod.py   monta o mod
tools/gerar_indice.py  gera o feed do catalogo
```

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

## 10. Como fazer o proximo lote

```bash
cd tools
python lote.py 05          # escreve planilha-05.py com o ingles
```

1. Leia a planilha.  Ela mostra os codigos de controle explicitos (`repr`).
2. Escreva `tools/pt/dialogo_05b.py` com um dict `DIALOGO`.
3. Registre o lote em `tools/pt/__init__.py`, na lista `LOTES`.
4. `python conferir.py` ate dar **0 problemas**.
5. `python build_mod.py`
6. Atualize os numeros em `tools/README_mod.md` e o `CHANGELOG.md`.
7. Commit, push, `gh release create`, e `python gerar_indice.py`.

### Tamanho do lote importa

Lotes 2, 3 e 5a (56, 59 e 43 falas) passaram com **zero** problemas.  O
lote 4 (65 falas, escrito com pressa) deu **32**.  Goldenrod tem 126 e foi
dividido em duas metades por isso.

**Ate ~60 falas por lote.**  Passar disso nao acelera, so gera retrabalho.

### O que descartar

Kana solto, fragmentos que comecam no meio de outra fala, strings vazias e
`'Object event.'` sao lixo do extrator, nao texto de jogo.  Deixe em
ingles em vez de publicar sujeira.

---

## 11. Estado atual

| | |
|---|---|
| Falas publicadas | 1977 |
| Falas **nossas** | 308 |
| Falas ainda derivadas | 1669 |
| Rotulos de menu (tela do jogo) | 151 |
| Nomes de item | 68 |
| Glifos acentuados | 25 |

Lotes prontos: 1 (New Bark), 2 (Cherrygrove), 3 (Violet), 4 (Azalea),
5a (Goldenrod cidade).

**Proximo:** lote 5b -- torre de radio, rotas 34 e 35, National Park.
Cerca de 77 falas; divida se achar melhor.

Depois: lote 6 (Ecruteak, Olivine, Cianwood) ja esta definido em
`lote.py`.  Faltam ainda as regioes do norte de Johto, a Liga e Kanto --
crie os lotes 7+ no mesmo formato.

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

# Changelog

## 0.8.0

**Comeca a traducao propria do dialogo.** Lote 1: as 87 falas de New Bark
Town, da casa do jogador, do laboratorio e da casa do Elm -- traduzidas a
partir do ingles original, nao adaptadas de ninguem.

`tools/conferir.py` confere cada uma contra o ingles e reprova o que quebra
a caixa de texto em silencio:

- a sequencia de `
` / `` / `` tem de ser identica em ordem e
  quantidade -- sao quebra de linha, rolagem e quebra de pagina;
- os tokens ({PLAYER}, {RIVAL}, {STRBUF}) idem;
- nenhuma linha acima de 18 colunas, medindo os tokens pelo que rendem;
- nenhum caractere sem glifo.

Na primeira passada ele acusou 26 problemas nas minhas proprias traducoes:
12 sequencias de controle que eu tinha alterado sem perceber e 13 linhas de
19 colunas. Todas corrigidas -- a versao publicada passa limpa.

Progresso: 87 de 2245 falas ja sao nossas. A atribuicao continua obrigatoria
enquanto houver uma unica fala derivada, e `tools/progresso.py` diz quantas
sao.

## 0.8.0

- Primeira versao: 1972 falas em portugues.
- Nomes de golpes mantidos no original.

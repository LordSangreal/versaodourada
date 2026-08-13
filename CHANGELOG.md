# Changelog

## 0.8.2

Conserta uma regressao silenciosa: o README voltava sozinho para o texto
da 0.3.0.

Ele morava DENTRO do `build_mod.py`, como uma string gigante, entao todo
build reescrevia o arquivo do repositorio com a versao congelada no codigo.
Eu atualizei a pagina na 0.8.0 e a publicacao da 0.8.1 a desfez, sem erro
nenhum.

Agora o README e um arquivo de verdade (`tools/README_mod.md`) e o build so
o copia para dentro do pacote. Se ele sumir, o build avisa em vez de gerar
um mod sem README.

## 0.8.2

- Primeira versao: 1972 falas em portugues.
- Nomes de golpes mantidos no original.

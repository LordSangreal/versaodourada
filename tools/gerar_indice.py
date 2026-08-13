"""Gera o feed de indice que o gen1recomp consome (site/data/index.json).

O app resolve uma fonte de indice a partir de uma URL .json direta
(src/mods/ModIndex.lua, ModIndex.resolveSource), entao nao e preciso GitHub
Pages: basta o repositorio ser publico e o jogador colar a URL raw deste
arquivo em Ajustes > indices de mod.

Uso:
    python tools/gerar_indice.py
"""
import json, os, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = "LordSangreal/versaodourada"
AUTHOR = "LordSangreal"
FOLDER = "%s@versaodourada" % AUTHOR
SCHEMA_VERSION = 1

manifest = json.load(open(os.path.join(ROOT, "manifest.json"), encoding="utf-8"))


def gh(path):
    """GET na API do GitHub via gh, que ja carrega a autenticacao."""
    exe = r"C:\Program Files\GitHub CLI\gh.exe"
    cmd = [exe if os.path.exists(exe) else "gh", "api", path]
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        raise SystemExit("gh api falhou: " + (out.stderr or "").strip())
    return json.loads(out.stdout)


def latest_block():
    """O bloco `latest`, com o zip do release mais novo nao-prerelease."""
    rels = gh("repos/%s/releases?per_page=100" % REPO)
    rels = [r for r in rels if not r.get("draft")]
    if not rels:
        return None, 0
    stable = [r for r in rels if not r.get("prerelease")] or rels
    rel = stable[0]
    zips = [a for a in rel.get("assets", []) if a["name"].endswith(".zip")]
    if not zips:
        raise SystemExit("o release %s nao tem asset .zip" % rel.get("tag_name"))
    a = zips[0]
    downloads = sum(x.get("download_count", 0)
                    for r in rels for x in r.get("assets", []))
    return {
        "version": rel["tag_name"].lstrip("v"),
        "tag": rel["tag_name"],
        "name": rel.get("name") or rel["tag_name"],
        "prerelease": bool(rel.get("prerelease")),
        "published_at": rel.get("published_at"),
        "zip": {"name": a["name"],
                "url": a["browser_download_url"],
                "size": a.get("size", 0)},
    }, downloads


def latest_confirmado(esperado, tentativas=6, espera=5):
    """A API do GitHub leva alguns segundos para listar um release recem-criado.

    Publicar o feed nesse intervalo grava um bloco `latest` apontando para a
    versao ANTERIOR -- foi o que aconteceu na 0.1.4: o feed dizia
    version 0.1.4 e latest.tag v0.1.3, entao o aplicativo comparava com o
    bloco `latest`, via 0.1.3 e concluia que nao havia atualizacao.
    Espera a API alcancar o manifest em vez de gravar o que vier.
    """
    import time
    for n in range(tentativas):
        bloco, _ = latest_block()
        if bloco and bloco["version"] == esperado:
            return bloco
        if n < tentativas - 1:
            print("  API ainda em %s, esperando %ss..."
                  % (bloco["version"] if bloco else "nada", espera))
            time.sleep(espera)
    raise SystemExit(
        "ABORTADO: o manifest diz %s mas o release mais novo na API e %s.\n"
        "Publique o release dessa versao antes de gerar o feed."
        % (esperado, bloco["version"] if bloco else "nenhum"))


latest = latest_confirmado(manifest["version"])

entry = {
    "folder": FOLDER,
    "id": manifest["id"],
    "title": "VersaoDourada",
    "author": AUTHOR,
    "version": manifest["version"],
    "categories": ["LANGUAGE"],
    "repo": "https://github.com/" + REPO,
    "summary": ("Pokemon Gold em portugues brasileiro. Traducao de R_Lopes e "
                "Night_Shadown; nomes de golpes no original."),
    "tags": ["portuguese", "brazilian", "translation", "gold", "gen2"],
    "github": REPO,
    "permissions": [],
    "api": manifest["api"],
    "profile": manifest["profile"],
    "games": manifest.get("games", []),
    "description_url": "data/mods/%s/description.md" % FOLDER,
}
if latest:
    entry["latest"] = latest
    entry["update_check"] = "ok"

feed = {
    "schema_version": SCHEMA_VERSION,
    "generated_at": datetime.datetime.now(datetime.UTC)
                    .strftime("%Y-%m-%dT%H:%M:%SZ"),
    "count": 1,
    "categories": ["LANGUAGE"],
    "mods": [entry],
}

out_dir = os.path.join(ROOT, "site", "data")
os.makedirs(os.path.join(out_dir, "mods", FOLDER), exist_ok=True)
with open(os.path.join(out_dir, "index.json"), "w", encoding="utf-8") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)

print("feed escrito: site/data/index.json")
print("  versao no manifest:", manifest["version"])
print("  release mais novo :", latest["tag"] if latest else "(nenhum)")

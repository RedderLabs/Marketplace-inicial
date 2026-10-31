#!/usr/bin/env python3
"""Convierte un proyecto web en un prompt de un solo paso (formato SELENE).

Uso:
  python3 exportar-prompt.py <carpeta-del-proyecto> [salida.md]

Lee <proyecto>/PROMPT-cabecera.md (obligatorio) y <proyecto>/PROMPT-notas.md (opcional),
y entre los dos añade una sección "## File:" por cada archivo de texto del proyecto.
Ignora node_modules, dist, public/, lockfiles, binarios y los propios PROMPT-*.md.
"""
import re
import sys
from pathlib import Path

RAIZ_PRIMERO = [
    "index.html", "package.json", "vite.config.ts", "vite.config.js", "astro.config.mjs",
    "tsconfig.json", "tsconfig.app.json", "tsconfig.node.json", ".gitignore",
]
CARPETAS = ["src"]
IGNORAR_DIRS = {"node_modules", "dist", ".git", "public", ".astro", ".vite"}
LENGUAJE = {
    ".html": "html", ".json": "json", ".ts": "ts", ".tsx": "tsx", ".js": "js", ".mjs": "js",
    ".jsx": "jsx", ".css": "css", ".astro": "astro", ".md": "md", ".svg": "svg",
}
TEXTO = set(LENGUAJE) | {""}
SOSPECHOSO = re.compile(
    r"(sk-[A-Za-z0-9]{16,}|AKIA[0-9A-Z]{16}|api[_-]?key\s*[:=]\s*['\"][^'\"]{8,}|"
    r"secret\s*[:=]\s*['\"][^'\"]{8,}|password\s*[:=]\s*['\"][^'\"]+)",
    re.IGNORECASE,
)


def archivos(proyecto: Path):
    vistos = []
    for nombre in RAIZ_PRIMERO:
        p = proyecto / nombre
        if p.is_file():
            vistos.append(p)
    for carpeta in CARPETAS:
        base = proyecto / carpeta
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and not (set(p.relative_to(proyecto).parts) & IGNORAR_DIRS):
                if p.suffix.lower() in TEXTO:
                    vistos.append(p)
    return vistos


def bloque(ruta: str, contenido: str, lenguaje: str) -> str:
    valla = "````" if "```" in contenido else "```"
    return f"## File: `{ruta}`\n\n{valla}{lenguaje}\n{contenido.rstrip()}\n{valla}\n"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    proyecto = Path(sys.argv[1]).resolve()
    salida = Path(sys.argv[2]) if len(sys.argv) > 2 else proyecto / "PROMPT.md"

    cabecera = proyecto / "PROMPT-cabecera.md"
    if not cabecera.is_file():
        print(f"Falta {cabecera}. Escríbelo primero (ver references/plantilla-prompt.md).", file=sys.stderr)
        return 1

    partes = [cabecera.read_text(encoding="utf-8").rstrip() + "\n"]
    avisos = []
    lista = archivos(proyecto)
    for p in lista:
        ruta = p.relative_to(proyecto).as_posix()
        try:
            contenido = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            avisos.append(f"Saltado (no es texto): {ruta}")
            continue
        for n, linea in enumerate(contenido.splitlines(), 1):
            if SOSPECHOSO.search(linea):
                avisos.append(f"Posible secreto en {ruta}:{n} — revísalo antes de compartir el prompt.")
        partes.append(bloque(ruta, contenido, LENGUAJE.get(p.suffix.lower(), "")))

    notas = proyecto / "PROMPT-notas.md"
    if notas.is_file():
        partes.append(notas.read_text(encoding="utf-8").rstrip() + "\n")

    salida.write_text("\n".join(partes), encoding="utf-8")
    print(f"{salida}: {len(lista)} archivos.")
    for a in avisos:
        print("Aviso:", a)
    return 0


if __name__ == "__main__":
    sys.exit(main())

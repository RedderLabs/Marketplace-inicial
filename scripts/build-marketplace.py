#!/usr/bin/env python3
"""Genera .claude-plugin/marketplace.json a partir de skills/ y categorias.json.

Crea:
  - un plugin "todo" con todas las skills de skills/ (un solo comando para instalarlo todo)
  - un plugin por categoría, con solo las skills de esa categoría

Uso (desde la raíz del repo):  python3 scripts/build-marketplace.py
"""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MARKETPLACE = "redder-roles"
PROPIETARIO = {"name": "Redder Labs", "url": "https://redderlabs.com"}

DESCRIPCIONES = {
    "desarrollo": "Roles de desarrollo: ingeniería de apps y web, webs premium.",
    "creativos": "Roles creativos: guion, novela, escritura.",
    "negocio": "Roles de negocio: análisis financiero, estrategia.",
    "herramientas": "Herramientas para crear, probar y mejorar skills.",
}


def main() -> int:
    carpeta_skills = RAIZ / "skills"
    skills = sorted(p.name for p in carpeta_skills.iterdir() if (p / "SKILL.md").is_file())
    if not skills:
        print("No hay ninguna skill en skills/.", file=sys.stderr)
        return 1

    categorias = json.loads((RAIZ / "categorias.json").read_text(encoding="utf-8"))

    sin_categoria = [s for s in skills if s not in categorias]
    for s in sin_categoria:
        print(f"Aviso: '{s}' no está en categorias.json. Va solo en el plugin 'todo'.")
    for s in sorted(set(categorias) - set(skills)):
        print(f"Aviso: '{s}' está en categorias.json pero no existe en skills/. Se ignora.")

    version_archivo = RAIZ / "VERSION"
    version = version_archivo.read_text(encoding="utf-8").strip() if version_archivo.exists() else None

    def plugin(nombre, visible, descripcion, lista=None):
        entrada = {"name": nombre, "displayName": visible, "source": "./", "description": descripcion}
        if lista is not None:
            entrada["skills"] = [f"./skills/{s}" for s in lista]
        if version:
            entrada["version"] = version
        return entrada

    plugins = [
        plugin(
            "todo",
            "Todas las skills",
            f"Instala de una vez las {len(skills)} skills del repo. "
            "No lo combines con los plugins por categoría o tendrás las skills repetidas.",
        )
    ]

    por_categoria = {}
    for s in skills:
        if s in categorias:
            por_categoria.setdefault(categorias[s], []).append(s)
    for cat in sorted(por_categoria):
        plugins.append(
            plugin(cat, cat.capitalize(), DESCRIPCIONES.get(cat, f"Skills de {cat}."), por_categoria[cat])
        )

    marketplace = {
        "name": MARKETPLACE,
        "description": "Skills de roles profesionales en español, de Redder Labs.",
        "owner": PROPIETARIO,
        "plugins": plugins,
    }

    destino = RAIZ / ".claude-plugin" / "marketplace.json"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text(json.dumps(marketplace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"marketplace.json generado: todo ({len(skills)} skills) + {len(por_categoria)} categorías.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

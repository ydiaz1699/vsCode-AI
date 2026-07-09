"""
Herramientas para leer las guías de generación.

Las guías viven en guides/gen-*.md y definen CÓMO crear cada archivo
del proyecto (estructura, reglas, formato esperado).
"""

from pathlib import Path
from strands.tools import tool

# Raíz del proyecto vsCode-AI
BASE_DIR = Path(__file__).resolve().parent.parent.parent


@tool
def read_guide(guide_name: str) -> str:
    """Lee una guía de generación para saber CÓMO crear un archivo específico.

    Las guías definen la estructura, reglas y formato que debe seguir cada
    archivo generado. Cada guía corresponde a un archivo del proyecto final
    (SKILL.md, HARDWARE.md, README.md, etc.).

    SIEMPRE consultar la guía correspondiente ANTES de generar un archivo.

    Args:
        guide_name: Nombre de la guía sin extensión .md.
                    Ejemplos: gen-skill, gen-hardware, gen-software,
                    gen-project-context, gen-readme, gen-architecture,
                    gen-conexiones-svg, gen-notas-hw, gen-coding-style,
                    gen-decisions, gen-roadmap, gen-tasks, gen-testing,
                    gen-changelog, gen-protocol, gen-secrets-template,
                    gen-copilot-instructions, gen-archivo-mapa
    """
    guides_dir = BASE_DIR / "guides"
    guide_file = guides_dir / f"{guide_name}.md"

    if not guide_file.exists():
        disponibles = sorted(f.stem for f in guides_dir.glob("gen-*.md"))
        return (
            f"ERROR: Guía '{guide_name}' no encontrada.\n"
            f"Guías disponibles: {', '.join(disponibles)}\n"
            f"Usa uno de estos nombres exactos (sin .md)."
        )

    content = guide_file.read_text(encoding="utf-8")
    return (
        f"=== GUÍA: {guide_name} ===\n\n"
        f"{content}\n\n"
        f"--- Fin de guía {guide_name} ---"
    )


@tool
def list_guides() -> str:
    """Lista todas las guías de generación disponibles con una breve descripción.

    Cada guía explica cómo crear un archivo específico del proyecto.
    Consultar esta lista para saber qué guías existen antes de generar archivos.
    """
    guides_dir = BASE_DIR / "guides"
    guides = sorted(guides_dir.glob("gen-*.md"))

    if not guides:
        return "ERROR: No se encontraron guías en guides/"

    # Extraer la primera línea significativa como descripción
    entradas = []
    for g in guides:
        try:
            lines = g.read_text(encoding="utf-8").strip().splitlines()
            desc = ""
            for line in lines:
                stripped = line.strip()
                if stripped and not stripped.startswith("#"):
                    desc = stripped[:80]
                    break
            if not desc:
                for line in lines:
                    if line.startswith("# "):
                        desc = line[2:].strip()
                        break
            entradas.append(f"  - {g.stem}: {desc}")
        except Exception:
            entradas.append(f"  - {g.stem}: (error al leer)")

    return (
        f"=== GUÍAS DE GENERACIÓN ({len(entradas)}) ===\n\n"
        + "\n".join(entradas)
        + "\n\n"
        f"Usa read_guide(nombre) para ver el contenido completo de una guía."
    )

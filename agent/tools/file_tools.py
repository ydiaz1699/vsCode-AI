"""
Tools para operaciones de archivo en el proyecto generado.

Permiten al agente crear archivos de salida, leer archivos existentes
y explorar la estructura de un directorio de proyecto.
"""

from pathlib import Path
from strands.tools import tool


@tool
def write_file(path: str, content: str) -> str:
    """Escribe un archivo en el proyecto que se está generando.

    Crea directorios intermedios automáticamente si no existen.
    Sobreescribe el archivo si ya existe.

    Args:
        path: Ruta relativa del archivo a crear.
              Ejemplos: .ai/SKILL.md, src/main.cpp, platformio.ini,
              docs/conexiones.drawio.svg, secrets.h.template,
              .ai/HARDWARE.md, README.md
        content: Contenido completo del archivo (texto UTF-8).
    """
    file_path = Path(path)

    # Seguridad: no permitir paths absolutos o traversal
    if file_path.is_absolute():
        return "ERROR: No se permiten rutas absolutas. Usa rutas relativas al proyecto."
    if ".." in file_path.parts:
        return "ERROR: No se permite '..' en la ruta. Usa rutas dentro del proyecto."

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")
        size = len(content.encode("utf-8"))
        return (
            f"✅ Archivo creado: {path}\n"
            f"   Tamaño: {size} bytes\n"
            f"   Directorio: {file_path.parent}"
        )
    except Exception as e:
        return f"ERROR al escribir '{path}': {e}"


@tool
def read_project_file(path: str) -> str:
    """Lee un archivo existente del proyecto (código fuente, config, docs).

    Útil para analizar código existente antes de generar documentación,
    o para verificar qué ya existe en el proyecto.

    Args:
        path: Ruta relativa al archivo a leer.
              Ejemplos: src/main.cpp, platformio.ini, .ai/SKILL.md,
              include/config.h, lib/sensor/sensor.cpp
    """
    file_path = Path(path)

    if file_path.is_absolute():
        return "ERROR: No se permiten rutas absolutas. Usa rutas relativas al proyecto."
    if ".." in file_path.parts:
        return "ERROR: No se permite '..' en la ruta."

    if not file_path.exists():
        return f"ERROR: Archivo no encontrado: {path}"
    if not file_path.is_file():
        return f"ERROR: '{path}' no es un archivo (¿es un directorio?)."

    try:
        content = file_path.read_text(encoding="utf-8")
        lines = content.count("\n") + 1
        size = len(content.encode("utf-8"))
        return (
            f"=== {path} ({lines} líneas, {size} bytes) ===\n\n"
            f"{content}"
        )
    except UnicodeDecodeError:
        return f"ERROR: '{path}' no es un archivo de texto (binario)."
    except Exception as e:
        return f"ERROR al leer '{path}': {e}"


@tool
def list_project_files(directory: str = ".") -> str:
    """Lista todos los archivos de un directorio del proyecto recursivamente.

    Muestra la estructura de árbol con tamaños. Útil para entender
    la organización de un proyecto existente antes de documentarlo.

    Args:
        directory: Ruta relativa al directorio a explorar.
                   Ejemplos: . (raíz), src, lib, include, .ai, docs
    """
    dir_path = Path(directory)

    if dir_path.is_absolute():
        return "ERROR: No se permiten rutas absolutas."
    if ".." in dir_path.parts:
        return "ERROR: No se permite '..' en la ruta."

    if not dir_path.exists():
        return f"ERROR: Directorio no encontrado: {directory}"
    if not dir_path.is_dir():
        return f"ERROR: '{directory}' no es un directorio."

    # Recopilar archivos recursivamente (excluir .git y __pycache__)
    excluded = {".git", "__pycache__", "node_modules", ".pio", ".vscode"}
    files = []
    dirs_found = set()

    for f in sorted(dir_path.rglob("*")):
        # Saltar directorios excluidos
        if any(part in excluded for part in f.parts):
            continue
        if f.is_file():
            rel = f.relative_to(dir_path)
            size = f.stat().st_size
            files.append(f"  {rel} ({size} bytes)")
            dirs_found.add(str(f.parent.relative_to(dir_path)))

    if not files:
        return f"Directorio '{directory}' está vacío."

    return (
        f"=== Archivos en '{directory}' ===\n"
        f"Total: {len(files)} archivos en {len(dirs_found)} directorios\n\n"
        + "\n".join(files)
    )

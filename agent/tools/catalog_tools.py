"""
Tools para acceder al catálogo de hardware (boards y peripherals).

El catálogo vive en catalog/boards/*.md y catalog/peripherals/*.md
Cada archivo usa frontmatter YAML con metadatos estructurados + contenido Markdown.
"""

from pathlib import Path
from strands.tools import tool
import frontmatter

# Base del proyecto (raíz de vsCode-AI)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


@tool
def load_board(board_id: str) -> str:
    """Carga las especificaciones completas de una placa del catálogo de hardware.

    Retorna el frontmatter YAML (metadatos estructurados: voltaje, pines, flash,
    protocolo, compatibilidad WiFi/BT) y la documentación completa en Markdown
    (pinout, consideraciones críticas, platformio.ini de referencia).

    Args:
        board_id: ID de la placa tal como aparece en el catálogo.
                  Ejemplos: esp32-devkit-v1, arduino-uno, esp8266-d1-mini-pro,
                  stm32-bluepill, rp2040-pico
    """
    boards_dir = BASE_DIR / "catalog" / "boards"
    board_file = boards_dir / f"{board_id}.md"

    if not board_file.exists():
        available = sorted(
            f.stem for f in boards_dir.glob("*.md")
            if not f.name.startswith("_")
        )
        return (
            f"ERROR: Placa '{board_id}' no encontrada en el catálogo.\n"
            f"Placas disponibles: {', '.join(available)}\n"
            f"Usa uno de estos IDs exactos."
        )

    post = frontmatter.load(str(board_file))
    metadata_str = "\n".join(f"  {k}: {v}" for k, v in post.metadata.items())

    return (
        f"=== PLACA: {post.metadata.get('name', board_id)} ===\n\n"
        f"Metadatos (frontmatter):\n{metadata_str}\n\n"
        f"Documentación completa:\n{post.content}"
    )


@tool
def load_peripheral(peripheral_id: str) -> str:
    """Carga las especificaciones de un periférico/sensor/actuador del catálogo.

    Retorna el frontmatter YAML (voltaje, protocolo, librería, pines requeridos,
    necesidad de level-shifter) y la documentación completa (conexiones por placa,
    código de ejemplo, compatibilidad, consideraciones críticas).

    Args:
        peripheral_id: ID del periférico tal como aparece en el catálogo.
                       Ejemplos: dht22, hc-sr04, ssd1306-oled, rc522-rfid,
                       nrf24l01, relay-5v, rf433-rcswitch, mpu6050
    """
    periphs_dir = BASE_DIR / "catalog" / "peripherals"
    periph_file = periphs_dir / f"{peripheral_id}.md"

    if not periph_file.exists():
        available = sorted(
            f.stem for f in periphs_dir.glob("*.md")
            if not f.name.startswith("_")
        )
        return (
            f"ERROR: Periférico '{peripheral_id}' no encontrado en el catálogo.\n"
            f"Periféricos disponibles: {', '.join(available)}\n"
            f"Usa uno de estos IDs exactos."
        )

    post = frontmatter.load(str(periph_file))
    metadata_str = "\n".join(f"  {k}: {v}" for k, v in post.metadata.items())

    return (
        f"=== PERIFÉRICO: {post.metadata.get('name', peripheral_id)} ===\n\n"
        f"Metadatos (frontmatter):\n{metadata_str}\n\n"
        f"Documentación completa:\n{post.content}"
    )


@tool
def list_catalog() -> str:
    """Lista todas las placas y periféricos disponibles en el catálogo de hardware.

    Retorna un resumen con ID, nombre y características principales de cada
    elemento. Úsalo para saber qué hardware está documentado antes de
    intentar cargar fichas individuales.
    """
    boards_dir = BASE_DIR / "catalog" / "boards"
    periphs_dir = BASE_DIR / "catalog" / "peripherals"

    # Listar boards con info básica
    boards_info = []
    for f in sorted(boards_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(str(f))
            meta = post.metadata
            wifi = "WiFi" if meta.get("wifi") else ""
            bt = f"BT{meta.get('bluetooth_version', '')}" if meta.get("bluetooth") else ""
            connectivity = " + ".join(filter(None, [wifi, bt])) or "Sin conectividad"
            boards_info.append(
                f"  - {meta.get('id', f.stem)}: {meta.get('name', '?')} "
                f"({meta.get('mcu', '?')}, {meta.get('ram_kb', '?')}KB RAM, "
                f"{connectivity})"
            )
        except Exception:
            boards_info.append(f"  - {f.stem}: (error al leer)")

    # Listar periféricos con info básica
    periphs_info = []
    for f in sorted(periphs_dir.glob("*.md")):
        if f.name.startswith("_"):
            continue
        try:
            post = frontmatter.load(str(f))
            meta = post.metadata
            periphs_info.append(
                f"  - {meta.get('id', f.stem)}: {meta.get('name', '?')} "
                f"({meta.get('protocol', '?')}, {meta.get('voltage_min', '?')}-"
                f"{meta.get('voltage_max', '?')}V, cat: {meta.get('category', '?')})"
            )
        except Exception:
            periphs_info.append(f"  - {f.stem}: (error al leer)")

    return (
        f"=== CATÁLOGO DE HARDWARE ===\n\n"
        f"PLACAS ({len(boards_info)}):\n" + "\n".join(boards_info) + "\n\n"
        f"PERIFÉRICOS ({len(periphs_info)}):\n" + "\n".join(periphs_info) + "\n\n"
        f"Usa load_board(id) o load_peripheral(id) para ver detalles completos."
    )

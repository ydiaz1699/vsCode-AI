"""
Herramientas para analizar código fuente existente.

Permiten al agente inspeccionar proyectos PlatformIO/Arduino existentes
para detectar placa, periféricos y generar documentación adaptada.
"""

import re
from pathlib import Path
from strands.tools import tool
import frontmatter

# Raíz del proyecto vsCode-AI (para acceder al catálogo)
BASE_DIR = Path(__file__).resolve().parent.parent.parent



@tool
def analyze_code(file_path: str) -> str:
    """Lee y analiza un archivo de código fuente, retornando su contenido
    junto con observaciones sobre patrones detectados.

    Detecta automáticamente: includes, defines, funciones principales,
    uso de delay(), credenciales hardcodeadas, y GPIOs restringidos.

    Args:
        file_path: Ruta al archivo de código fuente.
                   Ejemplos: src/main.cpp, include/config.h,
                   platformio.ini, lib/sensor/sensor.h
    """
    path = Path(file_path)

    if not path.exists():
        return f"ERROR: Archivo no encontrado: {file_path}"
    if not path.is_file():
        return f"ERROR: '{file_path}' no es un archivo."

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return f"ERROR: '{file_path}' no es un archivo de texto."

    lines = content.splitlines()
    observaciones = []

    # Detectar patrones problemáticos
    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # delay() en loop (anti-patrón)
        if "delay(" in stripped and not stripped.startswith("//"):
            observaciones.append(
                f"  ⚠️  L{i}: delay() detectado — considerar millis()"
            )

        # Credenciales hardcodeadas
        if re.search(
            r'(ssid|password|api_key|token)\s*=\s*"[^"]+',
            stripped, re.IGNORECASE
        ):
            observaciones.append(
                f"  ⚠️  L{i}: Posible credencial hardcodeada"
            )

        # GPIO restringidos ESP32
        gpio_match = re.findall(
            r'GPIO_NUM_(\d+)|#define\s+\w+PIN\s+(\d+)', stripped
        )
        for match in gpio_match:
            pin = int(match[0] or match[1])
            if pin in (6, 7, 8, 9, 10, 11):
                observaciones.append(
                    f"  ❌ L{i}: GPIO{pin} es restringido (flash SPI)"
                )

    # Detectar includes
    includes = [l.strip() for l in lines if l.strip().startswith("#include")]

    # Detectar funciones
    func_pattern = re.compile(
        r'^(?:void|int|float|bool|String|char)\s+(\w+)\s*\('
    )
    funciones = [
        func_pattern.match(l.strip()).group(1)
        for l in lines if func_pattern.match(l.strip())
    ]

    obs_str = "\n".join(observaciones) if observaciones else "  ✅ Sin problemas detectados"

    return (
        f"=== ANÁLISIS: {file_path} ({len(lines)} líneas) ===\n\n"
        f"Includes ({len(includes)}):\n"
        + "\n".join(f"  {inc}" for inc in includes[:20])
        + f"\n\nFunciones detectadas: "
        + f"{', '.join(funciones) if funciones else '(ninguna)'}\n\n"
        + f"Observaciones:\n{obs_str}\n\n"
        + f"--- Código completo ---\n{content}"
    )



@tool
def detect_board(directory: str = ".") -> str:
    """Detecta qué placa usa un proyecto PlatformIO analizando platformio.ini.

    Busca el campo 'board' en platformio.ini y lo cruza con el catálogo
    de vsCode-AI para dar información completa sobre la placa.

    Args:
        directory: Directorio raíz del proyecto PlatformIO.
                   Ejemplo: . (directorio actual), ./mi-proyecto
    """
    ini_path = Path(directory) / "platformio.ini"

    if not ini_path.exists():
        return (
            f"ERROR: No se encontró platformio.ini en '{directory}'.\n"
            f"¿Es un proyecto PlatformIO? Verifica la ruta."
        )

    content = ini_path.read_text(encoding="utf-8")

    # Buscar board = xxx
    board_match = re.search(r'^\s*board\s*=\s*(.+)$', content, re.MULTILINE)
    if not board_match:
        return "ERROR: No se encontró campo 'board' en platformio.ini"

    pio_board = board_match.group(1).strip()

    # Mapear boards de PlatformIO a IDs del catálogo
    BOARD_MAP = {
        "esp32dev": "esp32-devkit-v1",
        "esp32-s3-devkitc-1": "esp32-s3-devkitc",
        "esp32-c3-devkitm-1": "esp32-c3-devkitm",
        "d1_mini_pro": "esp8266-d1-mini-pro",
        "nodemcuv2": "esp8266-nodemcu-v3",
        "esp01_1m": "esp8266-esp01s",
        "uno": "arduino-uno",
        "nanoatmega328": "arduino-nano",
        "megaatmega2560": "arduino-mega",
        "bluepill_f103c8": "stm32-bluepill",
        "blackpill_f401cc": "stm32-blackpill",
        "pico": "rp2040-pico",
    }

    catalog_id = BOARD_MAP.get(pio_board)

    if catalog_id:
        board_file = BASE_DIR / "catalog" / "boards" / f"{catalog_id}.md"
        if board_file.exists():
            post = frontmatter.load(str(board_file))
            meta = post.metadata
            return (
                f"=== PLACA DETECTADA ===\n\n"
                f"PlatformIO board: {pio_board}\n"
                f"Catálogo ID: {catalog_id}\n"
                f"Nombre: {meta.get('name', '?')}\n"
                f"MCU: {meta.get('mcu', '?')}\n"
                f"Voltaje lógico: {meta.get('voltage_logic', '?')}V\n"
                f"WiFi: {'✅' if meta.get('wifi') else '❌'}\n"
                f"Bluetooth: {'✅ v' + str(meta.get('bluetooth_version', '')) if meta.get('bluetooth') else '❌'}\n"
                f"RAM: {meta.get('ram_kb', '?')} KB\n"
                f"Flash: {meta.get('flash_mb', '?')} MB\n"
                f"GPIOs restringidos: {meta.get('gpio_restricted', [])}\n\n"
                f"Usa load_board('{catalog_id}') para la ficha completa."
            )

    return (
        f"Placa PlatformIO detectada: {pio_board}\n"
        f"⚠️ No encontrada en el catálogo de vsCode-AI.\n"
        f"Catálogo ID intentado: {catalog_id or '(sin mapeo)'}\n"
        f"Considera agregar una ficha nueva al catálogo."
    )



@tool
def detect_peripherals(directory: str = ".") -> str:
    """Detecta periféricos usados en un proyecto analizando el código fuente.

    Busca patrones de librerías, includes y defines que correspondan
    a periféricos del catálogo de vsCode-AI.

    Args:
        directory: Directorio raíz del proyecto.
                   Ejemplo: . (directorio actual), ./mi-proyecto
    """
    dir_path = Path(directory)

    if not dir_path.exists():
        return f"ERROR: Directorio no encontrado: {directory}"

    # Patrones de detección: library/include → peripheral_id
    PATRONES_DETECCION = {
        "DHT.h": "dht22",
        "DHT sensor library": "dht22",
        "NewPing.h": "hc-sr04",
        "NewPing": "hc-sr04",
        "HCSR04": "hc-sr04",
        "Adafruit_SSD1306.h": "ssd1306-oled",
        "U8g2": "ssd1306-oled",
        "SSD1306Wire.h": "ssd1306-oled",
        "MFRC522.h": "rc522-rfid",
        "MFRC522": "rc522-rfid",
        "RF24.h": "nrf24l01",
        "nRF24L01": "nrf24l01",
        "RCSwitch.h": "rf433-rcswitch",
        "RCSwitch": "rf433-rcswitch",
        "MPU6050.h": "mpu6050",
        "Adafruit_MPU6050": "mpu6050",
    }

    # Buscar en archivos de código y platformio.ini
    extensiones = {".cpp", ".h", ".ino", ".c", ".hpp"}
    archivos_buscar = list(dir_path.rglob("platformio.ini"))
    for ext in extensiones:
        archivos_buscar.extend(dir_path.rglob(f"*{ext}"))

    detectados = {}  # peripheral_id → [evidencia]

    for f in archivos_buscar:
        try:
            content = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, Exception):
            continue

        for patron, periph_id in PATRONES_DETECCION.items():
            if patron in content:
                if periph_id not in detectados:
                    detectados[periph_id] = []
                rel_path = (
                    f.relative_to(dir_path)
                    if f.is_relative_to(dir_path) else f
                )
                detectados[periph_id].append(f"{rel_path} ('{patron}')")

    if not detectados:
        return (
            f"No se detectaron periféricos del catálogo en '{directory}'.\n"
            f"Archivos analizados: {len(archivos_buscar)}\n"
            f"Puede que use periféricos no catalogados."
        )

    # Formatear resultados
    resultados = []
    for periph_id, evidencia in sorted(detectados.items()):
        periph_file = BASE_DIR / "catalog" / "peripherals" / f"{periph_id}.md"
        nombre = periph_id
        if periph_file.exists():
            try:
                post = frontmatter.load(str(periph_file))
                nombre = post.metadata.get("name", periph_id)
            except Exception:
                pass

        resultados.append(
            f"  ✅ {periph_id} ({nombre})\n"
            f"     Evidencia: {'; '.join(evidencia[:3])}"
        )

    return (
        f"=== PERIFÉRICOS DETECTADOS en '{directory}' ===\n\n"
        f"Encontrados: {len(detectados)} periférico(s) del catálogo\n\n"
        + "\n".join(resultados)
        + f"\n\nUsa load_peripheral(id) para la ficha completa de cada uno."
    )

"""
firmware_agent.py — Agente Strands Nivel 1 para vsCode-AI

Agente inteligente que usa el catálogo de hardware, guías de generación y
el system prompt (synapse-v3.md) para crear proyectos firmware IoT/embebido.

En vez de copiar templates determinísticamente, el agente RAZONA sobre:
- Qué placa y periféricos usar (consultando el catálogo)
- Qué archivos generar (leyendo las guías)
- Cómo adaptar el código al contexto específico del proyecto

Uso:
    # Modo interactivo
    python -m agent.firmware_agent

    # Con query directa
    python -m agent.firmware_agent "Crea un sensor IoT con ESP32 y DHT22"

    # Con modelo alternativo (Anthropic directo, OpenAI, Ollama)
    STRANDS_MODEL=anthropic python -m agent.firmware_agent "..."
    STRANDS_MODEL=openai python -m agent.firmware_agent "..."
    STRANDS_MODEL=ollama python -m agent.firmware_agent "..."

Requisitos:
    pip install strands-agents strands-agents-tools python-frontmatter
    export AWS_REGION=us-east-1  # Para Bedrock (default)
"""

import os
import sys
from pathlib import Path

from strands import Agent

from agent.tools import ALL_TOOLS

# ─────────────────────────────────────────────────────────────────────────────
# Configuración de paths
# ─────────────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = BASE_DIR / "prompts"
SYSTEM_PROMPT_FILE = PROMPTS_DIR / "synapse-v3.md"

# ─────────────────────────────────────────────────────────────────────────────
# Cargar System Prompt
# ─────────────────────────────────────────────────────────────────────────────


def load_system_prompt() -> str:
    """Carga el system prompt desde prompts/synapse-v3.md.

    Agrega un preámbulo que informa al modelo sobre las herramientas
    disponibles y cómo debe usarlas.
    """
    if not SYSTEM_PROMPT_FILE.exists():
        raise FileNotFoundError(
            f"System prompt no encontrado: {SYSTEM_PROMPT_FILE}\n"
            f"Asegúrate de ejecutar desde la raíz de vsCode-AI."
        )

    synapse_prompt = SYSTEM_PROMPT_FILE.read_text(encoding="utf-8")

    # Preámbulo con instrucciones para el uso de tools
    tools_preamble = """
# HERRAMIENTAS DISPONIBLES

Tienes acceso a las siguientes herramientas para cumplir los objetivos del usuario.
DEBES usarlas activamente — no inventes datos de hardware ni estructuras de archivo.

## Catálogo de Hardware
- `list_catalog()` → Ver todas las placas y periféricos disponibles
- `load_board(board_id)` → Cargar ficha completa de una placa
- `load_peripheral(peripheral_id)` → Cargar ficha completa de un periférico

## Guías de Generación
- `list_guides()` → Ver todas las guías disponibles
- `read_guide(guide_name)` → Leer una guía para saber CÓMO generar un archivo

## Archivos de Proyecto
- `write_file(path, content)` → Crear/escribir un archivo en el proyecto de salida
- `read_project_file(path)` → Leer un archivo existente del proyecto
- `list_project_files(directory)` → Listar archivos de un directorio

## Análisis de Código
- `analyze_code(file_path)` → Analizar un archivo de código fuente
- `detect_board(directory)` → Detectar qué placa usa un proyecto (via platformio.ini)
- `detect_peripherals(directory)` → Detectar periféricos usados en el código

## Flujo de Trabajo Obligatorio

1. SIEMPRE consultar el catálogo ANTES de hablar sobre hardware
2. SIEMPRE leer la guía correspondiente ANTES de generar un archivo
3. SIEMPRE verificar compatibilidad de voltaje entre placa y periféricos
4. NUNCA inventar especificaciones que no estén en el catálogo
5. Para proyectos nuevos (/new): generar TODOS los archivos .ai/ + código + docs

---

"""
    return tools_preamble + synapse_prompt


# ─────────────────────────────────────────────────────────────────────────────
# Configurar modelo según entorno
# ─────────────────────────────────────────────────────────────────────────────


def get_model():
    """Selecciona el modelo según la variable de entorno STRANDS_MODEL.

    Valores soportados:
        - bedrock (default): Amazon Bedrock con Claude Sonnet
        - anthropic: API de Anthropic directa
        - openai: API de OpenAI (GPT-4o)
        - ollama: Modelo local via Ollama

    Variables de entorno adicionales:
        - STRANDS_MODEL_ID: Override del model_id específico
        - ANTHROPIC_API_KEY: Para modelo anthropic
        - OPENAI_API_KEY: Para modelo openai
        - OLLAMA_HOST: Host de Ollama (default: http://localhost:11434)
    """
    provider = os.environ.get("STRANDS_MODEL", "bedrock").lower()
    model_id_override = os.environ.get("STRANDS_MODEL_ID")

    if provider == "bedrock":
        # Default: Amazon Bedrock con Claude Sonnet 4
        from strands.models.bedrock import BedrockModel
        model_id = model_id_override or "us.anthropic.claude-sonnet-4-20250514-v1:0"
        return BedrockModel(
            model_id=model_id,
            region_name=os.environ.get("AWS_REGION", "us-east-1"),
        )

    elif provider == "anthropic":
        from strands.models.anthropic import AnthropicModel
        model_id = model_id_override or "claude-sonnet-4-20250514"
        return AnthropicModel(model_id=model_id)

    elif provider == "openai":
        from strands.models.openai import OpenAIModel
        model_id = model_id_override or "gpt-4o"
        return OpenAIModel(model_id=model_id)

    elif provider == "ollama":
        from strands.models.ollama import OllamaModel
        model_id = model_id_override or "llama3.1"
        host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        return OllamaModel(model_id=model_id, host=host)

    else:
        raise ValueError(
            f"Modelo '{provider}' no soportado.\n"
            f"Opciones: bedrock, anthropic, openai, ollama\n"
            f"Configura con: export STRANDS_MODEL=<opción>"
        )


# ─────────────────────────────────────────────────────────────────────────────
# Crear el Agente
# ─────────────────────────────────────────────────────────────────────────────


def create_firmware_agent() -> Agent:
    """Crea y retorna el agente firmware configurado con tools y system prompt."""
    system_prompt = load_system_prompt()
    model = get_model()

    agent = Agent(
        model=model,
        tools=ALL_TOOLS,
        system_prompt=system_prompt,
    )

    return agent


# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────────────────────────────────────


def main():
    """Punto de entrada principal del agente firmware."""
    print("🧙🏾‍♂️ vsCode-AI Firmware Agent (Strands SDK)")
    print("=" * 50)

    # Verificar que estamos en el directorio correcto
    if not (BASE_DIR / "catalog").exists():
        print(
            f"⚠️  No se encontró el catálogo en: {BASE_DIR / 'catalog'}\n"
            f"    Ejecuta desde la raíz del proyecto vsCode-AI:\n"
            f"    cd vsCode-AI && python -m agent.firmware_agent"
        )
        sys.exit(1)

    # Obtener query del usuario
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"\n📝 Query: {query}\n")
    else:
        print("\n¿Qué proyecto firmware quieres crear?")
        print("  Ejemplos:")
        print("  - Crea un sensor de temperatura IoT con ESP32 y DHT22")
        print("  - Documenta el proyecto en ./mi-proyecto/")
        print("  - /catalog para ver hardware disponible")
        print()
        query = input("🧙🏾‍♂️ > ")
        if not query.strip():
            print("❌ No se proporcionó ninguna query.")
            sys.exit(0)

    # Crear y ejecutar el agente
    print("⚡ Inicializando agente...")
    agent = create_firmware_agent()

    print("🚀 Procesando...\n")
    print("-" * 50)
    result = agent(query)
    print("-" * 50)
    print("\n✅ Agente completó la tarea.")

    return result


if __name__ == "__main__":
    main()

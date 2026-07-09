# Next Step: Integrar Strands Agents SDK

> **Estado**: Planificado (no implementado aún)
> **Prioridad**: Siguiente fase del proyecto
> **Dependencia**: AWS credentials con acceso a Bedrock (Claude)

---

## Qué es Strands Agents

[Strands Agents](https://strandsagents.com/) es un SDK open-source de AWS para construir
agentes de IA con un enfoque "model-driven". En vez de scripts deterministas, le das al
agente: un **modelo LLM** + un **system prompt** + **herramientas (tools)**, y el modelo
decide autónomamente cómo usarlas para completar la tarea.

- Repo: https://github.com/strands-agents/sdk-python
- Docs: https://strandsagents.com/
- Instalación: `pip install strands-agents strands-agents-tools`

## Por qué integrarlo en vsCode-AI

El `generator.py` actual es determinista: copia templates y reemplaza placeholders.
Con Strands Agents, el generador se convierte en un **agente inteligente** que:

1. **Razona** sobre qué archivos generar según el contexto del proyecto
2. **Consulta** el catálogo (boards/peripherals) como herramientas
3. **Lee** las guías de generación para saber CÓMO crear cada archivo
4. **Adapta** el contenido al código fuente real (no solo placeholders)
5. **Valida** compatibilidad de voltaje, pines, etc. antes de sugerir conexiones

## Plan de implementación

### Estructura propuesta

```
vsCode-AI/
├── ... (todo lo que ya existe se mantiene)
│
├── agent/                          ← NUEVO
│   ├── __init__.py
│   ├── firmware_agent.py           ← Agente principal
│   ├── docs_agent.py              ← Agente para documentar código existente
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── catalog_tools.py       ← load_board, load_peripheral, list_catalog
│   │   ├── guide_tools.py         ← read_guide (lee las 18 guías)
│   │   ├── file_tools.py          ← write_file, read_file, list_project_files
│   │   ├── analysis_tools.py      ← analyze_code, detect_board, detect_peripherals
│   │   └── platformio_tools.py    ← generate_ini, validate_config
│   └── README.md
│
└── requirements.txt               ← Agregar: strands-agents, strands-agents-tools
```

### Tools a implementar

Cada tool es una función Python con el decorador `@tool` que el agente puede llamar:

| Tool | Qué hace | Archivo |
|------|----------|---------|
| `load_board(board_id)` | Lee frontmatter YAML de una placa del catálogo | catalog_tools.py |
| `load_peripheral(peripheral_id)` | Lee frontmatter YAML de un periférico | catalog_tools.py |
| `list_catalog()` | Lista boards y periféricos disponibles | catalog_tools.py |
| `read_guide(guide_name)` | Lee una guía de generación (gen-skill.md, etc.) | guide_tools.py |
| `write_file(path, content)` | Escribe un archivo en el proyecto de salida | file_tools.py |
| `read_file(path)` | Lee un archivo existente del proyecto | file_tools.py |
| `list_project_files(directory)` | Lista archivos de un directorio | file_tools.py |
| `analyze_code(file_path)` | Lee y retorna contenido de un .cpp/.h/.ini | analysis_tools.py |

### Código de ejemplo (firmware_agent.py)

```python
from strands import Agent
from strands.tools import tool
from pathlib import Path
import frontmatter

BASE_DIR = Path(__file__).parent.parent

@tool
def load_board(board_id: str) -> str:
    """Carga las especificaciones completas de una placa del catálogo.

    Args:
        board_id: ID de la placa (ej: esp32-devkit-v1, arduino-uno)
    """
    board_file = BASE_DIR / "catalog" / "boards" / f"{board_id}.md"
    if not board_file.exists():
        available = [f.stem for f in (BASE_DIR / "catalog" / "boards").glob("*.md") if not f.name.startswith("_")]
        return f"ERROR: Placa '{board_id}' no encontrada. Disponibles: {', '.join(sorted(available))}"
    post = frontmatter.load(str(board_file))
    return f"Frontmatter:\n{post.metadata}\n\nDocumentación:\n{post.content}"

@tool
def load_peripheral(peripheral_id: str) -> str:
    """Carga las especificaciones de un periférico del catálogo.

    Args:
        peripheral_id: ID del periférico (ej: dht22, relay-5v, ssd1306-oled)
    """
    periph_file = BASE_DIR / "catalog" / "peripherals" / f"{peripheral_id}.md"
    if not periph_file.exists():
        available = [f.stem for f in (BASE_DIR / "catalog" / "peripherals").glob("*.md") if not f.name.startswith("_")]
        return f"ERROR: Periférico '{peripheral_id}' no encontrado. Disponibles: {', '.join(sorted(available))}"
    post = frontmatter.load(str(periph_file))
    return f"Frontmatter:\n{post.metadata}\n\nDocumentación:\n{post.content}"

@tool
def list_catalog() -> str:
    """Lista todas las placas y periféricos disponibles en el catálogo."""
    boards = sorted(f.stem for f in (BASE_DIR / "catalog" / "boards").glob("*.md") if not f.name.startswith("_"))
    periphs = sorted(f.stem for f in (BASE_DIR / "catalog" / "peripherals").glob("*.md") if not f.name.startswith("_"))
    return f"Boards ({len(boards)}): {', '.join(boards)}\nPeriféricos ({len(periphs)}): {', '.join(periphs)}"

@tool
def read_guide(guide_name: str) -> str:
    """Lee una guía de generación para saber CÓMO crear un archivo específico.

    Args:
        guide_name: Nombre de la guía sin extensión (ej: gen-skill, gen-hardware, gen-readme)
    """
    guide_file = BASE_DIR / "guides" / f"{guide_name}.md"
    if not guide_file.exists():
        available = sorted(f.stem for f in (BASE_DIR / "guides").glob("gen-*.md"))
        return f"ERROR: Guía '{guide_name}' no encontrada. Disponibles: {', '.join(available)}"
    return guide_file.read_text(encoding="utf-8")

@tool
def write_file(path: str, content: str) -> str:
    """Escribe un archivo en el proyecto que se está generando.

    Args:
        path: Ruta relativa del archivo (ej: .ai/SKILL.md, src/main.cpp)
        content: Contenido completo del archivo a escribir
    """
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    return f"✅ Archivo creado: {path} ({len(content)} bytes)"

@tool
def analyze_code(file_path: str) -> str:
    """Lee y analiza un archivo de código fuente.

    Args:
        file_path: Ruta al archivo de código (ej: src/main.cpp, platformio.ini)
    """
    path = Path(file_path)
    if not path.exists():
        return f"ERROR: Archivo no encontrado: {file_path}"
    content = path.read_text(encoding="utf-8")
    return f"=== {file_path} ({len(content)} chars) ===\n{content}"


# --- System Prompt (synapse-v3.md) ---
SYSTEM_PROMPT = (BASE_DIR / "prompts" / "synapse-v3.md").read_text(encoding="utf-8")

# --- Crear el Agente ---
firmware_agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",  # Bedrock Claude Sonnet
    tools=[load_board, load_peripheral, list_catalog, read_guide, write_file, analyze_code],
    system_prompt=SYSTEM_PROMPT
)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("🧙🏾‍♂️ ¿Qué proyecto quieres crear? > ")
    firmware_agent(query)
```

### Uso esperado

```bash
# Instalar dependencias
pip install strands-agents strands-agents-tools python-frontmatter

# Configurar AWS (Bedrock)
export AWS_REGION=us-east-1
export AWS_PROFILE=default  # o configurar credentials

# Ejecutar el agente
cd vsCode-AI/
python -m agent.firmware_agent "Crea un proyecto de cierre centralizado con ESP32 y BLE"

# El agente:
# 1. Lee el catálogo → esp32-devkit-v1.md
# 2. Lee guías → gen-skill.md, gen-hardware.md, etc.
# 3. Genera archivos adaptados al proyecto específico
# 4. Escribe todo en la carpeta de salida
```

### Modelos soportados

El agente puede usar cualquier proveedor:

```python
# Amazon Bedrock (default)
agent = Agent(model="us.anthropic.claude-sonnet-4-20250514-v1:0")

# Anthropic directo
from strands.models.anthropic import AnthropicModel
agent = Agent(model=AnthropicModel(model_id="claude-sonnet-4-20250514"))

# OpenAI
from strands.models.openai import OpenAIModel
agent = Agent(model=OpenAIModel(model_id="gpt-4o"))

# Ollama (local, gratis)
from strands.models.ollama import OllamaModel
agent = Agent(model=OllamaModel(model_id="llama3.1"))
```

### Nivel avanzado: Multi-agente

Para el futuro, se puede evolucionar a múltiples agentes especializados:

- **hw_agent**: Experto en hardware — genera HARDWARE.md, conexiones SVG, notas
- **code_agent**: Experto en firmware C++ — genera main.cpp, platformio.ini
- **docs_agent**: Experto en documentación — genera SKILL, README, archivo-mapa
- **orchestrator**: Professor Synapse — coordina los 3 agentes

## Requisitos previos

1. **AWS Account** con acceso a Amazon Bedrock
2. **Model access habilitado** para Claude Sonnet (o el modelo que elijas)
3. **AWS CLI configurado** (`aws configure`)
4. **Python 3.10+**

## Para empezar en un nuevo chat

Decirle a la IA:

```
Lee el archivo docs/next-strands-agent.md de mi repo ydiaz1699/vsCode-AI
y ayúdame a implementar el Nivel 1: firmware_agent.py con los tools del catálogo.
El repo ya tiene el catálogo (catalog/), las guías (guides/) y los prompts (prompts/).
Solo necesito crear la carpeta agent/ con los tools y el agente principal.
```

## Referencias

- [Strands Agents SDK](https://github.com/strands-agents/sdk-python)
- [Documentación oficial](https://strandsagents.com/)
- [Custom Tools Guide](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/)
- [Blog AWS: Introducing Strands 1.0](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-1-0-production-ready-multi-agent-orchestration-made-simple)
- [Agent Builder (ejemplo interactivo)](https://github.com/strands-agents/agent-builder)

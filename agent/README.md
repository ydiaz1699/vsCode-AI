# vsCode-AI Strands Agent

Agente inteligente basado en [Strands Agents SDK](https://strandsagents.com/) que usa el catálogo de hardware, guías de generación y el prompt Professor Synapse para crear proyectos firmware IoT/embebido.

## Requisitos

### Python 3.10+

```bash
pip install strands-agents strands-agents-tools python-frontmatter
```

### Credenciales (según el modelo)

**Amazon Bedrock (default):**
```bash
export AWS_REGION=us-east-1
export AWS_PROFILE=default
# Requiere model access habilitado para Claude Sonnet en Bedrock
```

**Anthropic API directa:**
```bash
export STRANDS_MODEL=anthropic
export ANTHROPIC_API_KEY=sk-ant-...
```

**OpenAI:**
```bash
export STRANDS_MODEL=openai
export OPENAI_API_KEY=sk-...
```

**Ollama (local, gratis):**
```bash
export STRANDS_MODEL=ollama
export STRANDS_MODEL_ID=llama3.1  # o cualquier modelo instalado
# Requiere Ollama corriendo: ollama serve
```

## Uso

### Desde la raíz del proyecto vsCode-AI:

```bash
# Modo interactivo
python -m agent.firmware_agent

# Con query directa
python -m agent.firmware_agent "Crea un sensor de temperatura IoT con ESP32 y DHT22"

# Documentar un proyecto existente
python -m agent.firmware_agent "Analiza ./mi-proyecto/ y genera toda la documentación .ai/"

# Ver catálogo
python -m agent.firmware_agent "/catalog"
```

### Importar en tu código:

```python
from agent.firmware_agent import create_firmware_agent

agent = create_firmware_agent()
result = agent("Crea un proyecto de cierre centralizado con ESP32 y BLE")
```

## Arquitectura

```
agent/
├── __init__.py              # Package init + versión
├── firmware_agent.py        # Agente principal (entry point)
├── README.md                # Este archivo
└── tools/
    ├── __init__.py          # Exporta ALL_TOOLS
    ├── catalog_tools.py     # load_board, load_peripheral, list_catalog
    ├── guide_tools.py       # read_guide, list_guides
    ├── file_tools.py        # write_file, read_project_file, list_project_files
    └── analysis_tools.py    # analyze_code, detect_board, detect_peripherals
```

## Tools disponibles

| Tool | Descripción | Módulo |
|------|-------------|--------|
| `load_board(board_id)` | Carga ficha completa de una placa del catálogo | catalog_tools |
| `load_peripheral(peripheral_id)` | Carga ficha completa de un periférico | catalog_tools |
| `list_catalog()` | Lista todo el hardware disponible | catalog_tools |
| `read_guide(guide_name)` | Lee una guía de generación | guide_tools |
| `list_guides()` | Lista todas las guías disponibles | guide_tools |
| `write_file(path, content)` | Crea un archivo en el proyecto de salida | file_tools |
| `read_project_file(path)` | Lee un archivo existente | file_tools |
| `list_project_files(directory)` | Lista archivos de un directorio | file_tools |
| `analyze_code(file_path)` | Analiza código fuente (detecta anti-patrones) | analysis_tools |
| `detect_board(directory)` | Detecta la placa via platformio.ini | analysis_tools |
| `detect_peripherals(directory)` | Detecta periféricos por librerías/includes | analysis_tools |

## Cómo funciona

1. El agente recibe una instrucción del usuario (ej: "Crea un proyecto IoT con ESP32 y DHT22")
2. Lee el system prompt (Professor Synapse / synapse-v3.md)
3. Decide autónomamente qué herramientas usar:
   - Consulta el catálogo para verificar hardware
   - Lee las guías para saber cómo generar cada archivo
   - Verifica compatibilidad de voltaje
4. Genera todos los archivos del proyecto usando `write_file()`
5. El resultado es un proyecto PlatformIO completo con documentación `.ai/`

## Variables de entorno

| Variable | Default | Descripción |
|----------|---------|-------------|
| `STRANDS_MODEL` | `bedrock` | Proveedor: bedrock, anthropic, openai, ollama |
| `STRANDS_MODEL_ID` | (auto) | Override del model ID específico |
| `AWS_REGION` | `us-east-1` | Región de AWS para Bedrock |
| `AWS_PROFILE` | `default` | Perfil AWS CLI |
| `ANTHROPIC_API_KEY` | — | API key de Anthropic |
| `OPENAI_API_KEY` | — | API key de OpenAI |
| `OLLAMA_HOST` | `http://localhost:11434` | Host de Ollama |

## Próximos pasos (Nivel 2 y 3)

- **Nivel 2**: `docs_agent.py` — Agente especializado en documentar código existente
- **Nivel 3**: Multi-agente con orquestador (hw_agent + code_agent + docs_agent)

Ver `docs/next-strands-agent.md` para el plan completo.

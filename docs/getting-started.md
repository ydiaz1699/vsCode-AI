# 🚀 Getting Started — Inicio Rápido en 5 Minutos

## Requisitos

| Herramienta | Versión Mínima | Instalación |
|-------------|---------------|-------------|
| VS Code | 1.80+ | [code.visualstudio.com](https://code.visualstudio.com/) |
| PlatformIO IDE | 3.3+ | Extensión de VS Code |
| Git | 2.30+ | `sudo apt install git` / `brew install git` |
| Python | 3.8+ | Requerido por PlatformIO |

## Instalación

```bash
# 1. Clonar el repositorio del framework
git clone https://github.com/tu-usuario/vsCode-AI.git
cd vsCode-AI

# 2. Verificar estructura
ls catalog/ templates/ guides/ prompts/ docs/
```

No se requieren dependencias adicionales — el framework es solo archivos Markdown y templates.

---

## Opción A: Usar con CLI (Copiar Templates)

Para usuarios que prefieren trabajar manualmente:

```bash
# 1. Crear directorio del proyecto
mkdir mi-proyecto && cd mi-proyecto

# 2. Inicializar PlatformIO
pio project init --board esp32dev --ide vscode

# 3. Crear estructura .ai/
mkdir -p .ai docs

# 4. Copiar templates base (reemplazar placeholders manualmente)
cp /path/to/vsCode-AI/templates/_base/PROJECT_CONTEXT.md .ai/
cp /path/to/vsCode-AI/templates/_base/HARDWARE.md .ai/
cp /path/to/vsCode-AI/templates/_base/SOFTWARE.md .ai/
cp /path/to/vsCode-AI/templates/_base/SKILL.md .ai/
cp /path/to/vsCode-AI/templates/_base/TASKS.md .ai/
cp /path/to/vsCode-AI/templates/_base/CHANGELOG.md .ai/
cp /path/to/vsCode-AI/templates/_base/DECISIONS.md .ai/
cp /path/to/vsCode-AI/templates/_base/ROADMAP.md .ai/

# 5. Copiar opcionales si aplica
# cp /path/to/vsCode-AI/templates/_optional/ARCHITECTURE.md .ai/
# cp /path/to/vsCode-AI/templates/_optional/PROTOCOL.md .ai/

# 6. Editar cada archivo reemplazando {{PLACEHOLDERS}} con valores reales
```

---

## Opción B: Usar con IA (Recomendado)

Para usuarios que trabajan con un asistente IA (Copilot, Claude, ChatGPT):

```
1. Copia el contenido de prompts/synapse-v3.md como system prompt de tu IA

2. Inicia con el comando:
   /new

3. La IA te preguntará:
   - ¿Qué hace el proyecto?
   - ¿Qué placa usas?
   - ¿Qué periféricos conectarás?

4. Synapse v3 generará automáticamente:
   - Estructura PlatformIO completa
   - Código base funcional
   - Documentación .ai/ completa
   - README.md para humanos

5. Para proyectos existentes sin documentación:
   - Copia prompts/generator-context.md como system prompt
   - Pega tu código fuente como contexto
   - La IA generará los 18 archivos de documentación
```

---

## Opción C: Manual (Sin IA, Sin CLI)

Para entender la estructura y completar a mano:

1. **Lee** `docs/architecture.md` para entender el diseño de 3 capas
2. **Crea** la carpeta `.ai/` en tu proyecto PlatformIO existente
3. **Abre** `guides/README.md` para ver qué archivos necesitas
4. **Sigue** cada guía (`guides/gen-*.md`) paso a paso
5. **Rellena** los templates copiando desde `templates/_base/`
6. **Verifica** que los IDs del catálogo sean correctos consultando `catalog/README.md`

---

## Verificación

Tu proyecto está correctamente configurado si tiene:

```
mi-proyecto/
├── .ai/
│   ├── PROJECT_CONTEXT.md   ← Contexto para IA
│   ├── HARDWARE.md          ← Conexiones
│   ├── SOFTWARE.md          ← platformio.ini docs
│   ├── SKILL.md             ← Reglas para IA
│   ├── TASKS.md             ← TODOs
│   ├── CHANGELOG.md         ← Historial
│   ├── DECISIONS.md         ← ADRs
│   └── ROADMAP.md           ← Plan
├── src/
│   └── main.cpp
├── platformio.ini
└── README.md
```

## Siguiente Paso

→ Consulta `docs/workflow.md` para ver los 3 flujos de trabajo disponibles.

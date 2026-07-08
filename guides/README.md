# 📋 Guías de Generación

Instrucciones para que la IA genere cada archivo de documentación del proyecto.

---

## Índice de Guías

### Archivos .ai/

| Guía | Archivo de Salida | Cuándo Generar |
|------|------------------|----------------|
| [gen-project-context.md](gen-project-context.md) | `.ai/PROJECT_CONTEXT.md` | Siempre (obligatorio) |
| [gen-hardware.md](gen-hardware.md) | `.ai/HARDWARE.md` | Siempre que haya hardware físico |
| [gen-software.md](gen-software.md) | `.ai/SOFTWARE.md` | Siempre (obligatorio) |
| [gen-skill.md](gen-skill.md) | `.ai/SKILL.md` | Siempre (obligatorio, mín. 3 reglas NUNCA) |
| [gen-architecture.md](gen-architecture.md) | `.ai/ARCHITECTURE.md` | Solo si FSM o arquitectura compleja |
| [gen-protocol.md](gen-protocol.md) | `.ai/PROTOCOL.md` | Solo si BLE/MQTT/HTTP/RF |
| [gen-coding-style.md](gen-coding-style.md) | `.ai/CODING_STYLE.md` | Solo si difiere del estándar |
| [gen-tasks.md](gen-tasks.md) | `.ai/TASKS.md` | Siempre (extraer TODOs/FIXMEs) |
| [gen-changelog.md](gen-changelog.md) | `.ai/CHANGELOG.md` | Siempre (Keep a Changelog) |
| [gen-decisions.md](gen-decisions.md) | `.ai/DECISIONS.md` | Siempre (ADR format, mín. 2) |
| [gen-testing.md](gen-testing.md) | `.ai/TESTING.md` | Solo si existen tests |
| [gen-roadmap.md](gen-roadmap.md) | `.ai/ROADMAP.md` | Siempre (obligatorio) |

### Archivos docs/

| Guía | Archivo de Salida | Cuándo Generar |
|------|------------------|----------------|
| [gen-conexiones-svg.md](gen-conexiones-svg.md) | `docs/conexiones.drawio.svg` | Solo si hay hardware |
| [gen-notas-hw.md](gen-notas-hw.md) | `docs/notas.md` | Solo si hay hardware (máx. 40 líneas) |
| [gen-copilot-instructions.md](gen-copilot-instructions.md) | `docs/copilot-instructions.md` | Siempre (obligatorio) |

### Archivos Raíz

| Guía | Archivo de Salida | Cuándo Generar |
|------|------------------|----------------|
| [gen-readme.md](gen-readme.md) | `README.md` | Siempre (para humanos, mín. 3 troubleshooting) |
| [gen-archivo-mapa.md](gen-archivo-mapa.md) | `archivo-mapa.yml` | Siempre (YAML con metadata completa) |
| [gen-secrets-template.md](gen-secrets-template.md) | `secrets.h.template` | Solo si WiFi/credenciales |

---

## Cómo Usar las Guías

### Uso con IA (recomendado)

1. Copia el contenido de la guía relevante en tu prompt
2. Proporciona el código fuente del proyecto como contexto
3. La IA generará el archivo siguiendo las instrucciones exactas

### Uso con el generador automático

```bash
# El prompt generator-context.md ya incluye todas las guías
# Solo necesitas proveer el código fuente
```

### Uso manual

1. Abre la guía del archivo que necesitas
2. Sigue los pasos numerados en "Instrucciones para la IA"
3. Usa el bloque de código como referencia de estructura esperada
4. Verifica contra la sección "Reglas"

---

## Reglas Comunes

Estas reglas aplican a **todas** las guías:

1. **Idioma:** Toda la documentación se escribe en español, excepto código y nombres técnicos
2. **Formato:** Markdown estricto, compatible con GitHub y VS Code
3. **Placeholders:** Nunca dejar `{{PLACEHOLDER}}` en archivos generados — todo debe ser contenido real
4. **Catálogo:** Siempre usar IDs del catálogo para referenciar hardware
5. **Consistencia:** Los nombres de componentes deben coincidir en todos los archivos
6. **Completitud:** Cada archivo debe ser usable inmediatamente sin edición adicional
7. **Concisión:** Preferir tablas y listas sobre párrafos largos
8. **Frontmatter:** Los archivos basados en templates mantienen el YAML frontmatter
9. **Links:** Usar rutas relativas para enlaces internos
10. **Actualización:** Incluir fecha de última actualización donde aplique

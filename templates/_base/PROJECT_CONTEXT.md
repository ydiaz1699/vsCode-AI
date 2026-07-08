---
template: project-context
version: "1.0"
required: true
description: "Contexto general del proyecto para asistentes IA"
---

# {{PROJECT_NAME}} — Contexto del Proyecto

## Propósito

{{PROJECT_PURPOSE}}

**Objetivo principal:** {{MAIN_OBJECTIVE}}
**Tipo de proyecto:** {{PROJECT_TYPE}}
**Plataforma destino:** {{TARGET_PLATFORM}}

## Referencias al Catálogo

| Tipo | Referencia | Notas |
|------|-----------|-------|
| Placa | [{{BOARD_ID}}](../../catalog/boards/{{BOARD_FILE}}) | {{BOARD_NOTES}} |
| Periférico | [{{PERIPHERAL_1_ID}}](../../catalog/peripherals/{{PERIPHERAL_1_FILE}}) | {{PERIPHERAL_1_NOTES}} |
| Periférico | [{{PERIPHERAL_2_ID}}](../../catalog/peripherals/{{PERIPHERAL_2_FILE}}) | {{PERIPHERAL_2_NOTES}} |
| Entorno | [{{ENVIRONMENT}}](../../catalog/environments/{{ENVIRONMENT_DIR}}/) | {{ENVIRONMENT_NOTES}} |

## Archivos Clave

| Archivo | Propósito | Notas |
|---------|-----------|-------|
| `src/main.cpp` | {{MAIN_FILE_PURPOSE}} | Punto de entrada |
| `platformio.ini` | Configuración de compilación | {{INI_NOTES}} |
| `include/config.h` | Constantes y configuración | {{CONFIG_NOTES}} |
| `lib/` | Librerías locales | {{LIB_NOTES}} |
| `.ai/HARDWARE.md` | Documentación de hardware | Conexiones y consumo |
| `.ai/SOFTWARE.md` | Documentación de software | Librerías y flags |

## Convenciones

- **Idioma del código:** {{CODE_LANGUAGE}}
- **Idioma de comentarios:** {{COMMENT_LANGUAGE}}
- **Estándar de código:** {{CODE_STANDARD}}
- **Nomenclatura de variables:** {{NAMING_CONVENTION}}
- **Nomenclatura de constantes:** {{CONSTANT_NAMING}}
- **Nomenclatura de archivos:** {{FILE_NAMING}}
- **Indentación:** {{INDENTATION}}
- **Largo máximo de línea:** {{MAX_LINE_LENGTH}}

## Cómo Compilar

```bash
# Compilar
{{BUILD_COMMAND}}

# Subir al dispositivo
{{UPLOAD_COMMAND}}

# Monitor serial
{{MONITOR_COMMAND}}
```

**Puerto serial por defecto:** {{SERIAL_PORT}}
**Velocidad de monitor:** {{MONITOR_SPEED}} baudios

## Notas Adicionales

{{ADDITIONAL_NOTES}}

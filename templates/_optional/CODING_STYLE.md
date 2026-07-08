---
template: coding-style
version: "1.0"
required: false
condition: "Generar solo si el proyecto necesita reglas de estilo que difieren del estándar PlatformIO/Arduino, o si hay convenciones específicas del equipo."
description: "Guía de estilo de código específica del proyecto"
---

> ⚠️ **Generar solo si** el proyecto necesita reglas de estilo que difieren del estándar PlatformIO/Arduino, o si hay convenciones específicas del equipo.

# {{PROJECT_NAME}} — Estilo de Código

## Base

- **Estándar base:** {{BASE_STANDARD}}
- **Referencia:** {{STANDARD_REFERENCE}}
- **Formatter:** {{FORMATTER}}
- **Linter:** {{LINTER}}

## Overrides del Estándar

Este proyecto modifica las siguientes reglas del estándar base:

| Regla del Estándar | Override del Proyecto | Razón |
|-------------------|---------------------|-------|
| {{OVERRIDE_1_RULE}} | {{OVERRIDE_1_VALUE}} | {{OVERRIDE_1_REASON}} |
| {{OVERRIDE_2_RULE}} | {{OVERRIDE_2_VALUE}} | {{OVERRIDE_2_REASON}} |
| {{OVERRIDE_3_RULE}} | {{OVERRIDE_3_VALUE}} | {{OVERRIDE_3_REASON}} |

## Nomenclatura

| Elemento | Convención | Ejemplo |
|----------|-----------|---------|
| Variables locales | {{LOCAL_VAR_CONVENTION}} | `{{LOCAL_VAR_EXAMPLE}}` |
| Variables globales | {{GLOBAL_VAR_CONVENTION}} | `{{GLOBAL_VAR_EXAMPLE}}` |
| Constantes | {{CONSTANT_CONVENTION}} | `{{CONSTANT_EXAMPLE}}` |
| Funciones | {{FUNCTION_CONVENTION}} | `{{FUNCTION_EXAMPLE}}` |
| Clases | {{CLASS_CONVENTION}} | `{{CLASS_EXAMPLE}}` |
| Pines GPIO | {{PIN_CONVENTION}} | `{{PIN_EXAMPLE}}` |
| Archivos .h | {{HEADER_CONVENTION}} | `{{HEADER_EXAMPLE}}` |
| Archivos .cpp | {{CPP_CONVENTION}} | `{{CPP_EXAMPLE}}` |
| Macros | {{MACRO_CONVENTION}} | `{{MACRO_EXAMPLE}}` |

## Idioma

| Elemento | Idioma | Ejemplo |
|----------|--------|---------|
| Nombres de variables | {{VAR_LANG}} | `{{VAR_LANG_EXAMPLE}}` |
| Nombres de funciones | {{FUNC_LANG}} | `{{FUNC_LANG_EXAMPLE}}` |
| Comentarios | {{COMMENT_LANG}} | `{{COMMENT_LANG_EXAMPLE}}` |
| Commits | {{COMMIT_LANG}} | `{{COMMIT_LANG_EXAMPLE}}` |
| Documentación .ai/ | {{DOC_LANG}} | `{{DOC_LANG_EXAMPLE}}` |
| Mensajes Serial | {{SERIAL_LANG}} | `{{SERIAL_LANG_EXAMPLE}}` |

## Reglas Específicas

### Estructura de archivos

```cpp
// {{FILE_STRUCTURE_COMMENT}}
// 1. Includes del sistema
#include <Arduino.h>
#include <{{SYSTEM_INCLUDE}}>

// 2. Includes de librerías externas
#include <{{LIB_INCLUDE}}>

// 3. Includes locales
#include "{{LOCAL_INCLUDE}}"

// 4. Definiciones y constantes
{{CONSTANTS_SECTION}}

// 5. Variables globales
{{GLOBALS_SECTION}}

// 6. Prototipos
{{PROTOTYPES_SECTION}}

// 7. Setup
void setup() { ... }

// 8. Loop
void loop() { ... }

// 9. Implementación de funciones
{{FUNCTIONS_SECTION}}
```

### Comentarios

```cpp
// Comentario de una línea — para explicaciones breves

/*
 * Bloque de comentarios — para explicar lógica compleja
 * que requiere más de una línea.
 */

/// @brief {{BRIEF_DESC}}
/// @param {{PARAM_NAME}} {{PARAM_DESC}}
/// @return {{RETURN_DESC}}
```

### Formato de constantes de pines

```cpp
// Formato: PIN_[PERIFÉRICO]_[FUNCIÓN]
constexpr uint8_t {{PIN_FORMAT_EXAMPLE}};
```

# 🏗️ Arquitectura del Framework

## Diseño de 3 Capas

El framework se organiza en 3 capas independientes que se conectan en el momento de la generación:

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA 3: PROYECTO                          │
│                                                             │
│  Tu proyecto PlatformIO con archivos .ai/ generados         │
│  Resultado final, listo para usar con IA                    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                    CAPA 2: GENERACIÓN                        │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐     │
│  │ Guides   │  │ Prompts  │  │ Templates            │     │
│  │ (18)     │  │ (2+1)    │  │ (_base + _optional)  │     │
│  └────┬─────┘  └────┬─────┘  └──────────┬───────────┘     │
│       │              │                    │                  │
│       └──────────────┼────────────────────┘                  │
│                      │                                       │
├──────────────────────┼───────────────────────────────────────┤
│                      │                                       │
│                    CAPA 1: CATÁLOGO                          │
│                                                             │
│  ┌──────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Boards   │  │ Peripherals  │  │ Environments │         │
│  │ (12)     │  │ (8)          │  │ (3)          │         │
│  └──────────┘  └──────────────┘  └──────────────┘         │
│                                                             │
│  Datos verificados, inmutables, referenciables              │
└─────────────────────────────────────────────────────────────┘
```

### Capa 1: Catálogo (Datos)

**Propósito:** Fuente única de verdad para hardware soportado.

- Cada placa y periférico tiene un ID único (`board-xxx`, `periph-xxx`)
- Los datos incluyen: voltaje, protocolos, pines, precio, specs
- Se referencia desde los proyectos con links relativos
- Es inmutable una vez publicado (versionado por ID)

**Directorio:** `catalog/`

### Capa 2: Generación (Lógica)

**Propósito:** Instrucciones para crear documentación correcta.

Tres componentes:

| Componente | Función | Cantidad |
|-----------|---------|----------|
| **Templates** | Plantillas con `{{PLACEHOLDERS}}` para copiar | 12 archivos |
| **Guides** | Instrucciones paso a paso para la IA | 18 archivos |
| **Prompts** | System prompts completos para sesiones IA | 3 archivos |

**Directorios:** `templates/`, `guides/`, `prompts/`

### Capa 3: Proyecto (Resultado)

**Propósito:** Tu proyecto final con documentación completa.

- Código fuente PlatformIO funcional
- Carpeta `.ai/` con contexto para asistentes IA
- README para humanos
- Configuración de Copilot

---

## Concepto: Frontmatter YAML

Cada template incluye un bloque YAML al inicio (frontmatter) con metadata:

```yaml
---
template: project-context      # Identificador del template
version: "1.0"                 # Versión del formato
required: true                 # ¿Es obligatorio?
condition: "Siempre"           # Cuándo generarlo
description: "..."             # Descripción breve
---
```

**Propósito del frontmatter:**
- Permite a herramientas automatizadas procesar templates
- Documenta condiciones de generación para la IA
- Facilita versionado de formatos de documentación
- Es removido del archivo final generado (solo vive en templates)

---

## Concepto: Guías de Generación

Las guías (`guides/gen-*.md`) son instrucciones estructuradas para que la IA genere archivos correctos:

```
┌─────────────────────────────────────────┐
│  Guía (guides/gen-hardware.md)          │
│                                         │
│  1. Archivo de salida: dónde va         │
│  2. Cuándo generarlo: condición         │
│  3. Instrucciones: 10 pasos exactos     │
│  4. Estructura esperada: ejemplo        │
│  5. Reglas: restricciones a cumplir     │
└────────────────────┬────────────────────┘
                     │
                     ▼ La IA sigue estas instrucciones
                     │
┌────────────────────┴────────────────────┐
│  Archivo generado (.ai/HARDWARE.md)     │
│                                         │
│  Contenido real, sin placeholders,      │
│  específico al proyecto del usuario     │
└─────────────────────────────────────────┘
```

**Diferencia entre Template y Guía:**
- **Template** = estructura con `{{PLACEHOLDERS}}` para copiar y llenar
- **Guía** = instrucciones para que la IA genere el contenido correcto automáticamente

---

## Flujo de Datos

```
                    ┌─────────┐
                    │ Usuario │
                    └────┬────┘
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      [Proyecto Nuevo]      [Proyecto Existente]
              │                     │
              ▼                     ▼
     synapse-v3.md          generator-context.md
              │                     │
              ▼                     ▼
     ┌────────────────┐    ┌────────────────┐
     │ Consulta       │    │ Analiza código │
     │ Catálogo       │    │ existente      │
     └───────┬────────┘    └───────┬────────┘
             │                     │
             ▼                     ▼
     ┌────────────────┐    ┌────────────────┐
     │ Aplica Guías   │    │ Aplica Guías   │
     │ + Templates    │    │ sin templates  │
     └───────┬────────┘    └───────┬────────┘
             │                     │
             └──────────┬──────────┘
                        │
                        ▼
               ┌────────────────┐
               │ Proyecto con   │
               │ .ai/ completa  │
               └────────────────┘
```

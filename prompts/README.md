# 🧠 Prompts del Sistema

Este directorio contiene los mega-prompts principales para trabajar con IA en proyectos de firmware embebido.

## Cuándo Usar Cada Uno

| Prompt | Caso de Uso | Resultado |
|--------|------------|-----------|
| [synapse-v3.md](synapse-v3.md) | **Crear proyecto nuevo** o **trabajar con código existente** en tiempo real | Código + documentación generados interactivamente |
| [generator-context.md](generator-context.md) | **Documentar proyecto existente** que ya tiene código pero le falta documentación .ai/ | 18 archivos de documentación generados |

## Diferencias Clave

### synapse-v3.md (Asistente Interactivo)
- Diseñado para **sesiones de trabajo continuas**
- Tiene comandos interactivos (`/new`, `/docs`, `/add-peripheral`, etc.)
- Genera código Y documentación juntos
- Conoce el catálogo completo de hardware
- Ideal para: comenzar proyectos, agregar features, debugging

### generator-context.md (Generador Batch)
- Diseñado para **una sola ejecución**
- Analiza código existente y genera toda la documentación
- No genera código nuevo, solo documentación
- Trabaja en 2 fases: análisis → generación
- Ideal para: proyectos legacy, organizar proyectos existentes, onboarding

## Uso Típico

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ¿Proyecto nuevo?  ──YES──▶  Usar synapse-v3.md               │
│       │                                                         │
│       NO                                                        │
│       │                                                         │
│       ▼                                                         │
│  ¿Tiene código pero no docs?  ──YES──▶  Usar generator-context │
│       │                                                         │
│       NO                                                        │
│       │                                                         │
│       ▼                                                         │
│  ¿Trabajar con IA interactivamente?  ──YES──▶  synapse-v3.md  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

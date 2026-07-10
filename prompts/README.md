# 🧠 Prompts del Sistema

Este directorio contiene los mega-prompts principales para trabajar con IA en proyectos de firmware embebido.

## Cuándo Usar Cada Uno

| Prompt | Caso de Uso | Resultado |
|--------|------------|-----------|
| [synapse-v3.md](synapse-v3.md) | **Crear proyecto nuevo** o **trabajar con código existente** en tiempo real | Código + documentación generados interactivamente |
| [generator-context.md](generator-context.md) | **Documentar proyecto existente** (versión simple, todo de golpe) | 18 archivos de documentación generados |
| [generator-context-v4.md](generator-context-v4.md) | **Documentar proyecto existente** (versión robusta, secuencial con checklist) | Análisis profundo + archivos uno a uno con verificación |
| [deep-analysis.md](deep-analysis.md) | **Debugging profundo** — encontrar causa raíz de bugs complejos | Diagnóstico con cadena causal, tests incrementales, fix verificado |

## Diferencias Clave

### synapse-v3.md (Asistente Interactivo)
- Diseñado para **sesiones de trabajo continuas**
- Tiene comandos interactivos (`/new`, `/docs`, `/add-peripheral`, etc.)
- Genera código Y documentación juntos
- Conoce el catálogo completo de hardware
- Ideal para: comenzar proyectos, agregar features, debugging

### generator-context.md (Generador Batch — v3 legacy)
- Diseñado para **una sola ejecución**
- Analiza código existente y genera toda la documentación
- No genera código nuevo, solo documentación
- Trabaja en 2 fases: análisis → generación
- ⚠️ Riesgo: puede olvidar archivos, alucinar datos, o truncarse por tokens
- Ideal para: proyectos SIMPLES (<5 archivos de código)

### generator-context-v4.md (Generador Secuencial — RECOMENDADO)
- Diseñado para **ejecución secuencial con checkpoints**
- 4 fases: análisis profundo → determinar archivos → generar 3/turno → verificar
- **Anti-alucinación:** marca `[VERIFICAR]` si no puede determinar un dato del código
- **Anti-olvido:** checklist obligatoria, CHECKPOINT entre fases, verificación final
- **Anti-token:** máximo 3 archivos por turno, pausa entre turnos para feedback
- Incluye análisis de SOURCE de librerías externas (timing, bloqueante, estado interno)
- Ideal para: TODO tipo de proyecto (simple o complejo)

### deep-analysis.md (Análisis Forense de Bugs)
- Diseñado para **debugging exhaustivo** de problemas complejos
- Metodología de 6 fases: mapeo → source → simulación → diferencial → tests → diagnóstico
- Lee el source code de librerías externas para entender comportamiento real
- Calcula tiempos exactos del sistema con las constantes reales
- Diseña tests incrementales que aíslan una variable a la vez
- Reconoce cuándo parar (problema de hardware vs software)
- Ideal para: bugs de timing, protocolos que no funcionan, interacción HW/SW, librerías con comportamiento inesperado

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
│  ¿Bug complejo / no funciona?  ──YES──▶  Usar deep-analysis   │
│       │                                                         │
│       NO                                                        │
│       │                                                         │
│       ▼                                                         │
│  ¿Trabajar con IA interactivamente?  ──YES──▶  synapse-v3.md  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---
template: decisions
version: "1.0"
required: true
description: "Registro de decisiones arquitectónicas (ADR)"
---

# {{PROJECT_NAME}} — Decisiones Arquitectónicas

Registro de decisiones importantes tomadas durante el desarrollo del proyecto.
Formato basado en [Architecture Decision Records (ADR)](https://adr.github.io/).

---

## ADR-001: {{ADR_1_TITLE}}

**Estado:** {{ADR_1_STATUS}}
**Fecha:** {{ADR_1_DATE}}
**Contexto:** {{ADR_1_CONTEXT}}

### Decisión

{{ADR_1_DECISION}}

### Alternativas Consideradas

| Opción | Pros | Contras |
|--------|------|---------|
| {{ADR_1_OPT_A}} | {{ADR_1_OPT_A_PROS}} | {{ADR_1_OPT_A_CONS}} |
| {{ADR_1_OPT_B}} | {{ADR_1_OPT_B_PROS}} | {{ADR_1_OPT_B_CONS}} |
| {{ADR_1_OPT_C}} | {{ADR_1_OPT_C_PROS}} | {{ADR_1_OPT_C_CONS}} |

### Consecuencias

- {{ADR_1_CONSEQUENCE_1}}
- {{ADR_1_CONSEQUENCE_2}}
- {{ADR_1_CONSEQUENCE_3}}

---

## ADR-002: {{ADR_2_TITLE}}

**Estado:** {{ADR_2_STATUS}}
**Fecha:** {{ADR_2_DATE}}
**Contexto:** {{ADR_2_CONTEXT}}

### Decisión

{{ADR_2_DECISION}}

### Alternativas Consideradas

| Opción | Pros | Contras |
|--------|------|---------|
| {{ADR_2_OPT_A}} | {{ADR_2_OPT_A_PROS}} | {{ADR_2_OPT_A_CONS}} |
| {{ADR_2_OPT_B}} | {{ADR_2_OPT_B_PROS}} | {{ADR_2_OPT_B_CONS}} |

### Consecuencias

- {{ADR_2_CONSEQUENCE_1}}
- {{ADR_2_CONSEQUENCE_2}}

---

## Plantilla para Nuevas Decisiones

```markdown
## ADR-XXX: [Título de la Decisión]

**Estado:** Propuesto | Aceptado | Deprecado | Sustituido por ADR-YYY
**Fecha:** YYYY-MM-DD
**Contexto:** [Descripción del problema o necesidad que motiva la decisión]

### Decisión

[Descripción clara de la decisión tomada]

### Alternativas Consideradas

| Opción | Pros | Contras |
|--------|------|---------|
| [Opción A] | [ventajas] | [desventajas] |
| [Opción B] | [ventajas] | [desventajas] |

### Consecuencias

- [Impacto positivo o negativo de la decisión]
- [Cambios requeridos en el código o arquitectura]
- [Deuda técnica introducida, si aplica]
```

---

## Índice de Decisiones

| ADR | Título | Estado | Fecha |
|-----|--------|--------|-------|
| 001 | {{ADR_1_TITLE}} | {{ADR_1_STATUS}} | {{ADR_1_DATE}} |
| 002 | {{ADR_2_TITLE}} | {{ADR_2_STATUS}} | {{ADR_2_DATE}} |

# Guía: Generar DECISIONS.md

## Archivo de Salida

`.ai/DECISIONS.md`

## Cuándo Generarlo

**Siempre.** Formato ADR obligatorio, mínimo 2 decisiones documentadas.

## Instrucciones para la IA

1. Identificar la primera decisión: elección de placa/MCU (¿por qué esta y no otra?)
2. Identificar la segunda decisión: elección de framework/protocolo de comunicación
3. Buscar en el código decisiones implícitas (¿por qué FreeRTOS? ¿por qué esta librería?)
4. Para cada decisión, documentar mínimo 2 alternativas que fueron consideradas
5. Listar pros y contras reales de cada alternativa (no genéricos)
6. Documentar las consecuencias de la decisión tomada
7. Asignar estado: Aceptado para decisiones finales, Propuesto para las en evaluación
8. Incluir la plantilla vacía al final para futuras decisiones
9. Crear índice de decisiones al final del archivo
10. Si hay código legacy o deuda técnica, documentar como decisión con contexto

## Estructura Esperada

```markdown
# [Nombre] — Decisiones Arquitectónicas

## ADR-001: [Título]
**Estado:** Aceptado
**Fecha:** YYYY-MM-DD
**Contexto:** [situación]

### Decisión
[qué se decidió]

### Alternativas Consideradas
| Opción | Pros | Contras |
|...|...|...|

### Consecuencias
- ...

## ADR-002: [Título]
...

## Plantilla para Nuevas Decisiones
\```markdown
## ADR-XXX: [Título]
...
\```
```

## Reglas

- Mínimo 2 ADRs por proyecto (placa + framework/protocolo)
- Cada ADR tiene mínimo 2 alternativas consideradas
- Los pros/contras son específicos y medibles cuando sea posible
- Estados válidos: Propuesto, Aceptado, Deprecado, Sustituido por ADR-XXX
- Las consecuencias incluyen tanto positivas como negativas
- No documentar decisiones triviales (indentación, formato de log)
- El contexto explica el PROBLEMA, no la solución
- La decisión es el QUÉ, no el CÓMO (eso va en ARCHITECTURE.md)

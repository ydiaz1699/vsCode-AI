# Guía: Generar TASKS.md

## Archivo de Salida

`.ai/TASKS.md`

## Cuándo Generarlo

**Siempre.** Extraer TODOs y FIXMEs del código fuente y organizarlos.

## Instrucciones para la IA

1. Buscar todos los comentarios `// TODO:` en el código fuente
2. Buscar todos los comentarios `// FIXME:` en el código fuente
3. Buscar comentarios `// HACK:`, `// XXX:`, `// BUG:` como FIXMEs adicionales
4. Para cada TODO/FIXME, extraer: archivo, línea, y descripción
5. Clasificar en las 4 secciones: TODO, FIXME, IN PROGRESS, DONE
6. Si no hay TODOs explícitos, crear tareas basadas en el estado del proyecto
7. Evaluar si hay funcionalidad incompleta o parcialmente implementada
8. Priorizar: seguridad > funcionalidad core > optimización > nice-to-have
9. Asignar nivel de prioridad visual (🔴 🟡 🟢) a cada tarea
10. Incluir la sección DONE con las tareas ya completadas (basado en git log si disponible)

## Estructura Esperada

```markdown
# [Nombre] — Tareas

## TODO
- [ ] [Descripción de la tarea]
- [ ] [Descripción de la tarea]

## FIXME
- [ ] 🐛 [Descripción del bug/problema]

## IN PROGRESS
- [ ] 🔄 [Tarea en desarrollo] — Asignado: [quien]

## DONE
- [x] ✅ [Tarea completada] — Completado: [fecha]
```

## Reglas

- Cada tarea es una acción concreta y verificable, no vaga
- Los FIXMEs incluyen el impacto del bug (qué falla, cuándo)
- No inventar tareas que no se derivan del código o del estado del proyecto
- Si una función tiene `// TODO:` sin contexto, expandir la descripción basándose en el código circundante
- Mantener el formato checkbox para poder marcar progreso
- Máximo 15 items en TODO (si hay más, priorizar los top 15)
- IN PROGRESS solo si hay evidencia de trabajo parcial (branches, código a medias)
- DONE se llena con commits recientes significativos

# Guía: Generar ROADMAP.md

## Archivo de Salida

`.ai/ROADMAP.md`

## Cuándo Generarlo

**Siempre.** La hoja de ruta es obligatoria para planificar el desarrollo.

## Instrucciones para la IA

1. Analizar el estado actual del proyecto (¿MVP? ¿prototipo? ¿producción?)
2. Identificar tareas inmediatas para completar la funcionalidad mínima (corto plazo)
3. Identificar mejoras y features adicionales para medio plazo
4. Proyectar visión futura: escalabilidad, nuevos features, optimizaciones (largo plazo)
5. Detectar bloqueantes actuales (hardware faltante, dependencias, decisiones pendientes)
6. Asignar prioridades basadas en dependencias (si B depende de A, A va primero)
7. Para corto plazo: ser específico y accionable (1-2 semanas)
8. Para largo plazo: ser más visionario pero realista
9. Los bloqueantes deben tener acción requerida concreta
10. Verificar que no haya contradicciones con TASKS.md (deben ser complementarios)

## Estructura Esperada

```markdown
# [Nombre] — Roadmap

## 🟢 Corto Plazo (1–2 semanas)
| # | Tarea | Prioridad | Dependencia | Estado |
|...|...|...|...|...|

## 🟡 Medio Plazo (1–2 meses)
| # | Tarea | Prioridad | Dependencia | Notas |
|...|...|...|...|...|

## 🔴 Largo Plazo (3+ meses)
| # | Tarea | Categoría | Notas |
|...|...|...|...|

## 🚧 Bloqueantes
| # | Bloqueante | Impacto | Acción | Responsable |
|...|...|...|...|...|
```

## Reglas

- Corto plazo: máximo 5-7 tareas, todas accionables en 1-2 semanas
- Medio plazo: máximo 4-5 tareas, con dependencias claras
- Largo plazo: máximo 3-4 items, más conceptuales
- Bloqueantes: solo incluir si hay impedimentos reales (no tareas pendientes)
- Las prioridades usan emoji: 🔴 Alta, 🟡 Media, 🟢 Baja
- Las dependencias referencian otras tareas del mismo roadmap
- No duplicar tareas entre TASKS.md y ROADMAP.md — TASKS es operativo, ROADMAP es estratégico
- Incluir fecha de última actualización al inicio

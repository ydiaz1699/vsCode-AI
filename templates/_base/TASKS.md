---
template: tasks
version: "1.0"
required: true
description: "Seguimiento de tareas del proyecto"
---

# {{PROJECT_NAME}} — Tareas

> Última actualización: {{LAST_UPDATE}}

## TODO

Tareas pendientes por implementar:

- [ ] {{TODO_1}}
- [ ] {{TODO_2}}
- [ ] {{TODO_3}}
- [ ] {{TODO_4}}
- [ ] {{TODO_5}}

## FIXME

Problemas conocidos que requieren corrección:

- [ ] 🐛 {{FIXME_1}}
- [ ] 🐛 {{FIXME_2}}

## IN PROGRESS

Tareas actualmente en desarrollo:

- [ ] 🔄 {{IN_PROGRESS_1}} — Asignado: {{ASSIGNEE_1}}
- [ ] 🔄 {{IN_PROGRESS_2}} — Asignado: {{ASSIGNEE_2}}

## DONE

Tareas completadas:

- [x] ✅ {{DONE_1}} — Completado: {{DONE_1_DATE}}
- [x] ✅ {{DONE_2}} — Completado: {{DONE_2_DATE}}
- [x] ✅ {{DONE_3}} — Completado: {{DONE_3_DATE}}

---

## Notas

- Las tareas se extraen automáticamente de comentarios `// TODO:` y `// FIXME:` en el código.
- Mover tareas entre secciones al cambiar su estado.
- Formato de prioridad: 🔴 Alta | 🟡 Media | 🟢 Baja

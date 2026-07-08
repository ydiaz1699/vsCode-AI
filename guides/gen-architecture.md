# Guía: Generar ARCHITECTURE.md

## Archivo de Salida

`.ai/ARCHITECTURE.md`

## Cuándo Generarlo

**Solo si** el proyecto tiene:
- Máquinas de estado (FSM) con 3+ estados
- Múltiples tareas concurrentes (FreeRTOS, tareas cooperativas)
- Arquitectura compleja con más de 3 módulos independientes
- Patrones como pub/sub, command, observer

## Instrucciones para la IA

1. Identificar los módulos principales del sistema (agrupaciones lógicas de funcionalidad)
2. Determinar las dependencias entre módulos (quién llama a quién)
3. Crear un diagrama ASCII que muestre la arquitectura en capas
4. Si hay FSM, extraer todos los estados del código (enums, switch/case)
5. Documentar cada transición de estado: condición y acción
6. Si hay FreeRTOS, listar cada tarea con prioridad, stack y core asignado
7. Documentar el flujo de datos desde la entrada (sensores) hasta la salida (actuadores/red)
8. Identificar recursos compartidos y mecanismos de sincronización (mutex, semáforos, queues)
9. Crear diagrama ASCII de la FSM con transiciones
10. Verificar que no haya deadlocks potenciales en tareas concurrentes

## Estructura Esperada

```markdown
# [Nombre] — Arquitectura

## Diagrama General
\```
┌────────────┐
│  Módulo A  │
└─────┬──────┘
      │
\```

## Componentes
| Componente | Tipo | Responsabilidad | Archivos | Dependencias |
|...|...|...|...|...|

## Máquina de Estados (FSM)
| Estado | Descripción | Transición a | Condición | Acción |
|...|...|...|...|...|

## Distribución de Tareas
| Tarea | Prioridad | Stack | Core | Período | Descripción |
|...|...|...|...|...|...|

## Flujo de Datos
\```
[Sensor] → [Proceso] → [Salida]
\```
```

## Reglas

- El diagrama ASCII debe usar caracteres box-drawing (┌ ─ ┐ │ └ ┘ ├ ┤ ┬ ┴ ┼ ▶ ▼)
- Cada módulo tiene un solo responsable (Single Responsibility)
- La FSM debe ser completa: todo estado tiene al menos una salida
- Las prioridades de FreeRTOS siguen la convención: mayor número = mayor prioridad
- El stack de tareas se documenta en bytes, no en words
- Indicar core pinning si es ESP32 dual-core (Core 0 = WiFi, Core 1 = aplicación por defecto)
- No generar este archivo para proyectos simples (1 archivo, sin FSM, sin RTOS)
- El flujo de datos muestra el camino feliz primero, luego los errores

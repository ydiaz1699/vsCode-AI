---
template: architecture
version: "1.0"
required: false
condition: "Generar solo si el proyecto tiene máquinas de estado (FSM), múltiples tareas concurrentes, o arquitectura compleja con más de 3 módulos."
description: "Arquitectura del sistema, componentes y flujos de datos"
---

> ⚠️ **Generar solo si** el proyecto tiene FSM, múltiples tareas concurrentes (FreeRTOS), o arquitectura compleja con más de 3 módulos independientes.

# {{PROJECT_NAME}} — Arquitectura

## Diagrama General

```
┌─────────────────────────────────────────────────────────────┐
│                        {{PROJECT_NAME}}                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  {{MODULE_1}} │  │  {{MODULE_2}} │  │  {{MODULE_3}} │     │
│  │              │  │              │  │              │     │
│  │ {{M1_DESC}}  │  │ {{M2_DESC}}  │  │ {{M3_DESC}}  │     │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘     │
│         │                  │                  │             │
│         └──────────────────┼──────────────────┘             │
│                            │                                │
│                   ┌────────▼────────┐                       │
│                   │   {{CORE_NAME}}  │                       │
│                   │  {{CORE_DESC}}   │                       │
│                   └────────┬────────┘                       │
│                            │                                │
│  ┌─────────────────────────▼─────────────────────────────┐ │
│  │                    HAL / Drivers                        │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐          │
│  │{{HW_1}}│  │{{HW_2}}│  │{{HW_3}}│  │{{HW_4}}│          │
│  └────────┘  └────────┘  └────────┘  └────────┘          │
└─────────────────────────────────────────────────────────────┘
```

## Componentes

| Componente | Tipo | Responsabilidad | Archivo(s) | Dependencias |
|-----------|------|-----------------|------------|--------------|
| {{MODULE_1}} | {{M1_TYPE}} | {{M1_RESPONSIBILITY}} | {{M1_FILES}} | {{M1_DEPS}} |
| {{MODULE_2}} | {{M2_TYPE}} | {{M2_RESPONSIBILITY}} | {{M2_FILES}} | {{M2_DEPS}} |
| {{MODULE_3}} | {{M3_TYPE}} | {{M3_RESPONSIBILITY}} | {{M3_FILES}} | {{M3_DEPS}} |
| {{CORE_NAME}} | Coordinador | {{CORE_RESPONSIBILITY}} | {{CORE_FILES}} | {{CORE_DEPS}} |
| HAL | Abstracción | Interfaz con hardware | {{HAL_FILES}} | — |

## Máquina de Estados (FSM)

| Estado | Descripción | Transición a | Condición | Acción |
|--------|-------------|-------------|-----------|--------|
| {{STATE_1}} | {{STATE_1_DESC}} | {{STATE_1_NEXT}} | {{STATE_1_COND}} | {{STATE_1_ACTION}} |
| {{STATE_2}} | {{STATE_2_DESC}} | {{STATE_2_NEXT}} | {{STATE_2_COND}} | {{STATE_2_ACTION}} |
| {{STATE_3}} | {{STATE_3_DESC}} | {{STATE_3_NEXT}} | {{STATE_3_COND}} | {{STATE_3_ACTION}} |
| {{STATE_4}} | {{STATE_4_DESC}} | {{STATE_4_NEXT}} | {{STATE_4_COND}} | {{STATE_4_ACTION}} |
| {{STATE_5}} | {{STATE_5_DESC}} | {{STATE_5_NEXT}} | {{STATE_5_COND}} | {{STATE_5_ACTION}} |

```
{{STATE_1}} ──[{{STATE_1_COND}}]──▶ {{STATE_2}}
     ▲                                    │
     │                        [{{STATE_2_COND}}]
     │                                    ▼
{{STATE_5}} ◀──[{{STATE_4_COND}}]── {{STATE_3}}
     ▲                                    │
     │                        [{{STATE_3_COND}}]
     └────────────────────────────────────┘
```

## Distribución de Tareas (FreeRTOS)

| Tarea | Prioridad | Stack | Core | Período | Descripción |
|-------|-----------|-------|------|---------|-------------|
| {{TASK_1}} | {{TASK_1_PRIO}} | {{TASK_1_STACK}} | {{TASK_1_CORE}} | {{TASK_1_PERIOD}} | {{TASK_1_DESC}} |
| {{TASK_2}} | {{TASK_2_PRIO}} | {{TASK_2_STACK}} | {{TASK_2_CORE}} | {{TASK_2_PERIOD}} | {{TASK_2_DESC}} |
| {{TASK_3}} | {{TASK_3_PRIO}} | {{TASK_3_STACK}} | {{TASK_3_CORE}} | {{TASK_3_PERIOD}} | {{TASK_3_DESC}} |

## Flujo de Datos

```
[Sensor] ──read──▶ [Buffer] ──process──▶ [Filter] ──publish──▶ [MQTT/BLE]
                                              │
                                              ▼
                                         [Display]
```

### Descripción del Flujo

1. **Adquisición:** {{FLOW_ACQUISITION}}
2. **Procesamiento:** {{FLOW_PROCESSING}}
3. **Salida:** {{FLOW_OUTPUT}}
4. **Feedback:** {{FLOW_FEEDBACK}}

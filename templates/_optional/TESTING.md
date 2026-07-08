---
template: testing
version: "1.0"
required: false
condition: "Generar solo si el proyecto tiene tests implementados o si se planea agregar testing."
description: "Plan y documentación de testing del proyecto"
---

> ⚠️ **Generar solo si** el proyecto tiene tests implementados o si se planea agregar testing.

# {{PROJECT_NAME}} — Testing

## Framework

| Campo | Valor |
|-------|-------|
| **Framework** | {{TEST_FRAMEWORK}} |
| **Runner** | {{TEST_RUNNER}} |
| **Entorno de test** | {{TEST_ENVIRONMENT}} |
| **Cobertura mínima** | {{MIN_COVERAGE}} |

## Cómo Ejecutar

### Tests unitarios

```bash
# Ejecutar todos los tests
{{RUN_ALL_TESTS}}

# Ejecutar test específico
{{RUN_SPECIFIC_TEST}}

# Ejecutar con output detallado
{{RUN_VERBOSE}}
```

### Tests en hardware real

```bash
# Subir tests al dispositivo
{{UPLOAD_TESTS}}

# Monitorear resultado
{{MONITOR_TESTS}}
```

## Casos de Prueba

| ID | Categoría | Descripción | Input | Expected Output | Estado |
|----|-----------|-------------|-------|----------------|--------|
| T-001 | {{T1_CATEGORY}} | {{T1_DESC}} | {{T1_INPUT}} | {{T1_EXPECTED}} | {{T1_STATUS}} |
| T-002 | {{T2_CATEGORY}} | {{T2_DESC}} | {{T2_INPUT}} | {{T2_EXPECTED}} | {{T2_STATUS}} |
| T-003 | {{T3_CATEGORY}} | {{T3_DESC}} | {{T3_INPUT}} | {{T3_EXPECTED}} | {{T3_STATUS}} |
| T-004 | {{T4_CATEGORY}} | {{T4_DESC}} | {{T4_INPUT}} | {{T4_EXPECTED}} | {{T4_STATUS}} |
| T-005 | {{T5_CATEGORY}} | {{T5_DESC}} | {{T5_INPUT}} | {{T5_EXPECTED}} | {{T5_STATUS}} |
| T-006 | {{T6_CATEGORY}} | {{T6_DESC}} | {{T6_INPUT}} | {{T6_EXPECTED}} | {{T6_STATUS}} |

## Tests de Integración

### Escenario 1: {{INTEGRATION_1_NAME}}

**Precondiciones:** {{INTEGRATION_1_PRE}}

**Pasos:**
1. {{INTEGRATION_1_STEP_1}}
2. {{INTEGRATION_1_STEP_2}}
3. {{INTEGRATION_1_STEP_3}}

**Resultado esperado:** {{INTEGRATION_1_EXPECTED}}

### Escenario 2: {{INTEGRATION_2_NAME}}

**Precondiciones:** {{INTEGRATION_2_PRE}}

**Pasos:**
1. {{INTEGRATION_2_STEP_1}}
2. {{INTEGRATION_2_STEP_2}}
3. {{INTEGRATION_2_STEP_3}}

**Resultado esperado:** {{INTEGRATION_2_EXPECTED}}

## Criterios de Aceptación

| Criterio | Umbral | Método de Verificación |
|----------|--------|----------------------|
| Compilación limpia | 0 warnings | `pio run` sin errores |
| Uso de RAM | < {{MAX_RAM}}% | Verificar con `pio run --target size` |
| Uso de Flash | < {{MAX_FLASH}}% | Verificar con `pio run --target size` |
| Estabilidad | {{STABILITY_HOURS}}h sin reboot | Monitor serial continuo |
| Tiempo de respuesta | < {{RESPONSE_TIME}}ms | Medición con osciloscopio/lógica |
| {{EXTRA_CRITERIA}} | {{EXTRA_THRESHOLD}} | {{EXTRA_METHOD}} |

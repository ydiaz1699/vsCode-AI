# Guía: Generar TESTING.md

## Archivo de Salida

`.ai/TESTING.md`

## Cuándo Generarlo

**Solo si** el proyecto tiene tests implementados (directorio `test/` con archivos), o si se planea agregar testing como parte del desarrollo.

## Instrucciones para la IA

1. Buscar directorio `test/` en el proyecto y listar los archivos de test existentes
2. Identificar el framework de testing utilizado (Unity, AUnit, GoogleTest, PlatformIO Test)
3. Extraer cada caso de test con su nombre, input esperado y output esperado
4. Documentar cómo ejecutar los tests (comandos exactos)
5. Si hay tests en hardware real vs nativo, documentar ambos
6. Identificar áreas sin cobertura de tests que deberían tenerla
7. Documentar tests de integración (flujos completos end-to-end)
8. Definir criterios de aceptación cuantificables
9. Si no hay tests pero debería haberlos, crear plan de testing mínimo
10. Documentar setup necesario para correr tests (hardware, mocks, configuración)

## Estructura Esperada

```markdown
# [Nombre] — Testing

## Framework
| Campo | Valor |
|-------|-------|
| Framework | Unity/AUnit/... |

## Cómo Ejecutar
\```bash
pio test ...
\```

## Casos de Prueba
| ID | Categoría | Descripción | Input | Expected | Estado |
|...|...|...|...|...|...|

## Tests de Integración
### Escenario 1: ...
...

## Criterios de Aceptación
| Criterio | Umbral | Verificación |
|...|...|...|
```

## Reglas

- Solo generar si hay evidencia de testing en el proyecto
- Los casos de prueba tienen IDs secuenciales (T-001, T-002, ...)
- Cada test documenta: input concreto, output esperado y estado actual
- Los comandos son copiables directamente sin modificación
- Tests de integración describen precondiciones y pasos exactos
- Los criterios de aceptación son numéricos cuando sea posible (%, ms, bytes)
- Si el proyecto no tiene tests pero es complejo, documentar el plan mínimo sugerido
- Distinguir entre tests nativos (PC) y tests embebidos (hardware)

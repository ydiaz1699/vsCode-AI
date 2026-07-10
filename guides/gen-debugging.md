# Guía: Generar DEBUGGING.md

## Archivo de Salida

`.ai/DEBUGGING.md`

## Cuándo Generarlo

**Solo si** el proyecto tiene:
- Problemas de comunicación entre componentes (RF, BLE, I2C, SPI, MQTT)
- Bugs resueltos que involucran timing, interrupciones o interacción hardware/software
- Dependencias externas cuyo comportamiento interno afecta la lógica del proyecto
- Cualquier bug cuya resolución requirió análisis del source de una librería

## Instrucciones para la IA

1. Identificar todos los bugs resueltos durante el desarrollo (git log, CHANGELOG, TASKS done)
2. Para cada bug resuelto, documentar la cadena causal completa: CAUSA → MECANISMO → EFECTO → SÍNTOMA
3. Documentar los HALLAZGOS del source de librerías externas que fueron clave para el diagnóstico
4. Extraer los TIEMPOS REALES calculados del sistema (constantes × repeticiones × overhead)
5. Listar las SUPOSICIONES FALSAS que tenía el código antes del fix
6. Documentar los TESTS INCREMENTALES usados y su resultado (qué aisló cada test)
7. Crear tabla de "Síntoma → Causa probable → Verificación" para debugging futuro
8. Documentar los PARÁMETROS CRÍTICOS del sistema con sus rangos válidos y qué pasa si se salen
9. Incluir sección de "Red Flags" — señales de que el problema es hardware vs software
10. Si hay quirks de librerías externas, documentarlos con referencia al source code

## Estructura Esperada

```markdown
# [Nombre] — Debugging & Diagnósticos

## Bugs Resueltos

### BUG-001: [Título del síntoma]
**Síntoma:** [lo que el usuario observaba]
**Causa raíz:** [la configuración/código/timing incorrecto]
**Cadena causal:**
\```
CAUSA: [qué estaba mal]
  ↓
MECANISMO: [cómo produce el efecto internamente]
  ↓
EFECTO: [estado corrupto]
  ↓
SÍNTOMA: [lo observable]
\```
**Fix:** [cambio aplicado]
**Verificación:** [test que confirma el fix]

## Hallazgos de Librerías Externas

### [Librería] — Comportamiento Interno
| Función | Lo que parece hacer | Lo que realmente hace | Fuente |
|...|...|...|...|

## Timing Real del Sistema

| Parámetro | Valor calculado | Fórmula | Impacto si cambia |
|...|...|...|...|

## Suposiciones Falsas Comunes

| Suposición | Realidad | Consecuencia |
|...|...|...|

## Tabla de Diagnóstico Rápido

| Síntoma | Causa probable | Cómo verificar |
|...|...|...|

## Parámetros Críticos

| Parámetro | Valor | Rango válido | Si es menor | Si es mayor |
|...|...|...|...|...|

## Red Flags: ¿Hardware o Software?

### Es HARDWARE si:
- [señal 1]
- [señal 2]

### Es SOFTWARE si:
- [señal 1]
- [señal 2]

## Quirks de Dependencias

### [Librería] v[X.Y.Z]
- [quirk 1 con referencia al source]
- [quirk 2]
```

## Reglas

- Solo documentar bugs que requirieron análisis profundo (no typos ni errores triviales)
- La cadena causal debe ser completa: desde la causa hasta el síntoma observable
- Los hallazgos de librerías incluyen LINK al source (GitHub line number) cuando es posible
- El timing se calcula con la fórmula explícita (para poder recalcular si cambian parámetros)
- Las suposiciones falsas son específicas: "pin 2 = interrupción 2" NO "parámetro incorrecto"
- La tabla de diagnóstico rápido tiene mínimo 5 entradas
- Los parámetros críticos incluyen rangos y consecuencias en ambas direcciones
- Red Flags deben ser verificables sin instrumentación especial (solo Serial + multímetro)
- Si un bug fue causado por hardware (cable suelto, pin incorrecto), documentarlo también
- Máximo 3 bugs detallados (los más instructivos), el resto en forma resumida

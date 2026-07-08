# Guía: Generar HARDWARE.md

## Archivo de Salida

`.ai/HARDWARE.md`

## Cuándo Generarlo

**Siempre que el proyecto involucre hardware físico** (placas, sensores, actuadores, displays, módulos de comunicación).

## Instrucciones para la IA

1. Identificar la placa principal desde `platformio.ini` y mapear al catálogo
2. Buscar todos los `#define` de pines en el código (`PIN_`, `GPIO_`, constantes numéricas asignadas a pines)
3. Identificar periféricos por sus includes (`#include <DHT.h>`, `#include <Wire.h>`, etc.)
4. Construir la tabla de wiring mapeando cada pin definido a su periférico y función
5. Estimar consumo energético basándose en datasheets del catálogo
6. Documentar la fuente de alimentación (USB, batería, adaptador)
7. Calcular autonomía estimada si usa batería
8. Escribir advertencias de voltaje para periféricos con incompatibilidad potencial
9. Verificar que no haya conflictos de pines (mismo GPIO para dos funciones)
10. Listar errores comunes específicos del hardware utilizado

## Estructura Esperada

```markdown
# [Nombre] — Hardware

## Referencias
### Placa Principal
- Componente: [nombre]
- Referencia: [link al catálogo]

### Periféricos
| Componente | Referencia | Cantidad | Protocolo |
|...|...|...|...|

## Tabla de Conexiones (Wiring)
| Periférico | Pin Periférico | Pin Placa | Función | Notas |
|...|...|...|...|...|

## Consumo Energético
| Estado | Corriente | Duración | Notas |
|...|...|...|...|

## Alimentación
- Fuente: ...
- Autonomía: ...

## Advertencias
> ⚠️ ...
```

## Reglas

- Cada pin físico debe aparecer máximo una vez en la tabla de wiring (detectar conflictos)
- Si un periférico usa 5V en placa de 3.3V, advertir explícitamente sobre level shifter
- El consumo se expresa en mA, con suficiente precisión para calcular batería
- Las advertencias usan el formato blockquote con emoji ⚠️
- Los periféricos I2C deben indicar dirección (0x76, 0x3C, etc.)
- Los periféricos SPI deben indicar pin CS
- Mínimo 3 estados en la tabla de consumo (sleep, idle, activo)
- Si hay batería, calcular autonomía: capacidad_mAh / consumo_promedio_mA

# 📋 Cómo Agregar un Periférico al Catálogo

Guía paso a paso para registrar un nuevo periférico (sensor, actuador, módulo) en el catálogo.

---

## Checklist

- [ ] 1. Verificar que no existe
- [ ] 2. Copiar template
- [ ] 3. Llenar frontmatter
- [ ] 4. Llenar contenido markdown
- [ ] 5. Registrar en catalog/README.md
- [ ] 6. Validar

---

## 1. Verificar que No Existe

```bash
# Buscar por nombre del chip/módulo
grep -ri "nombre-del-modulo" catalog/peripherals/

# Buscar por protocolo
grep -ri "I2C\|SPI\|OneWire" catalog/peripherals/

# Revisar tabla principal
cat catalog/README.md | grep -i "nombre"
```

Si existe un módulo similar (ej: DHT11 y DHT22), verificar si las diferencias justifican una entrada separada.

## 2. Copiar Template

```bash
# Crear archivo con ID en formato: periph-[nombre-corto].md
cp catalog/peripherals/_template.md catalog/peripherals/periph-nuevo-modulo.md
```

**Formato de ID:** `periph-[nombre-comercial-corto]`
- Ejemplos: `periph-dht22`, `periph-bme280`, `periph-relay-4ch`
- Todo en minúsculas, separado por guiones
- Usar el nombre más reconocible del chip/módulo

## 3. Llenar Frontmatter YAML

```yaml
---
id: periph-nuevo-modulo
name: "Nombre Comercial del Módulo"
category: "Sensor Temperatura / Actuador / Display / Comunicación / IMU"
chip: "CHIP-PRINCIPAL"
protocol: "I2C / SPI / OneWire / GPIO / PWM / UART"
voltage_min: 3.3
voltage_max: 5.0
logic_level: 3.3
current_ma: 15
i2c_address: "0x76"  # Solo si I2C
spi_max_mhz: 10      # Solo si SPI
frequency: "2.4GHz"   # Solo si RF
resolution: "16-bit"  # Solo si sensor
range: "-40°C a 80°C" # Solo si sensor
accuracy: "±0.5°C"    # Solo si sensor
datasheet: "https://url-del-datasheet"
library: "nombre/libreria@^version"
purchase_url: "https://url-de-compra"
price_usd: 3
added_date: "2024-01-15"
---
```

## 4. Llenar Contenido Markdown

```markdown
# [Nombre del Periférico]

## Resumen
[1-2 oraciones: qué mide/hace, protocolo, rango]

## Especificaciones
| Spec | Valor |
|------|-------|
| Protocolo | [I2C/SPI/GPIO] |
| Voltaje | [X]–[Y]V |
| Corriente | [X] mA |
| Rango | [especificación] |
| Precisión | [especificación] |

## Conexiones

### Con ESP32 (3.3V)
| Pin Módulo | Pin ESP32 | Función | Notas |
|-----------|-----------|---------|-------|
| VCC | 3.3V | Alimentación | NO usar 5V |
| GND | GND | Tierra | — |
| SDA | GPIO21 | I2C Data | Pull-up 4.7kΩ |
| SCL | GPIO22 | I2C Clock | Pull-up 4.7kΩ |

### Con Arduino UNO (5V)
| Pin Módulo | Pin Arduino | Función | Notas |
|-----------|-------------|---------|-------|
| VCC | 5V | Alimentación | — |
| GND | GND | Tierra | — |
| SDA | A4 | I2C Data | — |
| SCL | A5 | I2C Clock | — |

## Librería Recomendada

\```ini
lib_deps = nombre/libreria@^version
\```

## Código de Ejemplo

\```cpp
#include <Libreria.h>

// Ejemplo mínimo funcional
void setup() {
  // ...
}
void loop() {
  // ...
}
\```

## Compatibilidad

| Placa | Compatible | Notas |
|-------|-----------|-------|
| board-esp32-devkit-v1 | ✅ | Directo |
| board-arduino-uno-r3 | ✅ | — |
| board-esp8266-nodemcu | ⚠️ | Solo 1 I2C bus |

## Errores Comunes
1. [Error frecuente y solución]
2. [Error frecuente y solución]
3. [Error frecuente y solución]
```

## 5. Registrar en catalog/README.md

Agregar una fila a la tabla de periféricos:

```markdown
| [periph-nuevo-modulo](peripherals/nuevo-modulo.md) | Nombre Comercial | Protocolo | X.X–Y.YV | Categoría |
```

**Orden:** Mantener agrupado por categoría (Sensores, Actuadores, Displays, Comunicación).

## 6. Validar

```bash
# Verificar YAML válido
python3 -c "import yaml; yaml.safe_load(open('catalog/peripherals/periph-nuevo-modulo.md').read().split('---')[1])"

# Verificar link en README
grep "nuevo-modulo" catalog/README.md

# Verificar que la librería existe
pio pkg search "nombre-libreria"
```

### Criterios de Validación

| Criterio | Verificación |
|----------|-------------|
| ID único | No repetido en catalog/ |
| Voltaje verificado | Consultado en datasheet |
| Protocolo correcto | Confirmado con librería |
| Librería existente | `pio pkg search` la encuentra |
| Conexiones probadas | Al menos para ESP32 |
| Link en README | Apunta al archivo correcto |
| Código de ejemplo | Compila sin errores |

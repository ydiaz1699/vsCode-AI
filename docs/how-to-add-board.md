# 📋 Cómo Agregar una Placa al Catálogo

Guía paso a paso para registrar una nueva placa de desarrollo en el catálogo.

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

Antes de agregar, buscar si ya está catalogada:

```bash
# Buscar por nombre
grep -ri "nombre-de-la-placa" catalog/boards/

# Buscar por MCU
grep -ri "chip-mcu" catalog/boards/

# Revisar tabla principal
cat catalog/README.md | grep -i "nombre"
```

Si existe con otro nombre o ID, NO duplicar. Actualizar el existente.

## 2. Copiar Template

```bash
# Crear archivo con ID en formato: board-[marca]-[modelo].md
cp catalog/boards/_template.md catalog/boards/board-nueva-placa.md
```

**Formato de ID:** `board-[fabricante]-[modelo]`
- Ejemplos: `board-esp32-devkit-v1`, `board-arduino-nano`, `board-stm32-bluepill`
- Todo en minúsculas, separado por guiones
- Sin versiones a menos que sean modelos distintos

## 3. Llenar Frontmatter YAML

```yaml
---
id: board-nueva-placa
name: "Nombre Comercial de la Placa"
mcu: "CHIP-EXACTO"
architecture: "ARM Cortex-M4 / Xtensa LX6 / RISC-V / AVR"
clock_mhz: 240
flash_kb: 4096
ram_kb: 520
wifi: true
bluetooth: "BLE 5.0"  # false si no tiene
voltage: 3.3
gpio_count: 34
adc_channels: 18
pwm_channels: 16
uart: 3
spi: 2
i2c: 2
usb: "Micro-USB / USB-C / Mini-USB"
price_usd: 7
platformio_board: "nombre_exacto_en_platformio"
datasheet: "https://url-del-datasheet"
purchase_url: "https://url-de-compra"
added_date: "2024-01-15"
---
```

## 4. Llenar Contenido Markdown

```markdown
# [Nombre de la Placa]

## Resumen
[1-2 oraciones describiendo la placa y su caso de uso ideal]

## Especificaciones Principales
| Spec | Valor |
|------|-------|
| MCU | [chip] |
| Flash | [X] KB |
| RAM | [X] KB |
| Voltaje lógico | [X]V |
| GPIO disponibles | [X] |

## Pinout
[Tabla o imagen del pinout con funciones alternativas]

## Compatibilidad con Periféricos
| Periférico | Compatible | Notas |
|------------|-----------|-------|
| periph-dht22 | ✅ | Directo, cualquier GPIO |
| periph-bme280 | ✅ | I2C en GPIO21/22 |

## Notas de Uso
- [Particularidades importantes]
- [Limitaciones conocidas]
- [Tips de configuración en PlatformIO]

## PlatformIO
\```ini
[env:nombre]
platform = [platform]
board = [board_id]
framework = arduino
\```
```

## 5. Registrar en catalog/README.md

Agregar una fila a la tabla de placas:

```markdown
| [board-nueva-placa](boards/nueva-placa.md) | Nombre Comercial | CHIP | ✅/❌ | ✅/❌ | X.XV | ~$X USD |
```

**Orden:** Mantener agrupado por fabricante/familia (ESP32, Arduino, STM32, etc.)

## 6. Validar

```bash
# Verificar que el frontmatter es YAML válido
python3 -c "import yaml; yaml.safe_load(open('catalog/boards/board-nueva-placa.md').read().split('---')[1])"

# Verificar que el link funciona desde README
grep "nueva-placa" catalog/README.md

# Verificar que el platformio_board existe
pio boards | grep "nombre_exacto"
```

### Criterios de Validación

| Criterio | Verificación |
|----------|-------------|
| ID único | No repetido en catalog/ |
| Nombre exacto | Coincide con fabricante |
| MCU verificado | Consultado en datasheet |
| Voltaje correcto | Crítico para compatibilidad |
| PlatformIO ID válido | `pio boards` lo reconoce |
| Link en README | Apunta al archivo correcto |

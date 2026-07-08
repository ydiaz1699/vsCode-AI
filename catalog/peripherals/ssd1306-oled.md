---
id: "ssd1306-oled"
name: "SSD1306 128x64 OLED"
category: "display"
protocol: "I2C"
voltage_min: 3.3
voltage_max: 5.0
voltage_logic: "3.3-5V"
pins_required: [SDA, SCL]
i2c_address: "0x3C"
library: "adafruit/Adafruit SSD1306"
library_version: "^2.5.7"
level_shifter_needed: false
current_ma: 10
datasheet_url: "https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf"
---

# SSD1306 OLED 128x64

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje | 3.3 – 5V |
| Protocolo | I2C |
| Corriente | ~10 mA (depende de píxeles encendidos) |
| Level Shifter | No necesario |
| Resolución | 128 x 64 píxeles |
| Dirección I2C | 0x3C (o 0x3D) |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| VCC | Alimentación | 3.3-5V |
| GND | Tierra | — |
| SDA | Datos I2C | Pull-up integrado en módulo |
| SCL | Reloj I2C | Pull-up integrado en módulo |

## Conexión por Plataforma

### ESP32

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| VCC | 3.3V | — |
| GND | GND | — |
| SDA | GPIO21 | I2C por defecto |
| SCL | GPIO22 | I2C por defecto |

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| VCC | 5V | — |
| GND | GND | — |
| SDA | A4 | — |
| SCL | A5 | — |

## Consideraciones Críticas

- ⚠️ Verificar dirección I2C: **0x3C** (más común) o **0x3D** — usar I2C scanner
- ⚠️ **Arduino UNO**: buffer de 1KB (128×64/8) consume la mitad de la RAM disponible
- Algunos módulos chinos vienen con VCC/GND invertidos — verificar siempre
- Para ESP32 se puede reasignar SDA/SCL a cualquier GPIO

## Código de Ejemplo Mínimo

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial.begin(115200);
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println("SSD1306 no encontrado");
    for (;;);
  }
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Hola Mundo!");
  display.display();
}

void loop() {}
```

## platformio.ini

```ini
lib_deps =
    adafruit/Adafruit SSD1306@^2.5.7
    adafruit/Adafruit GFX Library@^1.11.5
```

## Compatibilidad con Placas del Catálogo

| Placa | Compatible | Notas |
|-------|-----------|-------|
| ESP32 DevKit | ✅ | Sin problemas de RAM |
| Arduino UNO | ⚠️ | Buffer 1KB usa 50% RAM |
| Arduino Nano | ⚠️ | Misma limitación de RAM |

## Referencias

- [Datasheet SSD1306](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)
- [Adafruit SSD1306 Library](https://github.com/adafruit/Adafruit_SSD1306)

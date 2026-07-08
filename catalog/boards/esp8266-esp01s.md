---
id: "esp8266-esp01s"
name: "ESP-01S"
mcu: "ESP8266EX"
architecture: "Xtensa L106"
cores: 1
clock_mhz: 80
ram_kb: 80
flash_mb: 1
voltage_logic: 3.3
voltage_vin: "3.3V (sin regulador)"
gpio_total: 4
gpio_restricted: []
gpio_input_only: []
adc_bits: 10
adc_channels: 1
dac_channels: 0
pwm_channels: 2
wifi: true
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: ""
platform: "espressif8266"
board: "esp01_1m"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 80
current_sleep_ua: 20
price_tier: "$"
---

# ESP-01S

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP8266EX |
| Arquitectura | Xtensa L106 (single-core, 32-bit) |
| Núcleos | 1 |
| Frecuencia | 80 MHz |
| RAM | 80 KB usuario |
| Flash | 1 MB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 3.3V directo (SIN regulador) |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz)
- Bluetooth: No disponible
- USB: No disponible (requiere adaptador UART externo)
- UART: 1x (TX=GPIO1, RX=GPIO3)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 4 (GPIO0, GPIO1, GPIO2, GPIO3) |
| GPIO Restringidos | Ninguno dedicado, pero GPIO1/3 son UART |
| Solo Entrada | Ninguno |
| ADC | A0 (no accesible en header, 1 canal) |
| DAC | No disponible |
| PWM | GPIO0, GPIO2 (software PWM) |
| I2C | SDA=GPIO0, SCL=GPIO2 (únicos disponibles) |
| SPI | No accesible en este formato |
| UART | TX=GPIO1, RX=GPIO3 |

## Niveles de Voltaje

- Lógica: 3.3V
- Alimentación: 3.3V EXACTO (no tolera 5V)
- Tolerancia 5V: **NO** - Alimentar con 5V destruye el módulo instantáneamente

## Consideraciones Críticas

- **Sin USB**: No tiene puerto USB ni chip UART. Se necesita un adaptador USB-UART externo (FT232RL, CP2102, CH340) para programar. Conectar TX-RX cruzado.
- **3.3V obligatorio**: No incluye regulador de voltaje. Alimentar SIEMPRE a 3.3V (máx 3.6V). Un Arduino de 5V en TX destruye el módulo. Usar divisor de voltaje en RX.
- **Solo 4 GPIO**: GPIO0 y GPIO2 son los únicos "libres" (GPIO1/3 son TX/RX). Extremadamente limitado para proyectos con múltiples sensores.
- **1MB flash muy limitado**: Sin espacio para OTA ni filesystem grande. El firmware debe ser compacto. Considerar ESP-01S con 1MB como módulo WiFi dedicado.
- **Boot mode**: GPIO0 debe estar HIGH para boot normal, LOW para flash. GPIO2 debe estar HIGH al boot. Usar pulsador para modo flash.
- **Picos de corriente**: WiFi consume picos de 300-400mA. El regulador 3.3V del Arduino UNO NO es suficiente. Usar fuente dedicada de 3.3V ≥ 500mA.

## platformio.ini de referencia

```ini
[env:esp01s]
platform = espressif8266
board = esp01_1m
framework = arduino
monitor_speed = 115200
upload_speed = 115200
upload_resetmethod = nodemcu
board_build.ldscript = eagle.flash.1m64.ld
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [ESP-01/ESP-01S Pinout](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)
- [Programming ESP-01](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)
- [ESP8266 Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)

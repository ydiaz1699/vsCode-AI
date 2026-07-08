---
id: "esp32-devkit-v1"
name: "ESP32 DevKit V1"
mcu: "ESP32-D0WDQ6"
architecture: "Xtensa LX6"
cores: 2
clock_mhz: 240
ram_kb: 520
flash_mb: 4
voltage_logic: 3.3
voltage_vin: "5V (USB) / 3.3V (3V3 pin)"
gpio_total: 34
gpio_restricted: [6, 7, 8, 9, 10, 11]
gpio_input_only: [34, 35, 36, 39]
adc_bits: 12
adc_channels: 18
dac_channels: 2
pwm_channels: 16
wifi: true
bluetooth: true
bluetooth_version: "4.2"
usb_native: false
uart_chip: "CP2102"
platform: "espressif32"
board: "esp32dev"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 120
current_sleep_ua: 5
price_tier: "$$"
---

# ESP32 DevKit V1

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP32-D0WDQ6 |
| Arquitectura | Xtensa LX6 (dual-core) |
| Núcleos | 2 |
| Frecuencia | 240 MHz |
| RAM | 520 KB SRAM |
| Flash | 4 MB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB / 3.3V directo |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz)
- Bluetooth: v4.2 BR/EDR + BLE
- USB: Micro-USB (CP2102 UART bridge)
- UART: 3x UART (UART0 para programación)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 34 (GPIO0-GPIO39) |
| GPIO Restringidos | GPIO6-11 (flash SPI interno) |
| Solo Entrada | GPIO34, 35, 36, 39 (sin pull-up) |
| ADC1 (8 canales) | GPIO32-39 |
| ADC2 (10 canales) | GPIO0, 2, 4, 12-15, 25-27 |
| DAC | GPIO25 (DAC1), GPIO26 (DAC2) |
| PWM | Cualquier GPIO de salida (16 canales LEDC) |
| I2C | SDA=GPIO21, SCL=GPIO22 (por defecto) |
| SPI | VSPI: MOSI=23, MISO=19, CLK=18, CS=5 |
| UART | TX0=1, RX0=3 / TX2=17, RX2=16 |

## Niveles de Voltaje

- Lógica: 3.3V (HIGH ≥ 2.475V, LOW ≤ 0.825V)
- Entrada máxima: 3.6V absoluto
- Tolerancia 5V: **NO** - Requiere divisor de voltaje o level shifter

## Consideraciones Críticas

- **Strapping Pins**: GPIO0 (boot mode), GPIO2 (debe ser LOW o flotante al boot), GPIO5 (SDIO timing), GPIO12 (voltaje flash), GPIO15 (silencia log en boot). No conectar cargas que alteren su estado durante arranque.
- **ADC2 incompatible con WiFi**: Cuando WiFi está activo, ADC2 (GPIO0,2,4,12-15,25-27) no funciona. Usar solo ADC1 (GPIO32-39) en proyectos con WiFi.
- **Distribución dual-core**: Core 0 maneja WiFi/BT por defecto. Usar `xTaskCreatePinnedToCore()` para asignar tareas críticas al Core 1.
- **GPIO6-11 prohibidos**: Conectados internamente al flash SPI. Usarlos causa crash inmediato.
- **Corriente por pin**: Máximo 40mA por GPIO, recomendado 20mA. Total sumado no debe exceder 1.2A.

## platformio.ini de referencia

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_speed = 921600
lib_deps =
board_build.partitions = default.csv
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Datasheet ESP32](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [Pinout Reference](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)
- [Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf)

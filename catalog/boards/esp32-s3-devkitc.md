---
id: "esp32-s3-devkitc"
name: "ESP32-S3 DevKitC-1"
mcu: "ESP32-S3"
architecture: "Xtensa LX7"
cores: 2
clock_mhz: 240
ram_kb: 512
flash_mb: 8
voltage_logic: 3.3
voltage_vin: "5V (USB)"
gpio_total: 45
gpio_restricted: [26, 27, 28, 29, 30, 31, 32]
gpio_input_only: []
adc_bits: 12
adc_channels: 20
dac_channels: 0
pwm_channels: 8
wifi: true
bluetooth: true
bluetooth_version: "5.0"
usb_native: true
uart_chip: ""
platform: "espressif32"
board: "esp32-s3-devkitc-1"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 150
current_sleep_ua: 7
price_tier: "$$$"
---

# ESP32-S3 DevKitC-1

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP32-S3 (Xtensa LX7) |
| Arquitectura | Xtensa LX7 (dual-core) |
| Núcleos | 2 |
| Frecuencia | 240 MHz |
| RAM | 512 KB SRAM + 8 MB PSRAM (OPI) |
| Flash | 8 MB (OPI) |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz) con WiFi 6 parcial
- Bluetooth: v5.0 LE + Mesh
- USB: Nativo USB-OTG (USB 1.1 Full Speed) + USB-Serial/JTAG
- UART: 3x UART

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 45 (GPIO0-GPIO48) |
| GPIO Restringidos | GPIO26-32 (PSRAM OPI, si se usa) |
| Solo Entrada | Ninguno |
| ADC1 (10 canales) | GPIO1-10 |
| ADC2 (10 canales) | GPIO11-20 |
| DAC | No disponible en S3 |
| PWM | 8 canales LEDC (cualquier GPIO) |
| I2C | SDA=GPIO8, SCL=GPIO9 (configurable) |
| SPI | FSPI: MOSI=35, MISO=37, CLK=36, CS=34 |
| UART | TX0=43, RX0=44 |
| USB-OTG | GPIO19 (D-), GPIO20 (D+) |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 3.6V
- Tolerancia 5V: **NO** - Usar level shifter para señales 5V

## Consideraciones Críticas

- **PSRAM OPI ocupa GPIO26-32**: Si la variante incluye PSRAM OPI, estos pines no están disponibles. Verificar el modelo exacto del módulo.
- **USB-OTG nativo**: GPIO19/20 están dedicados a USB. Permite actuar como host USB (leer pendrives, teclados) o device (HID, CDC, MSC) sin chip externo.
- **Instrucciones SIMD/Vectoriales**: El LX7 incluye extensiones PIE para aceleración de señales (DSP). Útil para procesamiento de audio/imagen en edge AI.
- **Sin DAC**: A diferencia del ESP32 clásico, el S3 no tiene convertidor digital-analógico. Usar PWM+filtro o DAC externo (MCP4725).
- **AI Acceleration**: Soporte de hardware para redes neuronales (vector instructions), ideal para TinyML con TFLite Micro.
- **Dos puertos USB**: USB-OTG (GPIO19/20) para aplicación + USB-Serial/JTAG para debug. Ambos pueden usarse simultáneamente.

## platformio.ini de referencia

```ini
[env:esp32s3]
platform = espressif32
board = esp32-s3-devkitc-1
framework = arduino
monitor_speed = 115200
upload_speed = 921600
board_build.arduino.memory_type = qio_opi
board_upload.flash_size = 8MB
build_flags =
    -DARDUINO_USB_MODE=1
    -DARDUINO_USB_CDC_ON_BOOT=1
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Datasheet ESP32-S3](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)
- [ESP32-S3 DevKitC-1 Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/hw-reference/esp32s3/user-guide-devkitc-1.html)
- [USB-OTG Programming](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/usb_host.html)

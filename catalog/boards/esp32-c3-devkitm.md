---
id: "esp32-c3-devkitm"
name: "ESP32-C3 DevKitM-1"
mcu: "ESP32-C3"
architecture: "RISC-V"
cores: 1
clock_mhz: 160
ram_kb: 400
flash_mb: 4
voltage_logic: 3.3
voltage_vin: "5V (USB)"
gpio_total: 22
gpio_restricted: [12, 13, 14, 15, 16, 17]
gpio_input_only: []
adc_bits: 12
adc_channels: 6
dac_channels: 0
pwm_channels: 6
wifi: true
bluetooth: true
bluetooth_version: "5.0"
usb_native: true
uart_chip: ""
platform: "espressif32"
board: "esp32-c3-devkitm-1"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 90
current_sleep_ua: 5
price_tier: "$"
---

# ESP32-C3 DevKitM-1

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP32-C3 |
| Arquitectura | RISC-V (single-core, 32-bit) |
| Núcleos | 1 |
| Frecuencia | 160 MHz |
| RAM | 400 KB SRAM |
| Flash | 4 MB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz)
- Bluetooth: v5.0 LE + Mesh
- USB: Nativo CDC/JTAG (USB 1.1)
- UART: 2x UART

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 22 (GPIO0-GPIO21) |
| GPIO Restringidos | GPIO12-17 (flash SPI) |
| Solo Entrada | Ninguno |
| ADC (6 canales) | GPIO0-5 |
| DAC | No disponible |
| PWM | 6 canales LEDC (cualquier GPIO) |
| I2C | SDA=GPIO8, SCL=GPIO9 (por defecto) |
| SPI | MOSI=GPIO7, MISO=GPIO2, CLK=GPIO6, CS=GPIO10 |
| UART | TX0=GPIO21, RX0=GPIO20 |
| USB | GPIO18 (D-), GPIO19 (D+) |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 3.6V
- Tolerancia 5V: **NO**

## Consideraciones Críticas

- **RISC-V single-core**: No tiene dual-core. Las tareas WiFi/BT comparten CPU con la aplicación. Optimizar uso de `delay()` y prioridades de FreeRTOS.
- **USB CDC nativo**: No necesita chip UART externo. GPIO18/19 proveen USB para programación y serial. Configurar `USB_CDC_ON_BOOT=1`.
- **Bajo costo/consumo**: Ideal para sensores IoT con batería. Deep sleep de 5µA permite años con batería CR2032 en lecturas periódicas.
- **GPIO limitados**: Solo 22 GPIO totales, 16 usables. Planificar cuidadosamente en proyectos con múltiples periféricos.
- **Sin DAC**: Igual que el S3, no incluye DAC. Usar PWM con filtro RC para señales analógicas simples.
- **Seguridad por hardware**: Incluye Secure Boot v2, Flash Encryption, y Digital Signature. Apto para producción segura.

## platformio.ini de referencia

```ini
[env:esp32c3]
platform = espressif32
board = esp32-c3-devkitm-1
framework = arduino
monitor_speed = 115200
upload_speed = 460800
build_flags =
    -DARDUINO_USB_MODE=1
    -DARDUINO_USB_CDC_ON_BOOT=1
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Datasheet ESP32-C3](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
- [ESP32-C3 DevKitM-1 Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitm-1.html)
- [RISC-V en ESP32-C3](https://www.espressif.com/en/news/ESP32_C3)

---
id: "esp8266-nodemcu-v3"
name: "NodeMCU V3 (ESP8266)"
mcu: "ESP8266EX"
architecture: "Xtensa L106"
cores: 1
clock_mhz: 160
ram_kb: 80
flash_mb: 4
voltage_logic: 3.3
voltage_vin: "5V (USB) / VIN"
gpio_total: 11
gpio_restricted: [6, 7, 8, 9, 10, 11]
gpio_input_only: []
adc_bits: 10
adc_channels: 1
dac_channels: 0
pwm_channels: 4
wifi: true
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: "CH340"
platform: "espressif8266"
board: "nodemcuv2"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 80
current_sleep_ua: 20
price_tier: "$"
---

# NodeMCU V3 (ESP8266)

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP8266EX |
| Arquitectura | Xtensa L106 (single-core, 32-bit) |
| Núcleos | 1 |
| Frecuencia | 80/160 MHz |
| RAM | 80 KB usuario |
| Flash | 4 MB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB / VIN |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz)
- Bluetooth: No disponible
- USB: Micro-USB (CH340 UART bridge)
- UART: 1.5x (UART0 full, UART1 solo TX en GPIO2)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 11 (usables) |
| GPIO Restringidos | GPIO6-11 (flash SPI) |
| Solo Entrada | A0 (ADC, 0-3.3V con divisor) |
| ADC | A0 (1 canal, 10 bits) |
| DAC | No disponible |
| PWM | Cualquier GPIO (software, ~1KHz) |
| I2C | SDA=D2(GPIO4), SCL=D1(GPIO5) |
| SPI | MOSI=D7(GPIO13), MISO=D6(GPIO12), CLK=D5(GPIO14), CS=D8(GPIO15) |
| UART | TX=GPIO1, RX=GPIO3 |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 3.6V en GPIO
- Tolerancia 5V: **NO** - No conectar señales de 5V directamente

## Consideraciones Críticas

- **Form factor ancho**: El NodeMCU V3 es más ancho que el V2/D1 Mini. En protoboard estándar ocupa ambos lados, sin pines laterales libres. Usar protoboard doble o cables.
- **CH340 requiere driver**: En algunos SO (Windows antiguo, macOS) requiere instalar driver CH340 manualmente. Si el puerto no aparece, instalar driver.
- **Boot pins**: GPIO0 (D3), GPIO2 (D4), GPIO15 (D8) son críticos al arranque. Mismas restricciones que D1 Mini.
- **4MB flash**: Menos que el D1 Mini Pro (16MB). Particionar cuidadosamente entre firmware y filesystem. OTA requiere ~50% del flash libre.
- **VIN expuesto**: El pin VIN provee 5V directo del USB. Útil para alimentar sensores de 5V, pero NO conectar a GPIO.
- **yield() obligatorio**: El event loop del WiFi necesita ejecutarse regularmente. Bucles largos sin `yield()` o `delay()` causan Soft WDT Reset.

## platformio.ini de referencia

```ini
[env:nodemcuv2]
platform = espressif8266
board = nodemcuv2
framework = arduino
monitor_speed = 115200
upload_speed = 921600
board_build.filesystem = littlefs
board_build.ldscript = eagle.flash.4m1m.ld
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [ESP8266 NodeMCU Pinout](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)
- [NodeMCU Documentation](https://nodemcu.readthedocs.io/)
- [ESP8266 Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)

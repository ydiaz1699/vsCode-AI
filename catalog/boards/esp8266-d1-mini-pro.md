---
id: "esp8266-d1-mini-pro"
name: "Wemos D1 Mini Pro"
mcu: "ESP8266EX"
architecture: "Xtensa L106"
cores: 1
clock_mhz: 160
ram_kb: 80
flash_mb: 16
voltage_logic: 3.3
voltage_vin: "5V (USB) / 3.3V (3V3 pin)"
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
uart_chip: "CP2104"
platform: "espressif8266"
board: "d1_mini_pro"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 80
current_sleep_ua: 20
price_tier: "$"
---

# Wemos D1 Mini Pro

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ESP8266EX |
| Arquitectura | Xtensa L106 (single-core, 32-bit) |
| Núcleos | 1 |
| Frecuencia | 80/160 MHz (configurable) |
| RAM | 80 KB usuario + 32 KB instrucciones |
| Flash | 16 MB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB / VIN |

## Conectividad

- WiFi: 802.11 b/g/n (2.4 GHz)
- Bluetooth: No disponible
- USB: Micro-USB (CP2104 UART bridge)
- UART: 1.5x (UART0 full, UART1 solo TX)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 11 (usables) |
| GPIO Restringidos | GPIO6-11 (flash SPI interno) |
| Solo Entrada | A0 (ADC, 0-1V rango real) |
| ADC | A0 (1 canal, 0-3.3V con divisor interno) |
| DAC | No disponible |
| PWM | D1, D2, D5-D8 (software PWM, cualquier GPIO) |
| I2C | SDA=D2(GPIO4), SCL=D1(GPIO5) |
| SPI | MOSI=D7(GPIO13), MISO=D6(GPIO12), CLK=D5(GPIO14), CS=D8(GPIO15) |
| UART | TX=D10(GPIO1), RX=D9(GPIO3) |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 3.6V en GPIO, 1.0V en ADC (3.3V con divisor)
- Tolerancia 5V: **NO** - Los pines NO son 5V tolerant. Usar level shifter obligatorio.

## Consideraciones Críticas

- **Pines de Boot**: GPIO0 (D3) debe estar HIGH para boot normal, LOW para flash. GPIO2 (D4) debe estar HIGH al boot. GPIO15 (D8) debe estar LOW al boot. No conectar pull-downs a D3/D4 ni pull-ups a D8.
- **NOT 5V tolerant**: A diferencia de Arduino, NINGÚN pin tolera 5V. Conectar sensores de 5V directamente destruye el chip. Usar divisores resistivos o level shifters.
- **Un solo ADC**: Solo existe A0 (0-1V nativo, 0-3.3V con divisor del board). Para múltiples señales analógicas, usar multiplexor externo (CD4051/ADS1115).
- **16MB flash ventaja**: La versión Pro tiene 16MB vs 4MB estándar. Permite SPIFFS/LittleFS grande para archivos web, logs, OTA con particiones duales.
- **PWM por software**: El ESP8266 no tiene hardware PWM dedicado. La resolución y frecuencia son limitadas. No apto para control servo preciso.
- **yield()/delay() obligatorio**: El loop principal debe ceder tiempo al stack WiFi. Loops sin yield() causan WDT reset.

## platformio.ini de referencia

```ini
[env:d1_mini_pro]
platform = espressif8266
board = d1_mini_pro
framework = arduino
monitor_speed = 115200
upload_speed = 921600
board_build.filesystem = littlefs
board_build.ldscript = eagle.flash.16m14m.ld
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Wemos D1 Mini Pro Wiki](https://www.wemos.cc/en/latest/d1/d1_mini_pro.html)
- [ESP8266 Pinout Reference](https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/)
- [ESP8266 Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)

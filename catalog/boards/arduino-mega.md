---
id: "arduino-mega"
name: "Arduino Mega 2560"
mcu: "ATmega2560"
architecture: "AVR 8-bit"
cores: 1
clock_mhz: 16
ram_kb: 8
flash_mb: 0.256
voltage_logic: 5.0
voltage_vin: "7-12V (VIN) / 5V (USB)"
gpio_total: 54
gpio_restricted: []
gpio_input_only: []
adc_bits: 10
adc_channels: 16
dac_channels: 0
pwm_channels: 15
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: "ATmega16U2"
platform: "atmelavr"
board: "megaatmega2560"
framework: "arduino"
monitor_speed: 9600
current_active_ma: 50
current_sleep_ua: 0
price_tier: "$$"
---

# Arduino Mega 2560

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ATmega2560 |
| Arquitectura | AVR 8-bit |
| Núcleos | 1 |
| Frecuencia | 16 MHz |
| RAM | 8 KB SRAM |
| Flash | 256 KB (8KB bootloader) |
| Voltaje Lógico | 5V |
| Voltaje Alimentación | 7-12V (VIN) / 5V USB |

## Conectividad

- WiFi: No disponible
- Bluetooth: No disponible
- USB: USB-B (ATmega16U2 como bridge)
- UART: 4x hardware (Serial, Serial1, Serial2, Serial3)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 54 digitales + 16 analógicos |
| GPIO Restringidos | D0/D1 (Serial0) |
| Solo Entrada | Ninguno |
| ADC (16 canales) | A0-A15 (10 bits, 0-5V) |
| DAC | No disponible |
| PWM (15 canales) | D2-D13, D44-D46 |
| I2C | SDA=D20, SCL=D21 |
| SPI | MOSI=D51, MISO=D50, CLK=D52, CS=D53 |
| UART0 | TX0=D1, RX0=D0 |
| UART1 | TX1=D18, RX1=D19 |
| UART2 | TX2=D16, RX2=D17 |
| UART3 | TX3=D14, RX3=D15 |
| Interrupciones | INT0-INT5 (D2,D3,D18,D19,D20,D21) |

## Niveles de Voltaje

- Lógica: 5V
- Entrada: 5V tolerant
- Tolerancia 5V: **SÍ** - Nativo 5V

## Consideraciones Críticas

- **4 puertos UART hardware**: Ideal para proyectos que necesitan comunicar con múltiples dispositivos seriales simultáneamente (GPS + GSM + Sensor + Debug).
- **6 interrupciones externas**: Más que UNO/Nano (solo 2). Pins D2,D3,D18,D19,D20,D21. Además soporta Pin Change Interrupts en todos los pines.
- **256KB flash generoso**: Permite firmware complejo con múltiples bibliotecas. Apto para proyectos CNC (GRBL/Marlin), domótica multi-sensor, displays gráficos.
- **8KB RAM**: 4x más que UNO. Permite buffers más grandes, más variables String, y displays con framebuffer parcial.
- **Form factor grande**: 101x53mm. No cabe en cajas pequeñas. Considerar Mega Pro Mini para versiones compactas.
- **Pines SPI diferentes al UNO**: SPI en pines 50-53, NO 11-13 como en UNO. Shields diseñados para UNO usan ICSP header (compatible) pero verificar CS.

## platformio.ini de referencia

```ini
[env:mega]
platform = atmelavr
board = megaatmega2560
framework = arduino
monitor_speed = 9600
upload_speed = 115200
lib_deps =
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Arduino Mega 2560 Pinout](https://docs.arduino.cc/hardware/mega-2560)
- [ATmega2560 Datasheet](https://ww1.microchip.com/downloads/en/devicedoc/atmel-2549-8-bit-avr-microcontroller-atmega640-1280-1281-2560-2561_datasheet.pdf)
- [Arduino Mega Schematic](https://www.arduino.cc/en/uploads/Main/arduino-mega2560_R3-schematic.pdf)

---
id: "arduino-uno"
name: "Arduino UNO R3"
mcu: "ATmega328P"
architecture: "AVR 8-bit"
cores: 1
clock_mhz: 16
ram_kb: 2
flash_mb: 0.032
voltage_logic: 5.0
voltage_vin: "7-12V (VIN) / 5V (USB)"
gpio_total: 20
gpio_restricted: []
gpio_input_only: []
adc_bits: 10
adc_channels: 6
dac_channels: 0
pwm_channels: 6
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: "ATmega16U2"
platform: "atmelavr"
board: "uno"
framework: "arduino"
monitor_speed: 9600
current_active_ma: 45
current_sleep_ua: 0
price_tier: "$"
---

# Arduino UNO R3

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ATmega328P |
| Arquitectura | AVR 8-bit |
| Núcleos | 1 |
| Frecuencia | 16 MHz |
| RAM | 2 KB SRAM |
| Flash | 32 KB (0.5KB bootloader) |
| Voltaje Lógico | 5V |
| Voltaje Alimentación | 7-12V (VIN) / 5V (USB) |

## Conectividad

- WiFi: No disponible
- Bluetooth: No disponible
- USB: USB-B (ATmega16U2 como bridge)
- UART: 1x hardware (pines 0/1)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 20 (D0-D13 + A0-A5) |
| GPIO Restringidos | D0/D1 (UART, evitar si se usa Serial) |
| Solo Entrada | Ninguno |
| ADC (6 canales) | A0-A5 (10 bits, 0-5V) |
| DAC | No disponible |
| PWM (6 canales) | D3, D5, D6, D9, D10, D11 (~) |
| I2C | SDA=A4, SCL=A5 |
| SPI | MOSI=D11, MISO=D12, CLK=D13, CS=D10 |
| UART | TX=D1, RX=D0 |
| Interrupciones | INT0=D2, INT1=D3 (solo estos dos) |

## Niveles de Voltaje

- Lógica: 5V (HIGH ≥ 3V, LOW ≤ 1.5V)
- Entrada: 5V tolerant en todos los pines
- Tolerancia 5V: **SÍ** - Nativo 5V

## Consideraciones Críticas

- **2KB RAM es muy poco**: Strings y buffers grandes agotan la RAM rápidamente. Usar macro `F("texto")` para mantener strings en flash. Evitar String class, usar char arrays.
- **Solo 2 interrupciones externas**: INT0 (D2) e INT1 (D3) son las únicas interrupciones externas hardware. Para más, usar Pin Change Interrupts (PCINT) que son más complejas.
- **32KB flash limita firmware**: Sin espacio para bibliotecas pesadas. Cada library reduce espacio disponible. Monitorear uso con el reporte del compilador.
- **Sin WiFi/BT nativo**: Requiere módulos externos (ESP-01 como WiFi, HC-05 como BT). Considerar ESP32 si se necesita conectividad.
- **Timer compartidos**: Timer0 (delay/millis), Timer1 (Servo), Timer2 (tone). PWM en D5/D6 usa Timer0 con frecuencia diferente (976Hz vs 490Hz).
- **LED en D13**: El LED integrado está en D13 (SCK del SPI). Puede interferir con comunicación SPI. Remover jumper si es necesario.

## platformio.ini de referencia

```ini
[env:uno]
platform = atmelavr
board = uno
framework = arduino
monitor_speed = 9600
upload_speed = 115200
lib_deps =
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Arduino UNO Schematic](https://www.arduino.cc/en/uploads/Main/Arduino_Uno_Rev3-schematic.pdf)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [Arduino UNO Pin Mapping](https://docs.arduino.cc/hardware/uno-rev3)

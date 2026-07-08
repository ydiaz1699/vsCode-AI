---
id: "arduino-nano"
name: "Arduino Nano (ATmega328P)"
mcu: "ATmega328P"
architecture: "AVR 8-bit"
cores: 1
clock_mhz: 16
ram_kb: 2
flash_mb: 0.032
voltage_logic: 5.0
voltage_vin: "7-12V (VIN) / 5V (USB)"
gpio_total: 22
gpio_restricted: []
gpio_input_only: []
adc_bits: 10
adc_channels: 8
dac_channels: 0
pwm_channels: 6
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: "CH340"
platform: "atmelavr"
board: "nanoatmega328"
framework: "arduino"
monitor_speed: 9600
current_active_ma: 45
current_sleep_ua: 0
price_tier: "$"
---

# Arduino Nano (ATmega328P)

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | ATmega328P |
| Arquitectura | AVR 8-bit |
| Núcleos | 1 |
| Frecuencia | 16 MHz |
| RAM | 2 KB SRAM |
| Flash | 32 KB (2KB bootloader) |
| Voltaje Lógico | 5V |
| Voltaje Alimentación | 7-12V (VIN) / 5V (USB Mini-B) |

## Conectividad

- WiFi: No disponible
- Bluetooth: No disponible
- USB: Mini-B (CH340 UART bridge en clones)
- UART: 1x hardware (pines D0/D1)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 22 (D0-D13 + A0-A7) |
| GPIO Restringidos | D0/D1 (UART) |
| Solo Entrada | A6, A7 (solo analógico, no digital) |
| ADC (8 canales) | A0-A7 (10 bits, 0-5V) |
| DAC | No disponible |
| PWM (6 canales) | D3, D5, D6, D9, D10, D11 |
| I2C | SDA=A4, SCL=A5 |
| SPI | MOSI=D11, MISO=D12, CLK=D13, CS=D10 |
| UART | TX=D1, RX=D0 |
| Interrupciones | INT0=D2, INT1=D3 |

## Niveles de Voltaje

- Lógica: 5V
- Entrada: 5V tolerant
- Tolerancia 5V: **SÍ** - Nativo 5V

## Consideraciones Críticas

- **A6/A7 solo analógico**: A diferencia del UNO, el Nano tiene pines A6 y A7 pero son SOLO entrada analógica. No pueden usarse como GPIO digital (no tienen circuito de salida).
- **Factor forma pequeño**: Ideal para protoboard. Cabe perfectamente dejando una fila libre a cada lado en protoboard estándar.
- **CH340 en clones**: Los clones chinos usan CH340 en lugar de FTDI/ATmega16U2. Requiere driver CH340 en algunos SO. En PlatformIO seleccionar el puerto correcto.
- **USB Mini-B**: Conector más frágil que Micro-USB. Evitar movimiento repetido del cable. Considerar soldar cable si es instalación permanente.
- **Mismas limitaciones que UNO**: 2KB RAM, 32KB flash, sin WiFi. Aplicar mismas prácticas (F() macro, evitar String, arrays estáticos).
- **Bootloader ocupa 2KB**: En el Nano el bootloader (old bootloader) ocupa 2KB vs 0.5KB del UNO. En PlatformIO esto es transparente pero reduce flash útil a 30KB.

## platformio.ini de referencia

```ini
[env:nano]
platform = atmelavr
board = nanoatmega328
framework = arduino
monitor_speed = 9600
upload_speed = 57600
; Para clones con old bootloader:
; board_upload.speed = 57600
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [Arduino Nano Pinout](https://docs.arduino.cc/hardware/nano)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [CH340 Driver](http://www.wch-ic.com/downloads/CH341SER_EXE.html)

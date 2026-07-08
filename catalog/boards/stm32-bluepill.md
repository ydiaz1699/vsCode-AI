---
id: "stm32-bluepill"
name: "STM32 Blue Pill (F103C8T6)"
mcu: "STM32F103C8T6"
architecture: "ARM Cortex-M3"
cores: 1
clock_mhz: 72
ram_kb: 20
flash_mb: 0.064
voltage_logic: 3.3
voltage_vin: "5V (5V pin) / 3.3V"
gpio_total: 37
gpio_restricted: []
gpio_input_only: []
adc_bits: 12
adc_channels: 10
dac_channels: 0
pwm_channels: 15
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: false
uart_chip: ""
platform: "ststm32"
board: "bluepill_f103c8"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 35
current_sleep_ua: 1
price_tier: "$"
---

# STM32 Blue Pill (F103C8T6)

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | STM32F103C8T6 |
| Arquitectura | ARM Cortex-M3 (32-bit) |
| Núcleos | 1 |
| Frecuencia | 72 MHz |
| RAM | 20 KB SRAM |
| Flash | 64 KB (algunos chips tienen 128KB) |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V (pin 5V) / 3.3V |

## Conectividad

- WiFi: No disponible
- Bluetooth: No disponible
- USB: USB Full Speed (1.1) nativo, pero resistor pull-up incorrecto en muchos clones
- UART: 3x USART hardware
- Programación: ST-Link V2 (SWD) recomendado

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 37 (PA0-PA15, PB0-PB15, PC13-PC15) |
| GPIO Restringidos | PA11/PA12 (USB), PA13/PA14 (SWD debug) |
| Solo Entrada | Ninguno |
| ADC (10 canales) | PA0-PA7, PB0-PB1 (12 bits, 0-3.3V) |
| DAC | No disponible en F103 |
| PWM (15 canales) | Timer1: PA8-PA11, Timer2: PA0-PA3, Timer3: PA6-PA7/PB0-PB1, Timer4: PB6-PB9 |
| I2C | I2C1: SCL=PB6, SDA=PB7 / I2C2: SCL=PB10, SDA=PB11 |
| SPI | SPI1: SCK=PA5, MISO=PA6, MOSI=PA7 / SPI2: SCK=PB13, MISO=PB14, MOSI=PB15 |
| UART | USART1: TX=PA9, RX=PA10 / USART2: TX=PA2, RX=PA3 / USART3: TX=PB10, RX=PB11 |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada: 5V tolerant en PINES DIGITALES (no en analógicos)
- Tolerancia 5V: **SÍ** en pines digitales (marcados FT en datasheet). **NO** en pines ADC.

## Consideraciones Críticas

- **Requiere ST-Link para programar**: No tiene bootloader USB confiable de fábrica. Usar ST-Link V2 (~$2) conectado a SWDIO/SWCLK. Alternativa: grabar bootloader STM32duino vía serial.
- **5V tolerant en digitales**: Los pines marcados "FT" (Five-volt Tolerant) aceptan 5V en entrada digital. Esto es una GRAN ventaja sobre ESP32. Pero pines ADC (PA0-PA7, PB0-PB1) NO son 5V tolerant.
- **Resistor USB incorrecto (R10)**: Clones chinos tienen R10=10K en lugar de 1.5K. USB no será detectado correctamente. Soldar 1.8K en paralelo o reemplazar.
- **Flash "oculto"**: Muchos chips STM32F103C8 vienen con 128KB de flash aunque están marcados como 64KB. No es garantizado pero es común.
- **DMA poderoso**: 7 canales DMA permiten transferencias sin CPU. Ideal para ADC continuo, SPI a displays, UART a alta velocidad.
- **RTC integrado**: Reloj de tiempo real con backup (pin VBAT para batería). Mantiene hora sin alimentación principal.

## platformio.ini de referencia

```ini
[env:bluepill]
platform = ststm32
board = bluepill_f103c8
framework = arduino
monitor_speed = 115200
upload_protocol = stlink
debug_tool = stlink
; Alternativa con bootloader STM32duino:
; upload_protocol = dfu
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [STM32F103C8 Datasheet](https://www.st.com/resource/en/datasheet/stm32f103c8.pdf)
- [Blue Pill Pinout](https://stm32-base.org/boards/STM32F103C8T6-Blue-Pill.html)
- [STM32duino Wiki](https://github.com/stm32duino/wiki/wiki)

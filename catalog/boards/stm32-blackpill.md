---
id: "stm32-blackpill"
name: "STM32 Black Pill (F401CC)"
mcu: "STM32F401CCU6"
architecture: "ARM Cortex-M4"
cores: 1
clock_mhz: 84
ram_kb: 96
flash_mb: 0.256
voltage_logic: 3.3
voltage_vin: "5V (USB)"
gpio_total: 36
gpio_restricted: []
gpio_input_only: []
adc_bits: 12
adc_channels: 16
dac_channels: 0
pwm_channels: 12
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: true
uart_chip: ""
platform: "ststm32"
board: "blackpill_f401cc"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 40
current_sleep_ua: 1
price_tier: "$$"
---

# STM32 Black Pill (F401CC)

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | STM32F401CCU6 |
| Arquitectura | ARM Cortex-M4 con FPU |
| Núcleos | 1 |
| Frecuencia | 84 MHz |
| RAM | 96 KB SRAM |
| Flash | 256 KB |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB |

## Conectividad

- WiFi: No disponible
- Bluetooth: No disponible
- USB: Nativo USB Full Speed (CDC, HID, MSC)
- UART: 3x USART
- Programación: USB DFU nativo / ST-Link (SWD)

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 36 (PA0-PA15, PB0-PB15, PC13-PC15) |
| GPIO Restringidos | PA11/PA12 (USB), PA13/PA14 (SWD) |
| Solo Entrada | Ninguno |
| ADC (16 canales) | PA0-PA7, PB0-PB1, PC0-PC5 (12 bits) |
| DAC | No disponible en F401 |
| PWM (12 canales) | Timer1-Timer5 (múltiples pines) |
| I2C | I2C1: SCL=PB6, SDA=PB7 / I2C2: SCL=PB10, SDA=PB3 |
| SPI | SPI1: SCK=PA5, MISO=PA6, MOSI=PA7 / SPI2: SCK=PB13, MISO=PB14, MOSI=PB15 |
| UART | USART1: TX=PA9, RX=PA10 / USART2: TX=PA2, RX=PA3 |
| USB | PA11 (DM), PA12 (DP) |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 4.0V (absoluto)
- Tolerancia 5V: **NO** - A diferencia del Blue Pill (F103), el F401 NO es 5V tolerant en ningún pin

## Consideraciones Críticas

- **NO es 5V tolerant**: A diferencia del STM32F103 (Blue Pill), el F401 NO tolera 5V en ningún pin. Máximo absoluto 4.0V. Usar level shifters obligatoriamente con periféricos de 5V.
- **FPU (Floating Point Unit)**: Hardware de punto flotante. Operaciones float/double son rápidas sin emulación por software. Ideal para cálculos matemáticos, DSP, control PID.
- **USB nativo funcional**: A diferencia del Blue Pill, el Black Pill tiene USB que funciona correctamente de fábrica. Puede actuar como CDC (serial), HID (teclado/mouse), MSC (pendrive).
- **Variante F411CE superior**: Existe versión con STM32F411CEU6: 100MHz, 128KB RAM, 512KB flash. Pin-compatible. Considerar para proyectos que necesitan más recursos.
- **DFU bootloader integrado**: Se puede programar por USB sin ST-Link. Mantener BOOT0 HIGH al reset para entrar en modo DFU.
- **Bajo consumo versátil**: Múltiples modos de bajo consumo (Sleep, Stop, Standby). Stop mode a 1µA con RTC activo.

## platformio.ini de referencia

```ini
[env:blackpill]
platform = ststm32
board = blackpill_f401cc
framework = arduino
monitor_speed = 115200
upload_protocol = dfu
; Alternativa con ST-Link:
; upload_protocol = stlink
; debug_tool = stlink
build_flags =
    -DUSBD_USE_CDC
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [STM32F401CC Datasheet](https://www.st.com/resource/en/datasheet/stm32f401cc.pdf)
- [WeAct Black Pill Wiki](https://github.com/WeActStudio/WeActStudio.MiniSTM32F4x1)
- [STM32F411CE (variante superior)](https://www.st.com/resource/en/datasheet/stm32f411ce.pdf)

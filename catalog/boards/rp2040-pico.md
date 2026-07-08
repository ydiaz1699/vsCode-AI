---
id: "rp2040-pico"
name: "Raspberry Pi Pico (RP2040)"
mcu: "RP2040"
architecture: "ARM Cortex-M0+"
cores: 2
clock_mhz: 133
ram_kb: 264
flash_mb: 2
voltage_logic: 3.3
voltage_vin: "5V (USB) / VSYS 1.8-5.5V"
gpio_total: 26
gpio_restricted: []
gpio_input_only: []
adc_bits: 12
adc_channels: 4
dac_channels: 0
pwm_channels: 16
wifi: false
bluetooth: false
bluetooth_version: ""
usb_native: true
uart_chip: ""
platform: "raspberrypi"
board: "pico"
framework: "arduino"
monitor_speed: 115200
current_active_ma: 90
current_sleep_ua: 2
price_tier: "$"
---

# Raspberry Pi Pico (RP2040)

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| MCU | RP2040 |
| Arquitectura | ARM Cortex-M0+ (dual-core) |
| Núcleos | 2 |
| Frecuencia | 133 MHz (overclockable a 250+MHz) |
| RAM | 264 KB SRAM (6 bancos independientes) |
| Flash | 2 MB (externo QSPI, W25Q16) |
| Voltaje Lógico | 3.3V |
| Voltaje Alimentación | 5V USB / VSYS 1.8-5.5V |

## Conectividad

- WiFi: No disponible (ver Pico W para WiFi)
- Bluetooth: No disponible (ver Pico W para BT)
- USB: Nativo USB 1.1 (device + host)
- UART: 2x UART hardware
- Programación: USB (UF2 drag-and-drop) / SWD

## Mapeo de Pines

| Función | Pines |
|---------|-------|
| GPIO Totales | 26 (GP0-GP25 en header, GP25=LED) |
| GPIO Restringidos | GP23 (SMPS), GP24 (VBUS sense), GP25 (LED), GP29 (VSYS/3 ADC) |
| Solo Entrada | Ninguno |
| ADC (4 canales) | GP26(ADC0), GP27(ADC1), GP28(ADC2), GP29(ADC3 interno) |
| DAC | No disponible (usar PWM+filtro) |
| PWM (16 canales) | 8 slices x 2 canales, cualquier GPIO |
| I2C | I2C0: SDA=GP4, SCL=GP5 / I2C1: SDA=GP6, SCL=GP7 |
| SPI | SPI0: SCK=GP18, MOSI=GP19, MISO=GP16, CS=GP17 / SPI1: SCK=GP10, MOSI=GP11, MISO=GP12, CS=GP13 |
| UART | UART0: TX=GP0, RX=GP1 / UART1: TX=GP4, RX=GP5 |
| PIO | 2x PIO con 4 state machines cada uno (8 total) |

## Niveles de Voltaje

- Lógica: 3.3V
- Entrada máxima: 3.63V
- Tolerancia 5V: **NO** - Necesita level shifter para señales de 5V

## Consideraciones Críticas

- **PIO (Programmable I/O)**: Característica ÚNICA del RP2040. 2 bloques PIO con 4 state machines cada uno permiten implementar protocolos por hardware: WS2812 (NeoPixel), VGA, I2S, protocolos custom. Ejecutan a frecuencia del sistema sin cargar CPU.
- **Dual-core real**: Ambos cores ejecutan código independientemente. Usar `setup1()`/`loop1()` en Arduino framework o `multicore_launch_core1()` en SDK. Comunicación vía FIFO o spinlocks.
- **Flash externo (QSPI)**: El flash está fuera del chip. Se puede reemplazar por chips más grandes (4/8/16MB) soldando otro W25Qxx. XIP (Execute In Place) directo.
- **UF2 drag-and-drop**: Programar manteniendo BOOTSEL al conectar USB. Aparece como pendrive, arrastrar archivo .uf2. No necesita drivers ni programador externo.
- **Overclock estable**: Frecuentemente se overclocka a 250MHz sin problemas. Algunos llegan a 400MHz+ con refrigeración. La RAM funciona a frecuencia del sistema.
- **Sin WiFi/BT en Pico básico**: La versión sin W no tiene conectividad inalámbrica. Para WiFi/BT usar Pico W (CYW43439). PlatformIO: `board = rpipicow`.

## platformio.ini de referencia

```ini
[env:pico]
platform = raspberrypi
board = pico
framework = arduino
monitor_speed = 115200
upload_protocol = picotool
; Para Pico W con WiFi:
; board = rpipicow
; build_flags = -DPICO_CYW43_SUPPORTED=1
```

## Proyectos que usan esta placa

- (Sin proyectos registrados)

## Referencias

- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [Raspberry Pi Pico Pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
- [PIO Programming Guide](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf#section_pio)
- [Pico SDK Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

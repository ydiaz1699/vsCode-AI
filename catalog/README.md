# 📦 Catálogo de Hardware

Índice centralizado de placas, periféricos y entornos disponibles para proyectos de firmware embebido.

---

## Placas

| ID | Nombre | MCU | WiFi | BT | Voltaje | Precio Aprox. |
|----|--------|-----|------|-----|---------|---------------|
| [board-esp32-devkit-v1](boards/esp32-devkit-v1.md) | ESP32 DevKit V1 | ESP32-WROOM-32 | ✅ | ✅ BLE 4.2 | 3.3V | ~$4 USD |
| [board-esp32-s3-devkit](boards/esp32-s3-devkit.md) | ESP32-S3 DevKitC | ESP32-S3-WROOM-1 | ✅ | ✅ BLE 5.0 | 3.3V | ~$7 USD |
| [board-esp32-c3-mini](boards/esp32-c3-mini.md) | ESP32-C3 Mini | ESP32-C3 RISC-V | ✅ | ✅ BLE 5.0 | 3.3V | ~$3 USD |
| [board-esp8266-nodemcu](boards/esp8266-nodemcu.md) | NodeMCU ESP8266 | ESP8266EX | ✅ | ❌ | 3.3V | ~$3 USD |
| [board-arduino-uno-r3](boards/arduino-uno-r3.md) | Arduino UNO R3 | ATmega328P | ❌ | ❌ | 5V | ~$12 USD |
| [board-arduino-nano](boards/arduino-nano.md) | Arduino Nano | ATmega328P | ❌ | ❌ | 5V | ~$5 USD |
| [board-arduino-mega](boards/arduino-mega.md) | Arduino Mega 2560 | ATmega2560 | ❌ | ❌ | 5V | ~$15 USD |
| [board-stm32-bluepill](boards/stm32-bluepill.md) | STM32 Blue Pill | STM32F103C8T6 | ❌ | ❌ | 3.3V | ~$3 USD |
| [board-raspberry-pico](boards/raspberry-pico.md) | Raspberry Pi Pico | RP2040 | ❌ | ❌ | 3.3V | ~$4 USD |
| [board-raspberry-pico-w](boards/raspberry-pico-w.md) | Raspberry Pi Pico W | RP2040 + CYW43439 | ✅ | ✅ BLE 5.2 | 3.3V | ~$6 USD |
| [board-esp32-wroom-32e](boards/esp32-wroom-32e.md) | ESP32-WROOM-32E | ESP32-D0WD-V3 | ✅ | ✅ BLE 4.2 | 3.3V | ~$4 USD |
| [board-teensy-41](boards/teensy-41.md) | Teensy 4.1 | IMXRT1062 ARM Cortex-M7 | ❌ | ❌ | 3.3V | ~$30 USD |

## Periféricos

| ID | Nombre | Protocolo | Voltaje | Categoría |
|----|--------|-----------|---------|-----------|
| [periph-dht22](peripherals/dht22.md) | DHT22 | OneWire | 3.3–5V | Sensor Temperatura/Humedad |
| [periph-bme280](peripherals/bme280.md) | BME280 | I2C / SPI | 3.3V | Sensor Ambiental |
| [periph-mpu6050](peripherals/mpu6050.md) | MPU6050 | I2C | 3.3V | IMU / Acelerómetro |
| [periph-relay-4ch](peripherals/relay-4ch.md) | Módulo Relay 4CH | GPIO | 5V (señal 3.3V) | Actuador |
| [periph-oled-ssd1306](peripherals/oled-ssd1306.md) | OLED SSD1306 128x64 | I2C / SPI | 3.3V | Display |
| [periph-servo-sg90](peripherals/servo-sg90.md) | Servo SG90 | PWM | 5V (señal 3.3V) | Actuador |
| [periph-hcsr04](peripherals/hcsr04.md) | HC-SR04 | GPIO (Trigger/Echo) | 5V | Sensor Distancia |
| [periph-nrf24l01](peripherals/nrf24l01.md) | NRF24L01+ | SPI | 3.3V | Comunicación RF |

## Entornos

Los entornos definen la configuración base de compilación y herramientas:

| Directorio | Descripción |
|------------|-------------|
| [`environments/platformio/`](environments/platformio/) | Configuraciones para PlatformIO (ESP32, Arduino, STM32) |
| [`environments/arduino-ide/`](environments/arduino-ide/) | Configuraciones para Arduino IDE 2.x |
| [`environments/esphome/`](environments/esphome/) | Configuraciones para ESPHome (YAML-based) |

---

## Cómo Usar

### Referenciar una placa en tu proyecto

En tu archivo `.ai/HARDWARE.md`, referencia la placa así:

```markdown
## Placa Principal
- **Referencia:** [board-esp32-devkit-v1](../../catalog/boards/esp32-devkit-v1.md)
- **Justificación:** WiFi integrado, suficiente GPIO para el proyecto.
```

### Referenciar un periférico

```markdown
## Periféricos
| Componente | Referencia | Cantidad |
|------------|-----------|----------|
| Sensor Temperatura | [periph-dht22](../../catalog/peripherals/dht22.md) | 1 |
| Display | [periph-oled-ssd1306](../../catalog/peripherals/oled-ssd1306.md) | 1 |
```

### Verificar compatibilidad de voltaje

Antes de conectar, verifica en la tabla que los voltajes sean compatibles. Si la placa es 3.3V y el periférico requiere 5V, necesitas un level shifter.

### Agregar nuevos componentes

Consulta las guías:
- [`docs/how-to-add-board.md`](../docs/how-to-add-board.md)
- [`docs/how-to-add-peripheral.md`](../docs/how-to-add-peripheral.md)

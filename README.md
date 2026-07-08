# vsCode-AI

> Framework de Context Engineering para Firmware Embebido

## El Problema

Cuando usamos asistentes de IA para desarrollar firmware embebido, enfrentamos tres problemas recurrentes:

1. **Repetición** — Cada nuevo proyecto requiere explicar desde cero la arquitectura, el hardware, las restricciones del microcontrolador y las convenciones del equipo.
2. **Duplicación** — Copiamos y pegamos archivos de contexto entre proyectos sin un estándar, generando versiones inconsistentes y desactualizadas.
3. **Improvisación** — Sin una estructura definida, cada interacción con la IA produce resultados impredecibles: código sin estilo consistente, configuraciones incompletas y documentación fragmentada.

## La Solución

vsCode-AI propone un **catálogo centralizado** de hardware, periféricos, templates y guías que alimentan un generador automático de proyectos. El resultado: proyectos PlatformIO completos con contexto embebido para IA desde el primer commit.

### Estructura del Framework

```
vsCode-AI/
├── catalog/                  # Catálogo centralizado de conocimiento
│   ├── boards/               # Fichas técnicas de placas (frontmatter YAML)
│   ├── peripherals/          # Fichas de periféricos y sensores
│   └── environments/         # Configuraciones de entorno (VSCode, tooling)
├── templates/                # Plantillas base para generación
│   └── _base/                # Templates con variables {{PLACEHOLDER}}
├── guides/                   # Guías de mejores prácticas
├── prompts/                  # Prompts reutilizables para IA
├── generator.py              # Motor de generación v3
├── examples/                 # Proyectos de ejemplo generados
├── docs/                     # Documentación del framework
├── requirements.txt          # Dependencias Python
└── README.md                 # Este archivo
```

## Quick Start

### Opción 1: Generator CLI (Recomendado)

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ver placas disponibles
python generator.py list-boards

# Ver periféricos disponibles
python generator.py list-peripherals

# Generar proyecto nuevo
python generator.py new --board esp32-devkit --name mi-proyecto --peripheral dht22

# Agregar periférico a proyecto existente
python generator.py add-peripheral --project ./mi-proyecto --peripheral relay-4ch
```

### Opción 2: Prompt + IA

1. Copia el contenido de `prompts/new-project.md` en tu asistente de IA
2. Responde las preguntas del prompt (placa, periféricos, descripción)
3. La IA generará la estructura completa usando el catálogo como referencia

### Opción 3: Copia Manual

1. Copia `templates/_base/` a tu nuevo proyecto
2. Reemplaza las variables `{{PLACEHOLDER}}` con tus datos
3. Agrega las fichas de hardware relevantes de `catalog/boards/`

## Estructura de un Proyecto Generado

```
mi-proyecto/
├── .ai/                      # Contexto para asistentes de IA
│   ├── PROJECT_CONTEXT.md    # Descripción general del proyecto
│   ├── ARCHITECTURE.md       # Arquitectura del sistema
│   ├── HARDWARE.md           # Hardware utilizado (de catálogo)
│   ├── PROTOCOL.md           # Reglas de interacción con IA
│   ├── CODING_STYLE.md       # Convenciones de código
│   └── TASKS.md              # Tareas pendientes
├── docs/                     # Documentación del proyecto
│   └── PINOUT.md             # Diagrama de conexiones
├── src/                      # Código fuente
│   └── main.cpp              # Punto de entrada
├── include/                  # Headers
│   └── secrets.h.template    # Template de credenciales
├── lib/                      # Librerías locales
├── test/                     # Tests unitarios
├── .vscode/                  # Configuración del editor
│   ├── extensions.json       # Extensiones recomendadas
│   └── settings.json         # Configuración PlatformIO
├── platformio.ini            # Configuración de PlatformIO
└── README.md                 # Documentación del proyecto
```

## Arquitectura

El framework opera en **3 capas**:

### Capa 1: Catálogo (Conocimiento)

Almacena el conocimiento reutilizable en archivos Markdown con frontmatter YAML:

- **Boards** — Especificaciones técnicas, pines, capacidades WiFi/BT, precios
- **Peripherals** — Protocolos, categorías, librerías recomendadas, conexiones
- **Environments** — Configuraciones de IDE y herramientas

### Capa 2: Generación (Motor)

`generator.py` lee el catálogo, procesa templates y produce proyectos completos:

- Parsea frontmatter YAML con `python-frontmatter`
- Inyecta variables en plantillas (`{{PROJECT_NAME}}`, `{{BOARD_ID}}`, etc.)
- Genera `platformio.ini` con configuración específica por placa
- Copia configuraciones de entorno

### Capa 3: Proyecto (Salida)

El proyecto generado es autónomo y contiene todo el contexto necesario para que cualquier asistente de IA entienda:

- Qué hardware se usa y sus restricciones
- Qué arquitectura seguir
- Qué estilo de código aplicar
- Qué tareas están pendientes

## Placas Soportadas

| ID | Nombre | MCU | WiFi | BT | Flash | RAM | Precio |
|----|--------|-----|------|----|-------|-----|--------|
| `esp32-devkit` | ESP32 DevKit v1 | ESP32 | ✅ | ✅ | 4MB | 520KB | ~$8 |
| `esp32-s3` | ESP32-S3 DevKit | ESP32-S3 | ✅ | ✅ | 8MB | 512KB | ~$12 |
| `esp32-c3` | ESP32-C3 Mini | ESP32-C3 | ✅ | ✅ | 4MB | 400KB | ~$5 |
| `esp32-cam` | ESP32-CAM AI-Thinker | ESP32 | ✅ | ✅ | 4MB | 520KB | ~$10 |
| `esp8266-d1mini` | Wemos D1 Mini | ESP8266 | ✅ | ❌ | 4MB | 80KB | ~$4 |
| `esp8266-nodemcu` | NodeMCU v3 | ESP8266 | ✅ | ❌ | 4MB | 80KB | ~$5 |
| `arduino-uno` | Arduino Uno R3 | ATmega328P | ❌ | ❌ | 32KB | 2KB | ~$12 |
| `arduino-mega` | Arduino Mega 2560 | ATmega2560 | ❌ | ❌ | 256KB | 8KB | ~$15 |
| `arduino-nano` | Arduino Nano | ATmega328P | ❌ | ❌ | 32KB | 2KB | ~$6 |
| `stm32-bluepill` | STM32 Blue Pill | STM32F103C8 | ❌ | ❌ | 64KB | 20KB | ~$4 |
| `rp2040-pico` | Raspberry Pi Pico | RP2040 | ❌ | ❌ | 2MB | 264KB | ~$4 |
| `rp2040-pico-w` | Raspberry Pi Pico W | RP2040 | ✅ | ✅ | 2MB | 264KB | ~$6 |

## Periféricos Soportados

| ID | Nombre | Protocolo | Categoría | Librería |
|----|--------|-----------|-----------|----------|
| `dht22` | DHT22 / AM2302 | OneWire | Sensor - Temperatura/Humedad | DHT sensor library |
| `bme280` | BME280 | I2C/SPI | Sensor - Ambiental | Adafruit BME280 |
| `relay-4ch` | Módulo Relay 4 Canales | GPIO | Actuador - Potencia | (nativo) |
| `oled-ssd1306` | Display OLED 0.96" | I2C | Display | Adafruit SSD1306 |
| `neopixel-strip` | Tira LED WS2812B | OneWire | LED - Direccionable | Adafruit NeoPixel |
| `servo-sg90` | Micro Servo SG90 | PWM | Actuador - Movimiento | ESP32Servo |
| `ultrasonic-hcsr04` | HC-SR04 Ultrasónico | GPIO | Sensor - Distancia | NewPing |
| `rfid-rc522` | Lector RFID RC522 | SPI | Comunicación - RFID | MFRC522 |

## Requisitos

- **Python** 3.8+
- **python-frontmatter** >= 1.0.0 (lectura de YAML frontmatter)
- **PyYAML** >= 6.0 (parsing YAML)
- **PlatformIO CLI** (opcional, para compilar proyectos generados)

```bash
# Instalar dependencias del generador
pip install -r requirements.txt

# Verificar PlatformIO (opcional)
pio --version
```

## Contribuir

1. Fork del repositorio
2. Crea tu feature branch (`git checkout -b feature/nueva-placa`)
3. Agrega la ficha en `catalog/boards/` o `catalog/peripherals/`
4. Actualiza los templates si es necesario
5. Ejecuta el generador para verificar
6. Commit y Pull Request

### Agregar una nueva placa

Crea un archivo en `catalog/boards/mi-placa.md`:

```markdown
---
id: mi-placa
name: "Mi Placa Custom"
mcu: "ESP32"
platform: espressif32
board: esp32dev
framework: arduino
wifi: true
bluetooth: true
flash: "4MB"
ram: "520KB"
price: "$10"
pins:
  gpio: 34
  adc: 18
  pwm: 16
  i2c: 2
  spi: 3
  uart: 3
---

# Mi Placa Custom

Descripción técnica de la placa...
```

## Licencia

MIT License — ver [LICENSE](LICENSE)

## Créditos

- **Autor**: @ydiaz1699
- **Evolución de**: [Context_Engineering_V2](../Context_Engineering_V2/) — Framework genérico de context engineering
- **Inspirado en**: Las mejores prácticas de documentación para asistentes de IA en proyectos embebidos

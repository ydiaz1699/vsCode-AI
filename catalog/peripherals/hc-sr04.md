---
id: "hc-sr04"
name: "HC-SR04"
category: "sensor"
protocol: "Digital"
voltage_min: 5.0
voltage_max: 5.0
voltage_logic: "5V"
pins_required: [TRIG, ECHO]
i2c_address: ""
library: ""
library_version: ""
level_shifter_needed: true
current_ma: 15
datasheet_url: "https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf"
---

# HC-SR04 — Sensor Ultrasónico

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje | 5V (único) |
| Protocolo | Digital (pulso) |
| Corriente | 15 mA |
| Level Shifter | **SÍ** (ECHO es salida 5V) |
| Rango | 2 – 400 cm |
| Ángulo | ~15° |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| VCC | Alimentación | 5V obligatorio |
| TRIG | Disparo | Pulso 10µs HIGH |
| ECHO | Respuesta | **Salida 5V** — peligro para MCU 3.3V |
| GND | Tierra | — |

## Conexión por Plataforma

### ESP32 ⚠️ REQUIERE DIVISOR

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| VCC | 5V (VIN) | — |
| TRIG | GPIO5 | Directo (3.3V acepta como HIGH) |
| ECHO | GPIO18 | **Divisor resistivo 1kΩ/2kΩ** |
| GND | GND | — |

> Divisor: ECHO → 1kΩ → GPIO18 → 2kΩ → GND (resultado ≈ 3.3V)

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| VCC | 5V | — |
| TRIG | D9 | — |
| ECHO | D10 | Directo (5V lógica) |
| GND | GND | — |

## Consideraciones Críticas

- 🚨 **ECHO puede DAÑAR GPIO 3.3V** — NUNCA conectar directo a ESP32
- Usar divisor resistivo 1kΩ + 2kΩ o level shifter bidireccional
- Mínima distancia fiable: 2 cm
- Superficies absorbentes (tela, espuma) dan lecturas erróneas
- Pulso TRIG: exactamente 10µs

## Código de Ejemplo Mínimo

```cpp
#define TRIG_PIN 5
#define ECHO_PIN 18

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  float distance = duration * 0.034 / 2.0;

  Serial.printf("Distancia: %.1f cm\n", distance);
  delay(100);
}
```

## platformio.ini

```ini
lib_deps =
    ; No requiere librería externa
```

## Compatibilidad con Placas del Catálogo

| Placa | Compatible | Notas |
|-------|-----------|-------|
| ESP32 DevKit | ⚠️ | Requiere divisor en ECHO |
| Arduino UNO | ✅ | Conexión directa |
| Arduino Nano | ✅ | Conexión directa |

## Referencias

- [Datasheet HC-SR04](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)
- [Tutorial ESP32 con divisor](https://randomnerdtutorials.com/esp32-hc-sr04-ultrasonic-arduino/)

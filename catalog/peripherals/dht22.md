---
id: "dht22"
name: "DHT22/AM2302"
category: "sensor"
protocol: "1-Wire"
voltage_min: 3.3
voltage_max: 5.5
voltage_logic: "3.3-5V"
pins_required: [DATA]
i2c_address: ""
library: "adafruit/DHT sensor library"
library_version: "^1.4.4"
level_shifter_needed: false
current_ma: 1.5
datasheet_url: "https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf"
---

# DHT22 / AM2302

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje | 3.3 – 5.5V |
| Protocolo | 1-Wire (propietario) |
| Corriente | 1.5 mA (máx 2.5 mA) |
| Level Shifter | No necesario |
| Rango Temp | -40 a 80°C ±0.5°C |
| Rango Hum | 0-100% ±2-5% |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| 1 (VCC) | Alimentación | 3.3-5.5V |
| 2 (DATA) | Datos | Pull-up 10kΩ obligatorio |
| 3 (NC) | No conectar | — |
| 4 (GND) | Tierra | — |

## Conexión por Plataforma

### ESP32

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| VCC | 3.3V | — |
| DATA | GPIO4 | Pull-up 10kΩ a VCC |
| GND | GND | — |

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| VCC | 5V | — |
| DATA | D2 | Pull-up 10kΩ a VCC |
| GND | GND | — |

## Consideraciones Críticas

- ⚠️ **Pull-up 10kΩ OBLIGATORIO** en línea DATA a VCC
- ⚠️ Intervalo mínimo entre lecturas: **2 segundos**
- ⚠️ La **primera lectura suele fallar** — descartarla o reintentar
- Cables largos (>1m) requieren pull-up más bajo (~4.7kΩ)

## Código de Ejemplo Mínimo

```cpp
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  delay(2000); // Esperar estabilización
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
    Serial.println("Error lectura DHT22");
    return;
  }
  Serial.printf("Temp: %.1f°C  Hum: %.1f%%\n", t, h);
  delay(2000);
}
```

## platformio.ini

```ini
lib_deps =
    adafruit/DHT sensor library@^1.4.4
    adafruit/Adafruit Unified Sensor@^1.1.9
```

## Compatibilidad con Placas del Catálogo

| Placa | Compatible | Notas |
|-------|-----------|-------|
| ESP32 DevKit | ✅ | 3.3V, funciona directo |
| Arduino UNO | ✅ | 5V, funciona directo |
| Arduino Nano | ✅ | 5V, funciona directo |

## Referencias

- [Datasheet DHT22](https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf)
- [Adafruit DHT Library](https://github.com/adafruit/DHT-sensor-library)

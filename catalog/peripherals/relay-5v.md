---
id: "relay-5v"
name: "Módulo Relé 5V"
category: "actuator"
protocol: "Digital"
voltage_min: 3.3
voltage_max: 5.0
voltage_logic: "3.3-5V"
pins_required: [IN]
i2c_address: ""
library: ""
library_version: ""
level_shifter_needed: false
current_ma: 75
datasheet_url: "https://www.songle.com/en/pdf/SRD.pdf"
---

# Módulo Relé 5V

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje señal | 3.3 – 5V |
| Protocolo | Digital |
| Corriente bobina | ~75 mA por canal |
| Level Shifter | No necesario |
| Carga máxima | 10A @ 250VAC / 10A @ 30VDC |
| Activación | **Active LOW** (mayoría) |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| VCC | Alimentación | 5V (bobina) |
| GND | Tierra | — |
| IN | Señal control | Active LOW en mayoría |
| COM | Común (carga) | — |
| NO | Normalmente Abierto | Conectado al encender |
| NC | Normalmente Cerrado | Conectado al apagar |

## Conexión por Plataforma

### ESP32

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| VCC | 5V (VIN) | No usar 3.3V |
| GND | GND | — |
| IN | GPIO26 | 3.3V activa la mayoría |

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| VCC | 5V | — |
| GND | GND | — |
| IN | D7 | — |

## Consideraciones Críticas

- ⚠️ La **MAYORÍA** de módulos son **Active LOW** (LOW = relé activado)
- ⚠️ **Verificar con LED** antes de conectar carga real
- 🚨 **NUNCA tocar terminales** COM/NO/NC con carga AC conectada
- 🚨 Usar **fusible** en línea de carga AC siempre
- ESP32 GPIO da 3.3V — suficiente para activar la mayoría de módulos con optoacoplador
- No alimentar relé desde pin 3.3V del MCU (insuficiente corriente)
- Para múltiples relés: alimentación externa 5V recomendada

## Código de Ejemplo Mínimo

```cpp
#define RELAY_PIN 26

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH); // Relé OFF (Active LOW)
  Serial.begin(115200);
}

void loop() {
  Serial.println("Relé ON");
  digitalWrite(RELAY_PIN, LOW);  // Active LOW = encender
  delay(2000);
  
  Serial.println("Relé OFF");
  digitalWrite(RELAY_PIN, HIGH); // HIGH = apagar
  delay(2000);
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
| ESP32 DevKit | ✅ | 3.3V activa módulos con optoacoplador |
| Arduino UNO | ✅ | 5V directo |
| Arduino Nano | ✅ | 5V directo |

## Referencias

- [Datasheet Relé SRD](https://www.songle.com/en/pdf/SRD.pdf)
- [Guía seguridad relés](https://randomnerdtutorials.com/guide-for-relay-module-with-arduino/)

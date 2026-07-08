---
id: "rf433-rcswitch"
name: "RF 433MHz (RC-Switch)"
category: "communication"
protocol: "Digital/INT"
voltage_min: 3.0
voltage_max: 12.0
voltage_logic: "5V (RX output)"
pins_required: [DATA]
i2c_address: ""
library: "sui77/rc-switch"
library_version: "^2.6.4"
level_shifter_needed: true
current_ma: 34
datasheet_url: "https://www.sparkfun.com/datasheets/RF/KLP_Walkthrough.pdf"
---

# RF 433MHz — TX/RX con RC-Switch

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje TX | 3 – 12V (más V = más alcance) |
| Voltaje RX | 5V |
| Protocolo | Digital con interrupciones |
| Corriente TX | ~34 mA |
| Level Shifter | **SÍ** (RX output es 5V) |
| Frecuencia | 433.92 MHz |
| Modulación | ASK/OOK |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| TX VCC | Alimentación TX | 3-12V |
| TX DATA | Datos transmisión | — |
| TX GND | Tierra | — |
| RX VCC | Alimentación RX | 5V |
| RX DATA | Datos recepción | **Salida 5V** |
| RX GND | Tierra | — |

## Conexión por Plataforma

### ESP32

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| TX VCC | 5V (VIN) | Más voltaje = más alcance |
| TX DATA | GPIO4 | Directo OK |
| TX GND | GND | — |
| RX VCC | 5V (VIN) | — |
| RX DATA | GPIO2 | **Divisor 1kΩ/2kΩ** |
| RX GND | GND | — |

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| TX VCC | 5V | — |
| TX DATA | D10 | — |
| TX GND | GND | — |
| RX VCC | 5V | — |
| RX DATA | D2 | **INT0 obligatorio** |
| RX GND | GND | — |

## Consideraciones Críticas

- ⚠️ **Pin de interrupción OBLIGATORIO** para recepción (Arduino: D2=INT0, D3=INT1)
- ⚠️ RX output es 5V — usar divisor para ESP32
- 🚨 **Antena 17.3 cm** de cable soldado al pad ANT mejora rango 10x
- Sin antena: alcance <1m. Con antena: 30-100m
- TX a 12V alcanza mayor distancia pero consume más
- ESP32: cualquier GPIO con interrupción sirve para RX

## Código de Ejemplo Mínimo

```cpp
#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

// --- TRANSMISOR ---
void setup() {
  Serial.begin(115200);
  mySwitch.enableTransmit(4); // GPIO4 TX
  // mySwitch.enableReceive(digitalPinToInterrupt(2)); // Para RX
}

void loop() {
  mySwitch.send(123456, 24); // Enviar código 24-bit
  Serial.println("Enviado: 123456");
  delay(2000);
}

// --- RECEPTOR (descomentar y comentar TX) ---
// void loop() {
//   if (mySwitch.available()) {
//     Serial.printf("Recibido: %ld\n", mySwitch.getReceivedValue());
//     mySwitch.resetAvailable();
//   }
// }
```

## platformio.ini

```ini
lib_deps =
    sui77/rc-switch@^2.6.4
```

## Compatibilidad con Placas del Catálogo

| Placa | Compatible | Notas |
|-------|-----------|-------|
| ESP32 DevKit | ⚠️ | Divisor en RX DATA |
| Arduino UNO | ✅ | RX en D2 (INT0) |
| Arduino Nano | ✅ | RX en D2 (INT0) |

## Referencias

- [RC-Switch Library](https://github.com/sui77/rc-switch)
- [Tutorial 433MHz](https://randomnerdtutorials.com/rf-433mhz-transmitter-receiver-module-with-arduino/)

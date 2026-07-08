---
id: "rc522-rfid"
name: "MFRC522"
category: "rfid"
protocol: "SPI"
voltage_min: 3.3
voltage_max: 3.3
voltage_logic: "3.3V"
pins_required: [SDA/CS, SCK, MOSI, MISO, RST]
i2c_address: ""
library: "miguelbalboa/MFRC522"
library_version: "^1.4.10"
level_shifter_needed: false
current_ma: 26
datasheet_url: "https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf"
---

# MFRC522 — Lector RFID

## Resumen

| Parámetro | Valor |
|-----------|-------|
| Voltaje | **3.3V SOLAMENTE** |
| Protocolo | SPI |
| Corriente | 26 mA |
| Level Shifter | No (opera a 3.3V) |
| Frecuencia | 13.56 MHz |
| Tarjetas | MIFARE 1K, 4K, Ultralight |

## Pines

| Pin | Función | Notas |
|-----|---------|-------|
| VCC | Alimentación | 3.3V SOLO |
| GND | Tierra | — |
| RST | Reset | — |
| SDA (SS) | Chip Select SPI | — |
| SCK | Clock SPI | — |
| MOSI | Master Out | — |
| MISO | Master In | — |
| IRQ | Interrupción | Opcional, no usado normalmente |

## Conexión por Plataforma

### ESP32

| Pin Módulo | GPIO ESP32 | Notas |
|------------|-----------|-------|
| VCC | 3.3V | NUNCA 5V |
| GND | GND | — |
| RST | GPIO27 | — |
| SDA/SS | GPIO5 | — |
| SCK | GPIO18 | VSPI default |
| MOSI | GPIO23 | VSPI default |
| MISO | GPIO19 | VSPI default |

### Arduino UNO

| Pin Módulo | Pin Arduino | Notas |
|------------|-------------|-------|
| VCC | 3.3V | NUNCA usar 5V |
| GND | GND | — |
| RST | D9 | — |
| SDA/SS | D10 | — |
| SCK | D13 | — |
| MOSI | D11 | — |
| MISO | D12 | — |

## Consideraciones Críticas

- 🚨 **NUNCA alimentar con 5V** — destruye el chip inmediatamente
- Arduino UNO: usar pin 3.3V (máx 50mA, suficiente para RC522)
- Pines SPI son tolerantes a 5V en datos pero VCC DEBE ser 3.3V
- Distancia de lectura: 2-5 cm (depende de antena y tarjeta)
- Si no lee: verificar soldadura del pin header y distancia

## Código de Ejemplo Mínimo

```cpp
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5
#define RST_PIN 27

MFRC522 rfid(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(115200);
  SPI.begin();
  rfid.PCD_Init();
  Serial.println("Acerque tarjeta...");
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
    return;

  Serial.print("UID:");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.printf(" %02X", rfid.uid.uidByte[i]);
  }
  Serial.println();
  rfid.PICC_HaltA();
}
```

## platformio.ini

```ini
lib_deps =
    miguelbalboa/MFRC522@^1.4.10
```

## Compatibilidad con Placas del Catálogo

| Placa | Compatible | Notas |
|-------|-----------|-------|
| ESP32 DevKit | ✅ | 3.3V nativo, ideal |
| Arduino UNO | ✅ | Usar pin 3.3V para VCC |
| Arduino Nano | ✅ | Usar pin 3.3V para VCC |

## Referencias

- [Datasheet MFRC522](https://www.nxp.com/docs/en/data-sheet/MFRC522.pdf)
- [Library MFRC522](https://github.com/miguelbalboa/rfid)

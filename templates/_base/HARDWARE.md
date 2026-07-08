---
template: hardware
version: "1.0"
required: true
condition: "Siempre si el proyecto involucra hardware físico"
description: "Documentación de hardware, conexiones y consumo energético"
---

# {{PROJECT_NAME}} — Hardware

## Referencias

### Placa Principal

- **Componente:** {{BOARD_NAME}}
- **Referencia:** [{{BOARD_ID}}](../../catalog/boards/{{BOARD_FILE}})
- **Voltaje lógico:** {{BOARD_VOLTAGE}}
- **Frecuencia:** {{BOARD_FREQUENCY}}

### Periféricos

| Componente | Referencia | Cantidad | Protocolo |
|------------|-----------|----------|-----------|
| {{PERIPHERAL_1_NAME}} | [{{PERIPHERAL_1_ID}}](../../catalog/peripherals/{{PERIPHERAL_1_FILE}}) | {{PERIPHERAL_1_QTY}} | {{PERIPHERAL_1_PROTOCOL}} |
| {{PERIPHERAL_2_NAME}} | [{{PERIPHERAL_2_ID}}](../../catalog/peripherals/{{PERIPHERAL_2_FILE}}) | {{PERIPHERAL_2_QTY}} | {{PERIPHERAL_2_PROTOCOL}} |
| {{PERIPHERAL_3_NAME}} | [{{PERIPHERAL_3_ID}}](../../catalog/peripherals/{{PERIPHERAL_3_FILE}}) | {{PERIPHERAL_3_QTY}} | {{PERIPHERAL_3_PROTOCOL}} |

## Tabla de Conexiones (Wiring)

| Periférico | Pin Periférico | Pin Placa | Función | Notas |
|------------|---------------|-----------|---------|-------|
| {{PERIPHERAL_1_NAME}} | VCC | {{P1_VCC_PIN}} | Alimentación | {{P1_VCC_NOTES}} |
| {{PERIPHERAL_1_NAME}} | GND | GND | Tierra | — |
| {{PERIPHERAL_1_NAME}} | {{P1_SIGNAL_PIN}} | GPIO{{P1_GPIO}} | {{P1_FUNCTION}} | {{P1_SIGNAL_NOTES}} |
| {{PERIPHERAL_2_NAME}} | VCC | {{P2_VCC_PIN}} | Alimentación | {{P2_VCC_NOTES}} |
| {{PERIPHERAL_2_NAME}} | GND | GND | Tierra | — |
| {{PERIPHERAL_2_NAME}} | SDA | GPIO{{P2_SDA}} | I2C Data | {{P2_SDA_NOTES}} |
| {{PERIPHERAL_2_NAME}} | SCL | GPIO{{P2_SCL}} | I2C Clock | {{P2_SCL_NOTES}} |

## Consumo Energético

| Estado | Corriente Estimada | Duración Típica | Notas |
|--------|-------------------|-----------------|-------|
| Deep Sleep | {{DEEP_SLEEP_CURRENT}} | {{DEEP_SLEEP_DURATION}} | {{DEEP_SLEEP_NOTES}} |
| Idle (WiFi conectado) | {{IDLE_CURRENT}} | {{IDLE_DURATION}} | {{IDLE_NOTES}} |
| Activo (transmitiendo) | {{ACTIVE_CURRENT}} | {{ACTIVE_DURATION}} | {{ACTIVE_NOTES}} |
| Pico máximo | {{PEAK_CURRENT}} | {{PEAK_DURATION}} | {{PEAK_NOTES}} |

**Consumo promedio estimado:** {{AVERAGE_CONSUMPTION}}

## Alimentación

- **Fuente:** {{POWER_SOURCE}}
- **Voltaje de entrada:** {{INPUT_VOLTAGE}}
- **Regulador:** {{REGULATOR}}
- **Batería (si aplica):** {{BATTERY_SPEC}}
- **Autonomía estimada:** {{ESTIMATED_AUTONOMY}}

## Advertencias

> ⚠️ **Voltaje:** {{VOLTAGE_WARNING}}

> ⚠️ **Corriente:** {{CURRENT_WARNING}}

> ⚠️ **Temperatura:** {{TEMPERATURE_WARNING}}

> ⚠️ **ESD:** {{ESD_WARNING}}

### Errores Comunes

1. {{COMMON_ERROR_1}}
2. {{COMMON_ERROR_2}}
3. {{COMMON_ERROR_3}}

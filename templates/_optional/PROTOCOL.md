---
template: protocol
version: "1.0"
required: false
condition: "Generar solo si el proyecto usa comunicación BLE, MQTT, HTTP, WebSocket, RF (NRF24, LoRa), o cualquier protocolo de red."
description: "Documentación del protocolo de comunicación"
---

> ⚠️ **Generar solo si** el proyecto usa comunicación BLE, MQTT, HTTP, WebSocket, RF (NRF24, LoRa), o cualquier protocolo de red.

# {{PROJECT_NAME}} — Protocolo de Comunicación

## Información General

| Campo | Valor |
|-------|-------|
| **Tipo** | {{PROTOCOL_TYPE}} |
| **Versión** | {{PROTOCOL_VERSION}} |
| **Transporte** | {{TRANSPORT}} |
| **Puerto/Canal** | {{PORT_CHANNEL}} |
| **Autenticación** | {{AUTH_METHOD}} |
| **Cifrado** | {{ENCRYPTION}} |
| **QoS** | {{QOS_LEVEL}} |

## Formato de Mensajes

| Campo | Tipo | Tamaño | Obligatorio | Descripción |
|-------|------|--------|-------------|-------------|
| {{FIELD_1}} | {{F1_TYPE}} | {{F1_SIZE}} | {{F1_REQUIRED}} | {{F1_DESC}} |
| {{FIELD_2}} | {{F2_TYPE}} | {{F2_SIZE}} | {{F2_REQUIRED}} | {{F2_DESC}} |
| {{FIELD_3}} | {{F3_TYPE}} | {{F3_SIZE}} | {{F3_REQUIRED}} | {{F3_DESC}} |
| {{FIELD_4}} | {{F4_TYPE}} | {{F4_SIZE}} | {{F4_REQUIRED}} | {{F4_DESC}} |
| {{FIELD_5}} | {{F5_TYPE}} | {{F5_SIZE}} | {{F5_REQUIRED}} | {{F5_DESC}} |

## Topics / Endpoints

| Topic/Endpoint | Dirección | Payload | Descripción |
|---------------|-----------|---------|-------------|
| `{{TOPIC_1}}` | {{T1_DIR}} | {{T1_PAYLOAD}} | {{T1_DESC}} |
| `{{TOPIC_2}}` | {{T2_DIR}} | {{T2_PAYLOAD}} | {{T2_DESC}} |
| `{{TOPIC_3}}` | {{T3_DIR}} | {{T3_PAYLOAD}} | {{T3_DESC}} |
| `{{TOPIC_4}}` | {{T4_DIR}} | {{T4_PAYLOAD}} | {{T4_DESC}} |

## Secuencia de Comunicación

```
┌──────────┐                    ┌──────────┐
│ {{NODE_A}}│                    │ {{NODE_B}}│
└────┬─────┘                    └────┬─────┘
     │                               │
     │──── {{SEQ_1_MSG}} ───────────▶│  (1) {{SEQ_1_DESC}}
     │                               │
     │◀─── {{SEQ_2_MSG}} ───────────│  (2) {{SEQ_2_DESC}}
     │                               │
     │──── {{SEQ_3_MSG}} ───────────▶│  (3) {{SEQ_3_DESC}}
     │                               │
     │◀─── {{SEQ_4_MSG}} ───────────│  (4) {{SEQ_4_DESC}}
     │                               │
```

## Códigos de Error

| Código | Nombre | Descripción | Acción Recomendada |
|--------|--------|-------------|-------------------|
| `{{ERR_1_CODE}}` | {{ERR_1_NAME}} | {{ERR_1_DESC}} | {{ERR_1_ACTION}} |
| `{{ERR_2_CODE}}` | {{ERR_2_NAME}} | {{ERR_2_DESC}} | {{ERR_2_ACTION}} |
| `{{ERR_3_CODE}}` | {{ERR_3_NAME}} | {{ERR_3_DESC}} | {{ERR_3_ACTION}} |
| `{{ERR_4_CODE}}` | {{ERR_4_NAME}} | {{ERR_4_DESC}} | {{ERR_4_ACTION}} |

## Ejemplo Completo

### Publicación de datos de sensor

```json
{
  "device_id": "{{DEVICE_ID}}",
  "timestamp": {{TIMESTAMP}},
  "type": "{{MSG_TYPE}}",
  "payload": {
    "{{DATA_FIELD_1}}": {{DATA_VALUE_1}},
    "{{DATA_FIELD_2}}": {{DATA_VALUE_2}},
    "{{DATA_FIELD_3}}": "{{DATA_VALUE_3}}"
  },
  "meta": {
    "rssi": {{RSSI}},
    "battery": {{BATTERY}},
    "fw_version": "{{FW_VERSION}}"
  }
}
```

### Comando de control

```json
{
  "device_id": "{{DEVICE_ID}}",
  "command": "{{COMMAND_NAME}}",
  "params": {
    "{{PARAM_1}}": {{PARAM_1_VALUE}},
    "{{PARAM_2}}": "{{PARAM_2_VALUE}}"
  },
  "request_id": "{{REQUEST_ID}}"
}
```

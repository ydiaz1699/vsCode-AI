# Guía: Generar PROTOCOL.md

## Archivo de Salida

`.ai/PROTOCOL.md`

## Cuándo Generarlo

**Solo si** el proyecto usa:
- BLE (Bluetooth Low Energy) — servicios, características, notificaciones
- MQTT — topics, payloads, QoS
- HTTP/REST — endpoints, métodos, responses
- WebSocket — mensajes bidireccionales
- RF (NRF24L01, LoRa, 433MHz) — paquetes custom
- Cualquier protocolo de comunicación entre dispositivos

## Instrucciones para la IA

1. Identificar el tipo de protocolo utilizado (MQTT, BLE, HTTP, etc.)
2. Extraer la configuración de conexión (broker, puerto, credenciales, UUIDs)
3. Documentar cada topic/endpoint/característica con su dirección y payload
4. Definir el formato de cada mensaje (JSON, binario, string)
5. Crear diagrama de secuencia ASCII mostrando el flujo de comunicación típico
6. Documentar códigos de error y sus significados
7. Incluir ejemplo completo copiable de un mensaje publicado y uno recibido
8. Si hay autenticación, documentar el flujo sin exponer credenciales
9. Documentar timeouts, reintentos y manejo de desconexión
10. Si usa JSON, documentar el schema completo de cada tipo de mensaje

## Estructura Esperada

```markdown
# [Nombre] — Protocolo de Comunicación

## Información General
| Campo | Valor |
|-------|-------|
| Tipo | MQTT/BLE/HTTP/... |

## Formato de Mensajes
| Campo | Tipo | Tamaño | Obligatorio | Descripción |
|...|...|...|...|...|

## Topics / Endpoints
| Topic/Endpoint | Dirección | Payload | Descripción |
|...|...|...|...|

## Secuencia de Comunicación
\```
[Device] ──msg──▶ [Server]
\```

## Códigos de Error
| Código | Nombre | Descripción | Acción |
|...|...|...|...|

## Ejemplo Completo
\```json
{...}
\```
```

## Reglas

- Nunca incluir credenciales reales (usar `secrets.h` references)
- Los topics MQTT usan formato jerárquico: `proyecto/dispositivo/acción`
- Los payloads JSON deben ser válidos y parseables
- Documentar QoS para cada topic MQTT (0, 1 o 2)
- Para BLE: documentar UUID de servicio y características
- Para HTTP: documentar método, headers requeridos y formato de respuesta
- Los ejemplos deben ser copiables directamente para testing (mosquitto_pub, curl, etc.)
- Incluir mínimo 3 topics/endpoints
- Los códigos de error incluyen la acción recomendada

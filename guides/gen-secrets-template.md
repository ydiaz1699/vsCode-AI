# Guía: Generar secrets.h.template

## Archivo de Salida

`secrets.h.template` (raíz del proyecto)

## Cuándo Generarlo

**Solo si** el proyecto usa WiFi, credenciales de API, tokens, o cualquier dato sensible que no debe estar en el repositorio.

## Instrucciones para la IA

1. Buscar en el código todas las constantes de credenciales (SSID, password, API keys, tokens)
2. Buscar includes de `secrets.h` o `credentials.h` en el código
3. Identificar todas las variables que se esperan en ese header
4. Crear template con valores placeholder descriptivos
5. Incluir tabla de zonas horarias comunes para configuración de NTP
6. Documentar cada campo con comentario explicativo
7. Agregar advertencia de no commitear el archivo real
8. Incluir instrucciones de cómo usar el template
9. Si hay múltiples entornos (dev/prod), documentar ambos
10. Verificar que el `.gitignore` incluya `secrets.h`

## Estructura Esperada

```cpp
// secrets.h.template
// ⚠️ COPIAR como secrets.h y llenar con valores reales
// ⚠️ NUNCA commitear secrets.h al repositorio
//
// Uso:
//   cp secrets.h.template include/secrets.h
//   # Editar include/secrets.h con tus credenciales

#ifndef SECRETS_H
#define SECRETS_H

// ─── WiFi ────────────────────────────────────
#define WIFI_SSID     "tu-red-wifi"
#define WIFI_PASSWORD "tu-password-wifi"

// ─── MQTT (si aplica) ────────────────────────
#define MQTT_SERVER   "192.168.1.100"
#define MQTT_PORT     1883
#define MQTT_USER     "usuario-mqtt"
#define MQTT_PASSWORD "password-mqtt"

// ─── API Keys (si aplica) ────────────────────
#define API_KEY       "tu-api-key-aqui"

// ─── NTP / Timezone ──────────────────────────
#define NTP_SERVER    "pool.ntp.org"
#define UTC_OFFSET    -3  // Ver tabla abajo

// ─── Tabla de Zonas Horarias ─────────────────
// | Zona              | UTC Offset | Código    |
// |-------------------|-----------|-----------|
// | Buenos Aires      | -3        | ART       |
// | Ciudad de México  | -6        | CST       |
// | Bogotá/Lima       | -5        | COT/PET   |
// | Madrid            | +1 (+2)   | CET/CEST  |
// | Santiago          | -4 (-3)   | CLT/CLST  |
// | New York          | -5 (-4)   | EST/EDT   |
// | São Paulo         | -3        | BRT       |
// | Caracas           | -4        | VET       |

#endif // SECRETS_H
```

## Reglas

- El template NUNCA tiene credenciales reales — solo placeholders descriptivos
- Incluir tabla de zonas horarias si el proyecto usa NTP
- El archivo se llama `.template` — el real (sin .template) va en `.gitignore`
- Cada sección tiene comentario separador con línea de caracteres
- Los placeholders son descriptivos ("tu-red-wifi") no genéricos ("xxx")
- Incluir instrucciones de uso en comentarios al inicio del archivo
- Si hay entorno dev vs prod, usar #ifdef para seleccionar
- Documentar tipos de datos esperados en comentarios (string, int, etc.)

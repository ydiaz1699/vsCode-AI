# Guía: Generar archivo-mapa.yml

## Archivo de Salida

`archivo-mapa.yml` (raíz del proyecto)

## Cuándo Generarlo

**Siempre.** El archivo mapa es un resumen YAML completo del proyecto para contexto rápido de IA.

## Instrucciones para la IA

1. Extraer metadata del proyecto (nombre, versión, autor, fecha)
2. Definir el objetivo principal en una frase
3. Documentar todo el hardware: placa, periféricos con pines y protocolos
4. Listar dependencias con versiones exactas de `platformio.ini`
5. Describir la arquitectura: patrón, módulos, FSM si existe
6. Documentar flujos principales del sistema (boot, loop principal, comunicación)
7. Listar limitaciones conocidas (memoria, velocidad, compatibilidad)
8. Mapear la estructura de directorios con propósito de cada carpeta
9. Incluir comandos completos de compilación, upload, monitor y test
10. Verificar que el YAML sea válido y parseable

## Estructura Esperada

```yaml
# archivo-mapa.yml — Mapa completo del proyecto
# Generado automáticamente — No editar manualmente

metadata:
  nombre: "[nombre]"
  version: "[X.Y.Z]"
  autor: "[autor]"
  fecha_creacion: "YYYY-MM-DD"
  ultima_actualizacion: "YYYY-MM-DD"
  plataforma: "[PlatformIO/Arduino IDE/ESPHome]"

objetivo: "[Descripción del propósito en una frase]"

hardware:
  placa:
    nombre: "[nombre]"
    mcu: "[chip]"
    catalog_id: "[board-xxx]"
  perifericos:
    - nombre: "[nombre]"
      catalog_id: "[periph-xxx]"
      protocolo: "[I2C/SPI/GPIO/PWM]"
      pines:
        - funcion: "[VCC/GND/DATA/SDA/SCL]"
          gpio: [número]

dependencias:
  - nombre: "[librería]"
    version: "[X.Y.Z]"
    proposito: "[para qué]"

arquitectura:
  patron: "[loop simple/FSM/FreeRTOS/event-driven]"
  modulos:
    - nombre: "[módulo]"
      archivo: "[path]"
      responsabilidad: "[qué hace]"
  fsm:
    - estado: "[nombre]"
      transicion_a: "[siguiente]"
      condicion: "[cuándo]"

flujos:
  boot:
    - "[paso 1]"
    - "[paso 2]"
  loop_principal:
    - "[paso 1]"
    - "[paso 2]"

limitaciones:
  - "[limitación 1]"
  - "[limitación 2]"

estructura:
  - path: "src/"
    proposito: "Código fuente principal"
  - path: "include/"
    proposito: "Headers y configuración"
  - path: "lib/"
    proposito: "Librerías locales"
  - path: ".ai/"
    proposito: "Documentación para IA"

comandos:
  compilar: "pio run"
  upload: "pio run --target upload"
  monitor: "pio device monitor"
  test: "pio test"
  clean: "pio run --target clean"
```

## Reglas

- El YAML debe ser válido (verificar indentación con 2 espacios)
- No usar tabs — solo espacios
- Strings con caracteres especiales van entre comillas
- Los pines GPIO son números enteros, no strings
- El archivo es un RESUMEN — no repetir toda la documentación .ai/
- Máximo 100 líneas de YAML (forzar concisión)
- Incluir comentario al inicio indicando que es auto-generado
- Las versiones de librerías son las exactas instaladas (no rangos)
- Si no hay FSM, omitir la sección `fsm` (no dejar vacía)
- Los flujos describen el orden real de ejecución

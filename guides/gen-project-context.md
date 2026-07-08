# Guía: Generar PROJECT_CONTEXT.md

## Archivo de Salida

`.ai/PROJECT_CONTEXT.md`

## Cuándo Generarlo

**Siempre.** Este archivo es obligatorio para todo proyecto. Es el primer archivo que la IA lee para entender el contexto.

## Instrucciones para la IA

1. Identificar el propósito principal del proyecto analizando `README.md`, nombre del directorio y comentarios en `main.cpp`
2. Detectar la placa utilizada desde `platformio.ini` (campo `board`)
3. Mapear la placa al ID correspondiente en el catálogo (`catalog/boards/`)
4. Listar todos los periféricos identificados en el código (includes, defines de pines)
5. Mapear cada periférico al ID correspondiente en el catálogo (`catalog/peripherals/`)
6. Identificar el entorno de desarrollo (PlatformIO, Arduino IDE, ESPHome)
7. Listar archivos clave del proyecto con su propósito
8. Extraer convenciones del código: idioma, nomenclatura, indentación
9. Documentar los comandos de compilación, upload y monitor
10. Agregar notas adicionales relevantes (limitaciones, dependencias externas)

## Estructura Esperada

```markdown
# [Nombre] — Contexto del Proyecto

## Propósito
[Descripción de 2-3 oraciones]

## Referencias al Catálogo
| Tipo | Referencia | Notas |
|------|-----------|-------|
| Placa | [ID](link) | ... |
| Periférico | [ID](link) | ... |

## Archivos Clave
| Archivo | Propósito | Notas |
|---------|-----------|-------|
| src/main.cpp | ... | ... |

## Convenciones
- Idioma del código: ...
- Nomenclatura: ...

## Cómo Compilar
\```bash
pio run ...
\```
```

## Reglas

- El propósito debe ser concreto, no genérico ("controlar relays vía MQTT" no "proyecto IoT")
- Toda referencia al catálogo debe usar el formato de link relativo correcto
- Si un componente no está en el catálogo, indicarlo con nota "No catalogado"
- Las convenciones se extraen del código existente, no se inventan
- Los comandos de compilación deben ser copiables directamente
- Mínimo 3 archivos en la tabla de archivos clave
- No incluir archivos de la carpeta `.ai/` en la tabla de archivos clave

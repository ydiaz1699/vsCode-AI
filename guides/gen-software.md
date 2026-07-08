# Guía: Generar SOFTWARE.md

## Archivo de Salida

`.ai/SOFTWARE.md`

## Cuándo Generarlo

**Siempre.** Este archivo es obligatorio para todo proyecto PlatformIO/Arduino.

## Instrucciones para la IA

1. Copiar el contenido exacto de `platformio.ini` en el bloque de código
2. Extraer cada librería de `lib_deps` y documentar su versión, propósito y fuente
3. Si hay librerías en `lib/` local, documentarlas también con nota "local"
4. Extraer todos los build flags de `build_flags` y documentar su propósito
5. Identificar dependencias del sistema (Python, PlatformIO version, drivers)
6. Documentar todos los comandos necesarios: compilar, subir, monitorear, debug, test
7. Si hay scripts personalizados (extra_scripts), documentarlos
8. Si hay particiones custom, documentar el esquema
9. Verificar que las versiones de librerías sean las más recientes estables
10. Incluir comandos de troubleshooting para problemas comunes de compilación

## Estructura Esperada

```markdown
# [Nombre] — Software

## platformio.ini
\```ini
[env:...]
platform = ...
\```

## Librerías
| Librería | Versión | Propósito | Fuente |
|...|...|...|...|

## Build Flags
| Flag | Valor | Propósito |
|...|...|...|

## Dependencias del Sistema
| Herramienta | Versión Mínima | Propósito |
|...|...|...|

## Comandos
### Compilación y Upload
\```bash
pio run ...
\```
```

## Reglas

- El `platformio.ini` se copia textualmente, sin modificar
- Cada librería debe tener una razón concreta de uso, no genérica
- Los build flags se explican individualmente — no agrupar
- Los comandos deben ser copiables directamente (no usar paths relativos ambiguos)
- Si una librería tiene alternativas conocidas, no mencionarlas (se registra en DECISIONS.md)
- Incluir mínimo: compilar, upload, clean, monitor, test
- Las versiones de PlatformIO y Python son las instaladas, no genéricas

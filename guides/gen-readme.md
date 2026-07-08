# Guía: Generar README.md

## Archivo de Salida

`README.md` (raíz del proyecto)

## Cuándo Generarlo

**Siempre.** El README es para humanos, no para la IA. Debe ser comprensible sin leer archivos .ai/.

## Instrucciones para la IA

1. Escribir título descriptivo del proyecto (no el nombre del directorio)
2. Incluir descripción de una oración que explique qué hace el proyecto
3. Listar el hardware necesario (placa + periféricos) con links de compra si posible
4. Documentar diagrama de conexiones simplificado (tabla o referencia al SVG)
5. Escribir instrucciones de instalación paso a paso (clonar, instalar PlatformIO, compilar)
6. Documentar configuración necesaria (secrets.h, WiFi, etc.)
7. Incluir tabla de troubleshooting con mínimo 3 problemas comunes y sus soluciones
8. Agregar sección de contribución si es proyecto público
9. Incluir licencia o referencia a LICENSE file
10. Agregar badges si aplica (PlatformIO, version, build status)

## Estructura Esperada

```markdown
# [Nombre del Proyecto]

[Descripción corta de una oración]

## Hardware Necesario
- [placa]
- [periféricos]

## Conexiones
| Periférico | Pin |
|...|...|

## Instalación
1. Clonar repositorio
2. Instalar PlatformIO
3. ...

## Configuración
\```bash
cp secrets.h.template include/secrets.h
# Editar secrets.h con tus credenciales
\```

## Uso
\```bash
pio run --target upload
pio device monitor
\```

## Troubleshooting
| Problema | Causa | Solución |
|...|...|...|

## Licencia
...
```

## Reglas

- El README es para HUMANOS — lenguaje claro, sin jerga innecesaria
- Mínimo 3 filas en la tabla de troubleshooting
- Los problemas de troubleshooting deben ser reales (no inventados)
- Instrucciones de instalación copiables directamente (no decir "instala X" sino dar el comando)
- Si necesita secrets.h, explicar exactamente qué campos llenar
- No incluir la documentación .ai/ completa — solo mencionarla como "documentación técnica"
- Incluir versión del proyecto si existe
- Si es hardware, incluir foto o diagrama del montaje final

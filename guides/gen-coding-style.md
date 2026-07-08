# Guía: Generar CODING_STYLE.md

## Archivo de Salida

`.ai/CODING_STYLE.md`

## Cuándo Generarlo

**Solo si** el proyecto tiene reglas de estilo que difieren significativamente del estándar por defecto de PlatformIO/Arduino, o si hay convenciones específicas del equipo que deben documentarse.

## Instrucciones para la IA

1. Analizar el código existente para extraer patrones de nomenclatura usados
2. Identificar el idioma predominante en variables, funciones y comentarios
3. Detectar la convención de indentación (espacios/tabs, cantidad)
4. Buscar patrones en nombres de pines (`PIN_`, `_PIN`, prefijos)
5. Identificar el estándar base que el código sigue (o se acerca)
6. Documentar overrides explícitos del estándar base
7. Extraer la estructura típica de archivos (orden de secciones)
8. Documentar formato de comentarios usado (Doxygen, simple, etc.)
9. Identificar si hay reglas sobre largo de línea, funciones, archivos
10. Si hay `.clang-format` o configuración similar, referenciarla

## Estructura Esperada

```markdown
# [Nombre] — Estilo de Código

## Base
- Estándar base: ...
- Formatter: ...

## Overrides del Estándar
| Regla | Override | Razón |
|...|...|...|

## Nomenclatura
| Elemento | Convención | Ejemplo |
|...|...|...|

## Idioma
| Elemento | Idioma | Ejemplo |
|...|...|...|

## Reglas Específicas
### Estructura de archivos
\```cpp
// Orden de secciones...
\```
```

## Reglas

- Solo generar si hay divergencias reales del estándar; no repetir lo obvio
- Las convenciones se extraen del código existente, no se inventan
- Si el código es inconsistente, documentar la convención que predomina
- Incluir al menos un ejemplo concreto por cada regla de nomenclatura
- El idioma de cada elemento se documenta por separado (puede ser mixto)
- Si hay formatter configurado, documentar cómo ejecutarlo
- No contradecir lo definido en `PROJECT_CONTEXT.md` (deben ser complementarios)
- Las reglas específicas incluyen el "por qué" cuando no es obvio

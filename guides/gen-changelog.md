# Guía: Generar CHANGELOG.md

## Archivo de Salida

`.ai/CHANGELOG.md`

## Cuándo Generarlo

**Siempre.** Formato Keep a Changelog obligatorio para todo proyecto.

## Instrucciones para la IA

1. Verificar si existe un CHANGELOG previo — si existe, actualizarlo (no sobreescribir)
2. Si es proyecto nuevo, crear con sección `[Unreleased]` y `[0.1.0]` con la fecha actual
3. Extraer cambios del historial git si está disponible (`git log --oneline`)
4. Clasificar cada cambio en su categoría correcta (Added, Changed, Fixed, etc.)
5. Para proyectos hardware, agregar categoría extra "Hardware" para cambios físicos
6. Cada entrada describe QUÉ cambió, no CÓMO se implementó
7. Agrupar cambios relacionados bajo la misma versión
8. Si no hay git history, documentar el estado actual como versión 0.1.0
9. Verificar que el formato siga estrictamente Keep a Changelog
10. Incluir link de comparación entre versiones si hay repositorio remoto

## Estructura Esperada

```markdown
# Changelog

Todos los cambios notables se documentan en este archivo.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/).

## [Unreleased]
### Added
- ...

## [0.1.0] — YYYY-MM-DD
### Added
- Estructura inicial
- ...
```

## Reglas

- Formato estricto Keep a Changelog — no inventar categorías
- Categorías válidas: Added, Changed, Deprecated, Removed, Fixed, Security, Hardware
- La fecha usa formato ISO: YYYY-MM-DD
- `[Unreleased]` siempre va primero, incluso si está vacía
- Los mensajes son concisos pero descriptivos (no "fixes" sino "Corrige timeout en conexión MQTT")
- No incluir detalles de implementación — solo el efecto visible
- Versión inicial es siempre 0.1.0 (no 1.0.0) salvo que sea release
- Si hay breaking changes, documentarlos prominentemente

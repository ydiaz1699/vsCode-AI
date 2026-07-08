---
template: changelog
version: "1.0"
required: true
description: "Registro de cambios del proyecto en formato Keep a Changelog"
---

# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.1.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Added
- {{UNRELEASED_ADDED_1}}
- {{UNRELEASED_ADDED_2}}

### Changed
- {{UNRELEASED_CHANGED_1}}

### Fixed
- {{UNRELEASED_FIXED_1}}

### Removed
- {{UNRELEASED_REMOVED_1}}

## [0.1.0] — {{INITIAL_DATE}}

### Added
- Estructura inicial del proyecto
- Configuración de PlatformIO para {{BOARD_NAME}}
- {{INITIAL_FEATURE_1}}
- {{INITIAL_FEATURE_2}}
- {{INITIAL_FEATURE_3}}
- Documentación `.ai/` completa

### Hardware
- Conexión de {{PERIPHERAL_1_NAME}} en GPIO{{PERIPHERAL_1_PIN}}
- Conexión de {{PERIPHERAL_2_NAME}} vía {{PERIPHERAL_2_PROTOCOL}}

---

## Convenciones

### Tipos de cambio

- **Added** — Funcionalidad nueva
- **Changed** — Cambios en funcionalidad existente
- **Deprecated** — Funcionalidad que será eliminada próximamente
- **Removed** — Funcionalidad eliminada
- **Fixed** — Corrección de errores
- **Security** — Correcciones de vulnerabilidades
- **Hardware** — Cambios en conexiones o componentes físicos

### Reglas

1. Cada versión tiene su propia sección con fecha en formato ISO (YYYY-MM-DD)
2. Los cambios se agrupan por tipo
3. La sección `[Unreleased]` siempre va primero
4. Los mensajes son concisos pero descriptivos
5. Se referencian issues/PRs cuando aplica: `(#123)`

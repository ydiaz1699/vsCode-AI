---
template: software
version: "1.0"
required: true
description: "Configuración de software, librerías y entorno de compilación"
---

# {{PROJECT_NAME}} — Software

## platformio.ini

```ini
[env:{{ENVIRONMENT_NAME}}]
platform = {{PLATFORM}}
board = {{BOARD}}
framework = {{FRAMEWORK}}
monitor_speed = {{MONITOR_SPEED}}
upload_speed = {{UPLOAD_SPEED}}
lib_deps =
    {{LIB_DEP_1}}
    {{LIB_DEP_2}}
    {{LIB_DEP_3}}
build_flags =
    {{BUILD_FLAG_1}}
    {{BUILD_FLAG_2}}
    {{BUILD_FLAG_3}}
board_build.partitions = {{PARTITIONS}}
monitor_filters = {{MONITOR_FILTERS}}
```

## Librerías

| Librería | Versión | Propósito | Fuente |
|----------|---------|-----------|--------|
| {{LIB_1_NAME}} | {{LIB_1_VERSION}} | {{LIB_1_PURPOSE}} | {{LIB_1_SOURCE}} |
| {{LIB_2_NAME}} | {{LIB_2_VERSION}} | {{LIB_2_PURPOSE}} | {{LIB_2_SOURCE}} |
| {{LIB_3_NAME}} | {{LIB_3_VERSION}} | {{LIB_3_PURPOSE}} | {{LIB_3_SOURCE}} |
| {{LIB_4_NAME}} | {{LIB_4_VERSION}} | {{LIB_4_PURPOSE}} | {{LIB_4_SOURCE}} |

## Build Flags

| Flag | Valor | Propósito |
|------|-------|-----------|
| `-D {{FLAG_1_NAME}}` | `{{FLAG_1_VALUE}}` | {{FLAG_1_PURPOSE}} |
| `-D {{FLAG_2_NAME}}` | `{{FLAG_2_VALUE}}` | {{FLAG_2_PURPOSE}} |
| `-D {{FLAG_3_NAME}}` | `{{FLAG_3_VALUE}}` | {{FLAG_3_PURPOSE}} |
| `-D {{FLAG_4_NAME}}` | `{{FLAG_4_VALUE}}` | {{FLAG_4_PURPOSE}} |

## Dependencias del Sistema

| Herramienta | Versión Mínima | Propósito |
|-------------|---------------|-----------|
| PlatformIO Core | {{PIO_VERSION}} | Compilación y gestión |
| Python | {{PYTHON_VERSION}} | Scripts auxiliares |
| Git | {{GIT_VERSION}} | Control de versiones |
| {{EXTRA_TOOL}} | {{EXTRA_TOOL_VERSION}} | {{EXTRA_TOOL_PURPOSE}} |

## Comandos

### Compilación y Upload

```bash
# Compilar proyecto
pio run -e {{ENVIRONMENT_NAME}}

# Subir firmware
pio run -e {{ENVIRONMENT_NAME}} --target upload

# Limpiar build
pio run -e {{ENVIRONMENT_NAME}} --target clean

# Monitor serial
pio device monitor --baud {{MONITOR_SPEED}}
```

### Utilidades

```bash
# Verificar librerías
pio pkg list

# Actualizar librerías
pio pkg update

# Ejecutar tests
pio test -e {{ENVIRONMENT_NAME}}

# Generar compile_commands.json
pio run -e {{ENVIRONMENT_NAME}} --target compiledb
```

### Debugging

```bash
# Iniciar debug session
pio debug -e {{ENVIRONMENT_NAME}}

# Ver tamaño del firmware
pio run -e {{ENVIRONMENT_NAME}} --target size

# Verificar filesystem
pio run -e {{ENVIRONMENT_NAME}} --target buildfs
```

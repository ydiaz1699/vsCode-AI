# 🔄 Flujos de Trabajo

Tres flujos principales para usar el framework según tu situación.

---

## Flujo 1: Proyecto Nuevo (7 pasos)

Para crear un proyecto de firmware desde cero con documentación completa.

```
┌──────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│Define│───▶│ Catálogo │───▶│ Genera   │───▶│ Código   │
│idea  │    │ verifica │    │ docs .ai/│    │ inicial  │
└──────┘    └──────────┘    └──────────┘    └──────────┘
                                                  │
┌──────────┐    ┌──────────┐    ┌──────────┐     │
│ Iteración│◀───│ Verificar│◀───│Compilar  │◀────┘
│          │    │ docs     │    │y probar  │
└──────────┘    └──────────┘    └──────────┘
```

### Pasos

| # | Acción | Herramienta | Resultado |
|---|--------|-------------|-----------|
| 1 | Definir objetivo y hardware | Manual / `/new` | Requisitos claros |
| 2 | Verificar compatibilidad en catálogo | `catalog/README.md` | Hardware validado |
| 3 | Crear estructura PlatformIO | `pio project init` | Proyecto base |
| 4 | Generar documentación .ai/ | Synapse v3 o manual | 8+ archivos .ai/ |
| 5 | Implementar código inicial | Con IA o manual | `src/main.cpp` funcional |
| 6 | Compilar y verificar | `pio run` | Build exitoso |
| 7 | Probar en hardware real | Upload + monitor | Funcionamiento verificado |

### Ejemplo con Synapse v3

```
Usuario: /new
Synapse: ¿Qué hace el proyecto? ¿Placa? ¿Periféricos?
Usuario: Estación meteorológica con ESP32, BME280 y OLED SSD1306, publica por MQTT
Synapse: [genera todo: estructura, código, .ai/, README]
```

---

## Flujo 2: Documentar Proyecto Existente (5 pasos)

Para proyectos que ya tienen código funcional pero carecen de documentación.

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│Código    │───▶│ Análisis │───▶│ Genera   │───▶│ Revisa   │───▶│ Commit   │
│existente │    │ Fase 1   │    │ Fase 2   │    │ y ajusta │    │ docs     │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

### Pasos

| # | Acción | Herramienta | Resultado |
|---|--------|-------------|-----------|
| 1 | Reunir código fuente completo | `cat src/*.cpp include/*.h platformio.ini` | Código disponible |
| 2 | Ejecutar análisis (Fase 1) | `generator-context.md` | Placa, periféricos, estilo identificados |
| 3 | Generar archivos (Fase 2) | `generator-context.md` | 12-18 archivos generados |
| 4 | Revisar y ajustar inexactitudes | Manual | Documentación verificada |
| 5 | Commitear documentación | `git add .ai/ docs/ README.md` | Proyecto documentado |

### Ejemplo

```
1. Copiar generator-context.md como system prompt
2. Pegar: platformio.ini + main.cpp + cualquier header
3. La IA genera los 18 archivos según condiciones
4. Revisar que las conexiones documentadas coincidan con la realidad
5. git add . && git commit -m "docs: agregar documentación .ai/ completa"
```

---

## Flujo 3: Trabajar con IA Usando Contexto

Para sesiones de desarrollo continuo aprovechando la documentación existente.

### Setup de Sesión

```
1. Cargar synapse-v3.md como system prompt
2. Adjuntar archivos .ai/ existentes como contexto:
   - .ai/PROJECT_CONTEXT.md (obligatorio)
   - .ai/HARDWARE.md (si hay hardware)
   - .ai/SKILL.md (obligatorio — reglas del proyecto)
   - .ai/TASKS.md (para saber qué hacer)
3. La IA ya conoce tu proyecto completo
```

### Comandos Disponibles

| Comando | Resultado |
|---------|-----------|
| `/add-peripheral DHT22 GPIO4` | Agrega periférico verificando catálogo y pines libres |
| `/check` | Audita código buscando problemas |
| `/update` | Actualiza TASKS, CHANGELOG y ROADMAP |
| `/catalog` | Muestra hardware disponible |

### Ventajas del Contexto

Sin documentación .ai/:
```
"Agrega un sensor de temperatura"
→ La IA no sabe qué placa, qué pines están ocupados, qué convenciones seguir
→ Resultado genérico, posiblemente incompatible
```

Con documentación .ai/:
```
"Agrega un sensor de temperatura"
→ La IA lee HARDWARE.md: ESP32, GPIO4/5/18/19 ocupados
→ Lee SKILL.md: nunca usar delay(), constexpr para pines
→ Lee catálogo: periph-dht22 compatible con 3.3V
→ Genera código específico, correcto y documentado
```

---

## Tabla de Mantenimiento

Acciones a tomar cuando ocurren eventos en el proyecto:

| Evento | Acción | Archivos a Actualizar |
|--------|--------|----------------------|
| Agregar periférico nuevo | Verificar catálogo + documentar conexión | `HARDWARE.md`, `TASKS.md`, `CHANGELOG.md` |
| Cambiar librería | Documentar razón del cambio | `SOFTWARE.md`, `DECISIONS.md`, `CHANGELOG.md` |
| Corregir bug | Registrar fix y lección aprendida | `TASKS.md`, `CHANGELOG.md` |
| Completar feature | Mover de TODO a DONE | `TASKS.md`, `ROADMAP.md`, `CHANGELOG.md` |
| Cambiar placa | Re-documentar todo el hardware | `HARDWARE.md`, `PROJECT_CONTEXT.md`, `DECISIONS.md` |
| Agregar protocolo | Generar PROTOCOL.md si no existe | `PROTOCOL.md`, `ARCHITECTURE.md` |
| Release / versión | Actualizar changelog y roadmap | `CHANGELOG.md`, `ROADMAP.md`, `README.md` |
| Nuevo integrante | Compartir docs + explicar estructura | `README.md`, `copilot-instructions.md` |
| Refactoring mayor | Documentar decisión + actualizar arq. | `DECISIONS.md`, `ARCHITECTURE.md`, `CHANGELOG.md` |
| Hardware dañado | Documentar causa y prevención | `HARDWARE.md` (advertencias), `docs/notas.md` |

---

## Tips

1. **Mantén .ai/ actualizado** — Documentación desactualizada es peor que ninguna
2. **Commitea docs junto con código** — `git add src/ .ai/` en el mismo commit
3. **Usa `/check` regularmente** — Detecta drift entre código y documentación
4. **El CHANGELOG es tu diario** — Cada sesión de trabajo debería tener una entrada
5. **ROADMAP > TASKS** — ROADMAP es estratégico (qué construir), TASKS es táctico (qué hacer hoy)

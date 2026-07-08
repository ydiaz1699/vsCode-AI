# Guía: Generar copilot-instructions.md

## Archivo de Salida

`docs/copilot-instructions.md`

## Cuándo Generarlo

**Siempre.** Este archivo configura el comportamiento de GitHub Copilot y otros asistentes IA en el proyecto.

## Instrucciones para la IA

1. Leer `.ai/SKILL.md` para obtener las reglas y el flujo de trabajo
2. Leer `.ai/PROJECT_CONTEXT.md` para obtener convenciones del proyecto
3. Sintetizar las reglas NUNCA en formato compatible con Copilot
4. Documentar el estilo de código esperado (idioma, nomenclatura)
5. Especificar el framework y plataforma para que Copilot sugiera código correcto
6. Listar patrones preferidos (millis() vs delay(), constexpr vs #define, etc.)
7. Indicar qué archivos leer para contexto antes de generar código
8. Incluir anti-patrones que Copilot debe evitar
9. Documentar el formato de comentarios esperado
10. Incluir instrucciones de compilación para verificar sugerencias

## Estructura Esperada

```markdown
# Copilot Instructions

## Proyecto
[Descripción breve]

## Reglas de Código
- [regla 1]
- [regla 2]

## Estilo
- [convención]

## Contexto
Lee estos archivos antes de sugerir:
- .ai/PROJECT_CONTEXT.md
- .ai/HARDWARE.md

## Anti-patrones
- NO usar [patrón malo]

## Compilación
\```bash
pio run
\```
```

## Reglas

- El archivo debe ser compatible con `.github/copilot-instructions.md`
- Máximo 60 líneas — Copilot procesa mejor instrucciones concisas
- Las reglas más importantes van primero (Copilot prioriza inicio del archivo)
- Incluir plataforma y framework en la primera sección
- Los anti-patrones son más efectivos que las reglas positivas para Copilot
- Referenciar archivos .ai/ como fuente de contexto adicional
- No duplicar todo el contenido de SKILL.md — sintetizar
- Incluir el comando de verificación (compilar) al final

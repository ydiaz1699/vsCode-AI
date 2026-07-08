# Guía: Generar SKILL.md

## Archivo de Salida

`.ai/SKILL.md`

## Cuándo Generarlo

**Siempre.** Este archivo es obligatorio. Define el comportamiento del asistente IA para este proyecto específico.

## Instrucciones para la IA

1. Definir el propósito del asistente basado en el tipo de proyecto (IoT, robótica, domótica, etc.)
2. Identificar la especialización requerida (framework, protocolos, hardware específico)
3. Documentar el flujo de trabajo en 5 pasos exactos (analizar → verificar → planificar → implementar → validar)
4. Extraer decisiones clave del proyecto que la IA debe respetar siempre
5. Escribir mínimo 3 reglas NUNCA basadas en el hardware y framework utilizados
6. Adaptar las reglas NUNCA al contexto específico (ej: si usa ESP32 → nunca delay() en loop)
7. Crear checklist de criterios de salida verificables para cada tarea
8. Escribir 3 ejemplos de prompts realistas que un usuario haría para este proyecto
9. Los ejemplos deben ser específicos al hardware/protocolo del proyecto, no genéricos
10. Verificar que las reglas NUNCA no contradigan las decisiones tomadas

## Estructura Esperada

```markdown
# [Nombre] — Instrucciones para IA

## Propósito
Eres un asistente especializado en [X]...

## Flujo de Trabajo
1. Analizar contexto...
2. Verificar catálogo...
3. Planificar cambios...
4. Implementar...
5. Validar...

## Decisiones Clave
- [decisión concreta]...

## NUNCA Hacer
1. NUNCA [regla específica del proyecto]
2. NUNCA [regla de seguridad hardware]
3. NUNCA [regla de calidad de código]

## Criterios de Salida
- [ ] [criterio verificable]...

## Ejemplos de Prompts
### Ejemplo 1: [categoría]
"[prompt realista]"
```

## Reglas

- Mínimo 3 reglas NUNCA, máximo 7 (más de 7 pierden efectividad)
- Las reglas NUNCA deben ser específicas y verificables, no vagas
- Cada regla NUNCA debe explicar la consecuencia de violarla
- Los ejemplos de prompt deben incluir detalles técnicos concretos (pines, topics, tiempos)
- El flujo de trabajo siempre tiene exactamente 5 pasos
- Los criterios de salida usan checkboxes `- [ ]` para ser marcables
- El propósito incluye placa, framework y entorno en el contexto técnico
- No repetir información que ya está en otros archivos .ai/ — referenciarlos

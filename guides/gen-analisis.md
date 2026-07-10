# Guía: Generar analisis_<proyecto>.md

## Archivo de Salida

`analisis_<nombre_del_proyecto>.md` (raíz del proyecto)

## Cuándo Generarlo

**SIEMPRE. Antes que cualquier otro archivo.** Este es el PRIMER archivo que se genera. Es la fuente de verdad para toda la documentación posterior.

## Propósito

1. **Fuente de verdad** — Todos los datos para generar docs vienen de AQUÍ, no de la "memoria" del LLM
2. **Handoff** — Si el chat se corta o necesitas otro LLM/chat, pegas este archivo y continúas
3. **Anti-alucinación** — Si un dato no está en este archivo, NO se documenta (o se marca [VERIFICAR])
4. **Checkpoint** — El usuario valida el análisis ANTES de que se genere documentación

## Instrucciones para la IA

1. Leer TODOS los archivos de código del proyecto (main.cpp, libs, headers, platformio.ini)
2. Completar la sección 1 (Identificación): placa, MCU, framework, catálogo
3. Completar la sección 2 (Periféricos): buscar #define de pines, #include de librerías
4. Completar la sección 3 (Librerías externas): por cada librería, documentar si es bloqueante, si tiene estado interno, si los parámetros son lo que parecen. **LEER EL SOURCE SI ES POSIBLE.**
5. Completar la sección 4 (Software): copiar platformio.ini textual, listar deps
6. Completar la sección 5 (Arquitectura): detectar FSM, módulos, interrupciones
7. Completar la sección 6 (Protocolo): si hay comunicación, documentar formato
8. Completar la sección 7 (Timing): extraer TODAS las constantes de tiempo y CALCULAR tiempos reales
9. Completar la sección 8 (Estilo): detectar convenciones del código existente
10. Completar la sección 9 (Estado): extraer TODOs, FIXMEs, decisiones implícitas
11. Completar la sección 10 (Pendientes): listar todo lo que NO se pudo determinar
12. Completar la sección 11 (Archivos): evaluar cada condición y marcar SÍ/NO

## Reglas

- Este archivo se genera PRIMERO, antes que cualquier .ai/ o docs/
- Todo lo que no se pueda determinar del código se marca `[VERIFICAR: pregunta]`
- Los cálculos de timing deben incluir la fórmula (no solo el resultado)
- La sección de librerías externas debe documentar COMPORTAMIENTO REAL, no lo que el nombre sugiere
- El archivo debe ser AUTO-CONTENIDO: si alguien lo lee sin el código, entiende el proyecto
- Máximo 200 líneas (forzar concisión — si se necesita más, hay demasiados [VERIFICAR])
- Los campos vacíos se marcan "—" o "[VERIFICAR]", NUNCA se dejan en blanco
- El archivo es TEMPORAL (se puede eliminar después de generar la documentación) o PERMANENTE (si el usuario quiere mantenerlo como referencia)
- Si se usa en otro chat, el nuevo LLM debe poder generar TODA la documentación solo con este archivo

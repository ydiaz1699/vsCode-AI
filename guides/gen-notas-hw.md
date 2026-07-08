# Guía: Generar notas.md (Hardware)

## Archivo de Salida

`docs/notas.md`

## Cuándo Generarlo

**Solo si** el proyecto tiene hardware físico. Máximo 40 líneas.

## Instrucciones para la IA

1. Leer `.ai/HARDWARE.md` para obtener el contexto del hardware
2. Identificar las notas más críticas que un desarrollador necesita al trabajar con este hardware
3. Documentar voltajes críticos y riesgos de daño
4. Listar errores comunes que la gente comete con estos componentes
5. Incluir tips de debugging específicos del hardware utilizado
6. Documentar quirks o comportamientos inesperados del hardware
7. Si hay soldadura requerida, mencionarlo
8. Si hay componentes frágiles o con orientación, advertir
9. Mantener todo en máximo 40 líneas — ser extremadamente conciso
10. Priorizar información que salva hardware (evitar quemar componentes)

## Estructura Esperada

```markdown
# Notas de Hardware

## Voltajes Críticos
- [nota sobre voltaje]

## Errores Comunes
- [error que destruye hardware]

## Tips de Debugging
- [cómo diagnosticar problemas]

## Quirks
- [comportamiento inesperado]
```

## Reglas

- Máximo absoluto: 40 líneas (incluyendo headers y líneas en blanco)
- Prioridad #1: información que previene daño al hardware
- Prioridad #2: solución a problemas comunes
- Prioridad #3: tips de debugging
- No repetir información de HARDWARE.md — esto es un "cheat sheet" rápido
- Usar bullet points cortos, no párrafos
- Si hay 5V en placa 3.3V, SIEMPRE advertir en primera línea
- Cada nota es accionable — no información genérica

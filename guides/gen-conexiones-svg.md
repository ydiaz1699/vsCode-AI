# Guía: Generar conexiones.drawio.svg

## Archivo de Salida

`docs/conexiones.drawio.svg`

## Cuándo Generarlo

**Solo si** el proyecto tiene hardware físico con conexiones entre placa y periféricos.

## Instrucciones para la IA

1. Leer `.ai/HARDWARE.md` para obtener la tabla de conexiones completa
2. Identificar la placa principal y todos los periféricos conectados
3. Crear un diagrama Draw.io en formato SVG con los siguientes elementos:
4. La placa se representa como rectángulo con fill `#dae8fc` (azul claro) y borde oscuro
5. Los periféricos se representan con fill `#d5e8d4` (verde claro) y borde oscuro
6. Las conexiones VCC (alimentación) se dibujan en **rojo** (`#FF0000`)
7. Las conexiones GND (tierra) se dibujan en **negro** (`#000000`)
8. Las señales digitales/analógicas se dibujan en **verde** (`#00AA00`)
9. Las conexiones I2C (SDA/SCL) se dibujan en **azul** (`#0000FF`) para SDA y **amarillo** (`#FFAA00`) para SCL
10. Etiquetar cada línea con el nombre del pin en ambos extremos

## Estructura Esperada

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Placa principal -->
  <rect x="300" y="200" width="200" height="200" 
        fill="#dae8fc" stroke="#6c8ebf" stroke-width="2" rx="5"/>
  <text x="400" y="230" text-anchor="middle" font-weight="bold">[BOARD_NAME]</text>
  
  <!-- Periférico -->
  <rect x="50" y="250" width="150" height="100" 
        fill="#d5e8d4" stroke="#82b366" stroke-width="2" rx="5"/>
  <text x="125" y="280" text-anchor="middle">[PERIPHERAL_NAME]</text>
  
  <!-- Conexión VCC (rojo) -->
  <line x1="200" y1="270" x2="300" y2="270" stroke="#FF0000" stroke-width="2"/>
  <text x="250" y="265" text-anchor="middle" fill="#FF0000" font-size="10">VCC</text>
  
  <!-- Conexión GND (negro) -->
  <line x1="200" y1="290" x2="300" y2="290" stroke="#000000" stroke-width="2"/>
  
  <!-- Señal (verde) -->
  <line x1="200" y1="310" x2="300" y2="310" stroke="#00AA00" stroke-width="2"/>
  
  <!-- I2C SDA (azul) -->
  <line x1="200" y1="330" x2="300" y2="330" stroke="#0000FF" stroke-width="2"/>
  
  <!-- I2C SCL (amarillo) -->
  <line x1="200" y1="350" x2="300" y2="350" stroke="#FFAA00" stroke-width="2"/>
</svg>
```

## Reglas

- Colores obligatorios:
  - Placa: `#dae8fc` (fill), `#6c8ebf` (stroke)
  - Periféricos: `#d5e8d4` (fill), `#82b366` (stroke)
  - VCC: `#FF0000` (rojo)
  - GND: `#000000` (negro)
  - Señal digital/analógica: `#00AA00` (verde)
  - I2C SDA: `#0000FF` (azul)
  - I2C SCL: `#FFAA00` (amarillo)
- La placa siempre va al centro del diagrama
- Los periféricos se distribuyen alrededor (arriba, abajo, izquierda, derecha)
- Cada conexión tiene etiqueta con nombre de pin
- El SVG debe ser legible sin zoom a tamaño A4
- Si hay más de 4 periféricos, distribuir en 2 columnas
- Incluir leyenda de colores en la esquina inferior derecha
- El archivo debe ser compatible con Draw.io para edición posterior

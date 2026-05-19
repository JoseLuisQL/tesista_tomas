# Avance: Capítulo VI reestructurado en formato tipo asesora con cuadros

Fecha: 2026-05-18

## Archivo generado

- `INVESTIGACION FINAL - PARA PRESENTAR_CAPITULO_VI_TIPO_ASESORA_2026-05-18_v11.docx`

## Archivo base utilizado

- `INVESTIGACION FINAL - PARA PRESENTAR_PREPARADO_FINAL_ASESORA_2026-05-18_v10.docx`

No se sobrescribió la versión anterior.

## Criterio aplicado

Se adaptó el formato mostrado por la asesora, pero según el tema de la tesis. En la tesis de ejemplo se comparan grupos de control y experimental; en esta investigación no corresponde esa estructura porque se evalúan modelos de Deep Learning. Por ello, se adaptó el esquema a:

- ejecuciones completas de entrenamiento;
- Accuracy por ejecución;
- umbral `μ0 = 0.75`;
- prueba t de Student para una muestra;
- comparación entre CNN/EfficientNetB0 y Swin-Tiny Transformer.

## Cambios realizados en el Capítulo VI

Se reemplazó el Capítulo VI por una estructura más parecida al modelo de la asesora:

1. `CAPÍTULO VI: RESULTADOS`
2. `PRESENTACIÓN DE RESULTADOS Y ANÁLISIS`
3. `6.1. CONTRASTACIÓN DE HIPÓTESIS`
4. `6.1.1. Hipótesis de investigación`
5. `6.1.2. Hipótesis nula`
6. `6.1.3. Prueba estadística paramétrica utilizada`
7. Fórmula de la prueba t de Student para una muestra.
8. Definición de símbolos.
9. Regla de decisión.
10. `6.2. ANÁLISIS E INTERPRETACIÓN`
11. Prueba de hipótesis general.
12. Prueba de hipótesis específica 1.
13. Prueba de hipótesis específica 2.
14. Prueba de hipótesis específica 3.

## Cuadros agregados

Se agregaron tablas/cuadros para que el capítulo tenga la forma de la guía de la asesora:

- Tabla 21: Criterio de eficiencia para la interpretación del Accuracy.
- Tabla 22: Resumen de ejecuciones para la hipótesis general.
- Tabla 23: Prueba t de Student para una muestra en la hipótesis general.
- Tabla 24: Ejecuciones del modelo CNN/EfficientNetB0 para la prueba de eficiencia.
- Tabla 25: Prueba t de Student para una muestra en el modelo CNN/EfficientNetB0.
- Tabla 26: Ejecuciones del modelo Swin-Tiny Transformer para la prueba de eficiencia.
- Tabla 27: Prueba t de Student para una muestra en el modelo Swin-Tiny Transformer.
- Tabla 28: Comparación de Accuracy entre CNN/EfficientNetB0 y Swin-Tiny Transformer por ejecución.
- Tabla 29: Prueba t para la comparación entre CNN/EfficientNetB0 y Swin-Tiny Transformer.

También se actualizó el índice manual de tablas hasta la Tabla 31.

## Fórmulas incorporadas

Se incorporaron fórmulas textuales centradas:

- Prueba t de Student para una muestra:

`t = (X̄ − μ₀) / (S / √N)`

- Prueba comparativa pareada para HE3:

`t = D̄ / (S_D / √N)`

## Por qué no se colocaron valores inventados

No se colocaron Accuracy de 5, 10 o 20 ejecuciones porque todavía deben salir de los notebooks experimentales. Para mantener rigor metodológico, los cuadros quedaron listos con campos `Por completar`. Cuando se ejecuten los notebooks, esos valores se reemplazan por:

- Accuracy por ejecución;
- promedio `X̄`;
- desviación estándar `S`;
- número de ejecuciones `N`;
- estadístico t;
- valor p;
- decisión;
- conclusión final.

## Validación realizada

- DOCX generado correctamente.
- Párrafos: 907.
- Tablas: 31.
- Imágenes internas: 40.
- No aparecen términos restringidos:
  - `INKAPA`;
  - `aplicativo`;
  - `sintético/sintética`;
  - `synthetic`;
  - `imágenes reales`;
  - `imágenes sintéticas`;
  - `etiqueta real`;
  - `Llunchuy Waqachiq`.
- Se retiraron del resumen y abstract los valores p anteriores, porque la nueva contrastación final debe completarse con ejecuciones independientes reales.

## Recomendación

Sí es recomendable usar esta estructura porque se parece al modelo de la asesora y ayuda a que el jurado vea claramente: hipótesis, datos, fórmula, cuadro estadístico, decisión y conclusión. La diferencia metodológica es que aquí no se comparan grupos de control y experimental; se comparan ejecuciones de modelos de Deep Learning contra el umbral de eficiencia `μ0 = 0.75`.

# Avance: contrastación de hipótesis con estructura tipo asesora

Fecha: 2026-05-17

## Archivo generado

- `INVESTIGACION FINAL - PARA PRESENTAR_CONTRASTACION_ASESORA_2026-05-17_v9.docx`

## Archivo guía revisado

- `ayuda del asesor.docx`

También se revisaron las imágenes compartidas por el usuario:

- `image.png`
- `image copy.png`
- `image copy 2.png`

## Estructura aplicada en el Capítulo VI

Se reemplazó el bloque anterior de resultados por una estructura más parecida al modelo de la asesora:

1. `CAPÍTULO VI`
2. `PRESENTACIÓN DE RESULTADOS Y ANÁLISIS`
3. `6.1. CONTRASTACIÓN DE HIPÓTESIS`
4. `6.1.1. Hipótesis de investigación`
5. `6.1.2. Hipótesis nula`
6. `6.1.3. Prueba estadística paramétrica utilizada`
7. Fórmula de la prueba t de Student para una muestra.
8. Definición de símbolos.
9. Nivel de significancia.
10. Regla de decisión.
11. `6.2. ANÁLISIS E INTERPRETACIÓN`
12. Prueba de hipótesis general.
13. Prueba de hipótesis específica para CNN/EfficientNetB0.
14. Prueba de hipótesis específica para Swin-Tiny Transformer.
15. Prueba de hipótesis específica para la comparación entre CNN/EfficientNetB0 y Swin-Tiny Transformer.

## Fórmulas insertadas

Se insertaron fórmulas como imágenes internas, siguiendo el estilo visual de la guía:

- Prueba t de Student para una muestra:

`t = (x̄ - μ₀) / (s / √n)`

- Prueba t pareada:

`t = D̄ / (sD / √n)`

## Tablas agregadas en el estilo de la guía

- Tabla 18: Resumen del desempeño general de los algoritmos de Deep Learning.
- Tabla 19: Resumen del desempeño del modelo CNN/EfficientNetB0.
- Tabla 20: Resumen del desempeño del modelo Swin-Tiny Transformer.
- Tabla 21: Resumen comparativo entre CNN/EfficientNetB0 y Swin-Tiny Transformer.

## Resultados estadísticos colocados

| Hipótesis | Resultado | Decisión |
|---|---:|---|
| HG | t = 222.76; p < 0.001 | Se rechaza H0G; se acepta HG. |
| HE1 | t = 192.18; p < 0.001 | Se rechaza H01; se acepta HE1. |
| HE2 | t = 143.24; p < 0.001 | Se rechaza H02; se acepta HE2. |
| HE3 | t = 1.67; p = 0.145 | No se rechaza H03; la diferencia no es significativa. |

## Validaciones realizadas

- El DOCX abre correctamente con `python-docx`.
- El documento tiene 26 tablas y 46 imágenes internas.
- Se validó la presencia de:
  - `CONTRASTACIÓN DE HIPÓTESIS`.
  - `Prueba estadística paramétrica utilizada`.
  - `Su fórmula es`.
  - `Tabla 18` a `Tabla 21`.
  - valores `t = 222.76`, `t = 192.18`, `t = 143.24` y `t = 1.67`.
- Se verificó que no queden menciones a:
  - `INKAPA`.
  - `aplicativo`.
  - `sintética/sintético`.
  - `derivada/derivado`.
  - `procedencia`.
  - `Para levantar`.

## Recomendación antes de presentar

Abrir el documento en Word y ejecutar **Ctrl + A → F9** para actualizar índices, numeración de tablas/figuras y páginas. Luego revisar visualmente la ubicación de las fórmulas, porque fueron insertadas como imágenes internas para mantener un aspecto similar al modelo de la asesora.

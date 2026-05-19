# Avance: levantamiento de observaciones de asesora

Fecha: 2026-05-17

## Archivo generado

- `INVESTIGACION FINAL - PARA PRESENTAR_OBSERVACIONES_LEVANTADAS_2026-05-17_v5.docx`

El documento original `INVESTIGACION FINAL - PARA PRESENTAR.docx` no fue sobrescrito.

## Fuentes revisadas

- `INVESTIGACION FINAL - PARA PRESENTAR.docx`
- `ayuda del asesor.docx`
- `tesis_ejemplo1.pdf`
- `dataset/CSV_PAPAS.csv`
- `dataset/CSV_PAPAS_7000_LIMPIO.csv`
- `codigo_entrenamiento/modelo-cnn.ipynb`
- `codigo_entrenamiento/modelo-swin.ipynb`

## Correcciones aplicadas

1. Se reformuló la estructura metodológica para sostener hipótesis de investigación.
2. Se agregó el tercer problema específico alineado con la comparación CNN/EfficientNetB0 vs Swin-Tiny Transformer.
3. Se incorporaron hipótesis general, nulas y específicas:
   - H0G/HG para desempeño eficiente de algoritmos de Deep Learning.
   - H01/HE1 para CNN/EfficientNetB0.
   - H02/HE2 para Swin-Tiny Transformer.
   - H03/HE3 para diferencia entre modelos.
4. Se definió el umbral operativo de eficiencia en 0.75 para accuracy y F1-score macro.
5. Se corrigió población, muestra y corpus:
   - 7000 imágenes etiquetadas.
   - 2800 imágenes reales.
   - 4200 imágenes sintéticas o derivadas.
6. Se corrigieron los subconjuntos:
   - Entrenamiento: 4874 imágenes.
   - Validación: 1079 imágenes.
   - Prueba: 1047 imágenes.
7. Se documentaron épocas por modelo:
   - CNN/EfficientNetB0: 12 épocas, 4 de cabeza clasificadora y 8 de ajuste fino.
   - Swin-Tiny Transformer: 12 épocas, 3 de cabeza clasificadora y 9 de ajuste fino.
8. Se cambió el Capítulo V a: `CAPÍTULO V: GENERACIÓN DEL MODELO DE ALGORITMOS DE DEEP LEARNING`.
9. Se creó el nuevo `CAPÍTULO VI: RESULTADOS` para explicar las hipótesis con base en las métricas.
10. Se renombró la discusión como `CAPÍTULO VII: DISCUSIÓN`.
11. Se retiraron las menciones a INKAPA y al desarrollo de aplicativo.
12. Se actualizaron métricas verificadas:
    - CNN/EfficientNetB0: accuracy 0.9933, F1 macro 0.9933, 1040/1047 aciertos.
    - Swin-Tiny Transformer: accuracy 0.9962, F1 macro 0.9962, 1043/1047 aciertos.
13. Se corrigieron conclusiones y recomendaciones para centrarlas en modelos Deep Learning.

## Validaciones realizadas

- El DOCX generado abre correctamente con `python-docx`.
- No quedan menciones a `INKAPA`.
- No queda la frase `7000 imágenes digitales reales`.
- No queda la palabra `aplicativo`.
- Se verificó la presencia de:
  - `CAPÍTULO V: GENERACIÓN DEL MODELO DE ALGORITMOS DE DEEP LEARNING`.
  - `CAPÍTULO VI: RESULTADOS`.
  - `CAPÍTULO VII: DISCUSIÓN`.
  - hipótesis H0G, HG, HE1, HE2 y HE3.

## Límites metodológicos declarados

- La comparación CNN vs Swin se dejó como descriptiva, no como diferencia estadísticamente significativa, porque no se encontraron archivos locales de predicciones pareadas para aplicar McNemar o bootstrap pareado.
- Las métricas globales corresponden a un test mixto con imágenes reales y sintéticas/derivadas; por ello se evitó presentarlas como validación externa exclusiva con fotografías reales nuevas.
- No se inventaron ejecuciones repetidas ni resultados por prueba t, porque no existen 20 entrenamientos verificables en los archivos locales.

## Pendiente recomendado antes de impresión final

- Abrir el DOCX en Word y actualizar campos/índices con `Ctrl + A` y luego `F9`, para refrescar índice de figuras, tablas y numeración de páginas.
- Revisar visualmente saltos de página e imágenes después de actualizar índices.
- Si la asesora exige significancia estadística para HE3, recuperar o generar los CSV de predicciones pareadas de CNN y Swin para aplicar McNemar o bootstrap pareado.

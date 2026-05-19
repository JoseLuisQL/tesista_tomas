# Avance: preparación del DOCX para cierre final según observaciones de asesora

Fecha: 2026-05-18

## Archivo generado

- `INVESTIGACION FINAL - PARA PRESENTAR_PREPARADO_FINAL_ASESORA_2026-05-18_v10.docx`

## Archivo base utilizado

- `INVESTIGACION FINAL - PARA PRESENTAR_OBSERVACIONES_LEVANTADAS_ESTADISTICO_2026-05-17_v8.docx`

No se sobrescribió el documento base.

## Cambios aplicados

### 1. Metodología

Se reforzó el Capítulo IV para que la metodología quede alineada con las observaciones de la asesora:

- enfoque cuantitativo;
- tipo aplicado;
- diseño experimental computacional;
- nivel evaluativo-comparativo;
- población/corpus de 7000 imágenes;
- muestra operativa de 7000 imágenes etiquetadas;
- subconjuntos de entrenamiento, validación y prueba;
- configuración de épocas por modelo;
- repeticiones completas de entrenamiento para contrastación estadística.

Se agregó una sección específica sobre épocas y repeticiones experimentales, precisando que una época no equivale a una ejecución independiente.

### 2. Hipótesis

Se mantuvo y ordenó la estructura solicitada:

- H0G / HG;
- H01 / HE1;
- H02 / HE2;
- H03 / HE3.

La interpretación estadística fue ajustada al criterio recomendado por la asesora:

- `μ0 = 0.75`;
- `Accuracy < 75 %`: no eficiente;
- `Accuracy >= 75 %`: eficiente;
- prueba t de Student para una muestra usando Accuracy por ejecución completa.

### 3. Capítulo V

El Capítulo V quedó orientado a la generación de modelos:

`CAPÍTULO V: GENERACIÓN DEL MODELO DE ALGORITMOS DE DEEP LEARNING`

Se redujo la interpretación final dentro de este capítulo y se dejó como procedimiento técnico de:

- construcción del corpus;
- preprocesamiento;
- entrenamiento CNN/EfficientNetB0;
- entrenamiento Swin-Tiny Transformer;
- generación de métricas, matrices y reportes;
- preparación para la interpretación en el Capítulo VI.

### 4. Capítulo VI

El Capítulo VI fue reorientado para la contrastación de hipótesis según la asesora:

- criterio de eficiencia por Accuracy;
- valor de referencia `μ0 = 0.75`;
- nivel de significancia `α = 0.05`;
- definición de `X̄`, `S`, `N` y `p valor`;
- estructura para HG, HE1, HE2 y HE3;
- Tabla 20: criterio estadístico para la contrastación;
- Tabla 21: matriz de contrastación preparada para ejecuciones repetidas.

### 5. Captions, tablas y figuras

Se corrigieron captions confundidos entre figuras y tablas:

- las métricas globales CNN pasaron a Tabla 13;
- el reporte por clase CNN pasó a Tabla 14;
- la construcción Swin quedó como Tabla 15;
- el entrenamiento Swin quedó como Tabla 16;
- las métricas globales Swin quedaron como Tabla 17;
- el reporte por clase Swin quedó como Tabla 18;
- la comparación global quedó como Tabla 19;
- el criterio estadístico quedó como Tabla 20;
- la matriz de contrastación quedó como Tabla 21;
- los anexos quedaron como Tablas 22 y 23.

También se normalizó la numeración de figuras para evitar saltos innecesarios.

### 6. Redacción neutral sobre imágenes

Se verificó que el documento preparado no contenga menciones visibles a:

- `INKAPA`;
- `aplicativo`;
- `sintético`, `sintética`, `synthetic`;
- `imágenes reales`;
- `imágenes sintéticas`;
- `etiqueta real`.

La redacción visible usa formulaciones neutrales como `imágenes`, `corpus de imágenes` o `etiqueta de referencia`.

### 7. Conclusiones y discusión

Se corrigió la contradicción previa donde se decía que no existía prueba pareada o comparativa. Ahora el documento queda preparado para completar la decisión final de HE3 con las ejecuciones equivalentes de ambos modelos.

## Validación realizada

- El DOCX abre correctamente con `python-docx`.
- Párrafos: 819.
- Tablas: 23.
- Imágenes internas: 41.
- No se encontraron términos restringidos en el texto visible.
- No se sobrescribió el archivo base.

## Pendiente para cerrar al 100 %

Para terminar la tesis al 100 %, falta ejecutar los notebooks experimentales nuevos y colocar los valores reales generados:

- `tabla_ejecuciones_accuracy_cnn.csv`;
- `tabla_t_student_cnn.csv`;
- `tabla_contrastacion_hipotesis_cnn.csv`;
- `tabla_ejecuciones_accuracy_swin.csv`;
- `tabla_t_student_swin.csv`;
- `tabla_contrastacion_hipotesis_swin.csv`.

Con esos resultados se deben reemplazar las partes preparadas del Capítulo VI por los valores finales de:

- Accuracy por ejecución;
- promedio `X̄`;
- desviación estándar `S`;
- número de ejecuciones `N`;
- t calculado;
- valor p;
- decisión de hipótesis;
- conclusión final.

## Recomendación antes de entregar

Abrir el documento en Word y ejecutar `Ctrl + A → F9` para actualizar índices, numeración y campos. Luego revisar visualmente los saltos de página, captions y ubicación de tablas/figuras.

# Avance: análisis completo de hipótesis en notebooks experimentales

Fecha: 2026-05-18

## Objetivo

Se completaron los notebooks experimentales para que generen las tablas necesarias para la contrastación de hipótesis recomendada por la asesora, usando como criterio de eficiencia el umbral `μ0 = 0.75` sobre `Accuracy`.

## Notebooks actualizados

- `codigo_entrenamiento/modelo-cnn-experimentos-contrastacion-epocas.ipynb`
- `codigo_entrenamiento/modelo-swin-experimentos-contrastacion-epocas.ipynb`

Los notebooks originales se mantienen sin la sección experimental:

- `codigo_entrenamiento/modelo-cnn.ipynb`
- `codigo_entrenamiento/modelo-swin.ipynb`

## Criterio de eficiencia incorporado

| Accuracy | Interpretación |
|---|---|
| `< 75%` | No es eficiente |
| `>= 75%` | Eficiente |

Valor de referencia:

`μ0 = 0.75`

Nivel de significancia:

`α = 0.05`

## Hipótesis incorporadas

Para cada modelo experimental se genera una tabla con:

- `H0: μ < 0.75`
- `H1: μ >= 0.75`

Interpretación:

- H0: el desempeño promedio del modelo, medido por Accuracy, es menor al 75%.
- H1: el desempeño promedio del modelo, medido por Accuracy, es igual o mayor al 75%.

## Prueba estadística incorporada

Se incorporó la prueba t de Student para una muestra, con cola derecha:

`t = (X̄ - μ0) / (S / √N)`

Donde:

- `X̄`: promedio de Accuracy obtenido en las ejecuciones.
- `μ0`: valor mínimo esperado, igual a 0.75.
- `S`: desviación estándar de las ejecuciones.
- `N`: número de ejecuciones completas.

## Archivos nuevos que generará cada notebook experimental

### CNN/EfficientNetB0

Dentro de `outputs_cnn_dataset_combinado/experimentos_epocas/`:

- `criterio_eficiencia_cnn.csv`
- `hipotesis_estadistica_cnn.csv`
- `tabla_configuraciones_epocas_cnn.csv`
- `resultados_repeticiones_cnn.csv`
- `resumen_por_config_epocas_cnn.csv`
- `tabla_ejecuciones_accuracy_cnn.csv`
- `tabla_t_student_cnn.csv`
- `tabla_contrastacion_hipotesis_cnn.csv`
- `reporte_contrastacion_hipotesis_cnn.md`

### Swin-Tiny Transformer

Dentro de `outputs_swin_dataset_combinado/experimentos_epocas/`:

- `criterio_eficiencia_swin.csv`
- `hipotesis_estadistica_swin.csv`
- `tabla_configuraciones_epocas_swin.csv`
- `resultados_repeticiones_swin.csv`
- `resumen_por_config_epocas_swin.csv`
- `tabla_ejecuciones_accuracy_swin.csv`
- `tabla_t_student_swin.csv`
- `tabla_contrastacion_hipotesis_swin.csv`
- `reporte_contrastacion_hipotesis_swin.md`

## Configuración recomendada para ejecutar la contrastación

En cada notebook experimental activar:

```python
RUN_EPOCH_SWEEP = False
RUN_TTEST_REPETITIONS = True
RUN_SEEDS = [123, 124, 125, 126, 127]
```

Configuración principal por defecto:

- CNN: `TTEST_CONFIG_NAME = "cnn_50_epocas"`
- Swin: `TTEST_CONFIG_NAME = "swin_50_epocas"`

## Validación realizada

- `modelo-cnn.ipynb`: válido, 18 celdas, sin sección experimental.
- `modelo-swin.ipynb`: válido, 18 celdas, sin sección experimental.
- `modelo-cnn-experimentos-contrastacion-epocas.ipynb`: válido, 20 celdas, con sección experimental completa.
- `modelo-swin-experimentos-contrastacion-epocas.ipynb`: válido, 20 celdas, con sección experimental completa.
- Las celdas experimentales compilan sintácticamente.
- Se verificó la presencia de criterio de eficiencia, hipótesis H0/H1, tabla de ejecuciones, prueba t, decisión, conclusión y reporte Markdown.

## Nota metodológica

La muestra para la prueba t debe estar formada por ejecuciones completas del entrenamiento desde cero con diferentes semillas. No se debe usar cada época como una ejecución independiente. Las épocas sirven para documentar el comportamiento del entrenamiento; las repeticiones por semilla sirven para la contrastación estadística.

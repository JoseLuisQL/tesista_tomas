# Avance: notebooks experimentales separados para contrastación y análisis por épocas

Fecha: 2026-05-18

## Objetivo

Se separaron los experimentos de contrastación de hipótesis y análisis por épocas en notebooks independientes, para conservar limpios los notebooks originales y ejecutar entrenamientos completos desde cero con semillas distintas.

## Notebooks originales conservados

Los notebooks originales quedaron sin la sección experimental:

- `codigo_entrenamiento/modelo-cnn.ipynb`
- `codigo_entrenamiento/modelo-swin.ipynb`

Estos archivos mantienen el flujo base de entrenamiento y evaluación general de cada modelo.

## Nuevos notebooks experimentales

Se generaron archivos separados para ejecutar los entrenamientos repetidos y el barrido por épocas:

- `codigo_entrenamiento/modelo-cnn-experimentos-contrastacion-epocas.ipynb`
- `codigo_entrenamiento/modelo-swin-experimentos-contrastacion-epocas.ipynb`

Cada notebook experimental conserva el flujo completo del modelo correspondiente y agrega la sección:

`Experimentos para contrastación de hipótesis y análisis por épocas`

## Uso recomendado

### 1. Barrido por épocas

Para documentar el comportamiento del modelo con distintas configuraciones de entrenamiento:

```python
RUN_EPOCH_SWEEP = True
RUN_TTEST_REPETITIONS = False
```

Configuraciones incluidas:

- 12 épocas.
- 50 épocas.
- 80 épocas.
- 100 épocas.

### 2. Repeticiones para prueba t de Student

Para cumplir la recomendación de la asesora, se deben ejecutar entrenamientos completos independientes con diferentes semillas:

```python
RUN_EPOCH_SWEEP = False
RUN_TTEST_REPETITIONS = True
RUN_SEEDS = [123, 124, 125, 126, 127]
```

Cada fila de la tabla estadística corresponde a una ejecución completa del entrenamiento, no a una época individual.

## Configuración estadística

Los notebooks experimentales mantienen:

```python
MU0_ACCURACY = 0.75
ALPHA = 0.05
PRIMARY_METRIC = "accuracy_global"
```

La prueba aplicada es t de Student para una muestra, comparando el promedio de Accuracy de las ejecuciones contra el valor mínimo esperado `μ0 = 0.75`.

## Archivos de salida esperados

### CNN/EfficientNetB0

Dentro de `outputs_cnn_dataset_combinado/experimentos_epocas/`:

- `resultados_repeticiones_cnn.csv`
- `resumen_por_config_epocas_cnn.csv`
- `tabla_t_student_cnn.csv`
- carpetas por configuración y ejecución.

### Swin-Tiny Transformer

Dentro de `outputs_swin_dataset_combinado/experimentos_epocas/`:

- `resultados_repeticiones_swin.csv`
- `resumen_por_config_epocas_swin.csv`
- `tabla_t_student_swin.csv`
- carpetas por configuración y ejecución.

## Validación realizada

- `modelo-cnn.ipynb`: 18 celdas, sin marcador experimental, válido.
- `modelo-swin.ipynb`: 18 celdas, sin marcador experimental, válido.
- `modelo-cnn-experimentos-contrastacion-epocas.ipynb`: 20 celdas, con marcador experimental, válido.
- `modelo-swin-experimentos-contrastacion-epocas.ipynb`: 20 celdas, con marcador experimental, válido.

## Recomendación metodológica

Para la tesis, no se debe usar cada época como una ejecución independiente. La tabla de contrastación debe construirse con entrenamientos completos repetidos desde cero, preferentemente con cinco o más semillas. Luego, con los CSV generados, se actualiza el Capítulo VI usando los valores reales de Accuracy, promedio, desviación estándar, t calculado y valor p.

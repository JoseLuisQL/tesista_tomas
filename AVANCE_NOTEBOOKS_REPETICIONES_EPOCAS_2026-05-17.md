# Avance: notebooks actualizados para repeticiones y análisis por épocas

Fecha: 2026-05-17

## Archivos modificados

- `codigo_entrenamiento/modelo-cnn.ipynb`
- `codigo_entrenamiento/modelo-swin.ipynb`

## Objetivo de la modificación

Se agregaron secciones nuevas para poder ejecutar entrenamientos documentables según la recomendación de la asesora:

1. Comparar configuraciones por número de épocas, similar al ejemplo de tesis.
2. Ejecutar varias repeticiones completas del entrenamiento.
3. Registrar `Accuracy` por ejecución.
4. Calcular promedio, desviación estándar, estadístico t y valor p contra `μ0 = 0.75`.

## Estado actual

Las nuevas secciones quedaron insertadas, pero desactivadas por seguridad:

```python
RUN_EPOCH_SWEEP = False
RUN_TTEST_REPETITIONS = False
```

Esto evita que el notebook ejecute automáticamente entrenamientos largos al correr todas las celdas.

## Configuraciones agregadas

### CNN/EfficientNetB0

```python
EPOCH_CONFIGS_CNN = [
    {"name": "cnn_12_epocas", "total_epochs": 12, "head_epochs": 4},
    {"name": "cnn_50_epocas", "total_epochs": 50, "head_epochs": 10},
    {"name": "cnn_80_epocas", "total_epochs": 80, "head_epochs": 16},
    {"name": "cnn_100_epocas", "total_epochs": 100, "head_epochs": 20},
]
```

### Swin-Tiny Transformer

```python
EPOCH_CONFIGS_SWIN = [
    {"name": "swin_12_epocas", "total_epochs": 12, "head_epochs": 3},
    {"name": "swin_50_epocas", "total_epochs": 50, "head_epochs": 10},
    {"name": "swin_80_epocas", "total_epochs": 80, "head_epochs": 16},
    {"name": "swin_100_epocas", "total_epochs": 100, "head_epochs": 20},
]
```

## Cómo ejecutar como el ejemplo de tesis

Para documentar resultados por épocas, activar:

```python
RUN_EPOCH_SWEEP = True
RUN_TTEST_REPETITIONS = False
```

Esto ejecuta una corrida por configuración de épocas: 12, 50, 80 y 100.

## Cómo ejecutar para cumplir la prueba t de la asesora

Para la prueba t de Student, activar:

```python
RUN_EPOCH_SWEEP = False
RUN_TTEST_REPETITIONS = True
RUN_SEEDS = [123, 124, 125, 126, 127]
```

Esto ejecuta 5 entrenamientos completos para la configuración seleccionada:

- CNN: `TTEST_CONFIG_NAME = "cnn_50_epocas"`
- Swin: `TTEST_CONFIG_NAME = "swin_50_epocas"`

Cada entrenamiento completo corresponde a una ejecución independiente. No se debe usar cada época como si fuera una ejecución.

## Archivos de salida que se generarán

### CNN

Dentro de:

`outputs_cnn_dataset_combinado/experimentos_epocas/`

se generarán:

- `resultados_repeticiones_cnn.csv`
- `resumen_por_config_epocas_cnn.csv`
- `tabla_t_student_cnn.csv`
- carpetas por configuración y ejecución.

### Swin

Dentro de:

`outputs_swin_dataset_combinado/experimentos_epocas/`

se generarán:

- `resultados_repeticiones_swin.csv`
- `resumen_por_config_epocas_swin.csv`
- `tabla_t_student_swin.csv`
- carpetas por configuración y ejecución.

## Tabla esperada para la asesora

Después de ejecutar repeticiones, se podrá documentar así:

| Ejecución | Seed | Configuración | Accuracy |
|---:|---:|---|---:|
| 1 | 123 | cnn_50_epocas | valor generado |
| 2 | 124 | cnn_50_epocas | valor generado |
| 3 | 125 | cnn_50_epocas | valor generado |
| 4 | 126 | cnn_50_epocas | valor generado |
| 5 | 127 | cnn_50_epocas | valor generado |

Luego se calcula:

- promedio de Accuracy;
- desviación estándar;
- t calculado;
- valor p;
- decisión frente a `μ0 = 0.75`.

## Validación realizada

- Ambos notebooks siguen siendo válidos con `nbformat`.
- `modelo-cnn.ipynb` quedó con 20 celdas.
- `modelo-swin.ipynb` quedó con 20 celdas.
- Las celdas nuevas compilan sintácticamente.
- Los flags de ejecución quedaron en `False`.

## Recomendación práctica

Primero probar en Kaggle con una ejecución corta:

```python
RUN_EPOCH_SWEEP = False
RUN_TTEST_REPETITIONS = True
RUN_SEEDS = [123, 124]
TTEST_CONFIG_NAME = "cnn_12_epocas"  # o "swin_12_epocas"
```

Si eso funciona, ejecutar la configuración completa con 5 semillas y 50 épocas. Solo después conviene actualizar el Capítulo VI con los valores reales generados.

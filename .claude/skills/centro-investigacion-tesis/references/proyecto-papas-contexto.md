# Contexto local del proyecto de tesis sobre papas nativas

## Ruta base

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista`

## Tema de trabajo

Tesis orientada a la identificación o clasificación de variedades de papas nativas mediante técnicas de Deep Learning y modelos de visión por computadora.

## Documento de tesis y plantilla estructural

- Tesis en avance: `C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\INVESTIGACION FINAL.docx`
- Tesis ejemplo estructural: `C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\tesis_ejemplo1.pdf`

`tesis_ejemplo1.pdf` solo debe usarse como guía estructural. No se debe copiar contenido.

## Dataset

Carpeta:

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\dataset`

Archivo tabular:

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\dataset\CSV_PAPAS.csv`

Columnas detectadas:

- `filename`
- `variedad`
- `color_piel`
- `intensidad_piel`
- `color_secundario_piel`
- `distribucion_color_secundario_piel`
- `color_pulpa`
- `color_secundario_pulpa`
- `distribucion_color_secundario_pulpa`
- `forma_general`
- `variante_forma`
- `profundidad_ojos`

Variedades detectadas en carpetas locales:

1. `PUKA_ÑATA`
2. `TOROPA_WAQRAN`
3. `PUMAPA_MAKIN`
4. `PUTISA`
5. `YURAQ_LEGUAS`
6. `YURAQ_JEWICHO`
7. `CANUTILLO`

Riesgo registrado: en una exploración previa se observó que el CSV contiene 2800 registros, pero la carpeta local visible parecía contener 42 imágenes, mientras los manifiestos de entrenamiento reportan 7000 imágenes. Antes de concluir resultados fuertes, revisar esta discrepancia.

## Notebooks de entrenamiento

- `C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\codigo_entrenamiento\modelo-cnn.ipynb`
- `C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\codigo_entrenamiento\modelo-swin.ipynb`

Modelos detectados:

- CNN/EfficientNetB0.
- Swin-Tiny.

Configuración observada en exploración previa:

- `SPLIT_PROTOCOL = "mixed_synthetic_eval"`
- `SEED = 123`
- `IMG_SIZE = 224`
- batch global 64
- entorno de ejecución asociado a Kaggle en rutas internas.

## Resultados CNN

Directorio:

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\resultados_entrenamiento\modelo_cnn\outputs_cnn_dataset_combinado`

Archivos clave:

- `metricas_cnn.csv`
- `metricas_test_por_origen_cnn.csv`
- `classification_report_cnn_global.csv`
- `classification_report_cnn_real_only.csv`
- `classification_report_cnn_synthetic_only.csv`
- `matriz_confusion_cnn.csv`
- `predicciones_test_cnn.csv`
- `historial_entrenamiento_cnn.csv`
- `split_protocol_config.json`
- `split_manifest_cnn_dataset_combinado_mixed_synthetic_eval.csv`

Modelos/exportación:

- `models\clasificador_papas_cnn_final.keras`
- `models\best_model_cnn_finetune.keras`
- `models\best_model_cnn_head.keras`
- `models\onnx\clasificador_papas_cnn_final.onnx`

## Resultados Swin

Directorio:

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista\resultados_entrenamiento\modelo_swit\outputs_swin_dataset_combinado`

Archivos clave:

- `metricas_swin.csv`
- `metricas_test_por_origen_swin.csv`
- `classification_report_swin_global.csv`
- `classification_report_swin_real_only.csv`
- `classification_report_swin_synthetic_only.csv`
- `matriz_confusion_swin.csv`
- `predicciones_test_swin.csv`
- `historial_entrenamiento_swin.csv`
- `split_protocol_config.json`
- `split_manifest_swin_dataset_combinado_mixed_synthetic_eval.csv`

Modelos/exportación:

- `models\swin_tiny_papas_final.pt`
- `models\best_model_swin.pt`
- `models\onnx\swin_tiny_papas_final.onnx`

## Métricas observadas en exploración previa

| Modelo | Accuracy test | Balanced accuracy | Macro F1 | Test real-only | Test synthetic-only |
|---|---:|---:|---:|---:|---:|
| CNN/EfficientNetB0 | 0.993314 | 0.993346 | 0.993317 | 1.000000 | 0.988976 |
| Swin-Tiny | 0.994269 | 0.994292 | 0.994250 | 1.000000 | 0.990551 |

Interpretación obligatoria:

- No afirmar que Swin es superior solo por diferencia mínima sin prueba pareada.
- No presentar el 1.0 real-only como prueba definitiva sin revisar tamaño, selección, fuga, duplicados y validación externa.
- Diferenciar siempre resultados globales, reales y sintéticos.

## Riesgos metodológicos y estadísticos

- Posible inflación por uso de imágenes sintéticas en validación/test.
- Posible fuga de datos o duplicados visuales entre train/val/test.
- Rutas internas de Kaggle pueden no corresponder a rutas locales.
- Diferencia entre modelos puede ser de muy pocos aciertos.
- Falta evidencia de pruebas pareadas como McNemar.
- Falta evidencia de intervalos de confianza o bootstrap.
- Riesgo de problemas Unicode en nombres con `Ñ`.
- Diferencia entre `modelo_swit` y `swin` puede causar confusión en redacción y rutas.

## Reglas para redacción de resultados

- Reportar tablas con modelo, split, accuracy, precision, recall, F1-score y balanced accuracy si están disponibles.
- Interpretar matrices de confusión por clase.
- Distinguir rendimiento en imágenes reales y sintéticas.
- Incluir limitaciones de generalización.
- No concluir causalidad ni superioridad sin prueba estadística adecuada.
- Conectar resultados con objetivos específicos.

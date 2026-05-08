# Clasificador de Variedades de Papa con Deep Learning - Proyecto de Tesis

Este repositorio contiene los archivos, el código fuente y la documentación de un proyecto de tesis enfocado en la **clasificación visual de variedades de papa** utilizando modelos avanzados de Deep Learning.

En este estudio se evalúa y compara el desempeño de dos arquitecturas de vanguardia en la visión computacional:
- **Redes Neuronales Convolucionales (CNN)**, específicamente utilizando `EfficientNetB0`.
- **Transformers de Visión**, utilizando la arquitectura jerárquica `Swin Transformer` (Swin-Tiny).

## 🗂️ Estructura del Repositorio

El proyecto está organizado de la siguiente manera:

- `codigo_entrenamiento/`: Contiene los Jupyter Notebooks utilizados para el entrenamiento, validación y evaluación de los modelos (`modelo-cnn.ipynb` y `modelo-swin.ipynb`).
- `dataset/`: Directorio preparado para almacenar las imágenes (reales y sintéticas) y los archivos CSV (manifiestos) utilizados para el entrenamiento y prueba.
- `resultados_entrenamiento/`: Carpeta (ignorada en el control de versiones por su tamaño) donde se almacenan los pesos de los modelos guardados (`.keras`, `.pt`), métricas, matrices de confusión y gráficos de desempeño.
- `referencias/`: Documentación bibliográfica, papers recopilados y material de investigación de apoyo.
- `docs/`: Documentación adicional del proyecto.
- `INVESTIGACION FINAL.docx`: Documento oficial y principal donde se redacta el cuerpo de la tesis (marco teórico, metodología, resultados y conclusiones).

## 🔬 Metodología y Herramientas

El proyecto no solo se enfoca en el desarrollo de IA, sino que sigue una metodología académica rigurosa:
- **Modelamiento:** Construcción de modelos utilizando bibliotecas estándar de la industria (TensorFlow/Keras para CNN y PyTorch para Swin Transformer).
- **Análisis de Resultados:** Comparación de métricas globales (Accuracy, Precision, Recall, F1-Score) analizando el comportamiento de los modelos frente a datos reales y datos sintéticos.
- **Asistencia IA (Centro de Investigación Local):** El proyecto incluye una estructura local de prompts y agentes (`.claude/` y `CLAUDE.md`) diseñados para asistir sistemáticamente en la redacción, revisión APA, validación metodológica y análisis estadístico de la tesis.

## 🚀 Uso y Reproducción

Para reproducir los entrenamientos:
1. Asegúrate de tener configurado un entorno virtual de Python con las dependencias necesarias instaladas (PyTorch, TensorFlow, OpenCV, Scikit-learn, etc.).
2. Coloca el dataset de imágenes de papas dentro de la carpeta `dataset/` siguiendo la estructura esperada por los scripts.
3. Ejecuta de forma secuencial los notebooks ubicados en la carpeta `codigo_entrenamiento/` (se recomienda usar Google Colab o un entorno local con soporte de GPU).

## 📄 Notas

> **Nota sobre archivos grandes:** Los modelos compilados finales (`best_model_swin.pt`, `clasificador_papas_cnn_final.keras`, etc.) pueden superar los 100 MB. Por restricciones de tamaño de GitHub, la carpeta `resultados_entrenamiento` se encuentra en el archivo `.gitignore` y los modelos no están subidos al repositorio.

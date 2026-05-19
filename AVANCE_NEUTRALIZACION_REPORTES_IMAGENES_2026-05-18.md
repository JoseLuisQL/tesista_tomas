# Avance: neutralización de reportes sobre imágenes

Fecha: 2026-05-18

## Objetivo

Se ajustaron los notebooks experimentales para que los textos visibles, títulos de secciones y archivos de salida de pruebas usen una formulación neutral basada en la palabra `imágenes`.

## Archivos actualizados

- `codigo_entrenamiento/modelo-cnn-experimentos-contrastacion-epocas.ipynb`
- `codigo_entrenamiento/modelo-swin-experimentos-contrastacion-epocas.ipynb`

## Cambios aplicados

- Se cambió el título visible de la sección de prueba a `Prueba profesional con imágenes propias`.
- Se ajustaron rutas y nombres de archivos de salida para usar nombres neutrales, por ejemplo:
  - `pruebas_imagenes_cnn`
  - `pruebas_imagenes_swin`
  - `resultados_imagenes_cnn.csv`
  - `resultados_imagenes_swin.csv`
  - `resumen_imagenes_cnn.csv`
  - `resumen_imagenes_swin.csv`
  - `grid_predicciones_imagenes_cnn.png`
  - `grid_predicciones_imagenes_swin.png`
- Se limpiaron las salidas ejecutadas anteriores de los notebooks experimentales para que no aparezcan reportes antiguos en pantalla.

## Validación realizada

- Ambos notebooks experimentales siguen siendo válidos con `nbformat`.
- Las celdas Python no mágicas compilan correctamente.
- Las salidas guardadas dentro de los notebooks quedaron vacías.
- Los textos visibles antiguos de la sección de prueba fueron neutralizados.

## Nota

No se cambió el análisis estadístico de hipótesis ni las configuraciones de entrenamiento por épocas y semillas. La modificación fue de redacción visible, nombres de salida y limpieza de salidas previas.

# Instrucciones del proyecto `tesista`

Este proyecto usa un Centro de Investigación local para apoyar la elaboración, revisión y sustentación de la tesis.

## Alcance

Estas instrucciones aplican solo al proyecto:

`C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista`

## Centro de Investigación local

Usar prioritariamente la skill local:

- `centro-investigacion-tesis`

Esta skill coordina especialistas locales ubicados en:

- `.claude\skills\tesis-lector-documental`
- `.claude\skills\tesis-especialista-tematico`
- `.claude\skills\tesis-revision-bibliografica-sistematica`
- `.claude\skills\tesis-metodologia-matriz`
- `.claude\skills\tesis-redaccion-academica`
- `.claude\skills\tesis-estadistica-modelos`
- `.claude\skills\tesis-apa7-integridad`
- `.claude\skills\tesis-formato-docx-universitario`
- `.claude\skills\tesis-sustentacion-defensa`

También existen agentes locales en:

- `.claude\agents\coordinador-centro-investigacion.md`
- `.claude\agents\metodologo-tesis.md`
- `.claude\agents\investigador-tematico.md`
- `.claude\agents\redactor-academico.md`
- `.claude\agents\estadistico-ml.md`
- `.claude\agents\auditor-apa-calidad.md`
- `.claude\agents\asesor-sustentacion.md`

## Regla obligatoria para fuentes académicas

Cuando cualquier skill o agente del Centro necesite investigación profunda, búsqueda de nuevos papers, antecedentes, fuentes o bibliografía, debe usar estrictamente el MCP SciSummary.

Herramientas preferidas:

- `mcp__scisummary__find-new-papers` para buscar nuevos papers.
- `mcp__scisummary__list-papers` para revisar la biblioteca del usuario.
- `mcp__scisummary__ask-entire-library` para consultar la biblioteca completa.
- `mcp__scisummary__ask-question-to-paper` para analizar un paper específico.
- `mcp__scisummary__get-paper-summaries` para recuperar resúmenes disponibles.
- `mcp__scisummary__import-paper-to-library` solo si el usuario autoriza importar un PDF.

No usar WebSearch ni WebFetch para buscar fuentes académicas nuevas salvo autorización explícita del usuario si SciSummary no entrega resultados suficientes.

## Flujo obligatorio de tesis

1. Si se inicia desde cero, comenzar por tema, problema, objetivos, hipótesis si corresponde, variables y matriz de consistencia.
2. Si se entrega una tesis avanzada, primero revisarla estrictamente antes de continuar redactando.
3. Trabajar por capítulos.
4. Al terminar un capítulo, entregarlo al usuario para aprobación.
5. No pasar al siguiente capítulo sin aprobación explícita.
6. Si hay observaciones críticas, corregirlas antes de continuar.
7. No inventar citas, referencias, autores, DOI, resultados, métricas ni datos.
8. No ayudar a ocultar plagio; exigir paráfrasis ética y citación correcta.

Frases válidas de aprobación del usuario:

- aprobado;
- apruebo;
- continúa;
- pasemos al siguiente capítulo;
- está conforme.

## Archivos principales

Documento de tesis en avance:

- `INVESTIGACION FINAL.docx`

Tesis ejemplo estructural:

- `tesis_ejemplo1.pdf`

Usar `tesis_ejemplo1.pdf` solo como guía de estructura, no como contenido para copiar.

## Datos y resultados

Dataset:

- `dataset\CSV_PAPAS.csv`
- `dataset\`

Notebooks:

- `codigo_entrenamiento\modelo-cnn.ipynb`
- `codigo_entrenamiento\modelo-swin.ipynb`

Resultados CNN:

- `resultados_entrenamiento\modelo_cnn\outputs_cnn_dataset_combinado`

Resultados Swin:

- `resultados_entrenamiento\modelo_swit\outputs_swin_dataset_combinado`

## Criterios para análisis de resultados

- Separar métricas globales, real-only y synthetic-only.
- Revisar matrices de confusión y reportes por clase.
- No afirmar superioridad entre CNN y Swin sin análisis pareado.
- Considerar McNemar, intervalos de confianza o bootstrap cuando se compare modelos.
- Advertir sobre posible inflación de métricas por imágenes sintéticas.
- Revisar fuga de datos, duplicados visuales y consistencia de splits.
- Conectar resultados con objetivos específicos.

## Estilo de trabajo

El tono debe ser académico, claro y estricto. Las observaciones deben clasificarse como críticas, mayores o menores. La redacción debe evitar frases genéricas de IA y mantener rigor metodológico.

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
- `.claude\agents\editor-docx-quirurgico.md`
- `.claude\agents\especialista-visual-academico.md`
- `.claude\agents\revisor-avance-docx-integral.md`
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

## Reglas de razonamiento metodológico

Antes de tomar decisiones académicas importantes, los agentes deben razonar metodológicamente:

- identificar la pregunta de investigación que se intenta resolver;
- verificar coherencia entre problema, objetivos, hipótesis, variables, diseño, muestra, instrumentos, resultados y conclusiones;
- explicar por qué una decisión metodológica es más defendible que otra;
- declarar alternativas descartadas, amenazas a la validez y límites de generalización;
- formular preguntas concretas si falta información;
- bloquear avance si hay inconsistencias críticas abiertas.

## Revisión obligatoria del DOCX de avance

Antes de continuar o redactar nuevas secciones sobre `INVESTIGACION FINAL.docx`, debe intervenir `revisor-avance-docx-integral` cuando el usuario pida revisar, continuar, corregir o integrar el avance.

Este revisor debe detectar problemas precisos de redacción, incoherencias metodológicas, hipótesis mal alineadas, resultados no sustentados, tablas/figuras no interpretadas, fallas APA y riesgos ante jurado. Si hay observaciones críticas, no se debe continuar hasta corregirlas o recibir una decisión explícita del usuario.

## Habilidades DOCX instaladas

Para edición y manipulación de Word/DOCX usar, además de las skills locales:

- `docx` para crear, leer, editar, reorganizar, insertar o reemplazar contenido en archivos `.docx`.
- `docx-manipulation` para modificaciones programáticas precisas con `python-docx`.
- `docx-perfect` y `tesis-formato-docx-universitario` para presentación académica, tablas, figuras, índices y cumplimiento universitario.

## Habilidades visuales instaladas

Para generación y análisis visual usar:

- `chart-visualization` para gráficos profesionales, visualizaciones de datos y figuras estadísticas.
- `image-generation` para diseñar prompts de imágenes o figuras ilustrativas.
- `ocr-service` para extracción de texto desde imágenes y documentos escaneados.
- `computer-vision-opencv` para análisis técnico de imágenes, segmentación, preprocesamiento y visión por computadora.
- `svg-illustration` y `mermaid-diagrams` para diagramas, flujos, arquitectura metodológica y esquemas reproducibles.

## Reglas obligatorias para imágenes, gráficos y extracción visual

- No inventar datos, clases, métricas, textos visibles, fuentes ni evidencias visuales.
- Los gráficos deben basarse en CSV, resultados, tablas o datos locales verificados; indicar siempre la fuente de datos.
- No subir datasets, resultados, imágenes de papas, capturas del documento ni evidencias de tesis a APIs o servicios externos de gráficos/OCR/generación visual sin autorización explícita del usuario.
- Los gráficos profesionales deben incluir título, ejes rotulados, leyenda, nota/fuente y diseño legible para tesis.
- Las imágenes generadas solo pueden usarse como ilustraciones o esquemas; no deben presentarse como evidencia empírica, fotografías del dataset ni resultados experimentales.
- Si una imagen es generada o sintética, debe declararse explícitamente en el caption, nota o texto acompañante.
- Para extraer información de imágenes, separar texto OCR, observación visual directa, inferencias y límites de confianza.
- No atribuir variedad de papa, procedencia, enfermedad, resultado de modelo o evidencia metodológica si la imagen no lo demuestra.
- Toda figura o gráfico destinado al DOCX debe coordinarse con `editor-docx-quirurgico` para inserción precisa, numeración, título, nota/fuente y preservación de formato.

## Reglas obligatorias para edición DOCX quirúrgica

- No sobrescribir el documento original; crear siempre una copia versionada de salida, salvo autorización explícita.
- Antes de editar, inventariar estructura, estilos, títulos, tablas, figuras, notas, fuentes y zonas objetivo.
- Mantener estrictamente Times New Roman tamaño 12 en cuerpo, tablas, notas y texto insertado, salvo estilos institucionales ya existentes para títulos o portada.
- No reformatear todo el documento si el usuario pidió un cambio puntual; editar solo los párrafos, tablas, figuras o secciones solicitadas.
- Insertar tablas con numeración, título, nota/fuente y formato académico uniforme; no inventar datos ni resultados.
- Insertar imágenes solo desde archivos proporcionados o ubicaciones locales verificadas; conservar proporción, ajustar al ancho disponible y añadir título, nota/fuente si corresponde.
- Toda tabla o figura agregada debe quedar citada o mencionada en el texto cuando forme parte del cuerpo de la tesis.
- Después de editar, reportar archivo generado, cambios aplicados y contenido que no fue modificado.

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
- Alinear cada tabla, figura y métrica con objetivo específico e hipótesis si corresponde.
- Separar descripción de resultados, interpretación estadística y discusión.
- No declarar aceptación/rechazo de hipótesis si no existe prueba o criterio estadístico suficiente.

## Estilo de trabajo

El tono debe ser académico, claro, humano y estricto. Las observaciones deben clasificarse como críticas, mayores o menores. La redacción debe evitar frases genéricas de IA, mantener rigor metodológico y explicar las decisiones con razonamiento comprensible, no con respuestas automáticas.

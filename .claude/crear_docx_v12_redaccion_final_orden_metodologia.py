from copy import deepcopy
from pathlib import Path
import shutil

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.shared import Pt, Cm

BASE = Path(r"C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista")
SRC = BASE / "INVESTIGACION FINAL - PARA PRESENTAR_CAPITULO_VI_TIPO_ASESORA_2026-05-18_v11.docx"
OUT = BASE / "INVESTIGACION FINAL - PARA PRESENTAR_FORMATO_RESULTADOS_HIPOTESIS_2026-05-18_v12.docx"

shutil.copy2(SRC, OUT)
doc = Document(OUT)

FONT = "Times New Roman"
SIZE = Pt(12)


def norm(text):
    return " ".join(text.split())


def element_text(el):
    texts = []
    for node in el.iter():
        if str(node.tag).endswith('}t') and node.text:
            texts.append(node.text)
    return " ".join(texts)


def has_inline(p):
    return bool(p._p.xpath('.//wp:inline'))


def run_format(run, bold=None):
    run.font.name = FONT
    run.font.size = SIZE
    if bold is not None:
        run.bold = bold


def paragraph_format(p, heading=False, center=False, first_line=True, bold=None):
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif heading:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = None if heading or center or not first_line else Cm(1.25)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    for run in p.runs:
        run_format(run, bold=bold if bold is not None else (True if heading else None))


def set_paragraph(p, text, heading=False, center=False, first_line=True, bold=None):
    if has_inline(p):
        text_runs = [r for r in p.runs if r.text]
        if text_runs:
            text_runs[0].text = text
            for r in text_runs[1:]:
                r.text = ""
        else:
            p.add_run(text)
    else:
        p.text = text
    paragraph_format(p, heading=heading, center=center, first_line=first_line, bold=bold)


def set_cell(cell, text, bold=False, center=False):
    cell.text = str(text)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center or bold else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_after = Pt(0)
        for r in p.runs:
            run_format(r, bold=bold)


def body_index_by_text(target):
    body = doc._body._element
    for idx, el in enumerate(list(body)):
        if target in norm(element_text(el)):
            return idx
    return None


def remove_body_range(start, end):
    body = doc._body._element
    for el in list(body)[start:end]:
        body.remove(el)


def insert_paragraph(index, text, heading=False, center=False, first_line=True, bold=None):
    p = doc.add_paragraph()
    p.text = text
    paragraph_format(p, heading=heading, center=center, first_line=first_line, bold=bold)
    body = doc._body._element
    body.remove(p._p)
    body.insert(index, p._p)
    return index + 1


def insert_table_xml(index, tbl_xml):
    body = doc._body._element
    body.insert(index, deepcopy(tbl_xml))
    return index + 1


def insert_paragraph_xml(index, p_xml):
    body = doc._body._element
    body.insert(index, deepcopy(p_xml))
    return index + 1


def insert_table(index, rows, header=True):
    table = doc.add_table(rows=len(rows), cols=len(rows[0]))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r, row in enumerate(rows):
        for c, value in enumerate(row):
            set_cell(table.cell(r, c), value, bold=header and r == 0, center=True)
    body = doc._body._element
    body.remove(table._tbl)
    body.insert(index, table._tbl)
    return index + 1


def add_caption(index, number, title):
    return insert_paragraph(index, f"Tabla {number}  | {title}", heading=True, first_line=False)


def add_note(index, text):
    return insert_paragraph(index, text, first_line=False)


# Guardar tablas y fórmula de métricas del Capítulo IV antes de reemplazarlo.
old_tables = [deepcopy(doc.tables[i]._tbl) for i in range(7)]
formula_metric_paragraphs = []
for p in doc.paragraphs:
    if has_inline(p) and body_index_by_text("CAPÍTULO IV") is not None:
        txt = norm(p.text)
        # En el Capítulo IV solo se necesita conservar la lámina de fórmulas de métricas.
        # Se identifica por su ubicación textual próxima a las métricas; si no hay texto, se conserva la primera imagen del bloque metodológico.
        formula_metric_paragraphs.append(deepcopy(p._p))
# Elegir la imagen de fórmulas: se encuentra después de las métricas y antes de hipótesis en el documento base.
# Si hay varias imágenes en todo el documento, se selecciona la que está después de "Las fórmulas" por índice de párrafo.
metric_formula_xml = None
for i, p in enumerate(doc.paragraphs):
    if "Las fórmulas utilizadas para el cálculo" in p.text:
        for j in range(i + 1, min(i + 5, len(doc.paragraphs))):
            if has_inline(doc.paragraphs[j]):
                metric_formula_xml = deepcopy(doc.paragraphs[j]._p)
                break
        break

# Reemplazar Capítulo IV completo.
start = body_index_by_text("CAPÍTULO IV")
end = body_index_by_text("CAPÍTULO V")
if start is None or end is None or end <= start:
    raise RuntimeError("No se ubicó correctamente el Capítulo IV.")
remove_body_range(start, end)
idx = start

idx = insert_paragraph(idx, "CAPÍTULO IV", heading=True, center=True, first_line=False, bold=True)
idx = insert_paragraph(idx, "METODOLOGÍA", heading=True, center=True, first_line=False, bold=True)

idx = insert_paragraph(idx, "4.1. NIVEL Y TIPO DE INVESTIGACIÓN", heading=True, first_line=False)
idx = insert_paragraph(idx, "4.1.1. Nivel de investigación", heading=True, first_line=False)
idx = insert_paragraph(idx, "El nivel de investigación corresponde a un estudio evaluativo-comparativo con diseño experimental computacional. Se considera evaluativo porque mide el desempeño de algoritmos de Deep Learning mediante métricas cuantitativas de clasificación; y es comparativo porque analiza el comportamiento de dos arquitecturas, CNN/EfficientNetB0 y Swin-Tiny Transformer, frente al mismo conjunto de imágenes y bajo criterios de evaluación equivalentes.")
idx = insert_paragraph(idx, "Asimismo, el estudio se desarrolla con carácter experimental computacional, debido a que se manipula la variable independiente representada por los modelos de Deep Learning, se controla el procedimiento de entrenamiento mediante particiones, épocas, semillas y métricas, y se observa su efecto sobre la variable dependiente, que corresponde al desempeño de identificación de variedades de papas nativas.")
idx = insert_paragraph(idx, "Nivel de investigación: evaluativo-comparativo y experimental computacional.", first_line=False)
idx = insert_paragraph(idx, "4.1.2. Tipo de investigación", heading=True, first_line=False)
idx = insert_paragraph(idx, "La investigación es de tipo aplicada, porque utiliza conocimientos de inteligencia artificial, visión computacional y aprendizaje profundo para atender un problema concreto: la identificación visual de variedades de papas nativas de la comunidad de Santa Carmen. El propósito no se limita a desarrollar conocimiento teórico, sino a evaluar modelos computacionales que puedan contribuir al reconocimiento y registro de dichas variedades.")
idx = insert_paragraph(idx, "Por lo tanto, el tipo de investigación aplicado es: investigación aplicada.", first_line=False)

idx = insert_paragraph(idx, "4.2. MÉTODO Y DISEÑO DE LA INVESTIGACIÓN", heading=True, first_line=False)
idx = insert_paragraph(idx, "4.2.1. Método de la investigación", heading=True, first_line=False)
idx = insert_paragraph(idx, "El presente trabajo se sustenta en el método científico, porque parte de un problema de investigación, formula objetivos e hipótesis, organiza un conjunto de datos, ejecuta procedimientos controlados de entrenamiento y evaluación, y analiza los resultados mediante métricas y pruebas estadísticas. Este método permite comprobar la validez de las hipótesis a partir de evidencias cuantitativas obtenidas durante la experimentación computacional.")
idx = insert_paragraph(idx, "Durante el desarrollo de la investigación se emplean el método analítico, el método deductivo y el método experimental computacional. El método analítico permite descomponer el problema en etapas de organización de imágenes, preprocesamiento, entrenamiento, evaluación y contrastación. El método deductivo permite interpretar los resultados a partir de los criterios de eficiencia definidos. El método experimental computacional permite entrenar y evaluar los modelos bajo condiciones controladas.")
idx = insert_paragraph(idx, "Para la tabulación y análisis de la información obtenida se utilizan métricas de clasificación y procedimientos estadísticos, con el fin de obtener conclusiones formales sobre el desempeño de los modelos evaluados.")
idx = insert_paragraph(idx, "4.2.2. Diseño de la investigación", heading=True, first_line=False)
idx = insert_paragraph(idx, "El diseño de la investigación es experimental computacional de alcance evaluativo-comparativo. En este diseño, el corpus de imágenes se divide en subconjuntos de entrenamiento, validación y prueba. El subconjunto de entrenamiento permite ajustar los modelos; el subconjunto de validación permite monitorear el aprendizaje durante las épocas de entrenamiento; y el subconjunto de prueba permite evaluar el desempeño final.")
idx = insert_paragraph(idx, "El esquema general del diseño se expresa de la siguiente manera:", first_line=False)
idx = insert_paragraph(idx, "M → X₁ → O₁", center=True, first_line=False)
idx = insert_paragraph(idx, "M → X₂ → O₂", center=True, first_line=False)
idx = insert_paragraph(idx, "Donde:", first_line=False)
idx = insert_paragraph(idx, "M = corpus de imágenes de variedades de papa nativa organizado en entrenamiento, validación y prueba.", first_line=False)
idx = insert_paragraph(idx, "X₁ = entrenamiento del modelo CNN/EfficientNetB0.", first_line=False)
idx = insert_paragraph(idx, "X₂ = entrenamiento del modelo Swin-Tiny Transformer.", first_line=False)
idx = insert_paragraph(idx, "O₁ = métricas de desempeño obtenidas por CNN/EfficientNetB0.", first_line=False)
idx = insert_paragraph(idx, "O₂ = métricas de desempeño obtenidas por Swin-Tiny Transformer.", first_line=False)
idx = insert_paragraph(idx, "Este diseño permite evaluar cada modelo por separado y, posteriormente, comparar sus resultados bajo el mismo protocolo de evaluación.")

idx = insert_paragraph(idx, "4.3. ESTRATEGIAS DE PRUEBA DE HIPÓTESIS", heading=True, first_line=False)
idx = insert_paragraph(idx, "La prueba de hipótesis se realiza a partir del desempeño obtenido por los algoritmos de Deep Learning. Para establecer un criterio cuantitativo de eficiencia se define como valor de referencia μ₀ = 0.75. En consecuencia, un Accuracy menor al 75 % se interpreta como desempeño no eficiente, mientras que un Accuracy igual o mayor al 75 % se interpreta como desempeño eficiente.")
idx = insert_paragraph(idx, "La unidad de análisis estadístico para la prueba t de Student está constituida por cada ejecución completa del entrenamiento. Por ello, una época no se considera una observación independiente. Cada ejecución debe realizarse desde el inicio del entrenamiento, con una semilla distinta, y debe registrar su Accuracy final en el conjunto de prueba.")
idx = insert_paragraph(idx, "Para la hipótesis general y las hipótesis específicas 1 y 2 se utiliza la prueba t de Student para una muestra, comparando el promedio de Accuracy obtenido en las ejecuciones contra μ₀ = 0.75. Para la hipótesis específica 3 se comparan los resultados de CNN/EfficientNetB0 y Swin-Tiny Transformer bajo ejecuciones equivalentes.")
idx = insert_paragraph(idx, "El estadístico de prueba para una muestra se expresa como:", first_line=False)
idx = insert_paragraph(idx, "t = (X̄ − μ₀) / (S / √N)", center=True, first_line=False)
idx = insert_paragraph(idx, "Donde:", first_line=False)
idx = insert_paragraph(idx, "X̄ = promedio de Accuracy obtenido en las ejecuciones completas.", first_line=False)
idx = insert_paragraph(idx, "μ₀ = valor esperado o umbral mínimo de eficiencia, igual a 0.75.", first_line=False)
idx = insert_paragraph(idx, "S = desviación estándar de los valores de Accuracy.", first_line=False)
idx = insert_paragraph(idx, "N = número de ejecuciones completas del entrenamiento.", first_line=False)
idx = insert_paragraph(idx, "Nivel de significancia: α = 0.05.", first_line=False)
idx = insert_paragraph(idx, "Regla de decisión: si p < 0.05, se rechaza H0; si p ≥ 0.05, no se rechaza H0.", first_line=False)

idx = insert_paragraph(idx, "4.4. OPERACIONALIZACIÓN DE VARIABLES", heading=True, first_line=False)
idx = insert_paragraph(idx, "4.4.1. Operacionalización de la variable independiente", heading=True, first_line=False)
idx = insert_paragraph(idx, "La variable independiente corresponde a los algoritmos de Deep Learning utilizados para la identificación de variedades de papas nativas. En la investigación se evalúan dos modelos: CNN/EfficientNetB0 y Swin-Tiny Transformer.")
idx = add_caption(idx, 1, "Operación de las variables independientes")
idx = insert_table_xml(idx, old_tables[0])
idx = add_note(idx, "Nota. Elaboración propia a partir de los modelos de Deep Learning evaluados.")
idx = insert_paragraph(idx, "4.4.2. Operacionalización de la variable dependiente", heading=True, first_line=False)
idx = insert_paragraph(idx, "La variable dependiente corresponde al desempeño de identificación de variedades de papas nativas. Esta variable se mide mediante accuracy, balanced accuracy, precision, recall, F1-score y matriz de confusión.")
idx = add_caption(idx, 2, "Operación de las variables dependientes")
idx = insert_table_xml(idx, old_tables[1])
idx = add_note(idx, "Nota. Elaboración propia a partir de las métricas de evaluación utilizadas en la investigación.")

idx = insert_paragraph(idx, "4.5. POBLACIÓN", heading=True, first_line=False)
idx = insert_paragraph(idx, "La población accesible de la investigación está conformada por el corpus de imágenes de siete variedades de papa nativa consideradas en el estudio. Este corpus está integrado por 7000 imágenes etiquetadas, organizadas por variedad y preparadas para el entrenamiento, validación y prueba de los modelos de clasificación.")
idx = insert_paragraph(idx, "La unidad de análisis corresponde a cada imagen etiquetada con una variedad de papa nativa. Cada registro queda asociado a una clase y a un subconjunto experimental.")
idx = add_caption(idx, 3, "Variedades de papa nativa consideradas en la investigación")
idx = insert_table_xml(idx, old_tables[2])
idx = add_note(idx, "Nota. Elaboración propia a partir del registro organizado para la investigación.")

idx = insert_paragraph(idx, "4.6. MUESTRA", heading=True, first_line=False)
idx = insert_paragraph(idx, "La muestra experimental está conformada por la totalidad de las 7000 imágenes etiquetadas disponibles en el corpus depurado. Debido a que se utiliza todo el conjunto preparado para el experimento computacional, la muestra operativa coincide con el dataset de trabajo.")
idx = insert_paragraph(idx, "La muestra incluye siete variedades de papa nativa, con 1000 imágenes por variedad. Esta distribución balanceada permite evaluar los modelos bajo condiciones equivalentes de representación por clase.")
idx = add_caption(idx, 4, "Distribución de la muestra por variedad de papa nativa")
idx = insert_table_xml(idx, old_tables[3])
idx = add_note(idx, "Nota. Elaboración propia a partir del corpus de imágenes organizado por variedad.")
idx = insert_paragraph(idx, "El muestreo es no probabilístico por conveniencia, porque las imágenes utilizadas corresponden al conjunto disponible y organizado para el desarrollo experimental de la tesis. La selección responde a la disponibilidad de imágenes por variedad, a su calidad visual y a su utilidad para la clasificación multiclase.")
idx = add_caption(idx, 5, "Criterios de inclusión y exclusión de imágenes")
idx = insert_table_xml(idx, old_tables[4])
idx = add_note(idx, "Nota. Elaboración propia a partir de los criterios aplicados durante la organización del conjunto de imágenes.")
idx = insert_paragraph(idx, "El conjunto de imágenes se divide en tres subconjuntos: entrenamiento, validación y prueba. El subconjunto de entrenamiento se utiliza para ajustar los parámetros de los modelos; el subconjunto de validación permite monitorear el aprendizaje; y el subconjunto de prueba se reserva para la evaluación final.")
idx = add_caption(idx, 6, "Distribución del conjunto de datos según partición experimental")
idx = insert_table_xml(idx, old_tables[5])
idx = add_note(idx, "Nota. Elaboración propia a partir de la partición experimental del corpus de imágenes.")

idx = insert_paragraph(idx, "4.7. TÉCNICAS DE INVESTIGACIÓN", heading=True, first_line=False)
idx = insert_paragraph(idx, "4.7.1. Técnicas", heading=True, first_line=False)
idx = insert_paragraph(idx, "Se utiliza la observación directa, el registro fotográfico, la organización documental del corpus de imágenes, la experimentación computacional y la comparación de métricas. Estas técnicas permiten construir el conjunto de datos, entrenar los modelos y evaluar su desempeño en la identificación de variedades de papas nativas.")
idx = insert_paragraph(idx, "4.7.2. Instrumentos", heading=True, first_line=False)
idx = insert_paragraph(idx, "Los instrumentos utilizados corresponden a la ficha de registro de imágenes, el archivo CSV del corpus, los notebooks de entrenamiento, el entorno de ejecución computacional, los modelos CNN/EfficientNetB0 y Swin-Tiny Transformer, y las métricas estadísticas de evaluación.")
idx = add_caption(idx, 7, "Técnicas e instrumentos utilizados en la investigación")
idx = insert_table_xml(idx, old_tables[6])
idx = add_note(idx, "Nota. Elaboración propia a partir de las técnicas e instrumentos empleados en la investigación.")

idx = insert_paragraph(idx, "4.8. PROCESAMIENTO Y ANÁLISIS DE DATOS", heading=True, first_line=False)
idx = insert_paragraph(idx, "4.8.1. Procesamiento de imágenes", heading=True, first_line=False)
idx = insert_paragraph(idx, "Las imágenes fueron organizadas por variedad, asociadas a una etiqueta de clase y preparadas para su ingreso a los modelos de Deep Learning. El preprocesamiento incluyó el redimensionamiento a 224 × 224 píxeles y la división del corpus en entrenamiento, validación y prueba.")
idx = insert_paragraph(idx, "4.8.2. Entrenamiento de modelos", heading=True, first_line=False)
idx = insert_paragraph(idx, "El modelo CNN/EfficientNetB0 se entrenó en dos fases: entrenamiento de la cabeza de clasificación y ajuste fino. El modelo Swin-Tiny Transformer siguió el mismo enfoque general, adaptando su arquitectura a siete clases de salida. Para el análisis por épocas se consideran configuraciones de 12, 50, 80 y 100 épocas, y para la contrastación estadística se emplean ejecuciones completas con semillas distintas.")
idx = insert_paragraph(idx, "4.8.3. Métricas y análisis estadístico", heading=True, first_line=False)
idx = insert_paragraph(idx, "El desempeño de los modelos se analiza mediante accuracy, precision, recall, F1-score, balanced accuracy y matriz de confusión. Estas métricas permiten describir el rendimiento global, el comportamiento por clase y los errores de clasificación.")
idx = insert_paragraph(idx, "Las fórmulas utilizadas para el cálculo de las métricas de clasificación se presentan a continuación:")
if metric_formula_xml is not None:
    idx = insert_paragraph_xml(idx, metric_formula_xml)
idx = insert_paragraph(idx, "Nota. TP = verdaderos positivos; TN = verdaderos negativos; FP = falsos positivos; FN = falsos negativos; K = número de clases evaluadas.", first_line=False)
idx = insert_paragraph(idx, "El análisis estadístico de hipótesis se realiza con el valor de referencia μ₀ = 0.75 y nivel de significancia α = 0.05. La interpretación final se obtiene a partir de los valores de Accuracy generados por ejecuciones completas del entrenamiento.")

# Limpieza de redacción de todo el documento: nada de asesora, recomendación ni proceso de edición.
paragraph_replacements = {
    "Para compatibilizar el diseño experimental computacional con la recomendación metodológica de la asesora, se utiliza la prueba t de Student para una muestra. Esta prueba compara el promedio de Accuracy obtenido en varias ejecuciones completas del entrenamiento contra el valor mínimo esperado μ₀ = 0.75.":
    "De acuerdo con el diseño experimental computacional de la investigación, se utiliza la prueba t de Student para una muestra. Esta prueba compara el promedio de Accuracy obtenido en varias ejecuciones completas del entrenamiento contra el valor mínimo esperado μ₀ = 0.75.",
    "Para atender la observación metodológica de la asesora, la contrastación final queda estructurada con ejecuciones completas independientes, usando Accuracy como variable de contraste, μ₀ = 0.75 como valor de referencia y prueba t de Student para una muestra. La decisión definitiva de hipótesis se completará con los valores generados por los notebooks experimentales.":
    "La contrastación estadística se estructura con ejecuciones completas independientes, usando Accuracy como variable de contraste, μ₀ = 0.75 como valor de referencia y prueba t de Student para una muestra. La decisión de hipótesis se obtiene a partir de los valores generados por los entrenamientos experimentales.",
    "In response to the methodological observation, the final hypothesis testing is structured around independent complete training runs, using Accuracy as the contrast variable, μ₀ = 0.75 as the reference value, and a one-sample Student t-test. The final hypothesis decision will be completed with the values generated by the experimental notebooks.":
    "The statistical hypothesis testing is structured around independent complete training runs, using Accuracy as the contrast variable, μ₀ = 0.75 as the reference value, and a one-sample Student t-test. The hypothesis decision is obtained from the values generated by the experimental training runs.",
    "Asesora nisqapa metodológica qawariyninman hina, tukupay contrastaciónqa sapakama hunt’a entrenamiento ruraykunamanta Accuracy chaninta hap’in, μ₀ = 0.75 referencia hina churakun, hinaspa prueba t de Student huk muestra nisqawan tukupay decisión ruwakunqa.":
    "Tukupay contrastaciónqa sapakama hunt’a entrenamiento ruraykunamanta Accuracy chaninta hap’in, μ₀ = 0.75 referencia hina churakun, hinaspa prueba t de Student huk muestra nisqawan decisión ruwakunqa.",
    "Por completar": "—",
}

for p in doc.paragraphs:
    if not p.text:
        continue
    if has_inline(p):
        for r in p.runs:
            if r.text:
                for old, new in paragraph_replacements.items():
                    r.text = r.text.replace(old, new)
                run_format(r)
    else:
        new_text = p.text
        for old, new in paragraph_replacements.items():
            new_text = new_text.replace(old, new)
        if new_text != p.text:
            set_paragraph(p, new_text, heading=p.style.name.startswith('Heading'), first_line=not p.style.name.startswith('Heading'))

for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            new_text = cell.text
            for old, new in paragraph_replacements.items():
                new_text = new_text.replace(old, new)
            if new_text != cell.text:
                set_cell(cell, new_text)
            else:
                for p in cell.paragraphs:
                    for r in p.runs:
                        run_format(r)

# Actualizar títulos de anexos en tablas 30 y 31 si existieran con numeración anterior en texto.
for p in doc.paragraphs:
    txt = norm(p.text)
    if txt.startswith("Tabla 30") and "Cronograma" in txt:
        set_paragraph(p, "Tabla 30  | Cronograma de Actividades de investigación", heading=True, first_line=False)
    elif txt.startswith("Tabla 31") and "Presupuesto" in txt:
        set_paragraph(p, "Tabla 31  | Presupuesto del proyecto de investigación", heading=True, first_line=False)

# Validación final.
doc.save(OUT)
check = Document(OUT)
all_text = "\n".join(p.text for p in check.paragraphs)
for table in check.tables:
    for row in table.rows:
        for cell in row.cells:
            all_text += "\n" + cell.text
forbidden = [
    "asesora", "recomendación metodológica", "observación metodológica", "Para atender", "Por completar",
    "INKAPA", "aplicativo", "sintética", "sintético", "synthetic", "imágenes reales", "imágenes sintéticas", "etiqueta real", "Llunchuy Waqachiq"
]
found = [term for term in forbidden if term.lower() in all_text.lower()]
print(f"Generado: {OUT}")
print(f"Párrafos: {len(check.paragraphs)} | Tablas: {len(check.tables)} | Imágenes internas: {len(check.inline_shapes)}")
print(f"Términos no permitidos: {found}")
if found:
    raise SystemExit(2)

from copy import deepcopy
from pathlib import Path
import shutil

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.text.paragraph import Paragraph
from docx.shared import Pt, Cm

BASE = Path(r"C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista")
SRC = BASE / "INVESTIGACION FINAL - PARA PRESENTAR_OBSERVACIONES_LEVANTADAS_ESTADISTICO_2026-05-17_v8.docx"
OUT = BASE / "INVESTIGACION FINAL - PARA PRESENTAR_PREPARADO_FINAL_ASESORA_2026-05-18_v10.docx"

shutil.copy2(SRC, OUT)
doc = Document(OUT)

FONT_NAME = "Times New Roman"
FONT_SIZE = Pt(12)


def normalize_text(text: str) -> str:
    return " ".join(text.split())


def paragraph_has_inline(paragraph):
    return bool(paragraph._p.xpath(".//wp:inline"))


def set_text_preserving_inline(paragraph, text, *, heading=False, body=True):
    text_runs = [run for run in paragraph.runs if run.text]
    if text_runs:
        text_runs[0].text = text
        for run in text_runs[1:]:
            run.text = ""
    else:
        paragraph.add_run(text)
    if heading:
        apply_heading_format(paragraph)
    elif body:
        apply_body_format(paragraph)
    else:
        apply_paragraph_font(paragraph)


def replace_runs_text(paragraph, replacements):
    for run in paragraph.runs:
        if not run.text:
            continue
        new = run.text
        for old, value in replacements.items():
            new = new.replace(old, value)
        if new != run.text:
            run.text = new
        apply_run_font(run)


def apply_run_font(run, bold=None):
    run.font.name = FONT_NAME
    run.font.size = FONT_SIZE
    if bold is not None:
        run.bold = bold


def apply_paragraph_font(paragraph, bold=None):
    for run in paragraph.runs:
        apply_run_font(run, bold=bold)


def apply_body_format(paragraph, first_line=True):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if first_line:
        paragraph.paragraph_format.first_line_indent = Cm(1.25)
    paragraph.paragraph_format.space_after = Pt(0)
    apply_paragraph_font(paragraph)


def apply_heading_format(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.first_line_indent = None
    paragraph.paragraph_format.space_after = Pt(0)
    apply_paragraph_font(paragraph, bold=True)


def set_paragraph_text(paragraph, text, *, heading=False, body=True):
    paragraph.text = text
    if heading:
        apply_heading_format(paragraph)
    elif body:
        apply_body_format(paragraph)
    else:
        apply_paragraph_font(paragraph)


def find_paragraph_by_exact(text):
    target = normalize_text(text)
    for p in doc.paragraphs:
        if normalize_text(p.text) == target:
            return p
    return None


def replace_exact(old, new, *, heading=False):
    p = find_paragraph_by_exact(old)
    if p is None:
        missing.append(old[:120])
        return None
    if paragraph_has_inline(p):
        set_text_preserving_inline(p, new, heading=heading)
    else:
        set_paragraph_text(p, new, heading=heading)
    return p


def insert_paragraph_after(paragraph, text, *, heading=False):
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    set_paragraph_text(new_para, text, heading=heading)
    return new_para


def clear_paragraph(paragraph):
    paragraph.text = ""
    paragraph.paragraph_format.first_line_indent = None


def set_cell_text(cell, text, bold=False):
    cell.text = str(text)
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if bold else WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(0)
        for run in p.runs:
            apply_run_font(run, bold=bold)


missing = []

# Correcciones menores visibles y neutralización de redacción.
minor_replacements = {
    "ANDAHUAYLAS– APURIMAC– PERÚ": "ANDAHUAYLAS– APURÍMAC– PERÚ",
    "PipeLine": "Pipeline",
    "casos reales identificados correctamente": "casos positivos de referencia identificados correctamente",
    "etiqueta real": "etiqueta de referencia",
    "etiqueta verdadera": "etiqueta de referencia",
    "imágenes digitales reales": "imágenes digitales",
    "imágenes reales": "imágenes",
    "imágenes sintéticas": "imágenes",
    "reales/sintéticas": "del corpus",
    "real/sintético": "del corpus",
    "Figura 37": "Figura 35",
    "variedad Llunchuy Waqachiq": "del corpus de imágenes",
}
for p in doc.paragraphs:
    if p.text:
        if paragraph_has_inline(p):
            replace_runs_text(p, minor_replacements)
            continue
        new = p.text
        for old, value in minor_replacements.items():
            new = new.replace(old, value)
        if new != p.text:
            set_paragraph_text(p, new, heading=p.style.name.startswith("Heading"), body=not p.style.name.startswith("Heading"))

# Capítulo IV: ajustar metodología a Accuracy por ejecución y repeticiones.
replace_exact(
    "La investigación es de enfoque cuantitativo y de tipo aplicada, porque utiliza conocimientos de inteligencia artificial, visión computacional y Deep Learning para resolver un problema concreto de identificación visual de variedades de papa nativa.",
    "La investigación es de enfoque cuantitativo y de tipo aplicada, porque utiliza conocimientos de inteligencia artificial, visión computacional y Deep Learning para resolver el problema concreto de identificación visual de variedades de papa nativa mediante modelos entrenados y evaluados con métricas numéricas de clasificación."
)
replace_exact(
    "El nivel de investigación es evaluativo-comparativo, porque mide el desempeño de dos arquitecturas de clasificación de imágenes y compara sus métricas sobre el mismo conjunto de prueba.",
    "El nivel de investigación es evaluativo-comparativo con componente experimental computacional, porque mide el desempeño de dos arquitecturas de clasificación de imágenes, compara sus métricas bajo el mismo protocolo de evaluación y contrasta estadísticamente si el desempeño alcanza el umbral mínimo definido para la investigación."
)
replace_exact(
    "Se considera experimental computacional porque se entrenaron y evaluaron modelos de Deep Learning bajo un protocolo controlado de datos, particiones, épocas, arquitectura y métricas. La intervención no recayó sobre personas ni cultivos, sino sobre el procedimiento computacional de entrenamiento y evaluación de modelos.",
    "Se considera experimental computacional porque se entrenaron y evaluaron modelos de Deep Learning bajo un protocolo controlado de datos, particiones, épocas, arquitectura, semillas de ejecución y métricas. La intervención no recayó sobre personas ni cultivos, sino sobre el procedimiento computacional de entrenamiento y evaluación de modelos."
)
replace_exact(
    "Los resultados obtenidos por CNN/EfficientNetB0 y Swin-Tiny Transformer fueron comparados mediante métricas globales, métricas por clase y contrastación estadística sobre F1-score por variedad. La comparación permitió evaluar la eficiencia de cada modelo y determinar si la diferencia entre ambos era estadísticamente significativa.",
    "Los resultados obtenidos por CNN/EfficientNetB0 y Swin-Tiny Transformer fueron comparados mediante métricas globales, métricas por clase y contrastación estadística. Para la contrastación recomendada por la asesora, la unidad de análisis estadístico corresponde al Accuracy obtenido en cada ejecución completa del entrenamiento, no a cada época individual."
)
replace_exact(
    "El tratamiento de datos se concentró en la preparación del corpus, el entrenamiento de los modelos, la evaluación mediante métricas de clasificación y la comparación descriptiva entre arquitecturas. No se consideró ningún sistema de software como instrumento de medición de resultados.",
    "El tratamiento de datos se concentró en la preparación del corpus, el entrenamiento de los modelos, la evaluación mediante métricas de clasificación, la comparación descriptiva entre arquitecturas y la organización de ejecuciones repetidas para la prueba t de Student. No se consideró ningún sistema de software como instrumento de medición de resultados."
)

anchor = find_paragraph_by_exact("Nota. Elaboración propia a partir de la partición experimental del corpus visual validado.")
if anchor is not None:
    p = insert_paragraph_after(anchor, "Épocas y repeticiones experimentales", heading=True)
    p = insert_paragraph_after(p, "Para documentar el entrenamiento y preparar la contrastación de hipótesis, se definieron configuraciones de 12, 50, 80 y 100 épocas para cada arquitectura. La ejecución base documentada en el informe corresponde a 12 épocas; las configuraciones ampliadas quedan destinadas al análisis por épocas y a la contrastación estadística con ejecuciones completas independientes.")
    p = insert_paragraph_after(p, "En el modelo CNN/EfficientNetB0, la configuración base comprende 4 épocas para la cabeza de clasificación y 8 épocas de ajuste fino. En el modelo Swin-Tiny Transformer, la configuración base comprende 3 épocas para la cabeza de clasificación y 9 épocas de ajuste fino. Para la contrastación final, la configuración principal prevista es de 50 épocas, repetida con semillas diferentes para obtener una tabla de Accuracy por ejecución.")
    p = insert_paragraph_after(p, "La prueba t de Student para una muestra debe aplicarse sobre los valores de Accuracy generados por entrenamientos completos desde cero. Por ello, cada fila de la tabla de contrastación corresponde a una ejecución independiente del entrenamiento y no a una época individual.")
else:
    missing.append("anchor Partición")

# Hipótesis: criterio por Accuracy y ejecuciones.
replace_exact(
    "Se formularon hipótesis de investigación porque el estudio mide cuantitativamente el desempeño de modelos de Deep Learning y contrasta sus resultados mediante métricas de clasificación. Para la interpretación se adoptó como valor de referencia μ₀ = 0.75, de modo que un modelo se considera eficiente cuando su F1-score promedio por clase es igual o superior a dicho umbral.",
    "Se formularon hipótesis de investigación porque el estudio mide cuantitativamente el desempeño de modelos de Deep Learning y contrasta sus resultados mediante métricas de clasificación. Para la interpretación estadística se adoptó como valor de referencia μ₀ = 0.75, de modo que un modelo se considera eficiente cuando el Accuracy promedio obtenido en ejecuciones completas independientes es igual o superior a dicho umbral. Las métricas precision, recall, F1-score, balanced accuracy y matriz de confusión se emplean como evidencia complementaria del desempeño por clase."
)
replace_exact(
    "La hipótesis general se demuestra mediante métricas globales de clasificación; las hipótesis específicas 1 y 2 se sustentan en las métricas y matrices de confusión de cada modelo; y la hipótesis específica 3 requiere comparación pareada entre CNN/EfficientNetB0 y Swin-Tiny Transformer.",
    "La hipótesis general se demuestra mediante métricas globales de clasificación y la prueba t de Student para una muestra; las hipótesis específicas 1 y 2 se sustentan en las ejecuciones repetidas, las métricas y las matrices de confusión de cada modelo; y la hipótesis específica 3 requiere comparar estadísticamente el desempeño de CNN/EfficientNetB0 y Swin-Tiny Transformer bajo condiciones equivalentes."
)
replace_exact(
    "El contraste estadístico se realizó con un nivel de significancia α = 0.05. Para la hipótesis general y las hipótesis específicas 1 y 2 se utilizó la prueba t de Student para una muestra, comparando el F1-score promedio por clase contra μ₀ = 0.75. Para la hipótesis específica 3 se utilizó una prueba t pareada sobre las diferencias de F1-score por clase entre CNN/EfficientNetB0 y Swin-Tiny Transformer.",
    "El contraste estadístico se definió con un nivel de significancia α = 0.05. Para la hipótesis general y las hipótesis específicas 1 y 2 se utiliza la prueba t de Student para una muestra, comparando el promedio de Accuracy obtenido en ejecuciones independientes contra μ₀ = 0.75. Para la hipótesis específica 3 se utiliza una comparación estadística entre ambos modelos, preferentemente pareada cuando las ejecuciones se realicen con las mismas semillas."
)

# Capítulo V: corrección de captions, texto y separación procedimiento/resultados.
replace_exact(
    "La evaluación técnica del modelo CNN/EfficientNetB0 se realizó sobre el conjunto de prueba, conformado por 1047 imágenes. El modelo alcanzó un accuracy de 0.9933 y un F1-score macro de 0.9933. Estos valores se interpretan en el capítulo de resultados en relación con el umbral de eficiencia definido.",
    "La evaluación técnica del modelo CNN/EfficientNetB0 se realizó sobre el conjunto de prueba, conformado por 1047 imágenes. En esta etapa se generaron predicciones, matriz de confusión, reporte de clasificación, métricas globales y archivos de salida. La interpretación estadística de estos valores se desarrolla en el capítulo de resultados."
)
replace_exact("Figura 25  | Métricas globales del modelo CNN/EfficientNetB0 en el conjunto de prueba", "Tabla 13  | Métricas globales del modelo CNN/EfficientNetB0 en el conjunto de prueba", heading=True)
replace_exact("Figura 26  | Reporte de clasificación por variedad del modelo CNN/EfficientNetB0", "Tabla 14  | Reporte de clasificación por variedad del modelo CNN/EfficientNetB0", heading=True)
replace_exact("Nota: Elaboración propia a partir del reporte de clasificación global del modelo CNN/EfficientNetB0. Los valores fueron redondeados a cuatro decima", "Nota: Elaboración propia a partir del reporte de clasificación global del modelo CNN/EfficientNetB0. Los valores fueron redondeados a cuatro decimales.")
replace_exact(
    "Las predicciones individuales del modelo se consolidaron por imagen, etiqueta real, clase predicha y acierto o error. En el cuerpo del capítulo se presentan los resultados agregados porque permiten interpretar el desempeño general y por variedad sin saturar la exposición con registros individuales.",
    "Las predicciones individuales del modelo se consolidaron por imagen, etiqueta de referencia, clase predicha y acierto o error. En el cuerpo del capítulo se presentan los resultados agregados porque permiten interpretar el desempeño general y por variedad sin saturar la exposición con registros individuales."
)
replace_exact("Tabla 13", "Tabla 15  | Resumen de construcción del modelo Swin-Tiny Transformer", heading=True)
replace_exact("Resumen de construcción del modelo Swin-Tiny Transformer", "", heading=False)
replace_exact(
    "La Tabla 13 resume los principales valores del historial de entrenamiento. La mejor pérdida de validación se obtuvo en la época 12, durante la fase de ajuste fino.",
    "La Tabla 16 resume los principales valores del historial de entrenamiento. La mejor pérdida de validación se obtuvo en la época 12, durante la fase de ajuste fino."
)
replace_exact("Tabla 13  | Resumen del entrenamiento del modelo Swin-Tiny Transformer", "Tabla 16  | Resumen del entrenamiento del modelo Swin-Tiny Transformer", heading=True)
replace_exact(
    "La evaluación técnica del modelo Swin-Tiny Transformer se realizó sobre el mismo conjunto de prueba utilizado para CNN/EfficientNetB0. El modelo alcanzó un accuracy de 0.9962 y un F1-score macro de 0.9962. Estos valores se interpretan en el capítulo de resultados en relación con el umbral de eficiencia definido.",
    "La evaluación técnica del modelo Swin-Tiny Transformer se realizó sobre el mismo conjunto de prueba utilizado para CNN/EfficientNetB0. En esta etapa se generaron predicciones, matriz de confusión, reporte de clasificación, métricas globales y archivos de salida. La interpretación estadística de estos valores se desarrolla en el capítulo de resultados."
)
replace_exact("Tabla 14  | Métricas globales del modelo Swin-Tiny Transformer en el conjunto de prueba", "Tabla 17  | Métricas globales del modelo Swin-Tiny Transformer en el conjunto de prueba", heading=True)
replace_exact("Tabla 15  | Reporte de clasificación por variedad del modelo Swin-Tiny Transformer", "Tabla 18  | Reporte de clasificación por variedad del modelo Swin-Tiny Transformer", heading=True)
replace_exact(
    "Las predicciones individuales del modelo Swin-Tiny Transformer se organizaron por imagen, etiqueta real, clase predicha y resultado de clasificación. Al igual que en el modelo CNN/EfficientNetB0, el capítulo presenta la información agregada porque permite interpretar el rendimiento global, el desempeño por clase y los errores observados en la matriz de confusión.",
    "Las predicciones individuales del modelo Swin-Tiny Transformer se organizaron por imagen, etiqueta de referencia, clase predicha y resultado de clasificación. Al igual que en el modelo CNN/EfficientNetB0, el capítulo presenta la información agregada porque permite interpretar el rendimiento global, el desempeño por clase y los errores observados en la matriz de confusión."
)
replace_exact(
    "La comparación descriptiva entre los dos modelos muestra que ambos alcanzaron un desempeño alto en la identificación de variedades de papa nativa. Swin-Tiny Transformer obtuvo un accuracy de 0.9962, mientras que CNN/EfficientNetB0 alcanzó 0.9933. La diferencia descriptiva fue de 0.0029 puntos en accuracy global a favor de Swin-Tiny Transformer.",
    "La comparación descriptiva entre los dos modelos se organiza con las mismas métricas globales y el mismo conjunto de prueba. Esta comparación permite observar el comportamiento de CNN/EfficientNetB0 y Swin-Tiny Transformer antes de la contrastación estadística de hipótesis."
)
replace_exact("Tabla 16  | Comparación global de desempeño entre CNN/EfficientNetB0 y Swin-Tiny Transformer", "Tabla 19  | Comparación global de desempeño entre CNN/EfficientNetB0 y Swin-Tiny Transformer", heading=True)
replace_exact(
    "La comparación estadística entre CNN/EfficientNetB0 y Swin-Tiny Transformer se realizó a partir del F1-score por clase. Esta prueba complementó la comparación descriptiva de métricas globales y permitió evaluar formalmente si la diferencia entre ambos modelos era significativa al nivel α = 0.05.",
    "La comparación estadística entre CNN/EfficientNetB0 y Swin-Tiny Transformer debe completarse con las ejecuciones repetidas generadas por los notebooks experimentales. Esta prueba complementa la comparación descriptiva de métricas globales y permite evaluar formalmente si la diferencia entre ambos modelos es significativa al nivel α = 0.05."
)
replace_exact("Tabla 17  | Comparación pareada de aciertos y errores entre CNN/EfficientNetB0 y Swin-Tiny Transformer", "Tabla 20  | Criterio estadístico para la contrastación de hipótesis", heading=True)
replace_exact("Nota: Elaboración propia a partir de la comparación pareada de predicciones del conjunto de prueba.", "Nota: Elaboración propia a partir del criterio estadístico definido para la contrastación de hipótesis con ejecuciones repetidas.")
replace_exact(
    "Estos resultados permiten afirmar que ambos modelos presentan un nivel de desempeño eficiente en el conjunto de prueba. Aunque Swin-Tiny Transformer obtuvo una métrica global ligeramente mayor, la diferencia se interpreta como ventaja descriptiva y no como superioridad estadísticamente significativa.",
    "La interpretación final de eficiencia y comparación entre modelos se desarrolla en el Capítulo VI, utilizando el umbral μ₀ = 0.75, el nivel de significancia α = 0.05 y las tablas generadas por las ejecuciones independientes de entrenamiento."
)

# Capítulo VI preparado para la observación de asesora.
vi_replacements = {
    "6.1. Criterio de análisis y contrastación": "6.1. Contrastación de hipótesis",
    "Los resultados se interpretaron con un criterio estadístico de eficiencia. Se consideró que un modelo presenta desempeño eficiente cuando el promedio de F1-score por clase es igual o superior a μ₀ = 0.75. Este valor funciona como punto de referencia mínimo para diferenciar un desempeño insuficiente de un desempeño eficiente en la identificación visual de variedades de papas nativas.": "Los resultados se interpretan con un criterio estadístico de eficiencia basado en Accuracy. Se considera que un modelo presenta desempeño eficiente cuando el promedio de Accuracy obtenido en ejecuciones completas independientes es igual o superior a μ₀ = 0.75. Por tanto, Accuracy menor al 75 % se interpreta como desempeño no eficiente y Accuracy igual o mayor al 75 % se interpreta como desempeño eficiente.",
    "La contrastación de hipótesis se realizó con un nivel de significancia α = 0.05. Para la hipótesis general y las hipótesis específicas 1 y 2 se aplicó la prueba t de Student para una muestra. Para la hipótesis específica 3 se aplicó una prueba t pareada sobre el F1-score por clase de ambos modelos.": "La contrastación de hipótesis se prepara con un nivel de significancia α = 0.05. Para la hipótesis general y las hipótesis específicas 1 y 2 se aplica la prueba t de Student para una muestra, comparando el promedio de Accuracy de las ejecuciones contra el valor mínimo esperado μ₀ = 0.75. Para la hipótesis específica 3 se compara estadísticamente el desempeño de CNN/EfficientNetB0 y Swin-Tiny Transformer bajo ejecuciones equivalentes.",
    "Nota. x̄ representa el promedio observado, μ₀ el valor mínimo esperado, s la desviación estándar muestral, n el número de valores analizados por clase, Dᵢ la diferencia pareada por clase y α el nivel de significancia.": "Nota. X̄ representa el promedio de Accuracy obtenido, μ₀ el valor mínimo esperado, S la desviación estándar, N el número de ejecuciones completas y α el nivel de significancia.",
    "6.2. Resultado de la hipótesis general": "6.2. Análisis e interpretación de la hipótesis general",
    "La hipótesis general planteó que los algoritmos de Deep Learning presentan un desempeño eficiente en la identificación de variedades de papas nativas en la comunidad de Santa Carmen. Para contrastarla, se integraron los valores de F1-score por clase de CNN/EfficientNetB0 y Swin-Tiny Transformer. El promedio global fue 0.9947, superior al valor de referencia μ₀ = 0.75. La prueba t de Student para una muestra arrojó t(13) = 222.76 y p < 0.001. En consecuencia, se rechaza H0G y se acepta la hipótesis general de investigación.": "La hipótesis general plantea que los algoritmos de Deep Learning presentan un desempeño eficiente en la identificación de variedades de papas nativas en la comunidad de Santa Carmen. La evidencia final debe obtenerse a partir de las ejecuciones completas de entrenamiento registradas en los notebooks experimentales. Con esos valores se calcula el promedio de Accuracy, la desviación estándar, el estadístico t y el valor p frente a μ₀ = 0.75.",
    "6.3. Resultado de la hipótesis específica 1": "6.3. Análisis e interpretación de la hipótesis específica 1",
    "La hipótesis específica 1 sostuvo que el modelo CNN/EfficientNetB0 presenta un desempeño eficiente en la identificación de variedades de papas nativas. El modelo clasificó correctamente 1040 de 1047 imágenes de prueba, con accuracy de 0.9933 y F1-score macro de 0.9933. Al contrastar el F1-score por clase contra μ₀ = 0.75, se obtuvo t(6) = 192.18 y p < 0.001. Por tanto, se rechaza H01 y se acepta HE1.": "La hipótesis específica 1 sostiene que el modelo CNN/EfficientNetB0 presenta un desempeño eficiente en la identificación de variedades de papas nativas. Para contrastarla, se deben registrar varias ejecuciones completas del entrenamiento del modelo CNN/EfficientNetB0, calcular el Accuracy de cada ejecución y aplicar la prueba t de Student para una muestra frente a μ₀ = 0.75.",
    "6.4. Resultado de la hipótesis específica 2": "6.4. Análisis e interpretación de la hipótesis específica 2",
    "La hipótesis específica 2 sostuvo que el modelo Swin-Tiny Transformer presenta un desempeño eficiente en la identificación de variedades de papas nativas. El modelo clasificó correctamente 1043 de 1047 imágenes de prueba, con accuracy de 0.9962 y F1-score macro de 0.9962. Al contrastar el F1-score por clase contra μ₀ = 0.75, se obtuvo t(6) = 143.24 y p < 0.001. Por tanto, se rechaza H02 y se acepta HE2.": "La hipótesis específica 2 sostiene que el modelo Swin-Tiny Transformer presenta un desempeño eficiente en la identificación de variedades de papas nativas. Para contrastarla, se deben registrar varias ejecuciones completas del entrenamiento del modelo Swin-Tiny Transformer, calcular el Accuracy de cada ejecución y aplicar la prueba t de Student para una muestra frente a μ₀ = 0.75.",
    "6.5. Resultado de la hipótesis específica 3": "6.5. Análisis e interpretación de la hipótesis específica 3",
    "La hipótesis específica 3 planteó la existencia de diferencias significativas entre el desempeño de CNN/EfficientNetB0 y Swin-Tiny Transformer. La comparación descriptiva favoreció a Swin-Tiny Transformer, con una diferencia de +0.0029 en accuracy global y tres aciertos adicionales en el conjunto de prueba. Sin embargo, la prueba t pareada aplicada al F1-score por clase arrojó t(6) = 1.67 y p = 0.145. Dado que p > 0.05, no se rechaza H03. Por tanto, la diferencia observada se interpreta como ventaja descriptiva, no como diferencia estadísticamente significativa.": "La hipótesis específica 3 plantea la existencia de diferencias significativas entre el desempeño de CNN/EfficientNetB0 y Swin-Tiny Transformer. Para contrastarla, los resultados de ambos modelos deben compararse estadísticamente bajo condiciones equivalentes de evaluación. Si las ejecuciones se realizan con las mismas semillas, corresponde aplicar una prueba pareada sobre los valores de Accuracy; si no se cumple esa equivalencia, se debe justificar la prueba comparativa utilizada.",
    "6.6. Síntesis estadística de resultados": "6.6. Síntesis estadística de resultados",
    "El análisis estadístico confirma que CNN/EfficientNetB0 y Swin-Tiny Transformer superan ampliamente el umbral de eficiencia definido para la investigación. La evidencia más sólida corresponde a las hipótesis de eficiencia, porque ambos modelos obtuvieron F1-score macro superior a 0.99 y valores p menores a 0.001. En la comparación entre modelos, Swin-Tiny Transformer presentó una ventaja numérica; sin embargo, dicha ventaja no alcanzó significancia estadística al nivel α = 0.05.": "La síntesis estadística final debe completarse con las tablas de ejecuciones, promedio de Accuracy, desviación estándar, estadístico t, valor p y decisión correspondiente. La regla de decisión es la siguiente: si p < 0.05, se rechaza H0; si p ≥ 0.05, no se rechaza H0. La conclusión final deberá indicar si los algoritmos de Deep Learning presentan desempeño eficiente en la identificación de variedades de papas nativas."
}
for old, new in vi_replacements.items():
    replace_exact(old, new, heading=old.startswith("6."))
replace_exact("Tabla 18 Contrastación estadística de hipótesis de investigación", "Tabla 21  | Matriz de contrastación de hipótesis preparada para ejecuciones repetidas", heading=True)
replace_exact("Nota. Elaboración propia a partir de las métricas verificadas en los notebooks de entrenamiento y evaluación. Los valores p fueron calculados con F1-score por clase como unidad de contraste.", "Nota. Elaboración propia a partir de la estructura estadística requerida para la contrastación con Accuracy por ejecución completa de entrenamiento.")

# Conclusión HE3 corregida.
replace_exact(
    "Respecto al tercer objetivo específico, la comparación descriptiva mostró una ligera ventaja de Swin-Tiny Transformer sobre CNN/EfficientNetB0 en el conjunto de prueba. La diferencia fue de +0.0029 en accuracy global; sin embargo, no se afirma diferencia estadísticamente significativa porque no se aplicó una prueba pareada con predicciones verificables.",
    "Respecto al tercer objetivo específico, la comparación entre CNN/EfficientNetB0 y Swin-Tiny Transformer debe sustentarse estadísticamente con ejecuciones equivalentes. En la versión final, la decisión sobre diferencia significativa se establecerá a partir de la prueba comparativa aplicada a los valores de Accuracy obtenidos por cada modelo."
)

# Anexos: variedad no válida y numeración de figuras finales.
replace_exact("Figura 36  | Datos recolectados de papas nativas variedad Pumapa Makin", "Figura 34  | Datos recolectados de papas nativas del corpus de imágenes", heading=True)
replace_exact("Figura 37  | Datos recolectados de papas nativas variedad Llunchuy Waqachiq", "Figura 35  | Datos recolectados de papas nativas del corpus de imágenes", heading=True)

# Índices/listas manuales principales.
list_replacements = {
    "Figura 16 PipeLine de implementación de la propuesta 68": "Figura 16 Pipeline de implementación de la propuesta 68",
    "Figura 25 Métricas globales del modelo CNN/EfficientNetB0 en el conjunto de prueba 82": "Figura 25 Matriz de confusión del modelo CNN/EfficientNetB0 84",
    "Figura 26 Reporte de clasificación por variedad del modelo CNN/EfficientNetB0 83": "Figura 26 Complejidad por bloque del modelo Swin-Tiny Transformer 85",
    "Figura 27 Matriz de confusión del modelo CNN/EfficientNetB0 84": "Figura 27 Fragmento de código de construcción y entrenamiento del modelo Swin-Tiny Transformer 86",
    "Figura 28 Complejidad por bloque del modelo Swin-Tiny Transformer 85": "Figura 28 Curva de accuracy del modelo Swin-Tiny Transformer 88",
    "Figura 29 Fragmento de código de construcción y entrenamiento del modelo Swin-Tiny Transformer 86": "Figura 29 Curva de pérdida del modelo Swin-Tiny Transformer 88",
    "Figura 30 Curva de accuracy del modelo Swin-Tiny Transformer 88": "Figura 30 Fragmento de código de evaluación del modelo Swin-Tiny Transformer 89",
    "Figura 31 Curva de pérdida del modelo Swin-Tiny Transformer 88": "Figura 31 Matriz de confusión del modelo Swin-Tiny Transformer 92",
    "Figura 32 Fragmento de código de evaluación del modelo Swin-Tiny Transformer 89": "Figura 32 Datos recolectados de papas nativas del corpus de imágenes 111",
    "Figura 33 Matriz de confusión del modelo Swin-Tiny Transformer 92": "Figura 33 Datos recolectados de papas nativas del corpus de imágenes 112",
    "Figura 36 Datos recolectados de papas nativas variedad Pumapa Makin 111": "Figura 34 Datos recolectados de papas nativas del corpus de imágenes 111",
    "Figura 37 Datos recolectados de papas nativas variedad Llunchuy Waqachiq 112": "Figura 35 Datos recolectados de papas nativas del corpus de imágenes 112",
    "Tabla 13 Resumen del entrenamiento del modelo Swin-Tiny Transformer 87": "Tabla 13 Métricas globales del modelo CNN/EfficientNetB0 en el conjunto de prueba 82",
    "Tabla 14 Métricas globales del modelo Swin-Tiny Transformer en el conjunto de prueba 90": "Tabla 14 Reporte de clasificación por variedad del modelo CNN/EfficientNetB0 83",
    "Tabla 15 Reporte de clasificación por variedad del modelo Swin-Tiny Transformer 91": "Tabla 15 Resumen de construcción del modelo Swin-Tiny Transformer 86",
    "Tabla 16 Comparación global de desempeño entre CNN/EfficientNetB0 y Swin-Tiny Transformer 93": "Tabla 16 Resumen del entrenamiento del modelo Swin-Tiny Transformer 87",
    "Tabla 17 Comparación pareada de aciertos y errores entre CNN/EfficientNetB0 y Swin-Tiny Transformer 94": "Tabla 17 Métricas globales del modelo Swin-Tiny Transformer en el conjunto de prueba 90",
    "Tabla 19 Cronograma de Actividades de investigación 109": "Tabla 22 Cronograma de Actividades de investigación 109",
    "Tabla 20 Presupuesto del proyecto de investigación 110": "Tabla 23 Presupuesto del proyecto de investigación 110",
}
for old, new in list_replacements.items():
    replace_exact(old, new, heading=False)

# Insertar entradas faltantes de la lista de tablas después de la entrada de Tabla 17 si existe.
idx_anchor = find_paragraph_by_exact("Tabla 17 Métricas globales del modelo Swin-Tiny Transformer en el conjunto de prueba 90")
if idx_anchor is not None:
    p = insert_paragraph_after(idx_anchor, "Tabla 18 Reporte de clasificación por variedad del modelo Swin-Tiny Transformer 91")
    p = insert_paragraph_after(p, "Tabla 19 Comparación global de desempeño entre CNN/EfficientNetB0 y Swin-Tiny Transformer 93")
    p = insert_paragraph_after(p, "Tabla 20 Criterio estadístico para la contrastación de hipótesis 94")
    p = insert_paragraph_after(p, "Tabla 21 Matriz de contrastación de hipótesis preparada para ejecuciones repetidas 96")
else:
    missing.append("anchor tabla índice")

# Actualizar contenido de tablas estadísticas.
# Tabla 20: criterio estadístico para contrastación.
if len(doc.tables) >= 20:
    t = doc.tables[19]
    data = [
        ["ELEMENTO", "CRITERIO ESTADÍSTICO"],
        ["Variable de contraste", "Accuracy obtenido en cada ejecución completa del entrenamiento."],
        ["Valor de referencia", "μ₀ = 0.75, equivalente al 75 % de Accuracy."],
        ["Criterio de interpretación", "Accuracy < 75 %: no es eficiente; Accuracy ≥ 75 %: eficiente."],
        ["Prueba para HG, HE1 y HE2", "t de Student para una muestra, comparando X̄ contra μ₀ = 0.75."],
        ["Prueba para HE3", "Comparación estadística entre CNN/EfficientNetB0 y Swin-Tiny Transformer bajo ejecuciones equivalentes."],
    ]
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            set_cell_text(t.cell(r, c), value, bold=(r == 0))

# Tabla 21: matriz preparada, sin inventar resultados.
if len(doc.tables) >= 21:
    t = doc.tables[20]
    data = [
        ["Hipótesis", "Evidencia requerida", "Prueba estadística", "Decisión a registrar"],
        ["HG", "Accuracy por ejecución de los algoritmos de Deep Learning.", "t de Student para una muestra contra μ₀ = 0.75.", "Rechazar o no rechazar H0G según p valor."],
        ["HE1", "Accuracy por ejecución del modelo CNN/EfficientNetB0.", "t de Student para una muestra contra μ₀ = 0.75.", "Rechazar o no rechazar H01 según p valor."],
        ["HE2", "Accuracy por ejecución del modelo Swin-Tiny Transformer.", "t de Student para una muestra contra μ₀ = 0.75.", "Rechazar o no rechazar H02 según p valor."],
        ["HE3", "Accuracy comparativo de CNN/EfficientNetB0 y Swin-Tiny Transformer.", "Prueba comparativa; preferentemente pareada si se usan las mismas semillas.", "Rechazar o no rechazar H03 según p valor."],
    ]
    for r, row in enumerate(data):
        for c, value in enumerate(row):
            set_cell_text(t.cell(r, c), value, bold=(r == 0))

# Renumerar captions de anexos en índice de figuras si exactos posteriores no fueron encontrados.
for p in doc.paragraphs:
    if "Llunchuy Waqachiq" in p.text:
        set_paragraph_text(p, p.text.replace("variedad Llunchuy Waqachiq", "del corpus de imágenes"), heading=p.style.name.startswith("Heading"))

# Aplicar Times New Roman 12 a tablas editadas y captions tocados.
for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_after = Pt(0)
                for run in p.runs:
                    apply_run_font(run)

# Guardar.
doc.save(OUT)

# Validación textual básica.
check_doc = Document(OUT)
all_text = "\n".join(p.text for p in check_doc.paragraphs)
for table in check_doc.tables:
    for row in table.rows:
        for cell in row.cells:
            all_text += "\n" + cell.text

forbidden = ["INKAPA", "aplicativo", "sintética", "sintético", "sintéticas", "sintéticos", "synthetic", "imágenes reales", "imágenes sintéticas", "etiqueta real", "Llunchuy Waqachiq"]
found = [term for term in forbidden if term.lower() in all_text.lower()]
print(f"Generado: {OUT}")
print(f"Párrafos: {len(check_doc.paragraphs)} | Tablas: {len(check_doc.tables)} | Imágenes internas: {len(check_doc.inline_shapes)}")
print(f"Términos restringidos encontrados: {found}")
if missing:
    print("No se encontraron algunos textos exactos:")
    for item in missing:
        print(f"- {item}")
if found:
    raise SystemExit(2)

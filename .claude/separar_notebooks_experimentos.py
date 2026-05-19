import json
from pathlib import Path

BASE = Path(r"C:\Users\jquis\OneDrive\Escritorio\TESIS TOMAS\tesista")
MARKER = "## Experimentos para contrastación de hipótesis y análisis por épocas"
CODE_MARKER = "# Configuración experimental para la tesis: barrido por épocas y repeticiones estadísticas"

FILES = [
    (
        BASE / "codigo_entrenamiento" / "modelo-cnn.ipynb",
        BASE / "codigo_entrenamiento" / "modelo-cnn-experimentos-contrastacion-epocas.ipynb",
    ),
    (
        BASE / "codigo_entrenamiento" / "modelo-swin.ipynb",
        BASE / "codigo_entrenamiento" / "modelo-swin-experimentos-contrastacion-epocas.ipynb",
    ),
]

for original_path, experiment_path in FILES:
    nb = json.loads(original_path.read_text(encoding="utf-8"))
    experiment_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")

    original_cells = nb["cells"]
    cleaned_cells = []
    removed = []
    for cell in original_cells:
        source = "".join(cell.get("source", []))
        if MARKER in source or CODE_MARKER in source:
            removed.append((cell.get("id"), cell.get("cell_type")))
            continue
        cleaned_cells.append(cell)

    nb["cells"] = cleaned_cells
    original_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Creado: {experiment_path}")
    print(f"Limpio original: {original_path}; celdas removidas: {removed}")

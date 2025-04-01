from pathlib import Path
import sys

file_path = Path(__file__).resolve()
root_path = file_path.parent
if root_path not in sys.path:
    sys.path.append(str(root_path))
ROOT = root_path.relative_to(Path.cwd())

# ML Model config
MODEL_DIR = ROOT / 'models_weights'
DETECTION_MODEL = MODEL_DIR / 'yolo11m_finetunned.pt'
# Webcam
WEBCAM_PATH = 0

CELLPHONE = ['Celular']
CELLPHONE_BATTERY = ['Bateria_Celular']
BATTERY = ['Bateria_Notebook']
NEEDLE = ['Agulha']
SYRINGE = ['Seringa']
SCORPION = ['Escorpiao']
PILHA = ['Pilha']

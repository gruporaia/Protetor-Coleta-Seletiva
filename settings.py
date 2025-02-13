from pathlib import Path
import sys

file_path = Path(__file__).resolve()
root_path = file_path.parent
if root_path not in sys.path:
    sys.path.append(str(root_path))
ROOT = root_path.relative_to(Path.cwd())

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
# Webcam
WEBCAM_PATH = 0

CELLPHONE = ['Celular']
CELLPHONE_BATTERY = ['Bateria de celular']
BATTERY = ['Bateria de notebook']
NEEDLE = ['Seringa']
SCORPION = ['Escorpião']
    
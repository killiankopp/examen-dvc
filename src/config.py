from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent

CONFIG_FILE_PATH = PROJECT_ROOT / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"

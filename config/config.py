from pathlib import Path


# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = Path(BASE_DIR, 'data')
CONFIG_DIR = Path(BASE_DIR, 'config')

# Create directories
DATA_DIR.mkdir(parents=True, exist_ok=True)

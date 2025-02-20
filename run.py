import sys
from pathlib import Path

# Adiciona o diretório src ao PYTHONPATH
src_path = str(Path(__file__).parent / "src")
if src_path not in sys.path:
    sys.path.append(src_path)

# Importa e executa a aplicação
from app import main

if __name__ == "__main__":
    main() 
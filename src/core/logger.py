import logging
from datetime import datetime
from pathlib import Path

def setup_logger():
    # Configura diretório de logs
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Nome do arquivo com data
    log_file = log_dir / f"sistema_{datetime.now().strftime('%Y%m%d')}.log"
    
    # Configura o logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger(__name__)
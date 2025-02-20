from pathlib import Path
import shutil
from datetime import datetime
from .logger import logger

def backup_database():
    try:
        # Cria diretório de backup
        backup_dir = Path("backups")
        backup_dir.mkdir(exist_ok=True)
        
        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"vendas_{timestamp}.db"
        
        # Copia o banco
        shutil.copy2("vendas.db", backup_file)
        logger.info(f"Backup criado: {backup_file}")
        
        # Remove backups antigos (mantém últimos 5)
        manter_ultimos_backups(5)
        
    except Exception as e:
        logger.error(f"Erro no backup: {str(e)}")
        raise

def manter_ultimos_backups(quantidade: int):
    """Mantém apenas os N backups mais recentes"""
    backup_dir = Path("backups")
    if not backup_dir.exists():
        return
        
    # Lista todos os backups ordenados por data
    backups = sorted(
        backup_dir.glob("vendas_*.db"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    
    # Remove os mais antigos
    for backup in backups[quantidade:]:
        backup.unlink()
        logger.info(f"Backup removido: {backup}")
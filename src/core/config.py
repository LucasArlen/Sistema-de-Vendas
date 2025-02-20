from pathlib import Path
from typing import Dict
import yaml

class Config:
    _instance = None
    _config: Dict = {}
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        self.load_config()
    
    def load_config(self):
        config_file = Path("config.yml")
        if config_file.exists():
            with open(config_file) as f:
                self._config = yaml.safe_load(f)
        else:
            self._config = self.default_config()
    
    @staticmethod
    def default_config():
        return {
            "database": {
                "path": "vendas.db",
                "backup_dir": "backups"
            },
            "logging": {
                "level": "INFO",
                "dir": "logs"
            }
        }
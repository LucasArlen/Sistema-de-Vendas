import pytest
import sqlite3
from pathlib import Path

@pytest.fixture
def test_db():
    """Cria um banco de dados de teste"""
    db_path = Path("test.db")
    conn = sqlite3.connect(db_path)
    
    # Cria as tabelas
    with open("src/core/schema.sql") as f:
        conn.executescript(f.read())
    
    yield conn
    
    # Limpa após os testes
    conn.close()
    db_path.unlink()
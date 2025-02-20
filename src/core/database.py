import sqlite3
from contextlib import contextmanager
from datetime import datetime
from typing import List, Optional
from .models import Cliente, Venda, Saida

@contextmanager
def get_db():
    conn = sqlite3.connect('vendas.db')
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS clientes (
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                telefone TEXT,
                endereco TEXT,
                email TEXT,
                observacoes TEXT,
                data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY,
                cliente_cpf TEXT,
                valor REAL NOT NULL,
                status TEXT NOT NULL,
                data DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (cliente_cpf) REFERENCES clientes (cpf)
            );

            CREATE TABLE IF NOT EXISTS saidas (
                id INTEGER PRIMARY KEY,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                categoria TEXT NOT NULL,
                data DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

def cadastrar_cliente(cliente: Cliente) -> bool:
    with get_db() as conn:
        try:
            cursor = conn.execute(
                """
                INSERT INTO clientes 
                    (cpf, nome, telefone, endereco, email, observacoes, data_cadastro) 
                VALUES 
                    (?, ?, ?, ?, ?, ?, ?)
                """,
                (cliente.cpf, cliente.nome, cliente.telefone, cliente.endereco, 
                 cliente.email, cliente.observacoes, cliente.data_cadastro)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

def registrar_venda(venda: Venda) -> int:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO vendas (cliente_cpf, valor, status, data) VALUES (?, ?, ?, ?)",
            (venda.cliente_cpf, venda.valor, venda.status, venda.data)
        )
        conn.commit()
        return cursor.lastrowid

def registrar_saida(saida: Saida) -> int:
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO saidas (descricao, valor, categoria, data) VALUES (?, ?, ?, ?)",
            (saida.descricao, saida.valor, saida.categoria, saida.data)
        )
        conn.commit()
        return cursor.lastrowid

def listar_clientes():
    with get_db() as conn:
        return [dict(row) for row in conn.execute("""
            SELECT * FROM clientes ORDER BY nome
        """).fetchall()]

def buscar_cliente(cpf: str):
    with get_db() as conn:
        result = conn.execute("""
            SELECT * FROM clientes WHERE cpf = ?
        """, [cpf]).fetchone()
        return dict(result) if result else None

def atualizar_cliente(cliente: Cliente) -> bool:
    with get_db() as conn:
        cursor = conn.execute("""
            UPDATE clientes 
            SET nome = ?, telefone = ?, endereco = ?, 
                email = ?, observacoes = ?
            WHERE cpf = ?
        """, (cliente.nome, cliente.telefone, cliente.endereco,
              cliente.email, cliente.observacoes, cliente.cpf))
        conn.commit()
        return cursor.rowcount > 0

def excluir_cliente(cpf: str) -> bool:
    with get_db() as conn:
        cursor = conn.execute("DELETE FROM clientes WHERE cpf = ?", [cpf])
        conn.commit()
        return cursor.rowcount > 0 
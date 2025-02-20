from datetime import datetime
from .database import get_db
from .models import Cliente, Venda
from .decorators import log_operation, handle_exceptions
from .exceptions import VendaError

def validar_cliente_existe(cpf: str) -> bool:
    """Verifica se um cliente existe pelo CPF"""
    with get_db() as conn:
        result = conn.execute(
            "SELECT 1 FROM clientes WHERE cpf = ?", 
            [cpf]
        ).fetchone()
        return bool(result)

@log_operation
@handle_exceptions
def registrar_nova_venda(venda: Venda) -> int:
    """Registra uma nova venda com validações"""
    if not validar_cliente_existe(venda.cliente_cpf):
        raise VendaError("Cliente não encontrado")
    
    from .database import registrar_venda
    return registrar_venda(venda) 
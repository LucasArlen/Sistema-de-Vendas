class SistemaException(Exception):
    """Exceção base do sistema"""
    pass

class ClienteError(SistemaException):
    """Erros relacionados a clientes"""
    pass

class VendaError(SistemaException):
    """Erros relacionados a vendas"""
    pass

class DatabaseError(SistemaException):
    """Erros de banco de dados"""
    pass
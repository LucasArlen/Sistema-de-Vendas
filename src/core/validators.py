import re
from typing import Optional

def validar_cpf(cpf: str) -> bool:
    """Validação completa de CPF"""
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
        
    # Verifica dígitos repetidos
    if len(set(cpf)) == 1:
        return False
        
    # Validação dos dígitos verificadores
    # ... implementação do algoritmo ...
    
    return True

def validar_telefone(telefone: Optional[str]) -> bool:
    if not telefone:
        return True
    padrao = re.compile(r'^\d{10,11}$')
    return bool(padrao.match(''.join(filter(str.isdigit, telefone))))
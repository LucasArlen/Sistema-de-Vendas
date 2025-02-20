import pytest
from datetime import datetime
from src.core.models import Cliente, Venda, Saida

def test_cliente_cpf_invalido():
    with pytest.raises(ValueError, match="CPF deve conter 11 dígitos"):
        Cliente(cpf="123", nome="Teste")

def test_cliente_valido():
    cliente = Cliente(
        cpf="12345678901",
        nome="Teste",
        telefone="123456789"
    )
    assert cliente.cpf == "12345678901"
    assert cliente.formatar_cpf() == "123.456.789-01"
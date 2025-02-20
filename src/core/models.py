from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Cliente:
    cpf: str
    nome: str
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    email: Optional[str] = None
    observacoes: Optional[str] = None
    data_cadastro: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        # Limpa o CPF mantendo apenas números
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        
        if not self.cpf or len(self.cpf) != 11:
            raise ValueError("CPF deve conter 11 dígitos")
        
        if not self.nome or len(self.nome) < 2:
            raise ValueError("Nome inválido")
        
        if self.telefone and not self.telefone.isdigit():
            raise ValueError("Telefone deve conter apenas números")
        
        if self.email and '@' not in self.email:
            raise ValueError("Email inválido")
    
    def formatar_cpf(self) -> str:
        """Retorna CPF formatado (XXX.XXX.XXX-XX)"""
        return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"

@dataclass
class Venda:
    cliente_cpf: str
    valor: float
    status: str  # "Pago" ou "Fiado"
    data: datetime = field(default_factory=datetime.now)
    id: Optional[int] = None

    def __post_init__(self):
        if self.valor <= 0:
            raise ValueError("Valor deve ser maior que zero")
        if self.status not in ["Pago", "Fiado"]:
            raise ValueError("Status inválido")

@dataclass
class Saida:
    descricao: str
    valor: float
    categoria: str
    data: datetime = field(default_factory=datetime.now)
    id: Optional[int] = None

    CATEGORIAS = [
        "Fornecedor",
        "Funcionário",
        "Manutenção",
        "Outros"
    ]

    def __post_init__(self):
        if not self.descricao:
            raise ValueError("Descrição é obrigatória")
        if self.valor <= 0:
            raise ValueError("Valor deve ser maior que zero")
        if self.categoria not in self.CATEGORIAS:
            raise ValueError(f"Categoria inválida. Use: {', '.join(self.CATEGORIAS)}") 
import streamlit as st
from datetime import datetime
from core.models import Venda
from core.database import get_db
from core.services import registrar_nova_venda

def render_vendas():
    st.title("Nova Venda")
    
    clientes = obter_clientes()
    if not clientes:
        st.warning("Nenhum cliente cadastrado. Cadastre um cliente primeiro.")
        return
        
    cliente_cpf = st.selectbox(
        "Cliente",
        options=clientes,
        format_func=lambda x: obter_nome_cliente(x)
    )
    
    valor = st.number_input("Valor", min_value=0.01, step=0.5)
    status = st.selectbox("Status", ["Pago", "Fiado"])
    
    if st.button("Registrar Venda"):
        try:
            venda = Venda(
                cliente_cpf=cliente_cpf,
                valor=valor,
                status=status,
                data=datetime.now()
            )
            registrar_nova_venda(venda)
            st.success("Venda registrada com sucesso!")
        except Exception as e:
            st.error(f"Erro ao registrar venda: {str(e)}")

def obter_clientes():
    with get_db() as conn:
        return [row[0] for row in conn.execute("SELECT cpf FROM clientes")]

def obter_nome_cliente(cpf):
    with get_db() as conn:
        result = conn.execute(
            """
            SELECT nome, cpf 
            FROM clientes 
            WHERE cpf = ?
            """, 
            [cpf]
        ).fetchone()
        if result:
            return f"{result['nome']} (CPF: {formatar_cpf(result['cpf'])})"
        return "Cliente não encontrado"

def formatar_cpf(cpf: str) -> str:
    """Formata o CPF para exibição"""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" 
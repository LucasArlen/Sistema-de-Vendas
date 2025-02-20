import streamlit as st
from datetime import datetime
from core.models import Cliente
from core.database import (
    cadastrar_cliente, listar_clientes, 
    buscar_cliente, atualizar_cliente,
    excluir_cliente
)

def render_clientes():
    st.title("Gestão de Clientes")
    
    # Tabs para separar listagem e cadastro
    tab1, tab2 = st.tabs(["📋 Lista de Clientes", "➕ Novo Cliente"])
    
    with tab1:
        render_lista_clientes()
    
    with tab2:
        render_form_cliente()

def render_lista_clientes():
    clientes = listar_clientes()
    
    # Campo de busca
    busca = st.text_input("🔍 Buscar cliente (nome ou CPF)", "")
    
    if busca:
        busca = busca.lower()
        clientes = [
            c for c in clientes 
            if busca in c['nome'].lower() or busca in c['cpf']
        ]
    
    # Lista de clientes
    for cliente in clientes:
        with st.expander(f"{cliente['nome']} - CPF: {formatar_cpf(cliente['cpf'])}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("📞 Telefone:", cliente['telefone'] or "Não informado")
                st.write("📧 Email:", cliente['email'] or "Não informado")
                st.write("📅 Cadastro:", cliente['data_cadastro'])
            
            with col2:
                st.write("📍 Endereço:", cliente['endereco'] or "Não informado")
                st.write("📝 Observações:", cliente['observacoes'] or "Nenhuma")
            
            # Botões de ação
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✏️ Editar", key=f"edit_{cliente['cpf']}"):
                    st.session_state['cliente_para_editar'] = cliente
                    st.rerun()
            
            with col2:
                if st.button("❌ Excluir", key=f"del_{cliente['cpf']}"):
                    if excluir_cliente(cliente['cpf']):
                        st.success("Cliente excluído com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao excluir cliente")

def render_form_cliente():
    # Verifica se é edição
    cliente_edicao = st.session_state.get('cliente_para_editar')
    
    # Formulário
    with st.form("form_cliente"):
        cpf = st.text_input(
            "CPF*", 
            value=cliente_edicao['cpf'] if cliente_edicao else "",
            help="Apenas números"
        )
        
        nome = st.text_input(
            "Nome*", 
            value=cliente_edicao['nome'] if cliente_edicao else ""
        )
        
        col1, col2 = st.columns(2)
        with col1:
            telefone = st.text_input(
                "Telefone", 
                value=cliente_edicao['telefone'] if cliente_edicao else ""
            )
            email = st.text_input(
                "Email", 
                value=cliente_edicao['email'] if cliente_edicao else ""
            )
        
        with col2:
            endereco = st.text_input(
                "Endereço", 
                value=cliente_edicao['endereco'] if cliente_edicao else ""
            )
            observacoes = st.text_area(
                "Observações", 
                value=cliente_edicao['observacoes'] if cliente_edicao else ""
            )
        
        submitted = st.form_submit_button("Salvar")
        
        if submitted:
            try:
                cliente = Cliente(
                    cpf=cpf,
                    nome=nome,
                    telefone=telefone,
                    endereco=endereco,
                    email=email,
                    observacoes=observacoes
                )
                
                if cliente_edicao:
                    if atualizar_cliente(cliente):
                        st.success("Cliente atualizado com sucesso!")
                        del st.session_state['cliente_para_editar']
                    else:
                        st.error("Erro ao atualizar cliente")
                else:
                    if cadastrar_cliente(cliente):
                        st.success("Cliente cadastrado com sucesso!")
                    else:
                        st.error("CPF já cadastrado")
                
                st.rerun()
                
            except ValueError as e:
                st.error(str(e))

def formatar_cpf(cpf: str) -> str:
    """Formata o CPF para exibição"""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" 
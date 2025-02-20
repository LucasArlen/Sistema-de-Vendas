import streamlit as st
from core.database import init_db
from core.logger import setup_logger
from core.config import Config
from ui.pages.dashboard import render_dashboard
from ui.pages.vendas import render_vendas
from ui.pages.clientes import render_clientes
from ui.pages.saidas import render_saidas

def main():
    # Inicializa logger
    setup_logger()
    
    # Carrega configurações
    config = Config.get_instance()._config
    
    # Configura página
    st.set_page_config(
        page_title=config['app']['title'],
        layout=config['app']['layout']
    )
    
    # Inicializa banco de dados
    init_db()
    
    # Menu lateral
    menu = st.sidebar.selectbox(
        "Menu",
        ["Dashboard", "Nova Venda", "Clientes", "Saídas"]
    )
    
    # Renderiza página selecionada
    if menu == "Dashboard":
        render_dashboard()
    elif menu == "Nova Venda":
        render_vendas()
    elif menu == "Clientes":
        render_clientes()
    elif menu == "Saídas":
        render_saidas()

if __name__ == "__main__":
    main() 
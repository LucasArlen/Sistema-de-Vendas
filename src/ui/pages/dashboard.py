import streamlit as st
from core.database import get_db

def render_dashboard():
    st.title("Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        vendas_dia = obter_vendas_dia()
        st.metric("Vendas Hoje", f"R$ {vendas_dia:.2f}")
    
    with col2:
        fiados = obter_total_fiado()
        st.metric("Total Fiado", f"R$ {fiados:.2f}")
    
    with col3:
        saidas = obter_saidas_dia()
        st.metric("Saídas Hoje", f"R$ {saidas:.2f}")

def obter_vendas_dia():
    with get_db() as conn:
        result = conn.execute("""
            SELECT COALESCE(SUM(valor), 0) 
            FROM vendas 
            WHERE DATE(data) = DATE('now')
            AND status = 'Pago'
        """).fetchone()
        return result[0]

def obter_total_fiado():
    with get_db() as conn:
        result = conn.execute("""
            SELECT COALESCE(SUM(valor), 0) 
            FROM vendas 
            WHERE status = 'Fiado'
        """).fetchone()
        return result[0]

def obter_saidas_dia():
    with get_db() as conn:
        result = conn.execute("""
            SELECT COALESCE(SUM(valor), 0) 
            FROM saidas 
            WHERE DATE(data) = DATE('now')
        """).fetchone()
        return result[0] 
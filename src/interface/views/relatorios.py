import streamlit as st

def relatorios_page():
    # Header
    st.markdown("""
    <div class="header-ipea">
        <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
    </div>
    """, unsafe_allow_html=True)


    # Seção de Exportar Relatórios
    st.markdown("## Exportar relatórios")
    
    st.markdown("**Período**")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("De", ["Maio 2023", "Junho 2023"], key="periodo_inicio")
    with col2:
        st.selectbox("Até", ["Maio 2023", "Junho 2023"], key="periodo_fim")

    # Tipos de dados
    st.markdown("### Tipos de dados")
    tipo1, tipo2, tipo3 = st.columns(3)
    with tipo1:
        st.checkbox("Receitas", key="cb_receitas")
    with tipo2:
        st.checkbox("Despesas", key="cb_despesas")
    with tipo3:
        st.checkbox("Alertas", key="cb_alertas")

    # Visualização prévia
    st.markdown("### Visualização prévia")
    st.selectbox("Formato", ["PDF", "Excel", "HTML"], key="formato_visualizacao")

    # Botão de exportar 
    st.markdown("""
    <div style='margin-top: 20px;'>
        <button style='
            background-color: #0F4C81;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        '>Exportar relatório ↓</button>
    </div>
    """, unsafe_allow_html=True)

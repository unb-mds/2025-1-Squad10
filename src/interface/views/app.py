import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random

import pathlib

# Configuração da página
st.set_page_config(
    page_title="IPEA",
    layout="wide",
    page_icon="📊"
)

# Estilo CSS
with open("./src/interface/views/styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Estado da sessão para controlar a página atual
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard"

# Função para mudar de página
def change_page(page_name):
    st.session_state.current_page = page_name

# Sidebar
with st.sidebar:
    st.title("IPEA")
    
    if not st.user.is_logged_in:
        st.button("Log in with Google", on_click=st.login)
    else:
        st.text_input("🔍 Search for...")
        st.markdown("### Navegação")
        
        # Botões de navegação
        
        if st.button("Dashboard"):
            change_page("Dashboard")
        if st.button("Relatórios"):
            change_page("Relatórios")
        if st.button("Alertas"):
            change_page("Alertas")
        if st.button("Análises inteligentes"):
            change_page("Análises inteligentes")
        if st.button("Dados"):
            change_page("Dados")
        
        st.markdown("---")
        if st.button("User"):
            change_page("User")
        if st.button("Configurações"):
            change_page("Configurações")
        if st.button("Logout"):
            st.logout()

# Funções simuladas
def get_total_receitas(): return 50800, 28.4
def get_total_despesas(): return 23600, -12.6
def get_alertas_ativos(): return 3, 3.1
def get_series_temporais():
    meses = pd.date_range("2023-01-01", periods=12, freq="M")
    receitas = [random.randint(80, 240) for _ in range(12)]
    despesas = [random.randint(60, 180) for _ in range(12)]
    return pd.DataFrame({"Meses": meses, "Receitas": receitas, "Despesas": despesas})
def get_valor_indicador(): return 23648
def get_gauge_value(): return 65

# Página principal
def main_page():
    # Cabeçalho
    st.markdown("""
    <div class="header-ipea">
        <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
    </div>
    """, unsafe_allow_html=True)

    # Métricas principais
    col1, col2, col3 = st.columns(3)
    receitas, receitas_var = get_total_receitas()
    despesas, despesas_var = get_total_despesas()
    alertas, alertas_var = get_alertas_ativos()

    # Card 1
    with col1:
        st.markdown(f"""
        <div class="card-metrica">
            <div class="card-topo"><span class="icon">👤</span><span class="titulo">Total de receitas</span></div>
            <div class="valor">{receitas:,}K</div>
            <div class="variacao {'positivo' if receitas_var >= 0 else 'negativo'}">{'▲' if receitas_var >= 0 else '▼'} {abs(receitas_var):.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Card 2
    with col2:
        st.markdown(f"""
        <div class="card-metrica">
            <div class="card-topo"><span class="icon">👁️</span><span class="titulo">Total de Despesas</span></div>
            <div class="valor">{despesas:,}K</div>
            <div class="variacao {'positivo' if despesas_var >= 0 else 'negativo'}">{'▲' if despesas_var >= 0 else '▼'} {abs(despesas_var):.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    # Card 3
    with col3:
        st.markdown(f"""
        <div class="card-metrica">
            <div class="card-topo"><span class="icon">➕</span><span class="titulo">Alertas Ativos</span></div>
            <div class="valor">{alertas}</div>
            <div class="variacao {'positivo' if alertas_var >= 0 else 'negativo'}">{'▲' if alertas_var >= 0 else '▼'} {abs(alertas_var):.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## ")

    # Gráfico e Indicadores
    col4, col5 = st.columns([3, 2])
    df = get_series_temporais()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Meses"], y=df["Receitas"], name="Receitas", line=dict(color="#A020F0")))
    fig.add_trace(go.Scatter(x=df["Meses"], y=df["Despesas"], name="Despesas", line=dict(color="#00CFFF")))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
    col4.plotly_chart(fig, use_container_width=True)

    with col5:
        st.markdown(f"""
        <div class='painel'>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque urna mi, varius nec tincidunt sed.</p>
        <h2 class='valor-indicador'>{get_valor_indicador():,}</h2>
        </div>
        """, unsafe_allow_html=True)

        gauge_value = get_gauge_value()
        gauge_fig = go.Figure(go.Indicator(
            mode="gauge+number", value=gauge_value, title={'text': ""},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#555555"},
                   'steps': [{'range': [0, 50], 'color': "#e0e0e0"}, {'range': [50, 100], 'color': "#b0b0b0"}],
                   'threshold': {'line': {'color': "white", 'width': 4}, 'thickness': 0.75, 'value': gauge_value}}
        ))
        gauge_fig.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=250, width=250, paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#333333"))
        st.plotly_chart(gauge_fig, use_container_width=True)



# Outras páginas 
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



def alertas_page():
    # Header
    st.markdown("""
    <div class="header-ipea">
        <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
    </div>
    """, unsafe_allow_html=True)
    st.write("Conteúdo da página de Alertas")

def analises_page():
    st.title("Análises Inteligentes")
    st.write("Conteúdo da página de Análises Inteligentes")

def dados_page():
    st.title("Dados")
    st.write("Conteúdo da página de Dados")

def user_page():
    st.title("Perfil do Usuário")
    st.write("Conteúdo da página do Usuário")

def configuracoes_page():
    st.title("Configurações")
    st.write("Conteúdo da página de Configurações")



# Renderização condicional da página

if st.user.is_logged_in:
    if st.session_state.current_page == "Dashboard":
        main_page()
        
    elif st.session_state.current_page == "Relatórios":
        relatorios_page()
    elif st.session_state.current_page == "Alertas":
        alertas_page()
    elif st.session_state.current_page == "Análises inteligentes":
        analises_page()
    elif st.session_state.current_page == "Dados":
        dados_page()
    elif st.session_state.current_page == "User":
        user_page()
    elif st.session_state.current_page == "Configurações":
        configuracoes_page()

else:
    st.title("Logue para usar aplicação.")
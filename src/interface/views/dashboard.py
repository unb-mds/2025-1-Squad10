import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import random
import requests


st.set_page_config(page_title="Dashboard IPEA", layout="wide")


if "pagina" not in st.session_state:
    st.session_state.pagina = "dashboard"



# Funções para integrações futuras
def get_total_receitas():
    # TODO: Substituir por integração 
    return 50800, 28.4  # valor, variação %

def get_total_despesas():
    # TODO: Substituir por integração 
    return 23600, -12.6  # valor, variação %

def get_alertas_ativos():
    # TODO: Substituir por integração real
    return 3, 3.1  # valor, variação %

def get_series_temporais():
    # TODO: Substituir por integração real
    meses = pd.date_range("2023-01-01", periods=12, freq="M")
    receitas = [random.randint(80, 240) for _ in range(12)]
    despesas = [random.randint(60, 180) for _ in range(12)]
    return pd.DataFrame({"Meses": meses, "Receitas": receitas, "Despesas": despesas})

def get_valor_indicador():
    # TODO: Substituir por integração real
    return 23648

def get_gauge_value():
    # TODO: Substituir por integração real
    return 65

# Estilização CSS
with open("./src/interface/views/styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("IPEA")
    st.text_input("🔍 Search for...")
    st.markdown("### Navegação")

    if st.button("Dashboard"):
        st.session_state.pagina = "dashboard"
    if st.button("Relatórios"):
        st.session_state.pagina = "relatorios"

    st.button("Alertas")
    st.button("Análises inteligentes")
    st.button("Dados")
    st.markdown("---")
    st.button("User")
    st.button("Configurações")

# Header
st.markdown("""
<div class="header-ipea">
    <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
</div>
""", unsafe_allow_html=True)

# Métricas principais
col1, col2, col3 = st.columns(3)

# Dados simulados (fáceis de trocar por API real depois)
receitas, receitas_var = get_total_receitas()
despesas, despesas_var = get_total_despesas()
alertas, alertas_var = get_alertas_ativos()

# Card 1
with col1:
    st.markdown(f"""
    <div class="card-metrica">
        <div class="card-topo">
            <span class="icon">👤</span>
            <span class="titulo">Total de receitas</span>
        </div>
        <div class="valor">{receitas:,}K</div>
        <div class="variacao {'positivo' if receitas_var >= 0 else 'negativo'}">{'▲' if receitas_var >= 0 else '▼'} {abs(receitas_var):.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

# Card 2
with col2:
    st.markdown(f"""
    <div class="card-metrica">
        <div class="card-topo">
            <span class="icon">👁️</span>
            <span class="titulo">Total de Despesas</span>
        </div>
        <div class="valor">{despesas:,}K</div>
        <div class="variacao {'positivo' if despesas_var >= 0 else 'negativo'}">{'▲' if despesas_var >= 0 else '▼'} {abs(despesas_var):.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

# Card 3
with col3:
    st.markdown(f"""
    <div class="card-metrica">
        <div class="card-topo">
            <span class="icon">➕</span>
            <span class="titulo">Alertas Ativos</span>
        </div>
        <div class="valor">{alertas}</div>
        <div class="variacao {'positivo' if alertas_var >= 0 else 'negativo'}">{'▲' if alertas_var >= 0 else '▼'} {abs(alertas_var):.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## ")

# Gráfico + Painel lateral
col4, col5 = st.columns([3, 2])

# Gráfico de Receitas e Despesas
df = get_series_temporais()

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Meses"], y=df["Receitas"], name="Receitas", line=dict(color="#A020F0")))
fig.add_trace(go.Scatter(x=df["Meses"], y=df["Despesas"], name="Despesas", line=dict(color="#00CFFF")))
fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white")
)

col4.plotly_chart(fig, use_container_width=True)

# Indicador e Gauge
with col5:
    valor_indicador = get_valor_indicador()

    st.markdown(f"""
    <div class='painel'>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque urna mi, varius nec tincidunt sed.</p>
    <h2 class='valor-indicador'>{valor_indicador:,}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
    """, unsafe_allow_html=True)

    gauge_value = get_gauge_value()

    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=gauge_value,
        title={'text': ""},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#555555"},
            'steps': [
                {'range': [0, 50], 'color': "#e0e0e0"},
                {'range': [50, 100], 'color': "#b0b0b0"}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': gauge_value
            }
        }
    ))

    gauge_fig.update_layout(
        margin=dict(l=20, r=20, t=30, b=20),
        height=250,
        width=250,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#333333")
    )

    st.plotly_chart(gauge_fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


import streamlit as st

def relatorios_page():
    # Header
    st.markdown("""
    <div class="header-ipea">
        <h3 class="titulo-ipea">Relatórios inteligentes IPEA</h3>
        <a href="#" class="login-icon"><i class="fas fa-user-circle"></i></a>
    </div>
    """, unsafe_allow_html=True)

    # Título
    st.markdown("<h2 class='titulo-secao'><i class='fas fa-file-export'></i> Exportar relatórios</h2>", unsafe_allow_html=True)

    # Período
    st.markdown("""
    <div class="secao">
        <label class="label">Período</label>
        <div class="filtros-periodo">
            <select class="custom-select" id="periodo-inicio">
                <option>Maio 2023</option>
                <option>Junho 2023</option>
                <option>Julho 2023</option>
            </select>
            <span class="ate">até</span>
            <select class="custom-select" id="periodo-fim">
                <option>Maio 2023</option>
                <option>Junho 2023</option>
                <option>Julho 2023</option>
            </select>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tipos de dados
    st.markdown("""
    <div class="secao">
        <label class="label">Tipos de dados</label>
        <div class="checkbox-container">
            <label class="checkbox-item">
                <input type="checkbox" name="tipo_dado" value="receitas"> Receitas
            </label>
            <label class="checkbox-item">
                <input type="checkbox" name="tipo_dado" value="despesas"> Despesas
            </label>
            <label class="checkbox-item">
                <input type="checkbox" name="tipo_dado" value="alertas"> Alertas
            </label>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Visualização prévia
    st.markdown("""
    <div class="secao">
        <label class="label">Visualização prévia</label>
        <select class="custom-select">
            <option>PDF</option>
            <option>Excel</option>
            <option>HTML</option>
        </select>
    </div>
    """, unsafe_allow_html=True)

    # Botão exportar
    st.markdown("""
    <div class="botao-container">
        <button class="btn-exportar">
            Exportar Relatório <span class="seta-baixo">↓</span>
        </button>
    </div>
    """, unsafe_allow_html=True)

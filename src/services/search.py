# backend.py

import ipeadatapy as ipea
import pandas as pd
import plotly.express as px


def get_by_code(codigo: str) -> pd.DataFrame:
    """
    Retorna os dados de séries temporais do IPEA a partir de um código específico de indicador.

    Parâmetros:
    -----------
    codigo : str
        Código do indicador, por exemplo 'PNAD12_PESSOAS12'.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com os dados da série temporal correspondente ao código.
    """
    return ipea.timeseries(codigo)


def get_by_theme(theme_nome: str) -> pd.DataFrame:
    """
    Retorna os metadados de todos os indicadores associados a um tema específico.

    Parâmetros:
    -----------
    theme_nome : str
        Nome (ou parte do nome) do tema. Busca é feita de forma case-insensitive.

    Retorno:
    --------
    pd.DataFrame
        DataFrame com os metadados de todos os indicadores encontrados no tema.

    Erros:
    ------
    ValueError
        Se o tema informado não for encontrado na base de dados.
    """
    # Busca todos os temas disponíveis
    temas = ipea.themes()

    # Filtra pelo nome informado (ignora maiúsculas/minúsculas)
    temas_filtrados = temas[temas['NAME'].str.lower().str.contains(theme_nome.lower())]

    if temas_filtrados.empty:
        raise ValueError(f"Tema '{theme_nome}' não encontrado.")

    # Para cada ID de tema encontrado, busca os metadados
    lista_dfs = [ipea.metadata(theme_id=theme_id) for theme_id in temas_filtrados["ID"]]

    # Junta todos os DataFrames em um único DataFrame
    df_concatenado = pd.concat(lista_dfs, ignore_index=True)

    return df_concatenado


def filtro(filtros: dict) -> pd.DataFrame:
    """
    Aplica filtros aos metadados dos indicadores do IPEA.

    Parâmetros:
    -----------
    filtros : dict
        Dicionário contendo os filtros a serem aplicados. Chaves possíveis:
        {
            "codigo": str,
            "tema": str,
            "organizacao": str,
            "pais": str,
            "frequencia": str,
            "unidade": str,
            "subtema": str,
            "data_inicio": str no formato 'YYYY-MM-DD',
            "data_fim": str no formato 'YYYY-MM-DD'
        }

    Retorno:
    --------
    pd.DataFrame
        DataFrame contendo os metadados filtrados de acordo com os critérios.
    """
    # Busca metadados gerais
    df = ipea.metadata()

    # Aplicação de filtros textuais diretos
    for chave, coluna in {
        "codigo": "CODE",
        "organizacao": "SOURCE",
        "pais": "COUNTRY",
        "frequencia": "FREQUENCY",
        "unidade": "UNIT",
        "subtema": "SUBTHEME"
    }.items():
        if filtros.get(chave):
            df = df[df[coluna].str.lower().str.contains(filtros[chave].lower(), na=False)]

    # Filtro por tema (mais robusto)
    if filtros.get("tema"):
        try:
            tema_df = get_by_theme(filtros["tema"])
            df = pd.merge(df, tema_df, how="inner")
        except ValueError as e:
            raise e

    # Filtro por datas de atualização
    df["LAST UPDATE"] = pd.to_datetime(df["LAST UPDATE"], errors="coerce")

    data_inicio = pd.to_datetime(filtros.get("data_inicio"), errors="coerce") if filtros.get("data_inicio") else None
    data_fim = pd.to_datetime(filtros.get("data_fim"), errors="coerce") if filtros.get("data_fim") else None

    if pd.notnull(data_inicio):
        df = df[df["LAST UPDATE"] >= data_inicio]

    if pd.notnull(data_fim):
        df = df[df["LAST UPDATE"] <= data_fim]

    # 🧹 Limpeza final dos dados (remove duplicatas e linhas vazias)
    df = df.drop_duplicates().dropna().reset_index(drop=True)

    return df


def gerar_grafico(df: pd.DataFrame):
    """
    Gera um gráfico de dispersão interativo utilizando Plotly,
    mostrando os indicadores ao longo do tempo.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame contendo os dados dos metadados filtrados.

    Retorno:
    --------
    plotly.graph_objects.Figure ou None
        Objeto de figura Plotly. Retorna None se o DataFrame estiver vazio.
    """
    if df.empty:
        return None

    # Cria gráfico de dispersão
    fig = px.scatter(
        df,
        x="LAST UPDATE",  # Eixo X → Data da última atualização
        y="CODE",          # Eixo Y → Código do indicador
        color="SOURCE",    # Cores por organização fornecedora dos dados
        title="Indicadores ao longo do tempo",
        hover_data=["TITLE", "UNIT", "FREQUENCY"],  # Informações ao passar o mouse
        labels={"LAST UPDATE": "Data", "CODE": "Código do Indicador"},
        template="plotly_dark"  # Tema escuro
    )

    # Personaliza tamanho dos marcadores
    fig.update_traces(marker=dict(size=10))

    # Define altura do gráfico
    fig.update_layout(height=600)

    return fig

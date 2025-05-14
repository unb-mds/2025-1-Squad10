import ipeadatapy as ipea
import pandas as pd

def filtro(
    organizacao_usuario: str,
    tema_usuario: str,
    codigo_usuario: str,
    data_inicio_usuario: str,
    data_fim_usuario: str,
    pais_usuario: str,
    frequencia_usuario: str,
    unidade_usuario: str,
    subtema_usuario: str
) -> pd.DataFrame:
    """
    Filtra os dados do IPEA com base nos critérios fornecidos pelo usuário.

    Args:
        organizacao_usuario (str): Nome ou acrônimo da organização fornecedora dos dados.
        tema_usuario (str): Nome do tema dos dados.
        codigo_usuario (str): Código do indicador.
        data_inicio_usuario (str): Data de início no formato 'YYYY-MM-DD'.
        data_fim_usuario (str): Data de fim no formato 'YYYY-MM-DD'.
        pais_usuario (str): Nome do país relacionado aos dados.
        frequencia_usuario (str): Frequência dos dados (ex. 'mensal', 'anual').
        unidade_usuario (str): Unidade de medida dos dados (ex. 'milhões', 'percentual').
        subtema_usuario (str): Nome do subtema dos dados.

    Raises:
        ValueError: Se as datas fornecidas não estiverem no formato correto.

    Returns:
        pd.DataFrame: DataFrame com os dados filtrados.
    """
    # Carrega metadados do IPEA e filtra por medidas em dólares
    informacoes = ipea.metadata()
    informacoes = informacoes[informacoes["MEASURE"].str.contains("\\$")]

    # Filtra pelo código do indicador (ex: 'PIB')
    if codigo_usuario.strip():
        informacoes = informacoes[informacoes["CODE"].str.contains(codigo_usuario.upper())]

    # Filtra pela organização fornecedora (ex: 'IBGE')
    if organizacao_usuario.strip():
        informacoes = pd.concat([
            informacoes[informacoes["SOURCE ACRONYM"].str.lower().str.contains(organizacao_usuario.lower())],
            informacoes[informacoes["SOURCE"].str.lower().str.contains(organizacao_usuario.lower())]
        ])
        informacoes = informacoes.sort_values(by='CODE').drop_duplicates()

    # Filtra pelo tema (ex: 'economia', 'educação')
    if tema_usuario.strip():
        getThemeID = ipea.themes()
        getThemeID = getThemeID[getThemeID['NAME'].str.lower().str.contains(tema_usuario.lower())]
        found = pd.DataFrame()
        if not getThemeID.empty:
            for id in getThemeID['ID']:
                find = ipea.metadata(theme_id=id)
                found = pd.concat([found, find])

        # Remove duplicatas após concatenação
        if not found.empty:
            informacoes = pd.concat([informacoes, found]).drop_duplicates()

    # Filtra pelo intervalo de datas
    if data_inicio_usuario.strip() or data_fim_usuario.strip():
        informacoes["LAST UPDATE"] = pd.to_datetime(informacoes["LAST UPDATE"], errors="coerce")

        try:
            if data_inicio_usuario.strip():
                data_inicio_usuario = pd.to_datetime(data_inicio_usuario, format="%Y-%m-%d")
            if data_fim_usuario.strip():
                data_fim_usuario = pd.to_datetime(data_fim_usuario, format="%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Formato de data inválido: {e}")

        # Filtra apenas os dados que estão dentro do intervalo de datas
        mask = pd.Series([True] * len(informacoes))
        if data_inicio_usuario is not None:
            mask &= informacoes["LAST UPDATE"] >= data_inicio_usuario
        if data_fim_usuario is not None:
            mask &= informacoes["LAST UPDATE"] <= data_fim_usuario

        informacoes = informacoes[mask].reset_index(drop=True)

    # Filtra pelo país
    if pais_usuario.strip():
        informacoes = informacoes[informacoes["COUNTRY"].str.lower().str.contains(pais_usuario.lower())]

    # Filtra pela frequência dos dados
    if frequencia_usuario.strip():
        informacoes = informacoes[informacoes["FREQUENCY"].str.lower().str.contains(frequencia_usuario.lower())]

    # Filtra pela unidade de medida
    if unidade_usuario.strip():
        informacoes = informacoes[informacoes["UNIT"].str.lower().str.contains(unidade_usuario.lower())]

    # Filtra pelo subtema
    if subtema_usuario.strip():
        informacoes = informacoes[informacoes["SUBTHEME"].str.lower().str.contains(subtema_usuario.lower())]

    return informacoes





















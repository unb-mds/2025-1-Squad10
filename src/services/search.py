import ipeadatapy as ipea
import pandas as pd

def organization(phrase: str):
    """
    Retorna um dataframe contendo as series com dados financeiros do IPEA de acordo com a string parametrizada referente ao órgão procurado.

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encontrado".
    """
    series = ipea.metadata()
    series = series[series["MEASURE"].str.contains("\\$")]
    series = pd.concat([series[series["SOURCE ACRONYM"].str.lower().str.contains(phrase.lower())],
                        series[series["SOURCE"].str.lower().str.contains(phrase.lower())]])
    series = series.sort_values(by='CODE').drop_duplicates()
    return "Não Encontrado" if series.empty else series

def theme(phrase: str):
    """
    Retorna um dataframe contendo as series com dados financeiros do IPEA de acordo com a string parametrizada referente ao tema procurado.

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encontrado".
    """
    getThemeID = ipea.themes()
    getThemeID = getThemeID[getThemeID['NAME'].str.lower().str.contains(phrase.lower())]
    found = pd.DataFrame()
    if not getThemeID.empty:
        for id in getThemeID['ID']:
            find = ipea.metadata(theme_id=id)
            find = find[find['MEASURE'].str.contains("\\$")]
            found = pd.concat([found, find])
        found = found.sort_values(by='CODE')
    return "Não Encontrado" if found.empty else found
    
def code(phrase: str):
    """
    Retorna um dataframe contendo as series com dados financeiros do IPEA de acordo com a string parametrizada referente ao código procurado.

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encontrado".
    """
    code = ipea.metadata()
    code = code[code["MEASURE"].str.contains("\\$")]
    code = code[code["CODE"].str.contains(phrase.upper())]
    code = code.sort_values(by='CODE')
    return "Não Encontrado" if code.empty else code

def date(data_inicio: str = None, data_final: str = None) -> pd.DataFrame:
    """
    Retorna os metadados das séries temporais do IPEA filtrados por intervalo de datas.
    Parâmetros:
    - data_inicio (str, opcional): Data inicial no formato 'YYYY-MM-DD'. Se fornecida, filtra as séries a partir desta data.
    - data_final (str, opcional): Data final no formato 'YYYY-MM-DD'. Se fornecida, filtra as séries até esta data.
    Regras de filtragem:
    - Ambos os parâmetros ausentes: Lança ValueError, pois pelo menos uma das datas deve ser especificada.
    - Apenas data_inicio presente: Retorna séries atualizadas a partir de data_inicio.
    - Apenas data_final presente: Retorna séries atualizadas até data_final.
    - Ambos os parâmetros presentes: Retorna séries atualizadas entre data_inicio e data_final, inclusive.
    Retorna:
    - pd.DataFrame: DataFrame contendo os metadados das séries filtrados pelo intervalo de datas.
    """
    if data_inicio is None and data_final is None:
        raise ValueError("Data de início e data final não podem ser ambas nulas.")

    # Carrega metadados e converte datas para datetime
    series = ipea.metadata()
    series = series[series["MEASURE"].str.contains("\\$")]
    series["LAST UPDATE"] = pd.to_datetime(series["LAST UPDATE"], errors="coerce")

    # Verifica formato das datas
    try:
        if data_inicio is not None:
            data_inicio = pd.to_datetime(data_inicio, format="%Y-%m-%d")
        if data_final is not None:
            data_final = pd.to_datetime(data_final, format="%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Formato de data inválido: {e}")

    # Filtragem eficiente
    mask = pd.Series([True] * len(series))
    if data_inicio is not None:
        mask &= series["LAST UPDATE"] >= data_inicio
    if data_final is not None:
        mask &= series["LAST UPDATE"] <= data_final

    return series[mask].reset_index(drop=True)
    
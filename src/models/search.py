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

def date(data_inicio:str = None,data_final:str = None):
    """
    Explicar a função. Dizer o tipo de dado que são os parametros
    Forma de data: YYYY-MM-DD
    """

    if data_inicio is None and data_final is None:
        raise ValueError("Data de início e data final não podem ser ambas nulas.")
    
    series = ipea.metadata()
    series["LAST UPDATE"] = pd.to_datetime(series["LAST UPDATE"],format="ISO8601")
    series["LAST UPDATE"] = pd.to_datetime(series["LAST UPDATE"], errors='coerce')

    # A partir de data_inicio e antes de data_final
    if data_inicio is not None and data_final is not None:
        df_filtrado = series[(series["LAST UPDATE"] >= data_inicio) & (series["LAST UPDATE"] <= data_final)]
        
    # Após data_inicio
    if data_final is None:
        df_filtrado = series[(series["LAST UPDATE"] >= data_inicio)]

    # Antes data_final
    if data_inicio is None:
        df_filtrado = series[(series["LAST UPDATE"] <= data_final)]

    return df_filtrado 

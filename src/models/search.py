import ipeadatapy as ipea
import pandas as pd

def organization(phrase: str):
    """
    Retorna um dataframe contendo as series do IPEA de acordo com a string parametrizada referente a um órgão procurado.

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encotrado".
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

    Caso a busca não seja bem sucedida sera retornado uma string "Não Encotrado".
    """
    getThemeID = ipea.themes()
    getThemeID['NAME'] = getThemeID['NAME'].str.lower()
    getThemeID = getThemeID[getThemeID['NAME'].str.contains(phrase.lower())]
    try:
        found = pd.DataFrame()
        for id in getThemeID['ID']:
            find = ipea.metadata(theme_id=id)
            find = find[find['MEASURE'].str.contains("\\$")]
            found = pd.concat([found, find], ignore_index=True)
        found = found.sort_values(by='CODE')
    except:
        return "Não Encontrado"
    else:
        return "Não Encontrado" if found.empty else found
    

import ipeadatapy as ipea
import pandas as pd
   
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
    

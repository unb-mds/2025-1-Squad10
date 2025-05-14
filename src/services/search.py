import ipeadatapy as ipea
import pandas as pd

def filtro(organizacao_usuario:str, tema_usuario:str, codigo_usuario:str, data_inicio_usuario:str, data_fim_usuario:str, pais_usuario:str, frequencia_usuario:str, unidade_usuario:str, subtema_usuario:str):
    # Carrega metadados iniciais
    informacoes = ipea.metadata()
    informacoes = informacoes[informacoes["MEASURE"].str.contains("\\$")]
    
    # Lista para armazenar DataFrames filtrados
    filtros = [informacoes]

    # Filtra pelo código do usuário
    if codigo_usuario.strip():
        filtros.append(informacoes[informacoes["CODE"].str.contains(codigo_usuario.upper())])

    # Filtra pela organização
    if organizacao_usuario.strip():
        org_mask = informacoes["SOURCE ACRONYM"].str.lower().str.contains(organizacao_usuario.lower()) | \
                   informacoes["SOURCE"].str.lower().str.contains(organizacao_usuario.lower())
        filtros.append(informacoes[org_mask])

    # Filtra pelo tema
    if tema_usuario.strip():
        temas = ipea.themes()
        temas_filtrados = temas[temas['NAME'].str.lower().str.contains(tema_usuario.lower())]
        if not temas_filtrados.empty:
            for theme_id in temas_filtrados['ID']:
                filtros.append(ipea.metadata(theme_id=theme_id))

    # Filtra pelas datas (com validação)
    if data_inicio_usuario.strip() or data_fim_usuario.strip():
        informacoes["LAST UPDATE"] = pd.to_datetime(informacoes["LAST UPDATE"], errors="coerce")
        try:
            data_inicio = pd.to_datetime(data_inicio_usuario.strip(), format="%Y-%m-%d") if data_inicio_usuario.strip() else None
            data_fim = pd.to_datetime(data_fim_usuario.strip(), format="%Y-%m-%d") if data_fim_usuario.strip() else None
        except ValueError as e:
            raise ValueError(f"Formato de data inválido: {e}")

        date_mask = pd.Series([True] * len(informacoes))
        if data_inicio is not None:
            date_mask &= informacoes["LAST UPDATE"] >= data_inicio
        if data_fim is not None:
            date_mask &= informacoes["LAST UPDATE"] <= data_fim
        filtros.append(informacoes[date_mask])

    # Filtra por país
    if pais_usuario.strip():
        filtros.append(informacoes[informacoes["COUNTRY"].str.lower().str.contains(pais_usuario.lower())])

    # Filtra por frequência
    if frequencia_usuario.strip():
        filtros.append(informacoes[informacoes["FREQUENCY"].str.lower().str.contains(frequencia_usuario.lower())])

    # Filtra por unidade
    if unidade_usuario.strip():
        filtros.append(informacoes[informacoes["UNIT"].str.lower().str.contains(unidade_usuario.lower())])

    # Filtra por subtema
    if subtema_usuario.strip():
        filtros.append(informacoes[informacoes["SUBTHEME"].str.lower().str.contains(subtema_usuario.lower())])

    # Junta todos os filtros e remove duplicatas
    informacoes_final = pd.concat(filtros).drop_duplicates().reset_index(drop=True)

    return informacoes_final

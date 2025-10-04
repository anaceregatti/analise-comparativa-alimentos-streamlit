"""
Centralização de cache e carregamento de dados
"""

import streamlit as st
import pandas as pd
from config.settings import DATA_FILE_PATH

@st.cache_data(persist="disk")
def load_data():
    """
    Carrega os dados do CSV com cache persistente em disco para melhor performance.
    Ideal para CSVs grandes que mudam pouco.
    """
    df = pd.read_csv(DATA_FILE_PATH)
    return sanitize_data(df)

def sanitize_data(df):
    """
    Aplica saneamento leve nos dados:
    - Remove espaços em branco desnecessários
    - Normaliza nomes de grupos
    - Remove linhas com dados inválidos
    """
    # Criar uma cópia para não modificar o original
    df_clean = df.copy()
    
    # Limpar espaços em branco em colunas de texto
    text_columns = ['alimento', 'grupo']
    for col in text_columns:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.strip()
    
    # Normalizar nomes de grupos (primeira letra maiúscula, resto minúscula)
    if 'grupo' in df_clean.columns:
        df_clean['grupo'] = df_clean['grupo'].str.title()
    
    # Remover linhas com dados inválidos
    df_clean = df_clean.dropna(subset=['alimento', 'grupo'])
    df_clean = df_clean[df_clean['alimento'] != '']
    df_clean = df_clean[df_clean['grupo'] != '']
    
    return df_clean

def get_food_data(df, food_name):
    """
    Retorna dados de um alimento específico
    """
    if not food_name:
        return pd.DataFrame()
    return df[df['alimento'] == food_name]

def get_groups(df):
    """
    Retorna grupos únicos de alimentos já ordenados e limpos
    """
    if df is None or df.empty or 'grupo' not in df.columns:
        return []
    
    grupos_unicos = df['grupo'].dropna().unique()
    grupos_limpos = [g for g in grupos_unicos if g and str(g).strip()]
    return sorted(grupos_limpos)

def get_food_groups(df):
    """
    Função de compatibilidade - retorna grupos únicos de alimentos limpos
    """
    return get_groups(df)

def get_filtered_foods(df, selected_groups):
    """
    Retorna alimentos filtrados por grupos selecionados
    """
    if not selected_groups:
        return df['alimento'].unique()
    return df[df['grupo'].isin(selected_groups)]['alimento'].unique()

def validate_food_selection(food1, food2):
    """
    Valida se a seleção de alimentos é válida
    """
    if not food1 or not food2:
        return False, "Selecione ambos os alimentos"
    
    if food1 == food2:
        return False, "Selecione alimentos diferentes"
    
    return True, "OK"

# Funções para diferentes fontes de dados (extensibilidade)
def load_from_csv(file_path):
    """
    Carrega dados de um arquivo CSV
    """
    return pd.read_csv(file_path)

def load_from_gsheet(sheet_url, sheet_name=None):
    """
    Carrega dados do Google Sheets (requer gspread)
    """
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        
        # Configurar credenciais (implementar conforme necessário)
        # scope = ['https://spreadsheets.google.com/feeds']
        # creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
        # gc = gspread.authorize(creds)
        # sheet = gc.open_by_url(sheet_url).sheet1
        # data = sheet.get_all_records()
        # return pd.DataFrame(data)
        
        # Placeholder para implementação futura
        raise NotImplementedError("Google Sheets integration not implemented yet")
    except ImportError:
        raise ImportError("gspread library required for Google Sheets integration")

def load_from_api(api_url, params=None):
    """
    Carrega dados de uma API REST
    """
    try:
        import requests
        
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        
        if response.headers.get('content-type', '').startswith('application/json'):
            data = response.json()
            return pd.DataFrame(data)
        else:
            # Assumir CSV se não for JSON
            from io import StringIO
            return pd.read_csv(StringIO(response.text))
            
    except ImportError:
        raise ImportError("requests library required for API integration")

def get_data_source_config():
    """
    Retorna configuração da fonte de dados atual
    """
    return {
        'type': 'csv',
        'path': DATA_FILE_PATH,
        'description': 'Arquivo CSV local com dados nutricionais'
    }

def switch_data_source(source_type, **kwargs):
    """
    Permite trocar a fonte de dados (para futuras implementações)
    """
    if source_type == 'csv':
        return load_from_csv(kwargs.get('file_path', DATA_FILE_PATH))
    elif source_type == 'gsheet':
        return load_from_gsheet(kwargs.get('sheet_url'), kwargs.get('sheet_name'))
    elif source_type == 'api':
        return load_from_api(kwargs.get('api_url'), kwargs.get('params'))
    else:
        raise ValueError(f"Fonte de dados não suportada: {source_type}")

# Funções de utilidade para análise de dados
def get_data_info(df):
    """
    Retorna informações sobre o dataset carregado
    """
    if df is None or df.empty:
        return {
            'total_rows': 0,
            'total_columns': 0,
            'groups_count': 0,
            'foods_count': 0,
            'columns': []
        }
    
    return {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'groups_count': len(get_groups(df)),
        'foods_count': len(df['alimento'].unique()) if 'alimento' in df.columns else 0,
        'columns': list(df.columns)
    }

def validate_data_structure(df):
    """
    Valida se a estrutura dos dados está correta
    """
    required_columns = ['alimento', 'grupo']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        return False, f"Colunas obrigatórias ausentes: {missing_columns}"
    
    if df.empty:
        return False, "Dataset vazio"
    
    return True, "Estrutura válida"

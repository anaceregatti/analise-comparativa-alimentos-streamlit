"""
Funcoes puras para calculos e formatacao
"""

import pandas as pd
from config.settings import NUMBER_FORMAT
from domain.palette import get_slot_colors, get_slot_solid

def format_number(value):
    """
    Formata numeros com ponto para milhares
    """
    if pd.isna(value) or value == 0:
        return NUMBER_FORMAT['na_value']
    
    if value >= 1000:
        return f"{value:,.1f}".replace(",", NUMBER_FORMAT['thousands_separator'])
    else:
        return f"{value:.{NUMBER_FORMAT['decimal_places']}f}"

def format_fractions(value):
    """
    Formata numeros para frações com 3 casas decimais
    """
    if pd.isna(value) or value == 0:
        return NUMBER_FORMAT['na_value']
    
    return f"{value:.3f}"

def calculate_macro_percentages(carb, lip, prot):
    """
    Calcula percentuais de macronutrientes
    """
    total = carb + lip + prot
    if total == 0:
        return 0, 0, 0
    
    carb_pct = (carb / total) * 100
    lip_pct = (lip / total) * 100
    prot_pct = (prot / total) * 100
    
    return carb_pct, lip_pct, prot_pct

def dynamic_upper_limit(df1, df2, columns, margin=0.1):
    """
    Calcula o upper limit dinâmico baseado no maior valor entre os dois DataFrames.
    Adiciona uma margem para melhor visualização.
    
    Args:
        df1: Primeiro DataFrame
        df2: Segundo DataFrame  
        columns: Lista de colunas para analisar
        margin: Margem percentual (padrão 0.1 = 10%)
        
    Returns:
        float: Upper limit calculado
    """
    max_value = 0
    
    for column in columns:
        if column in df1.columns:
            value1 = df1[column].iloc[0]
            if not pd.isna(value1) and value1 > max_value:
                max_value = value1
        
        if column in df2.columns:
            value2 = df2[column].iloc[0]
            if not pd.isna(value2) and value2 > max_value:
                max_value = value2
    
    # Adicionar margem e arredondar para cima
    upper_limit = max_value * (1 + margin)
    return upper_limit

def percent(parts: dict[str, float]) -> dict[str, float]:
    """
    Calcula percentuais de um dicionário de partes.
    
    Args:
        parts: Dicionário com {nome: valor}
        
    Returns:
        dict: Dicionário com {nome: percentual}
    """
    if not parts:
        return {}
    
    total = sum(parts.values())
    if total == 0:
        return {name: 0.0 for name in parts.keys()}
    
    return {name: (value / total) * 100 for name, value in parts.items()}

def get_nutrient_value(data, column, default=0):
    """
    Obtem valor de um nutriente com valor padrao
    """
    if data is None or data.empty or column not in data.columns:
        return default
    
    try:
        value = data[column].iloc[0]
        # Verificar se o valor é válido (não NaN, não None, não undefined, não string vazia)
        if (pd.isna(value) or 
            value is None or 
            str(value).lower() in ['undefined', 'nan', ''] or
            str(value).strip() == ''):
            return default
        
        # Tentar converter para float
        numeric_value = float(value)
        return numeric_value if numeric_value >= 0 else default
    except (IndexError, KeyError, ValueError, TypeError, AttributeError):
        return default

def is_valid_nutrient_value(value):
    """
    Verifica se um valor de nutriente e valido (nao nulo e maior que zero)
    """
    return not pd.isna(value) and value > 0

def clean_nutrient_data(data, columns):
    """
    Limpa dados de nutrientes removendo valores inválidos
    """
    if data is None or data.empty:
        return {}
    
    clean_data = {}
    for label, coluna in columns.items():
        if coluna in data.columns:
            valor = get_nutrient_value(data, coluna)
            if valor > 0:
                clean_data[label] = valor
    
    return clean_data

def calculate_macro_totals(data):
    """
    Calcula totais de macronutrientes para um alimento
    """
    carb = get_nutrient_value(data, 'carboidrato_g')
    lip = get_nutrient_value(data, 'lipideos_g')
    prot = get_nutrient_value(data, 'proteina_g')
    
    return {
        'carboidrato': carb,
        'lipideos': lip,
        'proteina': prot,
        'total': carb + lip + prot
    }

def get_basic_metrics(data):
    """
    Obtem metricas basicas de um alimento
    """
    return {
        'energia': get_nutrient_value(data, 'energia_kcal'),
        'fibra': get_nutrient_value(data, 'fibra_alimentar_g'),
        'agua': get_nutrient_value(data, 'umidade_pct'),
        'grupo': data['grupo'].iloc[0] if not data.empty and 'grupo' in data.columns else "Nao informado"
    }

def get_slot_scale(slot):
    """
    Retorna escala de cores para um slot específico
    """
    colors = get_slot_colors(slot)
    return {
        'primary': colors['primary'],
        'secondary': colors['secondary'],
        'solid': colors['solid'],
        'gradient': colors['gradient']
    }

def get_food_colors_by_slot():
    """
    Retorna cores para alimentos baseado em slots
    """
    return {
        'left': get_slot_solid('left'),    # Azul para alimento1
        'right': get_slot_solid('right')   # Verde para alimento2
    }

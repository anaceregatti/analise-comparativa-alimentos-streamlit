"""
Funções puras para filtros e manipulação de dados
"""

import pandas as pd
from typing import List, Optional, Union

def filter_foods_by_groups(df: pd.DataFrame, groups: List[str]) -> pd.DataFrame:
    """
    Filtra alimentos por grupos selecionados.
    
    Args:
        df: DataFrame com dados nutricionais
        groups: Lista de grupos para filtrar
        
    Returns:
        DataFrame filtrado com apenas os alimentos dos grupos especificados
    """
    if not groups or df.empty or 'grupo' not in df.columns:
        return df
    
    return df[df['grupo'].isin(groups)]

def row_by_food(df: pd.DataFrame, food_name: str) -> pd.DataFrame:
    """
    Retorna uma linha específica do DataFrame baseada no nome do alimento.
    
    Args:
        df: DataFrame com dados nutricionais
        food_name: Nome do alimento a ser buscado
        
    Returns:
        DataFrame com uma única linha contendo os dados do alimento
    """
    if df.empty or not food_name or 'alimento' not in df.columns:
        return pd.DataFrame()
    
    filtered = df[df['alimento'] == food_name]
    return filtered.copy()

def get_food_names(df: pd.DataFrame, groups: Optional[List[str]] = None) -> List[str]:
    """
    Retorna lista de nomes de alimentos, opcionalmente filtrados por grupos.
    
    Args:
        df: DataFrame com dados nutricionais
        groups: Lista opcional de grupos para filtrar
        
    Returns:
        Lista de nomes de alimentos únicos, ordenados alfabeticamente
    """
    if df.empty or 'alimento' not in df.columns:
        return []
    
    if groups:
        filtered_df = filter_foods_by_groups(df, groups)
    else:
        filtered_df = df
    
    food_names = filtered_df['alimento'].dropna().unique()
    return sorted([name for name in food_names if name and str(name).strip()])

def get_available_groups(df: pd.DataFrame) -> List[str]:
    """
    Retorna lista de grupos únicos disponíveis no DataFrame.
    
    Args:
        df: DataFrame com dados nutricionais
        
    Returns:
        Lista de grupos únicos, ordenados alfabeticamente
    """
    if df.empty or 'grupo' not in df.columns:
        return []
    
    groups = df['grupo'].dropna().unique()
    return sorted([group for group in groups if group and str(group).strip()])

def validate_food_exists(df: pd.DataFrame, food_name: str) -> bool:
    """
    Verifica se um alimento existe no DataFrame.
    
    Args:
        df: DataFrame com dados nutricionais
        food_name: Nome do alimento a verificar
        
    Returns:
        True se o alimento existe, False caso contrário
    """
    if df.empty or not food_name or 'alimento' not in df.columns:
        return False
    
    return food_name in df['alimento'].values

def get_food_count_by_group(df: pd.DataFrame, group: str) -> int:
    """
    Retorna o número de alimentos em um grupo específico.
    
    Args:
        df: DataFrame com dados nutricionais
        group: Nome do grupo
        
    Returns:
        Número de alimentos no grupo
    """
    if df.empty or not group or 'grupo' not in df.columns:
        return 0
    
    return len(df[df['grupo'] == group])

def get_groups_with_counts(df: pd.DataFrame) -> dict[str, int]:
    """
    Retorna dicionário com grupos e seus respectivos números de alimentos.
    
    Args:
        df: DataFrame com dados nutricionais
        
    Returns:
        Dicionário {grupo: quantidade}
    """
    if df.empty or 'grupo' not in df.columns:
        return {}
    
    group_counts = df['grupo'].value_counts().to_dict()
    return {group: count for group, count in group_counts.items() if group and str(group).strip()}

def filter_foods_by_name(df: pd.DataFrame, search_term: str) -> pd.DataFrame:
    """
    Filtra alimentos por termo de busca no nome.
    
    Args:
        df: DataFrame com dados nutricionais
        search_term: Termo para buscar no nome do alimento
        
    Returns:
        DataFrame filtrado com alimentos que contêm o termo
    """
    if df.empty or not search_term or 'alimento' not in df.columns:
        return df
    
    search_lower = search_term.lower()
    mask = df['alimento'].str.lower().str.contains(search_lower, na=False)
    return df[mask]

def get_food_nutritional_data(df: pd.DataFrame, food_name: str, nutrients: List[str]) -> dict:
    """
    Retorna dados nutricionais específicos de um alimento.
    
    Args:
        df: DataFrame com dados nutricionais
        food_name: Nome do alimento
        nutrients: Lista de colunas de nutrientes
        
    Returns:
        Dicionário com {nutriente: valor}
    """
    if df.empty or not food_name or not nutrients:
        return {}
    
    food_data = row_by_food(df, food_name)
    if food_data.empty:
        return {}
    
    result = {}
    for nutrient in nutrients:
        if nutrient in food_data.columns:
            value = food_data[nutrient].iloc[0]
            result[nutrient] = value if not pd.isna(value) else 0
    
    return result

def compare_foods_nutrition(df: pd.DataFrame, food1: str, food2: str, nutrients: List[str]) -> pd.DataFrame:
    """
    Compara dados nutricionais de dois alimentos.
    
    Args:
        df: DataFrame com dados nutricionais
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        nutrients: Lista de colunas de nutrientes para comparar
        
    Returns:
        DataFrame com comparação lado a lado
    """
    if df.empty or not food1 or not food2 or not nutrients:
        return pd.DataFrame()
    
    data1 = get_food_nutritional_data(df, food1, nutrients)
    data2 = get_food_nutritional_data(df, food2, nutrients)
    
    if not data1 or not data2:
        return pd.DataFrame()
    
    comparison_data = []
    for nutrient in nutrients:
        if nutrient in data1 and nutrient in data2:
            comparison_data.append({
                'Nutriente': nutrient,
                food1: data1[nutrient],
                food2: data2[nutrient]
            })
    
    return pd.DataFrame(comparison_data)

def get_food_groups_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Retorna resumo dos grupos de alimentos com estatísticas.
    
    Args:
        df: DataFrame com dados nutricionais
        
    Returns:
        DataFrame com resumo dos grupos
    """
    if df.empty or 'grupo' not in df.columns:
        return pd.DataFrame()
    
    summary = df.groupby('grupo').agg({
        'alimento': 'count',
        'energia_kcal': 'mean',
        'proteina_g': 'mean',
        'carboidrato_g': 'mean',
        'lipideos_g': 'mean'
    }).round(2)
    
    summary.columns = ['Total_Alimentos', 'Energia_Media', 'Proteina_Media', 'Carboidrato_Media', 'Lipideos_Media']
    summary = summary.reset_index()
    
    return summary.sort_values('Total_Alimentos', ascending=False)

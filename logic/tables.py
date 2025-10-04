"""
Funções para criação de tabelas padronizadas
"""

import pandas as pd
import streamlit as st
from domain.nutrients import (
    get_micronutrient_categories,
    get_complexo_b_mapping,
    get_lipid_fractions,
    get_protein_fractions,
    get_macronutrients,
    get_basic_nutrients,
    get_nutrient_unit
)
from logic.compute import format_number, format_fractions, get_nutrient_value

def paired_table(df1, df2, mapping: dict[str, str], food1: str, food2: str, formatter=format_number):
    """
    Função genérica para criar tabela pareada.
    
    Args:
        df1: DataFrame do primeiro alimento
        df2: DataFrame do segundo alimento
        mapping: Dicionário {label: coluna}
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        formatter: Função para formatar valores (padrão: format_number)
        
    Returns:
        DataFrame: Tabela padronizada (Nutriente, Alimento1, Alimento2)
    """
    dados_combinados = []
    
    for label, coluna in mapping.items():
        # Valor do alimento 1
        valor1 = get_nutrient_value(df1, coluna)
        valor1_str = formatter(valor1) if valor1 > 0 else "N/A"
        
        # Valor do alimento 2
        valor2 = get_nutrient_value(df2, coluna)
        valor2_str = formatter(valor2) if valor2 > 0 else "N/A"
        
        dados_combinados.append({
            'Nutriente': label,
            food1: valor1_str,
            food2: valor2_str
        })
    
    return pd.DataFrame(dados_combinados) if dados_combinados else pd.DataFrame()

def create_micronutrient_tables(data1, data2, food1, food2):
    """
    Cria tabelas de micronutrientes pareadas usando a função genérica
    """
    categorias = get_micronutrient_categories()
    resultado = {}
    
    for categoria, nutrientes in categorias.items():
        tabela = paired_table(data1, data2, nutrientes, food1, food2)
        if not tabela.empty:
            resultado[categoria] = tabela
    
    return resultado

def create_complexo_b_table(data1, data2, food1, food2):
    """
    Cria tabela específica do Complexo B usando a função genérica
    """
    complexo_b_mapping = get_complexo_b_mapping()
    
    # Converter mapeamento complexo para formato simples
    simple_mapping = {nutriente: coluna for nutriente, (coluna, _) in complexo_b_mapping.items()}
    
    return paired_table(data1, data2, simple_mapping, food1, food2)

def create_lipid_fractions_table(data1, data2, food1, food2):
    """
    Cria tabela de frações de lipídios usando a função genérica com formatação de 3 casas decimais
    """
    fracoes_lipidios = get_lipid_fractions()
    return paired_table(data1, data2, fracoes_lipidios, food1, food2, formatter=format_fractions)

def create_protein_fractions_table(data1, data2, food1, food2):
    """
    Cria tabela de frações de proteínas (aminoácidos) usando a função genérica com formatação de 3 casas decimais
    """
    aminoacidos = get_protein_fractions()
    return paired_table(data1, data2, aminoacidos, food1, food2, formatter=format_fractions)

def create_macronutrient_table(data1, data2, food1, food2):
    """
    Cria tabela de macronutrientes básicos usando a função genérica
    """
    # Combinar macronutrientes e nutrientes básicos
    macronutrientes = get_macronutrients()
    basic_nutrients = get_basic_nutrients()
    
    # Criar tabela de macronutrientes
    macro_table = paired_table(data1, data2, macronutrientes, food1, food2)
    
    # Criar tabela de nutrientes básicos
    basic_table = paired_table(data1, data2, basic_nutrients, food1, food2)
    
    # Combinar as tabelas
    if not macro_table.empty and not basic_table.empty:
        return pd.concat([macro_table, basic_table], ignore_index=True)
    elif not macro_table.empty:
        return macro_table
    elif not basic_table.empty:
        return basic_table
    else:
        return pd.DataFrame()

def standardize_table(df, food1, food2):
    """
    Padroniza tabelas para ter 3 colunas (Nutriente, alimento1, alimento2).
    Garante que a tabela tenha exatamente 3 colunas com nomes padronizados.
    
    Args:
        df: DataFrame para padronizar
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        
    Returns:
        DataFrame: Tabela padronizada com 3 colunas
    """
    if df.empty:
        return df
    
    # Se já tem 3 colunas, verificar se os nomes estão corretos
    if len(df.columns) == 3:
        expected_columns = ['Nutriente', food1, food2]
        if list(df.columns) == expected_columns:
            return df
        else:
            # Renomear colunas se necessário
            df_padronizado = df.copy()
            df_padronizado.columns = expected_columns
            return df_padronizado
    
    # Se tem 4 colunas, remover a coluna do meio
    if len(df.columns) == 4:
        df_padronizado = df.copy()
        df_padronizado = df_padronizado.drop(df_padronizado.columns[1], axis=1)
        df_padronizado.columns = ['Nutriente', food1, food2]
        return df_padronizado
    
    # Se tem 2 colunas, adicionar coluna de nutriente
    if len(df.columns) == 2:
        df_padronizado = df.copy()
        df_padronizado.insert(0, 'Nutriente', '')
        df_padronizado.columns = ['Nutriente', food1, food2]
        return df_padronizado
    
    return df

def display_colored_table(df, food1, food2):
    """
    Exibe tabela com cores nos cabeçalhos para reforçar comunicação visual.
    
    Args:
        df: DataFrame da tabela
        food1: Nome do primeiro alimento (azul/roxo)
        food2: Nome do segundo alimento (verde/rosa)
    """
    if df.empty:
        st.info("Nenhum dado disponível para exibir")
        return
    
    # Obter cores por slot usando novo sistema
    from domain.palette import get_slot_solid
    color1 = get_slot_solid('left')   # Azul para alimento 1
    color2 = get_slot_solid('right')  # Verde para alimento 2
    
    # CSS para dark mode com cores dos alimentos
    css_style = f"""
    <style>
    .colored-table {{
        border-collapse: collapse;
        width: 100%;
        background-color: #1e1e1e;
        color: #ffffff;
        font-size: 13px;
        line-height: 1.1;
    }}
    .colored-table th {{
        background-color: #2d2d2d;
        border: 1px solid #444444;
        padding: 6px 8px;
        text-align: center;
        font-weight: bold;
        color: #ffffff;
        font-size: 14px;
    }}
    .colored-table th:nth-child(1) {{
        background-color: #2d2d2d !important;
        color: #ffffff !important;
    }}
    .colored-table th:nth-child(2) {{
        background-color: {color1} !important;
        color: #ffffff !important;
        font-weight: bold;
    }}
    .colored-table th:nth-child(3) {{
        background-color: {color2} !important;
        color: #ffffff !important;
        font-weight: bold;
    }}
    .colored-table td {{
        border: 1px solid #444444;
        padding: 4px 6px;
        text-align: center;
        color: #ffffff;
        font-size: 13px;
        line-height: 1.2;
    }}
    .colored-table tr:nth-child(even) {{
        background-color: #2a2a2a;
    }}
    .colored-table tr:nth-child(odd) {{
        background-color: #1e1e1e;
    }}
    .colored-table tr:nth-child(even) td:nth-child(2) {{
        background-color: {color1}20 !important;
        color: #ffffff !important;
    }}
    .colored-table tr:nth-child(odd) td:nth-child(2) {{
        background-color: {color1}15 !important;
        color: #ffffff !important;
    }}
    .colored-table tr:nth-child(even) td:nth-child(3) {{
        background-color: {color2}20 !important;
        color: #ffffff !important;
    }}
    .colored-table tr:nth-child(odd) td:nth-child(3) {{
        background-color: {color2}15 !important;
        color: #ffffff !important;
    }}
    .colored-table tr {{
        height: 28px;
    }}
    .colored-table th, .colored-table td {{
        vertical-align: middle;
    }}
    </style>
    """
    
    # Aplicar CSS
    st.markdown(css_style, unsafe_allow_html=True)
    
    # Exibir tabela com estilo
    st.markdown(df.to_html(classes='colored-table', escape=False, index=False), unsafe_allow_html=True)

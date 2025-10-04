"""
Funções genéricas para criação de gráficos - API única
"""

import plotly.graph_objects as go
import pandas as pd
from config.settings import COLORS, CHART_HEIGHT, CHART_HEIGHT_SMALL, CHART_HEIGHT_MINI
from logic.compute import calculate_macro_percentages, dynamic_upper_limit, get_nutrient_value, clean_nutrient_data, get_slot_scale, get_food_colors_by_slot
from domain.palette import get_slot_solid

def get_first_nutrient(nutrientes1, nutrientes2, default="Nutriente"):
    """
    Obtém o primeiro nutriente de uma das listas para usar como título
    """
    if nutrientes1:
        return list(nutrientes1.keys())[0]
    elif nutrientes2:
        return list(nutrientes2.keys())[0]
    else:
        return default
from domain.nutrients import get_chart_colors, get_nutrient_color, get_macronutrients

def pie_macros(df_row, food_name, mapping=None, slot='left'):
    """
    Cria gráfico de pizza genérico para macronutrientes ou outros nutrientes.
    
    Args:
        df_row: DataFrame com uma linha do alimento
        food_name: Nome do alimento
        mapping: Dicionário {label: coluna} (padrão: MACROS)
        slot: Slot do alimento ('left' ou 'right')
    """
    if df_row is None or df_row.empty:
        return go.Figure()
    
    # Usar mapping padrão se não fornecido
    if mapping is None:
        mapping = get_macronutrients()
    
    # Obter valores dos nutrientes
    nutrientes = {}
    for label, coluna in mapping.items():
        valor = get_nutrient_value(df_row, coluna)
        if valor > 0:
            nutrientes[label] = valor
    
    if not nutrientes:
        fig = go.Figure()
        fig.add_annotation(
            text="Não há dados",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16)
        )
        fig.update_layout(
            title="Macronutrientes",
            showlegend=False,
            height=CHART_HEIGHT
        )
        return fig
    
    # Usar função de limpeza para evitar "undefined"
    nutrientes = clean_nutrient_data(df_row, mapping)
    
    if not nutrientes:
        fig = go.Figure()
        fig.add_annotation(
            text="Não há dados válidos",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16)
        )
        fig.update_layout(
            title="Macronutrientes",
            showlegend=False,
            height=CHART_HEIGHT
        )
        return fig
    
    labels = list(nutrientes.keys())
    values = list(nutrientes.values())
    
    # Cores específicas por nutriente
    colors = []
    for label in labels:
        colors.append(get_nutrient_color(label))
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        textinfo='percent',
        textposition='inside',
        textfont=dict(size=14, color='white'),
        marker=dict(colors=colors[:len(labels)]),
        hovertemplate='<b>%{label}</b><br>Valor: %{value:.2f}g<br>Percentual: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title=dict(
            text="Macronutrientes",
            font=dict(size=16, color='#2E3440')
        ),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.02,
            font=dict(size=12, color='white'),
            bgcolor='rgba(0,0,0,0.1)',
            bordercolor='rgba(255,255,255,0.2)',
            borderwidth=1
        ),
        height=CHART_HEIGHT,
        margin=dict(t=60, b=20, l=20, r=120),
        font=dict(family="Arial, sans-serif")
    )
    
    return fig

def bar_single(df_row, title, columns, units, upper_limit=None):
    """
    Cria gráfico de barras genérico para um alimento com várias barras.
    
    Args:
        df_row: DataFrame com uma linha do alimento
        title: Título do gráfico
        columns: Lista de colunas ou dicionário {label: coluna}
        units: Unidade dos valores (ex: "g", "mg", "kcal")
        upper_limit: Limite superior do eixo Y (opcional)
    """
    if df_row is None or df_row.empty:
        return go.Figure()
    
    # Converter columns para dicionário se for lista
    if isinstance(columns, list):
        columns = {col: col for col in columns}
    
    # Usar função de limpeza para evitar "undefined"
    nutrientes = clean_nutrient_data(df_row, columns)
    
    if not nutrientes:
        return go.Figure()
    
    # Cores específicas por nutriente
    colors = []
    for label in nutrientes.keys():
        colors.append(get_nutrient_color(label))
    
    fig = go.Figure()
    
    for i, (label, valor) in enumerate(nutrientes.items()):
        fig.add_trace(go.Bar(
            name=label,
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.1f}</b>"] if not pd.isna(valor) and valor is not None else [""],
            textposition='auto',
            marker_color=colors[i % len(colors)]
        ))
    
    # Calcular upper limit se não fornecido
    if upper_limit is None:
        upper_limit = max(nutrientes.values()) * 1.1
    
    # Título será obtido pela função get_first_nutrient
    
    fig.update_layout(
        title=get_first_nutrient(nutrientes, {}, "Nutriente"),  # Usar nome do nutriente como título
        xaxis_title=None,  # Remover "Nutrientes" redundante
        yaxis_title=f"Valor ({units})",
        yaxis=dict(range=[0, upper_limit]),
        height=CHART_HEIGHT_SMALL,
        font=dict(family="Arial, sans-serif"),
        showlegend=False
    )
    
    return fig

def bar_compare(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None, slot1='left', slot2='right'):
    """
    Cria gráfico de barras comparativo genérico para dois alimentos.
    
    Args:
        df1_row: DataFrame com uma linha do primeiro alimento
        df2_row: DataFrame com uma linha do segundo alimento
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        columns: Lista de colunas ou dicionário {label: coluna}
        title: Título do gráfico
        unit: Unidade dos valores (ex: "g", "mg", "kcal")
        upper_limit: Limite superior do eixo Y (opcional)
        slot1: Slot do primeiro alimento ('left' ou 'right')
        slot2: Slot do segundo alimento ('left' ou 'right')
    """
    if df1_row is None or df1_row.empty or df2_row is None or df2_row.empty:
        return go.Figure()
    
    # Converter columns para dicionário se for lista
    if isinstance(columns, list):
        columns = {col: col for col in columns}
    
    # Usar função de limpeza para evitar "undefined"
    nutrientes1 = clean_nutrient_data(df1_row, columns)
    nutrientes2 = clean_nutrient_data(df2_row, columns)
    
    if not nutrientes1 and not nutrientes2:
        return go.Figure()
    
    # Cores por slot
    color1 = get_slot_solid(slot1)
    color2 = get_slot_solid(slot2)
    
    fig = go.Figure()
    
    # Adicionar barras do primeiro alimento
    for i, (label, valor) in enumerate(nutrientes1.items()):
        fig.add_trace(go.Bar(
            name=food1,  # Nome simplificado
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.1f}</b>"] if not pd.isna(valor) and valor is not None else [""],
            textposition='auto',
            marker_color=color1,
            showlegend=(i == 0)  # Mostrar legenda apenas na primeira barra
        ))
    
    # Adicionar barras do segundo alimento
    for i, (label, valor) in enumerate(nutrientes2.items()):
        fig.add_trace(go.Bar(
            name=food2,  # Nome simplificado
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.1f}</b>"] if not pd.isna(valor) and valor is not None else [""],
            textposition='auto',
            marker_color=color2,
            showlegend=(i == 0)  # Mostrar legenda apenas na primeira barra
        ))
    
    # Calcular upper limit se não fornecido
    if upper_limit is None:
        all_values = list(nutrientes1.values()) + list(nutrientes2.values())
        if all_values:
            upper_limit = max(all_values) * 1.1
        else:
            upper_limit = 100
    
    fig.update_layout(
        title=get_first_nutrient(nutrientes1, nutrientes2),  # Usar nome do nutriente como título
        xaxis_title=None,  # Remover "Nutrientes" redundante
        yaxis_title=f"Valor ({unit})",
        yaxis=dict(range=[0, upper_limit]),
        height=CHART_HEIGHT_SMALL,
        font=dict(family="Arial, sans-serif"),
        showlegend=False
    )
    
    return fig

def bar_compare_aminoacidos(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None, slot1='left', slot2='right'):
    """
    Cria gráfico de barras comparativo específico para aminoácidos com altura maior e formatação adequada.
    
    Args:
        df1_row: DataFrame com uma linha do primeiro alimento
        df2_row: DataFrame com uma linha do segundo alimento
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        columns: Lista de colunas ou dicionário {label: coluna}
        title: Título do gráfico
        unit: Unidade dos valores (ex: "g", "mg", "kcal")
        upper_limit: Limite superior do eixo Y (opcional)
    """
    if df1_row is None or df1_row.empty or df2_row is None or df2_row.empty:
        return go.Figure()
    
    # Converter columns para dicionário se for lista
    if isinstance(columns, list):
        columns = {col: col for col in columns}
    
    # Usar função de limpeza para evitar "undefined"
    nutrientes1 = clean_nutrient_data(df1_row, columns)
    nutrientes2 = clean_nutrient_data(df2_row, columns)
    
    if not nutrientes1 and not nutrientes2:
        return go.Figure()
    
    # Cores por slot
    color1 = get_slot_solid(slot1)
    color2 = get_slot_solid(slot2)
    
    fig = go.Figure()
    
    # Adicionar barras do primeiro alimento
    for i, (label, valor) in enumerate(nutrientes1.items()):
        fig.add_trace(go.Bar(
            name=food1,  # Nome simplificado
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.3f}</b>"] if not pd.isna(valor) and valor is not None else [""],
            textposition='auto',
            marker_color=color1,
            width=0.4,  # Largura das barras maior
            showlegend=(i == 0)  # Mostrar legenda apenas na primeira barra
        ))
    
    # Adicionar barras do segundo alimento
    for i, (label, valor) in enumerate(nutrientes2.items()):
        fig.add_trace(go.Bar(
            name=food2,  # Nome simplificado
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.3f}</b>"] if not pd.isna(valor) and valor is not None else [""],
            textposition='auto',
            marker_color=color2,
            width=0.4,  # Largura das barras maior
            showlegend=(i == 0)  # Mostrar legenda apenas na primeira barra
        ))
    
    # Calcular upper limit se não fornecido
    if upper_limit is None:
        all_values = list(nutrientes1.values()) + list(nutrientes2.values())
        if all_values:
            upper_limit = max(all_values) * 1.1
        else:
            upper_limit = 100
    
    # Título será obtido pela função get_first_nutrient
    
    fig.update_layout(
        title=get_first_nutrient(nutrientes1, nutrientes2),  # Usar nome do nutriente como título
        xaxis_title=None,  # Remover "Aminoácidos" redundante
        yaxis_title=f"Valor ({unit})",
        yaxis=dict(
            range=[0, upper_limit],
            tickfont=dict(size=10)
        ),
        height=500,  # Altura maior para aminoácidos
        font=dict(family="Arial, sans-serif", size=12),
        showlegend=False,
        margin=dict(t=80, b=60, l=60, r=60),  # Margens maiores
        xaxis=dict(
            tickangle=-45,  # Rotacionar labels do eixo X
            tickfont=dict(size=10)
        )
    )
    
    return fig

def bar_compare_fractions(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None, slot1='left', slot2='right'):
    """
    Cria gráfico de barras comparativo específico para frações com 3 casas decimais.
    
    Args:
        df1_row: DataFrame com uma linha do primeiro alimento
        df2_row: DataFrame com uma linha do segundo alimento
        food1: Nome do primeiro alimento
        food2: Nome do segundo alimento
        columns: Lista de colunas ou dicionário {label: coluna}
        title: Título do gráfico
        unit: Unidade dos valores (ex: "g", "mg", "kcal")
        upper_limit: Limite superior do eixo Y (opcional)
    """
    if df1_row is None or df1_row.empty or df2_row is None or df2_row.empty:
        return go.Figure()
    
    # Converter columns para dicionário se for lista
    if isinstance(columns, list):
        columns = {col: col for col in columns}
    
    # Usar função de limpeza para evitar "undefined"
    nutrientes1 = clean_nutrient_data(df1_row, columns)
    nutrientes2 = clean_nutrient_data(df2_row, columns)
    
    if not nutrientes1 and not nutrientes2:
        return go.Figure()
    
    # Cores por slot
    color1 = get_slot_solid(slot1)
    color2 = get_slot_solid(slot2)
    
    fig = go.Figure()
    
    # Adicionar barras do primeiro alimento
    for i, (label, valor) in enumerate(nutrientes1.items()):
        fig.add_trace(go.Bar(
            name=food1,
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.3f}</b>"] if not pd.isna(valor) and valor is not None else [""],  # 3 casas decimais
            textposition='auto',
            marker_color=color1,
            width=0.4,
            showlegend=(i == 0)
        ))
    
    # Adicionar barras do segundo alimento
    for i, (label, valor) in enumerate(nutrientes2.items()):
        fig.add_trace(go.Bar(
            name=food2,
            x=[label],
            y=[valor],
            text=[f"<b>{valor:.3f}</b>"] if not pd.isna(valor) and valor is not None else [""],  # 3 casas decimais
            textposition='auto',
            marker_color=color2,
            width=0.4,
            showlegend=(i == 0)
        ))
    
    # Calcular upper limit se não fornecido
    if upper_limit is None:
        all_values = list(nutrientes1.values()) + list(nutrientes2.values())
        if all_values:
            upper_limit = max(all_values) * 1.1
        else:
            upper_limit = 100
    
    fig.update_layout(
        title=get_first_nutrient(nutrientes1, nutrientes2),  # Usar nome do nutriente como título
        xaxis_title=None,  # Remover "Nutrientes" redundante
        yaxis_title=f"Valor ({unit})",
        yaxis=dict(range=[0, upper_limit]),
        height=CHART_HEIGHT_SMALL,
        font=dict(family="Arial, sans-serif"),
        showlegend=False
    )
    
    return fig

# Funções auxiliares para compatibilidade (usando as genéricas)

def bar_macros(data, food_name, upper_limit=None):
    """
    Função de compatibilidade - usa bar_single genérica
    """
    mapping = get_macronutrients()
    return bar_single(data, "Macronutrientes", mapping, "g", upper_limit)

def bar_multiple_compare(data1, data2, columns, titles, y_title, food1, food2, color1=None, color2=None):
    """
    Função de compatibilidade - usa bar_compare genérica
    """
    # Converter para dicionário se necessário
    if isinstance(columns, list) and isinstance(titles, list):
        mapping = dict(zip(titles, columns))
    else:
        mapping = columns
    
    return bar_compare(data1, data2, food1, food2, mapping, "Comparativo de Nutrientes", y_title.split()[0])

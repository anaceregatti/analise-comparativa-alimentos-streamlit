"""
Registro de seções como "plugins" - cada seção é um dict/objeto
"""

import streamlit as st
import pandas as pd
from logic.tables import (
    create_micronutrient_tables,
    create_complexo_b_table,
    create_lipid_fractions_table,
    create_protein_fractions_table,
    create_macronutrient_table,
    standardize_table,
    paired_table,
    display_colored_table
)
from logic.compute import dynamic_upper_limit
from ui.charts import (
    bar_single,
    bar_compare,
    bar_compare_aminoacidos,
    bar_compare_fractions,
    pie_macros
)
from domain.nutrients import (
    get_macronutrients, get_basic_nutrients, get_micronutrient_categories,
    get_lipid_fractions, get_protein_fractions, get_complexo_b_mapping,
    get_energy_columns, get_macro_columns, get_fiber_columns, get_water_columns,
    get_mineral_columns, get_vitamin_liposoluble_columns, get_complexo_b_columns,
    get_precursores_vit_a_columns, get_outras_vitaminas_columns,
    get_lipid_fraction_columns, get_amino_acid_columns, get_nutrient_unit
)

def calculate_upper_limits(data1, data2, food1, food2):
    """
    Calcula upper_limit uma única vez por grupo de gráficos para melhor performance.
    Reutiliza os valores calculados em múltiplos gráficos.
    """
    # Calcular upper_limits para diferentes grupos de nutrientes
    energy_cols = get_energy_columns()
    macro_cols = get_macro_columns()
    fiber_cols = get_fiber_columns()
    water_cols = get_water_columns()
    mineral_cols = get_mineral_columns()
    vitamin_liposoluble_cols = get_vitamin_liposoluble_columns()
    complexo_b_cols = get_complexo_b_columns()
    precursores_cols = get_precursores_vit_a_columns()
    outras_vitaminas_cols = get_outras_vitaminas_columns()
    
    return {
        'energy': dynamic_upper_limit(data1, data2, energy_cols),
        'macro': dynamic_upper_limit(data1, data2, macro_cols),
        'fiber': dynamic_upper_limit(data1, data2, fiber_cols),
        'water': dynamic_upper_limit(data1, data2, water_cols),
        'mineral': dynamic_upper_limit(data1, data2, mineral_cols),
        'vitamin_liposoluble': dynamic_upper_limit(data1, data2, vitamin_liposoluble_cols),
        'complexo_b': dynamic_upper_limit(data1, data2, complexo_b_cols),
        'precursores': dynamic_upper_limit(data1, data2, precursores_cols),
        'outras_vitaminas': dynamic_upper_limit(data1, data2, outras_vitaminas_cols)
    }

def render_comparativos_macros(data1, data2, food1, food2):
    """
    Renderiza seção de comparativos de macronutrientes usando mapeamentos dirigidos por dados
    """
    st.markdown("### Comparativo Macros")
    
    # Calcular upper_limits uma única vez para melhor performance
    upper_limits = calculate_upper_limits(data1, data2, food1, food2)
    
    # Layout por alimento
    col_esq, col_dir = st.columns(2, gap="large")
    
    with col_esq:
        # Energia
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        energy_cols = get_energy_columns()
        energy_mapping = {"Energia": energy_cols[0]}  # Mapear para nome limpo
        fig_energia1 = bar_single(data1, "Energia", energy_mapping, "kcal", upper_limits['energy'])
        if fig_energia1.data:
            st.plotly_chart(fig_energia1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Macronutrientes
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        macro_cols = get_macro_columns()
        macro_mapping = {"Carboidrato": macro_cols[0], "Lipídio": macro_cols[1], "Proteína": macro_cols[2]}  # Mapear para nomes limpos
        fig_macro1 = bar_single(data1, "Macronutrientes", macro_mapping, "g", upper_limits['macro'])
        if fig_macro1.data:
            st.plotly_chart(fig_macro1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Fibra
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fiber_cols = get_fiber_columns()
        fiber_mapping = {"Fibra": fiber_cols[0]}  # Mapear para nome limpo
        fig_fibra1 = bar_single(data1, "Fibra", fiber_mapping, "g", upper_limits['fiber'])
        if fig_fibra1.data:
            st.plotly_chart(fig_fibra1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Água
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        water_cols = get_water_columns()
        water_mapping = {"Umidade": water_cols[0]}  # Mapear para nome limpo
        fig_agua1 = bar_single(data1, "Água", water_mapping, "%", upper_limits['water'])
        if fig_agua1.data:
            st.plotly_chart(fig_agua1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_dir:
        # Energia
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        energy_cols = get_energy_columns()
        energy_mapping = {"Energia": energy_cols[0]}  # Mapear para nome limpo
        fig_energia2 = bar_single(data2, "Energia", energy_mapping, "kcal", upper_limits['energy'])
        if fig_energia2.data:
            st.plotly_chart(fig_energia2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Macronutrientes
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        macro_cols = get_macro_columns()
        macro_mapping = {"Carboidrato": macro_cols[0], "Lipídio": macro_cols[1], "Proteína": macro_cols[2]}  # Mapear para nomes limpos
        fig_macro2 = bar_single(data2, "Macronutrientes", macro_mapping, "g", upper_limits['macro'])
        if fig_macro2.data:
            st.plotly_chart(fig_macro2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Fibra
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fiber_cols = get_fiber_columns()
        fiber_mapping = {"Fibra": fiber_cols[0]}  # Mapear para nome limpo
        fig_fibra2 = bar_single(data2, "Fibra", fiber_mapping, "g", upper_limits['fiber'])
        if fig_fibra2.data:
            st.plotly_chart(fig_fibra2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Água
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        water_cols = get_water_columns()
        water_mapping = {"Umidade": water_cols[0]}  # Mapear para nome limpo
        fig_agua2 = bar_single(data2, "Água", water_mapping, "%", upper_limits['water'])
        if fig_agua2.data:
            st.plotly_chart(fig_agua2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

def render_fracoes_macros(data1, data2, food1, food2):
    """
    Renderiza seção de frações de macronutrientes usando apenas tables.py e charts.py
    Inclui todos os gráficos comparativos das frações de lipídios
    """
    st.markdown("### Frações Macros")
    
    # Frações de lipídios
    st.markdown("#### Frações de Lipídios")
    fracoes_lipidios = create_lipid_fractions_table(data1, data2, food1, food2)
    if not fracoes_lipidios.empty:
        fracoes_lipidios_padronizado = standardize_table(fracoes_lipidios, food1, food2)
        display_colored_table(fracoes_lipidios_padronizado, food1, food2)
        
        # === GRÁFICOS COMPARATIVOS DAS FRAÇÕES DE LIPÍDIOS ===
        # Organizados em 3 linhas lado a lado
        
        # === LINHA 1: Ácidos Graxos Totais ===
        cols1 = st.columns(3)
        
        # Ácidos Graxos Saturados
        with cols1[0]:
            fig_saturados = bar_compare_fractions(data1, data2, food1, food2, {"Ác. graxos total saturados": "ac_graxos_total_saturados"}, "Ác. graxos total saturados", "g", slot1='left', slot2='right')
            if fig_saturados.data:
                st.plotly_chart(fig_saturados, use_container_width=True)
        
        # Ácidos Graxos Monoinsaturados
        with cols1[1]:
            fig_monoinsaturados = bar_compare_fractions(data1, data2, food1, food2, {"Ác. graxos totais monoinsaturados": "ac_graxos_totais_monoinsaturados"}, "Ác. graxos totais monoinsaturados", "g", slot1='left', slot2='right')
            if fig_monoinsaturados.data:
                st.plotly_chart(fig_monoinsaturados, use_container_width=True)
        
        # Ácidos Graxos Poliinsaturados
        with cols1[2]:
            # Título removido para limpeza da UI
            fig_poliinsaturados = bar_compare_fractions(data1, data2, food1, food2, {"Ác. graxos totais poliinsaturados": "ac_graxos_totais_poliinsaturados"}, "Ác. graxos totais poliinsaturados", "g")
            if fig_poliinsaturados.data:
                st.plotly_chart(fig_poliinsaturados, use_container_width=True)
        
        # === LINHA 2: Ácidos Graxos Específicos C18 ===
        # Título removido para limpeza da UI
        cols2 = st.columns(3)
        
        # Ácido Oleico (C18:1)
        with cols2[0]:
            # Título removido para limpeza da UI
            fig_oleico = bar_compare_fractions(data1, data2, food1, food2, {"18:1 indiferenciado": "col_18_e_1_indifernciado"}, "18:1 indiferenciado", "g")
            if fig_oleico.data:
                st.plotly_chart(fig_oleico, use_container_width=True)
        
        # Ácido Linoleico (C18:2)
        with cols2[1]:
            # Título removido para limpeza da UI
            fig_linoleico = bar_compare_fractions(data1, data2, food1, food2, {"18:2 indiferenciado": "col_18_e_2_indiferenciado"}, "18:2 indiferenciado", "g")
            if fig_linoleico.data:
                st.plotly_chart(fig_linoleico, use_container_width=True)
        
        # Ácido Linolênico (C18:3)
        with cols2[2]:
            # Título removido para limpeza da UI
            fig_linolenico = bar_compare_fractions(data1, data2, food1, food2, {"18:3 indiferenciado": "col_18_e_3_indiferenciado"}, "18:3 indiferenciado", "g")
            if fig_linolenico.data:
                st.plotly_chart(fig_linolenico, use_container_width=True)
        
        # === LINHA 3: Ácidos Graxos n-3 e Colesterol ===
        # Título removido para limpeza da UI
        cols3 = st.columns(3)
        
        # DHA (C22:6 n-3)
        with cols3[0]:
            # Título removido para limpeza da UI
            fig_dha = bar_compare_fractions(data1, data2, food1, food2, {"22:6 n-3 (DHA)": "col_22_e_6_n3_dha"}, "22:6 n-3 (DHA)", "g")
            if fig_dha.data:
                st.plotly_chart(fig_dha, use_container_width=True)
        
        # EPA (C20:5 n-3)
        with cols3[1]:
            # Título removido para limpeza da UI
            fig_epa = bar_compare_fractions(data1, data2, food1, food2, {"20:5 n-3 (EPA)": "col_20_e_5_n3_epa"}, "20:5 n-3 (EPA)", "g")
            if fig_epa.data:
                st.plotly_chart(fig_epa, use_container_width=True)
        
        # Colesterol
        with cols3[2]:
            # Título removido para limpeza da UI
            fig_colesterol = bar_compare_fractions(data1, data2, food1, food2, {"Colesterol": "colesterol_mg"}, "Colesterol", "mg")
            if fig_colesterol.data:
                st.plotly_chart(fig_colesterol, use_container_width=True)
    
    # Frações de proteínas
    st.markdown("#### Frações de Proteínas")
    fracoes_proteinas = create_protein_fractions_table(data1, data2, food1, food2)
    if not fracoes_proteinas.empty:
        fracoes_proteinas_padronizado = standardize_table(fracoes_proteinas, food1, food2)
        display_colored_table(fracoes_proteinas_padronizado, food1, food2)
        
        # Gráfico de aminoácidos com altura maior
        # Título removido para limpeza da UI
        aminoacidos_mapping = get_protein_fractions()
        fig_aminoacidos = bar_compare_aminoacidos(data1, data2, food1, food2, aminoacidos_mapping, "Aminoácidos", "g", slot1='left', slot2='right')
        if fig_aminoacidos.data:
            st.plotly_chart(fig_aminoacidos, use_container_width=True)

def render_minerais(data1, data2, food1, food2):
    """
    Renderiza seção de minerais usando mapeamentos dirigidos por dados
    Organizados em 3 linhas: Ferro/Cobre/Zinco, Cálcio/Magnésio/Fósforo, Sódio/Potássio/Selênio/Manganês
    """
    st.markdown("#### Minerais")
    minerais_tabelas = create_micronutrient_tables(data1, data2, food1, food2)
    
    if 'Minerais' in minerais_tabelas:
        display_colored_table(minerais_tabelas['Minerais'], food1, food2)
        
        # Gráficos comparativos para minerais organizados em 3 linhas
        # === LINHA 1: Ferro, Cobre, Zinco ===
        cols1 = st.columns(3)
        traco_minerals = ["ferro_mg", "cobre_mg", "zinco_mg"]
        
        for i, mineral_col in enumerate(traco_minerals):
            with cols1[i]:
                mineral_name = mineral_col.replace('_mg', '').title()
                mineral_mapping = {mineral_name: mineral_col}
                unit = get_nutrient_unit(mineral_col)
                
                fig_mineral = bar_compare(data1, data2, food1, food2, mineral_mapping, mineral_name, unit)
                if fig_mineral.data:
                    st.plotly_chart(fig_mineral, use_container_width=True)
        
        # === LINHA 2: Cálcio, Magnésio, Fósforo ===
        cols2 = st.columns(3)
        estruturais_minerals = ["calcio_mg", "magnesio_mg", "fosforo_mg"]
        
        for i, mineral_col in enumerate(estruturais_minerals):
            with cols2[i]:
                mineral_name = mineral_col.replace('_mg', '').title()
                mineral_mapping = {mineral_name: mineral_col}
                unit = get_nutrient_unit(mineral_col)
                
                fig_mineral = bar_compare(data1, data2, food1, food2, mineral_mapping, mineral_name, unit)
                if fig_mineral.data:
                    st.plotly_chart(fig_mineral, use_container_width=True)
        
        # === LINHA 3: Sódio, Potássio, Selênio, Manganês ===
        cols3 = st.columns(4)
        outros_minerals = ["sodio_mg", "potassio_mg", "selenio_mg", "manganes_mg"]
        
        for i, mineral_col in enumerate(outros_minerals):
            with cols3[i]:
                mineral_name = mineral_col.replace('_mg', '').title()
                mineral_mapping = {mineral_name: mineral_col}
                unit = get_nutrient_unit(mineral_col)
                
                fig_mineral = bar_compare(data1, data2, food1, food2, mineral_mapping, mineral_name, unit)
                if fig_mineral.data:
                    st.plotly_chart(fig_mineral, use_container_width=True)

def render_vitaminas_lipossoluveis(data1, data2, food1, food2):
    """
    Renderiza seção de vitaminas lipossolúveis usando mapeamentos dirigidos por dados
    """
    st.markdown("#### Vitaminas Lipossolúveis")
    vitaminas_tabelas = create_micronutrient_tables(data1, data2, food1, food2)
    
    if 'Vitaminas Lipossolúveis' in vitaminas_tabelas:
        display_colored_table(vitaminas_tabelas['Vitaminas Lipossolúveis'], food1, food2)
        
        # Gráficos comparativos usando listas de colunas
        vitamin_cols = get_vitamin_liposoluble_columns()
        
        # Criar colunas dinamicamente baseado no número de vitaminas
        num_vitamins = len(vitamin_cols)
        cols = st.columns(num_vitamins)
        
        for i, vitamin_col in enumerate(vitamin_cols):
            with cols[i]:
                # Mapear nome da coluna para nome da vitamina
                vitamin_name = vitamin_col.replace('vit_', 'Vitamina ').replace('_', ' ').title()
                if 'vit_a_ui' in vitamin_col:
                    vitamin_name = "Vitamina A"
                elif 'vitamina_d' in vitamin_col:
                    vitamin_name = "Vitamina D"
                elif 'vit_e_alfatocoferol' in vitamin_col:
                    vitamin_name = "Vitamina E"
                elif 'vit_k_filoquinona' in vitamin_col:
                    vitamin_name = "Vitamina K"
                
                vitamin_mapping = {vitamin_name: vitamin_col}
                unit = get_nutrient_unit(vitamin_col)
                
                # Título removido para limpeza da UI
                fig_vitamin = bar_compare(data1, data2, food1, food2, vitamin_mapping, vitamin_name, unit)
                if fig_vitamin.data:
                    st.plotly_chart(fig_vitamin, use_container_width=True)

def render_complexo_b(data1, data2, food1, food2):
    """
    Renderiza seção do Complexo B usando mapeamentos dirigidos por dados
    Organizados em 3 linhas: B1/B2/B3, B5/B6/B9, B12/Colina
    """
    st.markdown("#### Complexo B")
    complexo_b_tabela = create_complexo_b_table(data1, data2, food1, food2)
    if not complexo_b_tabela.empty:
        complexo_b_padronizado = standardize_table(complexo_b_tabela, food1, food2)
        display_colored_table(complexo_b_padronizado, food1, food2)
        
        # Gráficos comparativos organizados em 3 linhas
        
        # === LINHA 1: B1, B2 e B3 ===
        cols1 = st.columns(3)
        linha1_vitamins = ["tiamina_mg", "riboflavina_mg", "niacina_mg"]
        
        for i, vitamin_col in enumerate(linha1_vitamins):
            with cols1[i]:
                vitamin_name = vitamin_col.replace('_mg', '').replace('_', ' ').title()
                if 'tiamina' in vitamin_col:
                    vitamin_name = "Vitamina B1"
                elif 'riboflavina' in vitamin_col:
                    vitamin_name = "Vitamina B2"
                elif 'niacina' in vitamin_col:
                    vitamin_name = "Vitamina B3"
                
                vitamin_mapping = {vitamin_name: vitamin_col}
                unit = get_nutrient_unit(vitamin_col)
                
                # Título removido para limpeza da UI
                fig_vitamin = bar_compare(data1, data2, food1, food2, vitamin_mapping, vitamin_name, unit)
                if fig_vitamin.data:
                    st.plotly_chart(fig_vitamin, use_container_width=True)
        
        # === LINHA 2: B5, B6 e B9 ===
        cols2 = st.columns(3)
        linha2_vitamins = ["ac_pantontenico", "piridoxina_mg", "folato_dfe"]
        
        for i, vitamin_col in enumerate(linha2_vitamins):
            with cols2[i]:
                vitamin_name = vitamin_col.replace('_mg', '').replace('_', ' ').title()
                if 'ac_pantontenico' in vitamin_col:
                    vitamin_name = "Vitamina B5"
                elif 'piridoxina' in vitamin_col:
                    vitamin_name = "Vitamina B6"
                elif 'folato_dfe' in vitamin_col:
                    vitamin_name = "Vitamina B9"
                
                vitamin_mapping = {vitamin_name: vitamin_col}
                unit = get_nutrient_unit(vitamin_col)
                
                # Título removido para limpeza da UI
                fig_vitamin = bar_compare(data1, data2, food1, food2, vitamin_mapping, vitamin_name, unit)
                if fig_vitamin.data:
                    st.plotly_chart(fig_vitamin, use_container_width=True)
        
        # === LINHA 3: B12 e Colina ===
        cols3 = st.columns(2)
        linha3_vitamins = ["vit_b12", "colina_total"]
        
        for i, vitamin_col in enumerate(linha3_vitamins):
            with cols3[i]:
                vitamin_name = vitamin_col.replace('_mg', '').replace('_', ' ').title()
                if 'vit_b12' in vitamin_col:
                    vitamin_name = "Vitamina B12"
                elif 'colina_total' in vitamin_col:
                    vitamin_name = "Colina"
                
                vitamin_mapping = {vitamin_name: vitamin_col}
                unit = get_nutrient_unit(vitamin_col)
                
                # Título removido para limpeza da UI
                fig_vitamin = bar_compare(data1, data2, food1, food2, vitamin_mapping, vitamin_name, unit)
                if fig_vitamin.data:
                    st.plotly_chart(fig_vitamin, use_container_width=True)

def render_precursores_vitamina_a(data1, data2, food1, food2):
    """
    Renderiza seção de precursores da vitamina A usando mapeamentos dirigidos por dados
    """
    st.markdown("#### Precursores da Vitamina A")
    precursores_tabelas = create_micronutrient_tables(data1, data2, food1, food2)
    
    if 'Precursores da Vitamina A' in precursores_tabelas:
        display_colored_table(precursores_tabelas['Precursores da Vitamina A'], food1, food2)
        
        # Gráficos comparativos usando listas de colunas
        precursores_cols = get_precursores_vit_a_columns()
        
        # Criar colunas dinamicamente baseado no número de precursores
        num_precursores = len(precursores_cols)
        cols = st.columns(num_precursores)
        
        for i, precursor_col in enumerate(precursores_cols):
            with cols[i]:
                # Mapear nome da coluna para nome do precursor
                precursor_name = precursor_col.replace('_', ' ').title()
                if 'betacaroteno' in precursor_col:
                    precursor_name = "Betacaroteno"
                elif 'rae_mcg' in precursor_col:
                    precursor_name = "RAE"
                
                precursor_mapping = {precursor_name: precursor_col}
                unit = get_nutrient_unit(precursor_col)
                
                # Título removido para limpeza da UI
                fig_precursor = bar_compare(data1, data2, food1, food2, precursor_mapping, precursor_name, unit)
                if fig_precursor.data:
                    st.plotly_chart(fig_precursor, use_container_width=True)

def render_outras_vitaminas(data1, data2, food1, food2):
    """
    Renderiza seção de outras vitaminas usando mapeamentos dirigidos por dados
    """
    st.markdown("#### Outras Vitaminas")
    outras_vitaminas_tabelas = create_micronutrient_tables(data1, data2, food1, food2)
    
    if 'Outras Vitaminas' in outras_vitaminas_tabelas:
        display_colored_table(outras_vitaminas_tabelas['Outras Vitaminas'], food1, food2)
        
        # Gráficos comparativos usando listas de colunas
        outras_vitaminas_cols = get_outras_vitaminas_columns()
        
        # Criar colunas dinamicamente baseado no número de vitaminas
        num_vitamins = len(outras_vitaminas_cols)
        cols = st.columns(num_vitamins)
        
        for i, vitamin_col in enumerate(outras_vitaminas_cols):
            with cols[i]:
                # Mapear nome da coluna para nome da vitamina
                vitamin_name = vitamin_col.replace('_', ' ').title()
                if 'c_mg' in vitamin_col:
                    vitamin_name = "Vitamina C"
                elif 'luteina_zeoxantina' in vitamin_col:
                    vitamin_name = "Luteína + Zeaxantina"
                
                vitamin_mapping = {vitamin_name: vitamin_col}
                unit = get_nutrient_unit(vitamin_col)
                
                # Título removido para limpeza da UI
                fig_vitamin = bar_compare(data1, data2, food1, food2, vitamin_mapping, vitamin_name, unit)
                if fig_vitamin.data:
                    st.plotly_chart(fig_vitamin, use_container_width=True)

# Registro de seções como "plugins" - cada seção é um dict/objeto
SECTIONS_REGISTRY = {
    "Comparativos Macros": {
        "id": "comparativos_macros",
        "label": "Comparativos Macros",
        "kind": "macro",
        "needs": ["alimento1", "alimento2"],
        "render": render_comparativos_macros
    },
    "Frações Macros": {
        "id": "fracoes_macros",
        "label": "Frações Macros",
        "kind": "macro",
        "needs": ["alimento1", "alimento2"],
        "render": render_fracoes_macros
    },
    "Minerais": {
        "id": "minerais",
        "label": "Minerais",
        "kind": "micro",
        "needs": ["alimento1", "alimento2"],
        "render": render_minerais
    },
    "Vitaminas Lipossolúveis": {
        "id": "vitaminas_lipossoluveis",
        "label": "Vitaminas Lipossolúveis",
        "kind": "micro",
        "needs": ["alimento1", "alimento2"],
        "render": render_vitaminas_lipossoluveis
    },
    "Complexo B": {
        "id": "complexo_b",
        "label": "Complexo B",
        "kind": "micro",
        "needs": ["alimento1", "alimento2"],
        "render": render_complexo_b
    },
    "Precursores Vitamina A": {
        "id": "precursores_vitamina_a",
        "label": "Precursores Vitamina A",
        "kind": "micro",
        "needs": ["alimento1", "alimento2"],
        "render": render_precursores_vitamina_a
    },
    "Outras Vitaminas": {
        "id": "outras_vitaminas",
        "label": "Outras Vitaminas",
        "kind": "micro",
        "needs": ["alimento1", "alimento2"],
        "render": render_outras_vitaminas
    }
}

def render_section(section_name, data1, data2, food1, food2):
    """
    Renderiza uma seção específica usando o registro de seções
    """
    if section_name in SECTIONS_REGISTRY:
        section = SECTIONS_REGISTRY[section_name]
        section["render"](data1, data2, food1, food2)
    else:
        st.warning(f"Seção '{section_name}' não encontrada")

def get_section_info(section_name):
    """
    Retorna informações de uma seção específica
    """
    return SECTIONS_REGISTRY.get(section_name, None)

def get_sections_by_kind(kind):
    """
    Retorna seções filtradas por tipo (macro/micro)
    """
    return {name: section for name, section in SECTIONS_REGISTRY.items() if section["kind"] == kind}

def get_available_sections():
    """
    Retorna todas as seções disponíveis
    """
    return list(SECTIONS_REGISTRY.keys())

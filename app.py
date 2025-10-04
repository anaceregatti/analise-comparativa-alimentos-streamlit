"""
Aplicação Streamlit refatorada - Página principal enxuta
"""

import streamlit as st
import pandas as pd

# Imports das camadas
from config.settings import configure_page, UI_CONFIG
from data.loader import load_data, get_groups
from logic.filters import filter_foods_by_groups, row_by_food, get_food_names, get_available_groups
from ui.state import (
    init_state, get_selected_groups, toggle_group, clear_groups,
    get_selected_sections, toggle_section, get_ordered_sections, StateKeys,
    has_selection_changed, set_current_selection, get_current_foods, get_current_data,
    clear_current_selection, is_valid_selection, should_update_selection,
    handle_chips_interaction, get_safe_food_names, handle_food_change_autoclear,
    # Sistema de instância fixa
    create_fixed_instance, get_fixed_instance, has_fixed_instance, clear_fixed_instance,
    should_create_new_instance, should_update_instance, get_instance_foods, get_instance_data,
    is_instance_valid, handle_filtering_with_fixed_instance, handle_food_selection_with_fixed_instance,
    should_replace_food_in_instance
)
from ui.components import inject_css, food_card, chips_grid, section_selector, sticky_sections_menu
from ui.charts import pie_macros
from ui.sections import SECTIONS_REGISTRY

# Funções auxiliares removidas - lógica movida para main() enxuta

def main():
    """
    Função principal enxuta que orquestra a aplicação
    """
    # 1. Configurar página e CSS
    configure_page()
    inject_css()
    
    # 2. Carregar dados
    df = load_data()
    init_state()
    
    # 3. Renderizar títulos
    st.markdown(f"""
    <div class="main-header">
        <h1>{UI_CONFIG['main_title']}</h1>
        <p>{UI_CONFIG['main_subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 4. Informações de contato
    st.markdown("""
    <div style="text-align: center; margin: 20px 0; padding: 15px; background-color: #f8f9fa; border-radius: 8px; border-left: 4px solid #007bff;">
        <p style="margin: 0; color: #6c757d; font-size: 14px;">
            <strong>Desenvolvido por Rodrigo Ceregatti</strong><br>
            <a href="mailto:rodrigo@co-labore.com" style="color: #007bff; text-decoration: none;">rodrigo@co-labore.com</a><br>
            <small>Caso encontre algum bug ou falha na aplicação, documentar caso para o email acima com mais informações</small>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 5. Chips esquerda/direita → selectbox(es)
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown(f"### {UI_CONFIG['food1_label']}")
        chips_grid(get_available_groups(df), "left")
        if st.button(UI_CONFIG['clear_button_text'], key=StateKeys.CLEAR_BUTTON_LEFT):
            clear_groups("left")
            # Usar st.rerun() para melhor performance
            st.rerun()
        
        # Gerenciar interação das chips
        handle_chips_interaction("left")
        
        selected_groups_1 = get_selected_groups("left")
        filtered_foods_1 = get_safe_food_names(df, selected_groups_1, "left")
        food1 = st.selectbox(
            UI_CONFIG['select_food1_placeholder'],
            [''] + filtered_foods_1,
            key=StateKeys.ALIMENTO_1
        )
        
        # Autoclear quando alimento muda
        if food1:
            handle_food_change_autoclear("left", food1)
    
    with col2:
        st.markdown(f"### {UI_CONFIG['food2_label']}")
        chips_grid(get_available_groups(df), "right")
        if st.button(UI_CONFIG['clear_button_text'], key=StateKeys.CLEAR_BUTTON_RIGHT):
            clear_groups("right")
            # Usar st.rerun() para melhor performance
            st.rerun()
        
        # Gerenciar interação das chips
        handle_chips_interaction("right")
        
        selected_groups_2 = get_selected_groups("right")
        filtered_foods_2 = get_safe_food_names(df, selected_groups_2, "right")
        food2 = st.selectbox(
            UI_CONFIG['select_food2_placeholder'],
            [''] + filtered_foods_2,
            key=StateKeys.ALIMENTO_2
        )
        
        # Autoclear quando alimento muda
        if food2:
            handle_food_change_autoclear("right", food2)
    
    # Os valores dos alimentos já estão sendo gerenciados automaticamente pelo Streamlit
    # através das keys StateKeys.ALIMENTO_1 e StateKeys.ALIMENTO_2
    
    # 6. Sistema de instância fixa (comparação estável)
    # LÓGICA CORRIGIDA: Usar instância fixa como fonte de verdade
    
    # Verificar se há instância fixa ativa
    if has_fixed_instance() and is_instance_valid():
        # Usar dados da instância fixa (comparação estável)
        data1, data2 = get_instance_data()
        current_food1, current_food2 = get_instance_foods()
        
        # SÓ atualizar se há uma nova seleção válida (não apenas filtros)
        if is_valid_selection(food1, food2) and should_update_instance(food1, food2):
            # Substituição inteligente: atualizar apenas o alimento que mudou
            if should_replace_food_in_instance("left", food1):
                # Substituir alimento1, manter alimento2
                new_data1 = row_by_food(df, food1)
                if not new_data1.empty and data2 is not None:
                    create_fixed_instance(food1, current_food2, new_data1, data2)
                    data1 = new_data1
                    current_food1 = food1
                else:
                    st.error("Erro ao carregar dados do novo alimento.")
                    return
            elif should_replace_food_in_instance("right", food2):
                # Substituir alimento2, manter alimento1
                new_data2 = row_by_food(df, food2)
                if data1 is not None and not new_data2.empty:
                    create_fixed_instance(current_food1, food2, data1, new_data2)
                    data2 = new_data2
                    current_food2 = food2
                else:
                    st.error("Erro ao carregar dados do novo alimento.")
                    return
    elif is_valid_selection(food1, food2):
        # Criar nova instância fixa apenas se não há instância ativa
        data1 = row_by_food(df, food1)
        data2 = row_by_food(df, food2)
        
        if not data1.empty and not data2.empty:
            # Criar nova instância fixa
            create_fixed_instance(food1, food2, data1, data2)
            current_food1, current_food2 = food1, food2
        else:
            st.error("Erro ao carregar dados dos alimentos selecionados.")
            return
    else:
        # Não há instância válida e seleção inválida
        st.info("Selecione dois alimentos para começar a comparação.")
        return
        
    # Verificar se temos dados válidos
    if not data1.empty and not data2.empty:
        # Usar alimentos da instância fixa (já obtidos acima)
        
        # Cards (food_card)
        st.markdown("---")
        st.markdown("### Resumo Macros")
        
        col_esq, col_dir = st.columns(2, gap="large")
        
        with col_esq:
            food_card(data1, current_food1, slot='left')
        
        with col_dir:
            food_card(data2, current_food2, slot='right')
        
        # Gráficos de pizza (charts.pie_macros)
        st.markdown("---")
        
        col_esq, col_dir = st.columns(2, gap="large")
        
        with col_esq:
            st.plotly_chart(
                pie_macros(data1, current_food1, slot='left'),
                use_container_width=True
            )
        
        with col_dir:
            st.plotly_chart(
                pie_macros(data2, current_food2, slot='right'),
                use_container_width=True
            )
        
        # section_selector([...])
        st.markdown("---")
        st.markdown(f"### {UI_CONFIG['sections_title']}")
        section_selector([])
        
        # Sticky menu para navegação rápida
        sticky_sections_menu()
        
        # Para cada seção selecionada: SECTIONS_REGISTRY[id].render(df1_row, df2_row, food1, food2)
        # Usar ordenação inteligente baseada no layout esperado
        ordered_sections = get_ordered_sections()
        if ordered_sections:
            st.markdown("---")
            
            # Usar alimentos da instância fixa (já obtidos acima)
            for section_id in ordered_sections:
                if section_id in SECTIONS_REGISTRY:
                    section = SECTIONS_REGISTRY[section_id]
                    section["render"](data1, data2, current_food1, current_food2)
                else:
                    st.warning(f"Seção '{section_id}' não encontrada")
    
    elif food1 == food2 and food1 != '':
        st.warning("Por favor, selecione alimentos diferentes para comparação.")
        # Limpar instância fixa se alimentos são iguais
        clear_fixed_instance()
    elif not food1 and not food2:
        st.info("Selecione dois alimentos para começar a comparação.")
        # Limpar instância fixa se nenhum alimento selecionado
        clear_fixed_instance()
    else:
        # Caso onde apenas um alimento está selecionado
        clear_fixed_instance()

if __name__ == "__main__":
    main()

"""
Componentes de UI reutilizáveis
"""

import streamlit as st
from ui.state import get_selected_sections, toggle_section
from config.settings import SECTIONS_CONFIG, UI_CONFIG
from domain.palette import get_slot_gradient

def inject_css(path="styles/theme.css"):
    """
    Injeta CSS externo no Streamlit
    """
    try:
        # Ler arquivo CSS externo
        with open(path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo CSS não encontrado: {path}")
        st.info("Certifique-se de que o arquivo styles/theme.css existe.")

def food_card(df_row, food_name, slot='left'):
    """
    Cria um card com informações básicas do alimento
    
    Args:
        df_row: DataFrame com uma linha do alimento
        food_name: Nome do alimento
        slot: Slot do alimento ('left' ou 'right')
    """
    if df_row is None or df_row.empty:
        st.error(f"Dados não encontrados para {food_name}")
        return
    
    # Obter valores básicos
    energia = df_row['energia_kcal'].iloc[0] if 'energia_kcal' in df_row.columns else 0
    proteina = df_row['proteina_g'].iloc[0] if 'proteina_g' in df_row.columns else 0
    carboidrato = df_row['carboidrato_g'].iloc[0] if 'carboidrato_g' in df_row.columns else 0
    lipideos = df_row['lipideos_g'].iloc[0] if 'lipideos_g' in df_row.columns else 0
    fibra = df_row['fibra_alimentar_g'].iloc[0] if 'fibra_alimentar_g' in df_row.columns else 0
    umidade = df_row['umidade_pct'].iloc[0] if 'umidade_pct' in df_row.columns else 0
    
    # Obter gradiente por slot
    gradient_colors = get_slot_gradient(slot)
    
    # Card HTML com layout solicitado:
    # linha1: carboidrato, lipideo, proteina
    # linha2: kcal, fibra, umidade (%)
    card_html = f"""
    <div style="
        background: linear-gradient(135deg, {gradient_colors[0]} 0%, {gradient_colors[1]} 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    ">
        <h3 style="margin: 0 0 15px 0; text-align: center; font-size: 1.2em;">
            {food_name}
        </h3>
        <!-- Linha 1: carboidrato, lipideo, proteina -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 10px;">
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{carboidrato:.1f}g</div>
                <div style="font-size: 0.9em; opacity: 0.9;">carboidrato</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{lipideos:.1f}g</div>
                <div style="font-size: 0.9em; opacity: 0.9;">lipídios</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{proteina:.1f}g</div>
                <div style="font-size: 0.9em; opacity: 0.9;">proteína</div>
            </div>
        </div>
        <!-- Linha 2: kcal, fibra, umidade (%) -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;">
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{energia:.0f}</div>
                <div style="font-size: 0.9em; opacity: 0.9;">kcal</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{fibra:.1f}g</div>
                <div style="font-size: 0.9em; opacity: 0.9;">fibra</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 1.5em; font-weight: bold;">{umidade:.1f}%</div>
                <div style="font-size: 0.9em; opacity: 0.9;">umidade</div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)

def chips_grid(groups, slot):
    """
    Renderiza chips de grupos com layout responsivo em até 3 linhas
    """
    from ui.state import get_selected_groups, toggle_group, StateKeys
    
    selected_groups = get_selected_groups(slot)
    
    # Calcular número de colunas baseado no número de grupos
    # Máximo 3 linhas, então dividir grupos por 3
    num_groups = len(groups)
    cols_per_row = max(1, (num_groups + 2) // 3)  # Arredondar para cima
    
    # Criar até 3 linhas de chips
    for row in range(min(3, (num_groups + cols_per_row - 1) // cols_per_row)):
        start_idx = row * cols_per_row
        end_idx = min(start_idx + cols_per_row, num_groups)
        row_groups = groups[start_idx:end_idx]
        
        if row_groups:
            # Criar colunas para esta linha
            cols = st.columns(len(row_groups))
            
            for i, group in enumerate(row_groups):
                with cols[i]:
                    is_selected = group in selected_groups
                    if st.button(
                        group, 
                        key=StateKeys.get_chip_key(slot, group),
                        type="primary" if is_selected else "secondary",
                        use_container_width=True
                    ):
                        toggle_group(slot, group)
                        st.rerun()

def section_selector(available_sections):
    """
    Renderiza os botões de seções
    """
    from ui.state import get_selected_sections, toggle_section
    
    st.markdown(f"**{UI_CONFIG['sections_subtitle']}**")
    
    # Obter seções selecionadas
    selected_sections = get_selected_sections()
    
    # Se não há seções específicas, usar todas as seções configuradas
    if not available_sections:
        # Layout principal: Macros (esquerda) e Micros (direita)
        col_left, col_right = st.columns(2, gap="large")
        
        # === SEÇÕES MACROS (LADO ESQUERDO) ===
        with col_left:
            st.markdown(f"#### {UI_CONFIG['macros_title']}")
            
            # Primeira linha de botões Macros
            col_macro1, col_macro2 = st.columns(2)
            
            with col_macro1:
                macro_config = SECTIONS_CONFIG['macros']['comparativos_macros']
                if st.button(macro_config['label'], key=macro_config['key'], 
                           type="primary" if macro_config['id'] in selected_sections else "secondary"):
                    toggle_section(macro_config['id'])
                    st.rerun()
            
            with col_macro2:
                macro_config = SECTIONS_CONFIG['macros']['fracoes_macros']
                if st.button(macro_config['label'], key=macro_config['key'], 
                           type="primary" if macro_config['id'] in selected_sections else "secondary"):
                    toggle_section(macro_config['id'])
                    st.rerun()
        
        # === SEÇÕES MICROS (LADO DIREITO) ===
        with col_right:
            st.markdown(f"#### {UI_CONFIG['micros_title']}")
            
            # Primeira linha de botões Micros
            col_micro1, col_micro2 = st.columns(2)
            
            with col_micro1:
                micro_config = SECTIONS_CONFIG['micros']['minerais']
                if st.button(micro_config['label'], key=micro_config['key'], 
                           type="primary" if micro_config['id'] in selected_sections else "secondary"):
                    toggle_section(micro_config['id'])
                    st.rerun()
            
            with col_micro2:
                micro_config = SECTIONS_CONFIG['micros']['vitaminas_lipossoluveis']
                if st.button(micro_config['label'], key=micro_config['key'], 
                           type="primary" if micro_config['id'] in selected_sections else "secondary"):
                    toggle_section(micro_config['id'])
                    st.rerun()
            
            # Segunda linha de botões Micros
            col_micro3, col_micro4 = st.columns(2)
            
            with col_micro3:
                micro_config = SECTIONS_CONFIG['micros']['precursores_vitamina_a']
                if st.button(micro_config['label'], key=micro_config['key'], 
                           type="primary" if micro_config['id'] in selected_sections else "secondary"):
                    toggle_section(micro_config['id'])
                    st.rerun()
            
            with col_micro4:
                micro_config = SECTIONS_CONFIG['micros']['complexo_b']
                if st.button(micro_config['label'], key=micro_config['key'], 
                           type="primary" if micro_config['id'] in selected_sections else "secondary"):
                    toggle_section(micro_config['id'])
                    st.rerun()
            
            # Terceira linha de botões Micros
            col_micro5, col_micro6 = st.columns(2)
            
            with col_micro5:
                micro_config = SECTIONS_CONFIG['micros']['outras_vitaminas']
                if st.button(micro_config['label'], key=micro_config['key'], 
                           type="primary" if micro_config['id'] in selected_sections else "secondary"):
                    toggle_section(micro_config['id'])
                    st.rerun()
            
            with col_micro6:
                # Espaço vazio para manter layout
                pass

def sticky_sections_menu():
    """
    Renderiza um menu sticky compacto com as seções disponíveis
    """
    selected_sections = get_selected_sections()
    
    if not selected_sections:
        return
    
    # HTML do sticky menu
    sticky_html = f"""
    <div class="sticky-menu" id="sticky-menu">
        <div class="sticky-menu-content">
            <div class="sticky-menu-title">Seções Ativas</div>
            <div class="sticky-menu-buttons">
    """
    
    # Adicionar botões para cada seção selecionada
    for section_id in selected_sections:
        # Encontrar a configuração da seção
        section_config = None
        for category, sections in SECTIONS_CONFIG.items():
            for key, config in sections.items():
                if config['id'] == section_id:
                    section_config = config
                    break
            if section_config:
                break
        
        if section_config:
            sticky_html += f"""
                <button class="sticky-menu-button active" onclick="toggleStickySection('{section_id}')">
                    {section_config['label']}
                </button>
            """
    
    sticky_html += """
            </div>
        </div>
    </div>
    
    <script>
        function toggleStickySection(sectionId) {
            const buttons = document.querySelectorAll('button[data-testid*="btn_"]');
            for (let button of buttons) {
                if (button.textContent.includes(sectionId)) {
                    button.click();
                    break;
                }
            }
        }
        
        function updateStickyMenu() {
            const stickyMenu = document.getElementById('sticky-menu');
            if (!stickyMenu) {
                return;
            }
            
            const scrollY = window.scrollY;
            if (scrollY > 200) {
                stickyMenu.classList.add('visible');
            } else {
                stickyMenu.classList.remove('visible');
            }
        }
        
        window.addEventListener('scroll', updateStickyMenu);
        
        setTimeout(() => {
            updateStickyMenu();
        }, 1000);
    </script>
    """
    
    st.markdown(sticky_html, unsafe_allow_html=True)

"""
Exemplo de uso dos componentes de UI refatorados
"""

from data.loader import load_data
from logic.filters import row_by_food
from ui.components import inject_css, food_card, chips_grid, section_selector
from ui.state import init_state, get_selected_groups, get_selected_sections

def example_components_usage():
    """
    Exemplo de como usar os componentes de UI refatorados
    """
    print("=== Exemplo de Uso dos Componentes de UI ===\n")
    
    # 1. Inicializar estado
    print("1. Inicializando estado...")
    init_state()
    print("   ✓ Estado inicializado")
    
    # 2. Carregar dados
    print("\n2. Carregando dados...")
    df = load_data()
    foods = df['alimento'].unique()[:2]
    data1 = row_by_food(df, foods[0])
    print(f"   ✓ Dados carregados: {len(df)} linhas")
    print(f"   ✓ Alimentos de exemplo: {foods[0]}, {foods[1]}")
    
    # 3. Testar inject_css
    print("\n3. Função inject_css:")
    print("   ✓ inject_css() - CSS embutido")
    print("   ✓ inject_css('styles/theme.css') - CSS externo")
    print("   ✓ Fallback automático se arquivo não existir")
    
    # 4. Testar food_card
    print("\n4. Função food_card:")
    print(f"   ✓ food_card(df_row, food_name)")
    print(f"   ✓ Contém apenas HTML/CSS e st.metric")
    print(f"   ✓ Exemplo: food_card(data1, '{foods[0]}')")
    
    # 5. Testar chips_grid
    print("\n5. Função chips_grid:")
    print("   ✓ chips_grid(groups, slot)")
    print("   ✓ Renderiza 6 chips por linha")
    print("   ✓ Usa state.toggle_group automaticamente")
    print("   ✓ Exemplo: chips_grid(groups, 'left')")
    
    # 6. Testar section_selector
    print("\n6. Função section_selector:")
    print("   ✓ section_selector(available_sections)")
    print("   ✓ Renderiza botões de seções")
    print("   ✓ Chama state.toggle_section automaticamente")
    print("   ✓ Exemplo: section_selector([]) - todas as seções")
    print("   ✓ Exemplo: section_selector(['Minerais']) - seções específicas")
    
    # 7. Demonstração de uso declarativo
    print("\n7. Uso declarativo no app.py:")
    print("   # Configurar página")
    print("   setup_page()  # chama configure_page() + inject_css()")
    print("   ")
    print("   # Seleção de alimentos")
    print("   chips_grid(groups, 'left')   # Alimento 1")
    print("   chips_grid(groups, 'right')  # Alimento 2")
    print("   ")
    print("   # Cards de alimentos")
    print("   food_card(data1, food1)")
    print("   food_card(data2, food2)")
    print("   ")
    print("   # Seletor de seções")
    print("   section_selector([])  # Todas as seções")
    
    # 8. Vantagens da refatoração
    print("\n8. Vantagens da refatoração:")
    print("   ✓ App fica declarativo")
    print("   ✓ Cada parte da tela é um componente reaproveitável")
    print("   ✓ Componentes encapsulam estado")
    print("   ✓ Fácil manutenção e reutilização")
    print("   ✓ Separação clara de responsabilidades")
    
    # 9. Estrutura dos componentes
    print("\n9. Estrutura dos componentes:")
    print("   inject_css(path='styles/theme.css')")
    print("   ├── Lê arquivo CSS externo")
    print("   └── Fallback para CSS embutido")
    print("   ")
    print("   food_card(df_row, food_name)")
    print("   ├── HTML/CSS personalizado")
    print("   └── st.metric para métricas")
    print("   ")
    print("   chips_grid(groups, slot)")
    print("   ├── 6 chips por linha")
    print("   └── state.toggle_group(slot, group)")
    print("   ")
    print("   section_selector(available_sections)")
    print("   ├── Botões de seções")
    print("   └── state.toggle_section(section)")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_components_usage()

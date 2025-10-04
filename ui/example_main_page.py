"""
Exemplo de uso da página principal enxuta
"""

def example_main_page_usage():
    """
    Exemplo de como usar a página principal enxuta
    """
    print("=== Exemplo de Uso da Página Principal Enxuta ===\n")
    
    # 1. Imports conforme especificado
    print("1. Imports conforme especificado:")
    print("   from config.settings import configure_page")
    print("   from data.loader import load_data, get_groups")
    print("   from ui.state import ...")
    print("   from ui.components import inject_css, food_card, chips_grid, section_selector")
    print("   from ui.sections import SECTIONS_REGISTRY")
    
    # 2. Fluxo enxuto
    print("\n2. Fluxo enxuto:")
    print("   ✓ configure_page() e inject_css()")
    print("   ✓ df = load_data()")
    print("   ✓ render títulos")
    print("   ✓ chips esquerda/direita → selectbox(es)")
    print("   ✓ quando food1 && food2:")
    print("     - cards (food_card)")
    print("     - gráficos de pizza (charts.pie_macros)")
    print("     - section_selector([...])")
    print("     - para cada seção selecionada: SECTIONS_REGISTRY[id].render(...)")
    
    # 3. Antes da refatoração
    print("\n3. Antes da refatoração:")
    print("   ❌ Funções auxiliares complexas")
    print("   ❌ Lógica espalhada em múltiplas funções")
    print("   ❌ Difícil de entender o fluxo")
    print("   ❌ Código duplicado")
    
    # 4. Depois da refatoração
    print("\n4. Depois da refatoração:")
    print("   ✅ Página principal enxuta")
    print("   ✅ Fluxo linear e claro")
    print("   ✅ Lógica centralizada em main()")
    print("   ✅ Fácil de entender e manter")
    
    # 5. Estrutura da função main()
    print("\n5. Estrutura da função main():")
    print("   def main():")
    print("       # 1. Configurar página e CSS")
    print("       configure_page()")
    print("       inject_css()")
    print("       ")
    print("       # 2. Carregar dados")
    print("       df = load_data()")
    print("       init_state()")
    print("       ")
    print("       # 3. Renderizar títulos")
    print("       st.markdown(...)")
    print("       ")
    print("       # 4. Chips esquerda/direita → selectbox(es)")
    print("       col1, col2 = st.columns(2)")
    print("       # ... lógica de seleção")
    print("       ")
    print("       # 5. Quando food1 && food2:")
    print("       if food1 and food2 and food1 != food2:")
    print("           # Cards, gráficos, seções")
    
    # 6. Vantagens da página principal enxuta
    print("\n6. Vantagens da página principal enxuta:")
    print("   ✓ Fluxo linear: Fácil de seguir")
    print("   ✓ Lógica centralizada: Tudo em main()")
    print("   ✓ Fácil manutenção: Mudanças em um lugar")
    print("   ✓ Código limpo: Sem funções auxiliares desnecessárias")
    print("   ✓ Performance: Menos chamadas de função")
    print("   ✓ Debugging: Fácil de debugar")
    
    # 7. Uso do SECTIONS_REGISTRY
    print("\n7. Uso do SECTIONS_REGISTRY:")
    print("   # Para cada seção selecionada")
    print("   for section_id in selected_sections:")
    print("       if section_id in SECTIONS_REGISTRY:")
    print("           section = SECTIONS_REGISTRY[section_id]")
    print("           section['render'](data1, data2, food1, food2)")
    print("       else:")
    print("           st.warning(f'Seção {section_id} não encontrada')")
    
    # 8. Componentes utilizados
    print("\n8. Componentes utilizados:")
    print("   ✓ inject_css(): CSS personalizado")
    print("   ✓ food_card(): Cards de alimentos")
    print("   ✓ chips_grid(): Chips de grupos")
    print("   ✓ section_selector(): Seletor de seções")
    print("   ✓ pie_macros(): Gráficos de pizza")
    print("   ✓ SECTIONS_REGISTRY: Registro de seções")
    
    # 9. Fluxo de dados
    print("\n9. Fluxo de dados:")
    print("   df = load_data()")
    print("   ↓")
    print("   chips_grid() → selectbox() → food1, food2")
    print("   ↓")
    print("   row_by_food(df, food1) → data1")
    print("   row_by_food(df, food2) → data2")
    print("   ↓")
    print("   food_card(data1, food1)")
    print("   food_card(data2, food2)")
    print("   ↓")
    print("   pie_macros(data1, food1)")
    print("   pie_macros(data2, food2)")
    print("   ↓")
    print("   section_selector([])")
    print("   ↓")
    print("   SECTIONS_REGISTRY[id].render(data1, data2, food1, food2)")
    
    # 10. Resultado final
    print("\n10. Resultado final:")
    print("   ✅ Página principal enxuta")
    print("   ✅ Fluxo linear e claro")
    print("   ✅ Lógica centralizada em main()")
    print("   ✅ Fácil de entender e manter")
    print("   ✅ Performance otimizada")
    print("   ✅ Código limpo e organizado")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_main_page_usage()

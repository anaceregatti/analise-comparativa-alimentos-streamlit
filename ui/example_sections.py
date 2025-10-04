"""
Exemplo de uso das seções como "plugins"
"""

from ui.sections import (
    SECTIONS_REGISTRY, render_section, get_section_info, 
    get_sections_by_kind, get_available_sections
)

def example_sections_usage():
    """
    Exemplo de como usar as seções como "plugins"
    """
    print("=== Exemplo de Uso das Seções como Plugins ===\n")
    
    # 1. Registro de seções
    print("1. Registro de seções:")
    print("   ✓ Cada seção é um dict/objeto")
    print("   ✓ Estrutura: {id, label, kind, needs, render}")
    print("   ✓ Registradas: 7 seções")
    
    # 2. Estrutura das seções
    print("\n2. Estrutura das seções:")
    for name, section in SECTIONS_REGISTRY.items():
        print(f"   {name}:")
        print(f"     id: {section['id']}")
        print(f"     label: {section['label']}")
        print(f"     kind: {section['kind']}")
        print(f"     needs: {section['needs']}")
        print(f"     render: {section['render'].__name__}")
    
    # 3. Seções registradas
    print("\n3. Seções registradas:")
    print("   ✓ Comparativos Macros (macro)")
    print("   ✓ Frações Macros (macro)")
    print("   ✓ Minerais (micro)")
    print("   ✓ Vitaminas Lipossolúveis (micro)")
    print("   ✓ Complexo B (micro)")
    print("   ✓ Precursores Vitamina A (micro)")
    print("   ✓ Outras Vitaminas (micro)")
    
    # 4. Funções de utilidade
    print("\n4. Funções de utilidade:")
    print("   ✓ get_available_sections(): Lista todas as seções")
    print("   ✓ get_section_info(name): Informações de uma seção")
    print("   ✓ get_sections_by_kind(kind): Filtra por tipo")
    print("   ✓ render_section(name, data1, data2, food1, food2): Renderiza seção")
    
    # 5. Exemplo de uso
    print("\n5. Exemplo de uso:")
    print("   # Obter todas as seções")
    print("   sections = get_available_sections()")
    print("   print(sections)")
    print("   ")
    print("   # Obter seções por tipo")
    print("   macro_sections = get_sections_by_kind('macro')")
    print("   micro_sections = get_sections_by_kind('micro')")
    print("   ")
    print("   # Obter informações de uma seção")
    print("   info = get_section_info('Minerais')")
    print("   print(info)")
    print("   ")
    print("   # Renderizar seção")
    print("   render_section('Minerais', data1, data2, food1, food2)")
    
    # 6. Orquestração simples no app.py
    print("\n6. Orquestração simples no app.py:")
    print("   # Resolver df, escolhas e seções selecionadas")
    print("   df = load_data()")
    print("   food1, food2 = get_selected_foods()")
    print("   selected_sections = get_selected_sections()")
    print("   ")
    print("   # Iterar nas seções escolhidas")
    print("   for section in selected_sections:")
    print("       render_section(section, data1, data2, food1, food2)")
    
    # 7. Vantagens das seções como plugins
    print("\n7. Vantagens das seções como plugins:")
    print("   ✓ Registro centralizado: Todas as seções em um lugar")
    print("   ✓ Estrutura padronizada: Dict/objeto com metadados")
    print("   ✓ Renderização isolada: Cada seção usa apenas tables.py e charts.py")
    print("   ✓ Orquestração simples: app.py só itera nas seções escolhidas")
    print("   ✓ Extensibilidade: Fácil adicionar novas seções")
    print("   ✓ Manutenibilidade: Mudanças isoladas em cada seção")
    
    # 8. Renderização isolada
    print("\n8. Renderização isolada:")
    print("   ✓ Cada seção usa apenas tables.py e charts.py")
    print("   ✓ Nada de lógica inline")
    print("   ✓ Funções puras para renderização")
    print("   ✓ Separação clara de responsabilidades")
    
    # 9. Exemplo de renderização
    print("\n9. Exemplo de renderização:")
    print("   def render_minerais(data1, data2, food1, food2):")
    print("       # Usa apenas tables.py e charts.py")
    print("       tabela = create_micronutrient_tables(data1, data2, food1, food2)")
    print("       st.dataframe(tabela['Minerais'])")
    print("       ")
    print("       fig = bar_compare(data1, data2, food1, food2, mapping, 'Minerais', 'mg')")
    print("       st.plotly_chart(fig)")
    
    # 10. Resultado final
    print("\n10. Resultado final:")
    print("   ✅ Registro de seções: Dict/objeto com metadados")
    print("   ✅ Seções registradas: 7 seções (2 macro, 5 micro)")
    print("   ✅ Renderização isolada: Apenas tables.py e charts.py")
    print("   ✅ Orquestração simples: app.py só itera nas seções escolhidas")
    print("   ✅ Extensibilidade: Fácil adicionar novas seções")
    print("   ✅ Manutenibilidade: Mudanças isoladas")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_sections_usage()

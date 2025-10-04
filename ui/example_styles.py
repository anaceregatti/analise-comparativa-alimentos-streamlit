"""
Exemplo de uso da refatoração de estilos
"""

from ui.components import inject_css

def example_styles_usage():
    """
    Exemplo de como usar a refatoração de estilos
    """
    print("=== Exemplo de Uso da Refatoração de Estilos ===\n")
    
    # 1. Refatoração de estilos
    print("1. Refatoração de estilos:")
    print("   ✓ CSS movido do main() para styles/theme.css")
    print("   ✓ Mínimo CSS inline apenas onde estritamente necessário")
    print("   ✓ Arquivo externo como fonte única de estilos")
    
    # 2. Antes da refatoração
    print("\n2. Antes da refatoração:")
    print("   ❌ CSS inline no main()")
    print("   ❌ CSS embutido em inject_css()")
    print("   ❌ Duplicação de estilos")
    print("   ❌ Difícil manutenção")
    
    # 3. Depois da refatoração
    print("\n3. Depois da refatoração:")
    print("   ✅ CSS centralizado em styles/theme.css")
    print("   ✅ Mínimo CSS inline")
    print("   ✅ Arquivo externo como fonte única")
    print("   ✅ Fácil manutenção")
    
    # 4. Estrutura dos estilos
    print("\n4. Estrutura dos estilos:")
    print("   ✓ styles/theme.css: Arquivo principal de estilos")
    print("   ✓ Classes CSS: .food-card, .food-name, .food-group, .chart-container")
    print("   ✓ Estilos Streamlit: .stSelectbox, .stDataFrame, .stButton")
    print("   ✓ Cores de grupos: .chip-amilaceo, .chip-bebida, etc.")
    
    # 5. Uso da função inject_css
    print("\n5. Uso da função inject_css:")
    print("   # Carregar estilos do arquivo externo")
    print("   inject_css()  # Usa styles/theme.css por padrão")
    print("   inject_css('styles/theme.css')  # Caminho explícito")
    print("   ")
    print("   # Tratamento de erro se arquivo não existir")
    print("   try:")
    print("       inject_css('styles/theme.css')")
    print("   except FileNotFoundError:")
    print("       st.error('Arquivo CSS não encontrado')")
    
    # 6. Classes CSS disponíveis
    print("\n6. Classes CSS disponíveis:")
    print("   ✓ .main-header: Cabeçalho principal")
    print("   ✓ .food-card: Card de alimento")
    print("   ✓ .food-name: Nome do alimento")
    print("   ✓ .food-group: Grupo do alimento")
    print("   ✓ .metric-card: Card de métrica")
    print("   ✓ .chart-container: Container de gráfico")
    print("   ✓ .table-container: Container de tabela")
    
    # 7. Estilos Streamlit
    print("\n7. Estilos Streamlit:")
    print("   ✓ .stSelectbox: Campos de seleção")
    print("   ✓ .stDataFrame: Tabelas de dados")
    print("   ✓ .stButton: Botões de grupos")
    print("   ✓ Cores específicas para cada grupo")
    
    # 8. Vantagens da refatoração
    print("\n8. Vantagens da refatoração:")
    print("   ✓ CSS centralizado: Todos os estilos em um arquivo")
    print("   ✓ Fácil manutenção: Mudanças em um lugar")
    print("   ✓ Reutilização: Classes CSS reutilizáveis")
    print("   ✓ Organização: Estrutura clara e organizada")
    print("   ✓ Performance: Carregamento otimizado")
    print("   ✓ Versionamento: Controle de versão dos estilos")
    
    # 9. Estrutura do arquivo de tema
    print("\n9. Estrutura do arquivo de tema:")
    print("   styles/theme.css")
    print("   ├── .main-header: Cabeçalho principal")
    print("   ├── .food-card: Card de alimento")
    print("   ├── .food-name: Nome do alimento")
    print("   ├── .food-group: Grupo do alimento")
    print("   ├── .metric-card: Card de métrica")
    print("   ├── .chart-container: Container de gráfico")
    print("   ├── .table-container: Container de tabela")
    print("   ├── .stSelectbox: Campos de seleção")
    print("   ├── .stDataFrame: Tabelas de dados")
    print("   ├── .stButton: Botões de grupos")
    print("   └── Cores de grupos: .chip-amilaceo, .chip-bebida, etc.")
    
    # 10. Resultado final
    print("\n10. Resultado final:")
    print("   ✅ CSS movido do main() para styles/theme.css")
    print("   ✅ Mínimo CSS inline apenas onde estritamente necessário")
    print("   ✅ Arquivo externo como fonte única de estilos")
    print("   ✅ Fácil manutenção e organização")
    print("   ✅ Performance otimizada")
    print("   ✅ Controle de versão dos estilos")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_styles_usage()

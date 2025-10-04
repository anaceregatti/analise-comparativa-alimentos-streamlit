"""
Exemplo de uso das funções genéricas de gráficos
"""

from data.loader import load_data
from logic.filters import row_by_food
from ui.charts import pie_macros, bar_single, bar_compare
from domain.nutrients import get_macronutrients, get_basic_nutrients, get_micronutrient_categories

def example_charts_usage():
    """
    Exemplo de como usar as funções genéricas de gráficos
    """
    print("=== Exemplo de Uso das Funções Genéricas de Gráficos ===\n")
    
    # 1. Carregar dados
    print("1. Carregando dados...")
    df = load_data()
    foods = df['alimento'].unique()[:2]
    data1 = row_by_food(df, foods[0])
    data2 = row_by_food(df, foods[1])
    print(f"   ✓ Dados carregados: {len(df)} linhas")
    print(f"   ✓ Alimentos de exemplo: {foods[0]}, {foods[1]}")
    
    # 2. Função pie_macros genérica
    print("\n2. Função pie_macros genérica:")
    print("   ✓ pie_macros(df_row, food_name, mapping=MACROS)")
    print("   ✓ Recebe colunas e títulos via mapping")
    print("   ✓ Cores vêm da paleta em domain/nutrients.py")
    print("   ✓ Exemplo: pie_macros(data1, 'Alimento', get_macronutrients())")
    
    # 3. Função bar_single genérica
    print("\n3. Função bar_single genérica:")
    print("   ✓ bar_single(df_row, title, columns, units, upper_limit=None)")
    print("   ✓ Um alimento, várias barras")
    print("   ✓ Recebe colunas e títulos")
    print("   ✓ Exemplo: bar_single(data1, 'Macronutrientes', get_macronutrients(), 'g')")
    
    # 4. Função bar_compare genérica
    print("\n4. Função bar_compare genérica:")
    print("   ✓ bar_compare(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None)")
    print("   ✓ Duas barras por nutriente")
    print("   ✓ Recebe colunas e títulos")
    print("   ✓ Exemplo: bar_compare(data1, data2, 'Alimento1', 'Alimento2', get_macronutrients(), 'Comparativo', 'g')")
    
    # 5. Eliminação de duplicação
    print("\n5. Eliminação de duplicação:")
    print("   ✓ Antes: 8 figuras muito parecidas")
    print("   ✓ Depois: 3 funções genéricas")
    print("   ✓ Uso em loops para múltiplos nutrientes")
    
    # 6. Exemplos de uso em loops
    print("\n6. Exemplos de uso em loops:")
    print("   # Macronutrientes")
    print("   mapping = get_macronutrients()")
    print("   bar_single(data1, 'Macronutrientes', mapping, 'g')")
    print("   ")
    print("   # Nutrientes básicos")
    print("   mapping = get_basic_nutrients()")
    print("   bar_single(data1, 'Nutrientes Básicos', mapping, 'g')")
    print("   ")
    print("   # Micronutrientes por categoria")
    print("   categorias = get_micronutrient_categories()")
    print("   for categoria, mapping in categorias.items():")
    print("       bar_single(data1, categoria, mapping, 'mg')")
    
    # 7. Vantagens da API única
    print("\n7. Vantagens da API única:")
    print("   ✓ Funções genéricas: Recebem colunas e títulos")
    print("   ✓ Cores centralizadas: Paleta em domain/nutrients.py")
    print("   ✓ Eliminação de duplicação: 8 figuras → 3 funções")
    print("   ✓ Uso em loops: Fácil para múltiplos nutrientes")
    print("   ✓ Flexibilidade: Mapping customizado")
    print("   ✓ Consistência: Interface padronizada")
    
    # 8. Estrutura das funções genéricas
    print("\n8. Estrutura das funções genéricas:")
    print("   pie_macros(df_row, food_name, mapping=None)")
    print("   ├── Usa mapping padrão se não fornecido")
    print("   ├── Recebe colunas e títulos via mapping")
    print("   └── Cores da paleta get_chart_colors('macros')")
    print("   ")
    print("   bar_single(df_row, title, columns, units, upper_limit=None)")
    print("   ├── Um alimento, várias barras")
    print("   ├── Recebe colunas e títulos")
    print("   └── Cores da paleta get_chart_colors('macros')")
    print("   ")
    print("   bar_compare(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None)")
    print("   ├── Duas barras por nutriente")
    print("   ├── Recebe colunas e títulos")
    print("   └── Cores da paleta get_chart_colors('macros')")
    
    # 9. Exemplos de uso prático
    print("\n9. Exemplos de uso prático:")
    print("   # Gráfico de pizza dos macronutrientes")
    print("   fig = pie_macros(data1, 'Alimento1')")
    print("   ")
    print("   # Gráfico de barras dos macronutrientes")
    print("   fig = bar_single(data1, 'Macronutrientes', get_macronutrients(), 'g')")
    print("   ")
    print("   # Gráfico comparativo dos macronutrientes")
    print("   fig = bar_compare(data1, data2, 'Alimento1', 'Alimento2', get_macronutrients(), 'Comparativo Macros', 'g')")
    print("   ")
    print("   # Loop para micronutrientes")
    print("   for categoria, mapping in get_micronutrient_categories().items():")
    print("       fig = bar_single(data1, categoria, mapping, 'mg')")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_charts_usage()

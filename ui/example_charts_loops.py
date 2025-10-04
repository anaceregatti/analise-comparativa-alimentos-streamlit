"""
Exemplo pratico de uso das funcoes genericas em loops para eliminar duplicacao
"""

from data.loader import load_data
from logic.filters import row_by_food
from ui.charts import pie_macros, bar_single, bar_compare
from domain.nutrients import (
    get_macronutrients, get_basic_nutrients, get_micronutrient_categories,
    get_lipid_fractions, get_protein_fractions
)

def example_charts_loops():
    """
    Exemplo pratico de como usar as funcoes genericas em loops
    """
    print("=== Exemplo Pratico: Eliminacao de Duplicacao com Loops ===\n")
    
    # 1. Carregar dados
    print("1. Carregando dados...")
    df = load_data()
    foods = df['alimento'].unique()[:2]
    data1 = row_by_food(df, foods[0])
    data2 = row_by_food(df, foods[1])
    print(f"   ✓ Dados carregados: {len(df)} linhas")
    print(f"   ✓ Alimentos: {foods[0]}, {foods[1]}")
    
    # 2. Antes: 8 figuras muito parecidas
    print("\n2. Antes da refatoracao (8 figuras muito parecidas):")
    print("   ❌ bar_macros(data1, 'Alimento1')")
    print("   ❌ bar_macros(data2, 'Alimento2')")
    print("   ❌ bar_energia(data1, 'Alimento1')")
    print("   ❌ bar_energia(data2, 'Alimento2')")
    print("   ❌ bar_fibra(data1, 'Alimento1')")
    print("   ❌ bar_fibra(data2, 'Alimento2')")
    print("   ❌ bar_agua(data1, 'Alimento1')")
    print("   ❌ bar_agua(data2, 'Alimento2')")
    print("   ❌ ... e mais 4 funcoes similares")
    
    # 3. Depois: 3 funcoes genericas
    print("\n3. Depois da refatoracao (3 funcoes genericas):")
    print("   ✅ pie_macros(df_row, food_name, mapping=MACROS)")
    print("   ✅ bar_single(df_row, title, columns, units, upper_limit=None)")
    print("   ✅ bar_compare(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None)")
    
    # 4. Exemplo 1: Macronutrientes
    print("\n4. Exemplo 1: Macronutrientes")
    print("   # Antes: bar_macros(data1, 'Alimento1')")
    print("   # Depois:")
    print("   mapping = get_macronutrients()")
    print("   bar_single(data1, 'Macronutrientes', mapping, 'g')")
    print("   bar_single(data2, 'Macronutrientes', mapping, 'g')")
    
    # 5. Exemplo 2: Nutrientes basicos
    print("\n5. Exemplo 2: Nutrientes basicos")
    print("   # Antes: bar_energia(data1, 'Alimento1')")
    print("   # Depois:")
    print("   mapping = get_basic_nutrients()")
    print("   bar_single(data1, 'Nutrientes Basicos', mapping, 'g')")
    print("   bar_single(data2, 'Nutrientes Basicos', mapping, 'g')")
    
    # 6. Exemplo 3: Micronutrientes por categoria
    print("\n6. Exemplo 3: Micronutrientes por categoria")
    print("   # Antes: 4 funcoes separadas para cada categoria")
    print("   # Depois:")
    print("   categorias = get_micronutrient_categories()")
    print("   for categoria, mapping in categorias.items():")
    print("       bar_single(data1, categoria, mapping, 'mg')")
    print("       bar_single(data2, categoria, mapping, 'mg')")
    
    # 7. Exemplo 4: Graficos comparativos
    print("\n7. Exemplo 4: Graficos comparativos")
    print("   # Antes: 4 funcoes separadas para cada tipo")
    print("   # Depois:")
    print("   # Macronutrientes")
    print("   bar_compare(data1, data2, 'Alimento1', 'Alimento2', get_macronutrients(), 'Comparativo Macros', 'g')")
    print("   # Nutrientes basicos")
    print("   bar_compare(data1, data2, 'Alimento1', 'Alimento2', get_basic_nutrients(), 'Comparativo Basicos', 'g')")
    print("   # Micronutrientes")
    print("   for categoria, mapping in get_micronutrient_categories().items():")
    print("       bar_compare(data1, data2, 'Alimento1', 'Alimento2', mapping, f'Comparativo {categoria}', 'mg')")
    
    # 8. Exemplo 5: Fracoes de lipidios
    print("\n8. Exemplo 5: Fracoes de lipidios")
    print("   # Antes: bar_lipidios(data1, 'Alimento1')")
    print("   # Depois:")
    print("   mapping = get_lipid_fractions()")
    print("   bar_single(data1, 'Fracoes de Lipidios', mapping, 'g')")
    print("   bar_compare(data1, data2, 'Alimento1', 'Alimento2', mapping, 'Comparativo Lipidios', 'g')")
    
    # 9. Exemplo 6: Aminoacidos
    print("\n9. Exemplo 6: Aminoacidos")
    print("   # Antes: bar_aminoacidos(data1, 'Alimento1')")
    print("   # Depois:")
    print("   mapping = get_protein_fractions()")
    print("   bar_single(data1, 'Aminoacidos', mapping, 'g')")
    print("   bar_compare(data1, data2, 'Alimento1', 'Alimento2', mapping, 'Comparativo Aminoacidos', 'g')")
    
    # 10. Vantagens da eliminacao de duplicacao
    print("\n10. Vantagens da eliminacao de duplicacao:")
    print("   ✓ Codigo mais limpo: 8 funcoes → 3 genericas")
    print("   ✓ Manutencao mais facil: Mudancas em um lugar")
    print("   ✓ Consistencia visual: Cores e estilos padronizados")
    print("   ✓ Flexibilidade: Mapping customizado")
    print("   ✓ Reutilizacao: Mesmas funcoes para diferentes nutrientes")
    print("   ✓ Escalabilidade: Facil adicionar novos tipos de graficos")
    
    # 11. Estrutura das funcoes genericas
    print("\n11. Estrutura das funcoes genericas:")
    print("   pie_macros(df_row, food_name, mapping=None)")
    print("   ├── Usa mapping padrao se nao fornecido")
    print("   ├── Recebe colunas e titulos via mapping")
    print("   └── Cores da paleta get_chart_colors('macros')")
    print("   ")
    print("   bar_single(df_row, title, columns, units, upper_limit=None)")
    print("   ├── Um alimento, varias barras")
    print("   ├── Recebe colunas e titulos")
    print("   └── Cores da paleta get_chart_colors('macros')")
    print("   ")
    print("   bar_compare(df1_row, df2_row, food1, food2, columns, title, unit, upper_limit=None)")
    print("   ├── Duas barras por nutriente")
    print("   ├── Recebe colunas e titulos")
    print("   └── Cores da paleta get_chart_colors('macros')")
    
    # 12. Resultado final
    print("\n12. Resultado final:")
    print("   ✅ API unica: 3 funcoes genericas")
    print("   ✅ Eliminacao de duplicacao: 8 figuras → 3 funcoes")
    print("   ✅ Uso em loops: Facil para multiplos nutrientes")
    print("   ✅ Cores centralizadas: Paleta em domain/nutrients.py")
    print("   ✅ Flexibilidade: Mapping customizado")
    print("   ✅ Consistencia: Interface padronizada")
    
    print("\n=== Exemplo concluido ===")

if __name__ == "__main__":
    example_charts_loops()

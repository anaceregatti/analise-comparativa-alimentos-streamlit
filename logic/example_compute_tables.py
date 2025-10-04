"""
Exemplo de uso das funções de cálculos e formatação refatoradas
"""

from data.loader import load_data
from logic.filters import row_by_food
from logic.compute import format_number, dynamic_upper_limit, percent
from logic.tables import paired_table, standardize_table
from domain.nutrients import get_macronutrients, get_basic_nutrients

def example_compute_tables_usage():
    """
    Exemplo de como usar as funções de cálculos e formatação refatoradas
    """
    print("=== Exemplo de Uso das Funções de Cálculos e Formatação ===\n")
    
    # 1. Carregar dados
    print("1. Carregando dados...")
    df = load_data()
    foods = df['alimento'].unique()[:2]
    data1 = row_by_food(df, foods[0])
    data2 = row_by_food(df, foods[1])
    print(f"   ✓ Dados carregados: {foods[0]} vs {foods[1]}")
    
    # 2. Testar format_number
    print("\n2. Função format_number:")
    test_values = [0, 1.5, 100, 1000, 1500.75]
    for value in test_values:
        formatted = format_number(value)
        print(f"   {value} -> {formatted}")
    
    # 3. Testar dynamic_upper_limit
    print("\n3. Função dynamic_upper_limit:")
    columns = ['energia_kcal', 'proteina_g', 'carboidrato_g']
    upper_limit = dynamic_upper_limit(data1, data2, columns)
    print(f"   Colunas: {columns}")
    print(f"   Upper limit: {upper_limit}")
    
    # 4. Testar percent
    print("\n4. Função percent:")
    parts = {'Carboidrato': 50, 'Lipídios': 30, 'Proteína': 20}
    percentages = percent(parts)
    print(f"   Partes: {parts}")
    print(f"   Percentuais: {percentages}")
    
    # 5. Testar paired_table genérica
    print("\n5. Função paired_table genérica:")
    mapping = {
        'Energia (kcal)': 'energia_kcal',
        'Proteína (g)': 'proteina_g',
        'Carboidrato (g)': 'carboidrato_g',
        'Lipídios (g)': 'lipideos_g'
    }
    table = paired_table(data1, data2, mapping, foods[0], foods[1])
    print(f"   Tabela criada com {len(table)} linhas:")
    print(table.to_string(index=False))
    
    # 6. Testar standardize_table
    print("\n6. Função standardize_table:")
    # Criar uma tabela com 4 colunas para testar
    test_df = table.copy()
    test_df.insert(1, 'Extra', 'test')
    print(f"   Tabela original: {len(test_df.columns)} colunas")
    standardized = standardize_table(test_df, foods[0], foods[1])
    print(f"   Tabela padronizada: {len(standardized.columns)} colunas")
    print(standardized.to_string(index=False))
    
    # 7. Testar com mapeamentos do domain/nutrients.py
    print("\n7. Usando mapeamentos do domain/nutrients.py:")
    
    # Macronutrientes
    macros = get_macronutrients()
    macro_table = paired_table(data1, data2, macros, foods[0], foods[1])
    print(f"   Tabela de macronutrientes ({len(macro_table)} linhas):")
    print(macro_table.to_string(index=False))
    
    # Nutrientes básicos
    basic = get_basic_nutrients()
    basic_table = paired_table(data1, data2, basic, foods[0], foods[1])
    print(f"   Tabela de nutrientes básicos ({len(basic_table)} linhas):")
    print(basic_table.to_string(index=False))
    
    # 8. Testar formatter personalizado
    print("\n8. Formatter personalizado:")
    def custom_formatter(value):
        if value == 0:
            return "Zero"
        return f"{value:.2f}g"
    
    custom_table = paired_table(data1, data2, mapping, foods[0], foods[1], formatter=custom_formatter)
    print(f"   Tabela com formatter personalizado:")
    print(custom_table.to_string(index=False))
    
    # 9. Testar percent com dados reais
    print("\n9. Percent com dados reais:")
    real_parts = {
        'Carboidrato': data1['carboidrato_g'].iloc[0],
        'Lipídios': data1['lipideos_g'].iloc[0],
        'Proteína': data1['proteina_g'].iloc[0]
    }
    real_percentages = percent(real_parts)
    print(f"   Partes reais: {real_parts}")
    print(f"   Percentuais reais: {real_percentages}")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_compute_tables_usage()

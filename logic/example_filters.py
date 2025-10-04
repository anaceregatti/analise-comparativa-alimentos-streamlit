"""
Exemplo de uso das funções de filtros puras
"""

from data.loader import load_data
from logic.filters import (
    filter_foods_by_groups, row_by_food, get_food_names, get_available_groups,
    validate_food_exists, get_food_count_by_group, get_groups_with_counts,
    filter_foods_by_name, get_food_nutritional_data, compare_foods_nutrition,
    get_food_groups_summary
)

def example_filters_usage():
    """
    Exemplo de como usar as funções de filtros puras
    """
    print("=== Exemplo de Uso das Funções de Filtros ===\n")
    
    # 1. Carregar dados
    print("1. Carregando dados...")
    df = load_data()
    print(f"   ✓ Dados carregados: {len(df)} linhas, {len(df.columns)} colunas")
    
    # 2. Obter grupos disponíveis
    print("\n2. Grupos disponíveis:")
    groups = get_available_groups(df)
    print(f"   Total de grupos: {len(groups)}")
    for i, group in enumerate(groups[:5], 1):
        print(f"   {i}. {group}")
    if len(groups) > 5:
        print(f"   ... e mais {len(groups) - 5} grupos")
    
    # 3. Filtrar alimentos por grupos
    print("\n3. Filtrar alimentos por grupos:")
    selected_groups = groups[:3]  # Primeiros 3 grupos
    filtered_df = filter_foods_by_groups(df, selected_groups)
    print(f"   Alimentos nos grupos {selected_groups}: {len(filtered_df)}")
    
    # 4. Obter nomes de alimentos filtrados
    print("\n4. Nomes de alimentos filtrados:")
    food_names = get_food_names(df, selected_groups)
    print(f"   Total de alimentos: {len(food_names)}")
    for i, food in enumerate(food_names[:5], 1):
        print(f"   {i}. {food}")
    if len(food_names) > 5:
        print(f"   ... e mais {len(food_names) - 5} alimentos")
    
    # 5. Obter dados de um alimento específico
    print("\n5. Dados de um alimento específico:")
    if food_names:
        food_name = food_names[0]
        food_data = row_by_food(df, food_name)
        print(f"   Alimento: {food_name}")
        print(f"   Dados: {len(food_data)} linha(s)")
        if not food_data.empty:
            print(f"   Grupo: {food_data['grupo'].iloc[0]}")
            print(f"   Energia: {food_data['energia_kcal'].iloc[0]} kcal")
    
    # 6. Validar existência de alimento
    print("\n6. Validação de existência:")
    test_food = "Maçã" if "Maçã" in food_names else food_names[0] if food_names else "Teste"
    exists = validate_food_exists(df, test_food)
    print(f"   Alimento '{test_food}' existe: {exists}")
    
    # 7. Contagem por grupo
    print("\n7. Contagem de alimentos por grupo:")
    group_counts = get_groups_with_counts(df)
    for group, count in list(group_counts.items())[:5]:
        print(f"   {group}: {count} alimentos")
    if len(group_counts) > 5:
        print(f"   ... e mais {len(group_counts) - 5} grupos")
    
    # 8. Busca por nome
    print("\n8. Busca por nome:")
    search_term = "batata"
    search_results = filter_foods_by_name(df, search_term)
    print(f"   Alimentos contendo '{search_term}': {len(search_results)}")
    if not search_results.empty:
        for i, food in enumerate(search_results['alimento'].head(3), 1):
            print(f"   {i}. {food}")
    
    # 9. Dados nutricionais específicos
    print("\n9. Dados nutricionais específicos:")
    if food_names:
        nutrients = ['energia_kcal', 'proteina_g', 'carboidrato_g', 'lipideos_g']
        nutrition_data = get_food_nutritional_data(df, food_names[0], nutrients)
        print(f"   Nutrientes de '{food_names[0]}':")
        for nutrient, value in nutrition_data.items():
            print(f"   {nutrient}: {value}")
    
    # 10. Comparação de alimentos
    print("\n10. Comparação de alimentos:")
    if len(food_names) >= 2:
        food1, food2 = food_names[0], food_names[1]
        comparison = compare_foods_nutrition(df, food1, food2, nutrients)
        print(f"   Comparação entre '{food1}' e '{food2}':")
        if not comparison.empty:
            print(comparison.to_string(index=False))
    
    # 11. Resumo dos grupos
    print("\n11. Resumo dos grupos:")
    summary = get_food_groups_summary(df)
    if not summary.empty:
        print("   Top 5 grupos por número de alimentos:")
        for i, row in summary.head().iterrows():
            print(f"   {row['grupo']}: {row['Total_Alimentos']} alimentos")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_filters_usage()

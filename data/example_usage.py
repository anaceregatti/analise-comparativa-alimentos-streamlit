"""
Exemplo de uso da camada de dados refatorada
"""

from data.loader import (
    load_data, get_groups, get_food_data, get_filtered_foods,
    get_data_info, validate_data_structure, get_data_source_config,
    switch_data_source
)

def example_usage():
    """
    Exemplo de como usar as funções da camada de dados
    """
    print("=== Exemplo de Uso da Camada de Dados ===\n")
    
    # 1. Carregar dados com cache e saneamento
    print("1. Carregando dados...")
    df = load_data()
    print(f"   ✓ Dados carregados: {len(df)} linhas, {len(df.columns)} colunas")
    
    # 2. Obter informações do dataset
    print("\n2. Informações do dataset:")
    info = get_data_info(df)
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # 3. Validar estrutura dos dados
    print("\n3. Validação da estrutura:")
    is_valid, message = validate_data_structure(df)
    print(f"   ✓ {message}")
    
    # 4. Obter grupos únicos e limpos
    print("\n4. Grupos disponíveis:")
    groups = get_groups(df)
    print(f"   Total de grupos: {len(groups)}")
    for i, group in enumerate(groups[:5], 1):  # Mostrar apenas os primeiros 5
        print(f"   {i}. {group}")
    if len(groups) > 5:
        print(f"   ... e mais {len(groups) - 5} grupos")
    
    # 5. Filtrar alimentos por grupo
    print("\n5. Filtragem por grupos:")
    selected_groups = groups[:3]  # Primeiros 3 grupos
    filtered_foods = get_filtered_foods(df, selected_groups)
    print(f"   Alimentos nos grupos {selected_groups}: {len(filtered_foods)}")
    
    # 6. Obter dados de um alimento específico
    print("\n6. Dados de um alimento específico:")
    if len(filtered_foods) > 0:
        food_name = filtered_foods[0]
        food_data = get_food_data(df, food_name)
        print(f"   Alimento: {food_name}")
        print(f"   Dados: {len(food_data)} linha(s)")
        if not food_data.empty:
            print(f"   Grupo: {food_data['grupo'].iloc[0]}")
            print(f"   Energia: {food_data['energia_kcal'].iloc[0]} kcal")
    
    # 7. Configuração da fonte de dados
    print("\n7. Configuração da fonte de dados:")
    config = get_data_source_config()
    for key, value in config.items():
        print(f"   {key}: {value}")
    
    # 8. Exemplo de troca de fonte de dados (conceitual)
    print("\n8. Exemplo de troca de fonte de dados:")
    print("   Para trocar para Google Sheets:")
    print("   df = switch_data_source('gsheet', sheet_url='https://...')")
    print("   Para trocar para API:")
    print("   df = switch_data_source('api', api_url='https://api...')")
    
    print("\n=== Exemplo concluído ===")

if __name__ == "__main__":
    example_usage()

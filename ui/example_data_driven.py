"""
Exemplo de uso da refatoracao com mapeamentos dirigidos por dados
"""

def example_data_driven_usage():
    """
    Exemplo de como usar mapeamentos dirigidos por dados
    """
    print("=== Exemplo de Uso de Mapeamentos Dirigidos por Dados ===\n")
    
    # 1. Listas de colunas em domain/nutrients.py
    print("1. Listas de colunas em domain/nutrients.py:")
    print("   ENERGY_COLS = ['energia_kcal']")
    print("   MACRO_COLS = ['carboidrato_g', 'lipideos_g', 'proteina_g']")
    print("   FIBER_COLS = ['fibra_alimentar_g']")
    print("   WATER_COLS = ['umidade_pct']")
    print("   MINERAL_COLS = ['cobre_mg', 'ferro_mg', 'zinco_mg']")
    print("   VITAMIN_LIPOSOLUBLE_COLS = ['vit_a_ui', 'vitamina_d', 'vit_e_alfatocoferol', 'vit_k_filoquinona']")
    print("   COMPLEXO_B_COLS = ['tiamina_mg', 'riboflavina_mg', 'niacina_mg', ...]")
    print("   PRECURSORES_VIT_A_COLS = ['betacaroteno', 'rae_mcg']")
    print("   OUTRAS_VITAMINAS_COLS = ['c_mg', 'luteina_zeoxantina']")
    print("   LIPID_FRACTION_COLS = ['colesterol_mg', 'ac_graxos_total_saturados', ...]")
    print("   AMINO_ACID_COLS = ['alanina', 'arginina', 'cisteina', ...]")
    
    # 2. Antes da refatoracao
    print("\n2. Antes da refatoracao:")
    print("   ❌ Blocos quase identicos")
    print("   ❌ Minerais Cobre/Ferro/Zinco - codigo duplicado")
    print("   ❌ Vitaminas A/D/E/K - codigo duplicado")
    print("   ❌ Fibras/agua/energia/macros - codigo duplicado")
    print("   ❌ Difícil manutencao")
    print("   ❌ Propenso a erros")
    
    # 3. Depois da refatoracao
    print("\n3. Depois da refatoracao:")
    print("   ✅ Listas de colunas centralizadas")
    print("   ✅ Iteracao em listas de colunas")
    print("   ✅ charts.bar_single e charts.bar_compare em loops")
    print("   ✅ compute.dynamic_upper_limit")
    print("   ✅ Facil manutencao")
    print("   ✅ Menos propenso a erros")
    
    # 4. Exemplo de uso
    print("\n4. Exemplo de uso:")
    print("   # Obter listas de colunas")
    print("   energy_cols = get_energy_columns()")
    print("   macro_cols = get_macro_columns()")
    print("   mineral_cols = get_mineral_columns()")
    print("   ")
    print("   # Iterar em listas de colunas")
    print("   for col in energy_cols:")
    print("       mapping = {col: col}")
    print("       fig = bar_single(data, title, mapping, unit)")
    print("       st.plotly_chart(fig)")
    print("   ")
    print("   # Para minerais")
    print("   for col in mineral_cols:")
    print("       mineral_name = col.replace('_mg', '').title()")
    print("       mapping = {mineral_name: col}")
    print("       unit = get_nutrient_unit(col)")
    print("       fig = bar_compare(data1, data2, food1, food2, mapping, title, unit)")
    print("       st.plotly_chart(fig)")
    
    # 5. Vantagens da refatoracao
    print("\n5. Vantagens da refatoracao:")
    print("   ✓ Eliminacao de duplicacao: Blocos quase identicos removidos")
    print("   ✓ Mapeamentos dirigidos por dados: Listas de colunas centralizadas")
    print("   ✓ Iteracao em loops: charts.bar_single e charts.bar_compare")
    print("   ✓ Facil manutencao: Mudancas em um lugar")
    print("   ✓ Menos propenso a erros: Codigo padronizado")
    print("   ✓ Reutilizacao: Mesmo padrao para todas as secoes")
    print("   ✓ Flexibilidade: Facil adicionar/remover colunas")
    
    # 6. Estrutura das listas
    print("\n6. Estrutura das listas:")
    print("   ENERGY_COLS = ['energia_kcal']")
    print("   MACRO_COLS = ['carboidrato_g', 'lipideos_g', 'proteina_g']")
    print("   FIBER_COLS = ['fibra_alimentar_g']")
    print("   WATER_COLS = ['umidade_pct']")
    print("   MINERAL_COLS = ['cobre_mg', 'ferro_mg', 'zinco_mg']")
    print("   VITAMIN_LIPOSOLUBLE_COLS = ['vit_a_ui', 'vitamina_d', 'vit_e_alfatocoferol', 'vit_k_filoquinona']")
    print("   COMPLEXO_B_COLS = ['tiamina_mg', 'riboflavina_mg', 'niacina_mg', 'ac_pantontenico', 'piridoxina_mg', 'folato_dfe', 'vit_b12', 'colina_total']")
    print("   PRECURSORES_VIT_A_COLS = ['betacaroteno', 'rae_mcg']")
    print("   OUTRAS_VITAMINAS_COLS = ['c_mg', 'luteina_zeoxantina']")
    print("   LIPID_FRACTION_COLS = ['colesterol_mg', 'ac_graxos_total_saturados', 'ac_graxos_totais_monoinsaturados', 'ac_graxos_totais_poliinsaturados']")
    print("   AMINO_ACID_COLS = ['alanina', 'arginina', 'cisteina', 'fenilalanina', 'glicina', 'histidina', 'isoleucina', 'leucina', 'lisina', 'metionina', 'prolina', 'serina', 'tirosina', 'treonina', 'triptofano', 'valina']")
    
    # 7. Funcoes getter
    print("\n7. Funcoes getter:")
    print("   get_energy_columns() -> ['energia_kcal']")
    print("   get_macro_columns() -> ['carboidrato_g', 'lipideos_g', 'proteina_g']")
    print("   get_fiber_columns() -> ['fibra_alimentar_g']")
    print("   get_water_columns() -> ['umidade_pct']")
    print("   get_mineral_columns() -> ['cobre_mg', 'ferro_mg', 'zinco_mg']")
    print("   get_vitamin_liposoluble_columns() -> ['vit_a_ui', 'vitamina_d', 'vit_e_alfatocoferol', 'vit_k_filoquinona']")
    print("   get_complexo_b_columns() -> ['tiamina_mg', 'riboflavina_mg', 'niacina_mg', ...]")
    print("   get_precursores_vit_a_columns() -> ['betacaroteno', 'rae_mcg']")
    print("   get_outras_vitaminas_columns() -> ['c_mg', 'luteina_zeoxantina']")
    print("   get_lipid_fraction_columns() -> ['colesterol_mg', 'ac_graxos_total_saturados', ...]")
    print("   get_amino_acid_columns() -> ['alanina', 'arginina', 'cisteina', ...]")
    
    # 8. Uso em secoes
    print("\n8. Uso em secoes:")
    print("   # Minerais")
    print("   mineral_cols = get_mineral_columns()")
    print("   for col in mineral_cols:")
    print("       mineral_name = col.replace('_mg', '').title()")
    print("       mapping = {mineral_name: col}")
    print("       unit = get_nutrient_unit(col)")
    print("       fig = bar_compare(data1, data2, food1, food2, mapping, mineral_name, unit)")
    print("   ")
    print("   # Vitaminas Lipossoluveis")
    print("   vitamin_cols = get_vitamin_liposoluble_columns()")
    print("   for col in vitamin_cols:")
    print("       vitamin_name = col.replace('vit_', 'Vitamina ').replace('_', ' ').title()")
    print("       mapping = {vitamin_name: col}")
    print("       unit = get_nutrient_unit(col)")
    print("       fig = bar_compare(data1, data2, food1, food2, mapping, vitamin_name, unit)")
    
    # 9. Resultado final
    print("\n9. Resultado final:")
    print("   ✅ Eliminacao de duplicacao: Blocos quase identicos removidos")
    print("   ✅ Mapeamentos dirigidos por dados: Listas de colunas centralizadas")
    print("   ✅ Iteracao em loops: charts.bar_single e charts.bar_compare")
    print("   ✅ Facil manutencao: Mudancas em um lugar")
    print("   ✅ Menos propenso a erros: Codigo padronizado")
    print("   ✅ Reutilizacao: Mesmo padrao para todas as secoes")
    print("   ✅ Flexibilidade: Facil adicionar/remover colunas")
    
    print("\n=== Exemplo concluido ===")

if __name__ == "__main__":
    example_data_driven_usage()

"""
Mapeamentos de nutrientes e unidades centralizados
"""

# MACRONUTRIENTES PRINCIPAIS
MACROS = {
    'Carboidrato': 'carboidrato_g',
    'Lipídio': 'lipideos_g',
    'Proteína': 'proteina_g'
}

# NUTRIENTES BÁSICOS
BASIC_NUTRIENTS = {
    'Energia': 'energia_kcal',
    'Fibra': 'fibra_alimentar_g',
    'Umidade': 'umidade_pct'
}

# MICRONUTRIENTES POR CATEGORIA
MICROS_BY_CATEGORY = {
    'Minerais': {
        'Cálcio': 'calcio_mg',
        'Cobre': 'cobre_mg',
        'Ferro': 'ferro_mg',
        'Fósforo': 'fosforo_mg',
        'Magnésio': 'magnesio_mg',
        'Manganês': 'manganes_mg',
        'Potássio': 'potassio_mg',
        'Selênio': 'se',
        'Sódio': 'sodio_mg',
        'Zinco': 'zinco_mg'
    },
    'Vitaminas Lipossolúveis': {
        'Vitamina A': 'vit_a_ui',
        'Vitamina D': 'vitamina_d',
        'Vitamina E': 'vit_e_alfatocoferol',
        'Vitamina K': 'vit_k_filoquinona'
    },
    'Precursores da Vitamina A': {
        'Betacaroteno': 'betacaroteno',
        'RAE': 'rae_mcg'
    },
    'Complexo B': {
        'Vitamina B1': 'tiamina_mg',
        'Vitamina B2': 'riboflavina_mg',
        'Vitamina B3': 'niacina_mg',
        'Vitamina B5': 'ac_pantontenico',
        'Vitamina B6': 'piridoxina_mg',
        'Vitamina B9': 'folato_dfe',
        'Vitamina B12': 'vit_b12',
        'Colina': 'colina_total'
    },
    'Outras Vitaminas': {
        'Vitamina C': 'c_mg',
        'Luteína + Zeaxantina': 'luteina_zeoxantina'
    }
}

# FRAÇÕES DE LIPÍDIOS
LIPID_FRACTIONS = {
    'Colesterol': 'colesterol_mg',
    'Ác. graxos total saturados': 'ac_graxos_total_saturados',
    '18:1 indiferenciado': 'col_18_e_1_indifernciado',
    '18:2 indiferenciado': 'col_18_e_2_indiferenciado',
    '18:3 indiferenciado': 'col_18_e_3_indiferenciado',
    '22:6 n-3 (DHA)': 'col_22_e_6_n3_dha',
    '20:5 n-3 (EPA)': 'col_20_e_5_n3_epa',
    'Ác. graxos totais monoinsaturados': 'ac_graxos_totais_monoinsaturados',
    'Ác. graxos totais poliinsaturados': 'ac_graxos_totais_poliinsaturados'
}

# AMINOÁCIDOS
AMINO_ACIDS = {
    'Alanina': 'alanina',
    'Arginina': 'arginina',
    'Asparagina': 'asparagina',
    'Ácido Aspártico': 'acido_aspartico',
    'Aminoácidos': 'cisteina',
    'Fenilalanina': 'fenilalanina',
    'Glicina': 'glicina',
    'Histidina': 'histidina',
    'Isoleucina': 'isoleucina',
    'Leucina': 'leucina',
    'Lisina': 'lisina',
    'Metionina': 'metionina',
    'Prolina': 'prolina',
    'Serina': 'serina',
    'Tirosina': 'tirosina',
    'Treonina': 'treonina',
    'Triptofano': 'triptofano',
    'Valina': 'valina'
}

# DICIONÁRIO DE UNIDADES POR NUTRIENTE
NUTRIENT_UNITS = {
    # Macronutrientes
    'carboidrato_g': 'g',
    'lipideos_g': 'g',
    'proteina_g': 'g',
    'fibra_alimentar_g': 'g',
    'energia_kcal': 'kcal',
    'umidade_pct': '%',
    
    # Minerais
    'calcio_mg': 'mg',
    'cobre_mg': 'mg',
    'ferro_mg': 'mg',
    'fosforo_mg': 'mg',
    'magnesio_mg': 'mg',
    'manganes_mg': 'mg',
    'potassio_mg': 'mg',
    'se': 'µg',
    'sodio_mg': 'mg',
    'zinco_mg': 'mg',
    
    # Vitaminas Lipossolúveis
    'vit_a_ui': 'UI',
    'vitamina_d': 'µg',
    'vit_e_alfatocoferol': 'mg',
    'vit_k_filoquinona': 'µg',
    
    # Precursores Vitamina A
    'betacaroteno': 'µg',
    'rae_mcg': 'mcg',
    
    # Complexo B
    'tiamina_mg': 'mg',
    'riboflavina_mg': 'mg',
    'niacina_mg': 'mg',
    'ac_pantontenico': 'mg',
    'piridoxina_mg': 'mg',
    'folato_dfe': 'mcg',
    'vit_b12': 'µg',
    'colina_total': 'mg',
    
    # Outras Vitaminas
    'c_mg': 'mg',
    'luteina_zeoxantina': 'µg',
    
    # Frações de Lipídios
    'colesterol_mg': 'mg',
    'ac_graxos_total_saturados': 'g',
    'col_18_e_1_indifernciado': 'g',
    'col_18_e_2_indiferenciado': 'g',
    'col_18_e_3_indiferenciado': 'g',
    'col_22_e_6_n3_dha': 'g',
    'col_20_e_5_n3_epa': 'g',
    'ac_graxos_totais_monoinsaturados': 'g',
    'ac_graxos_totais_poliinsaturados': 'g',
    
    # Aminoácidos
    'alanina': 'g',
    'arginina': 'g',
    'asparagina': 'g',
    'acido_aspartico': 'g',
    'cisteina': 'g',
    'fenilalanina': 'g',
    'glicina': 'g',
    'histidina': 'g',
    'isoleucina': 'g',
    'leucina': 'g',
    'lisina': 'g',
    'metionina': 'g',
    'prolina': 'g',
    'serina': 'g',
    'tirosina': 'g',
    'treonina': 'g',
    'triptofano': 'g',
    'valina': 'g'
}

# LISTAS DE COLUNAS PARA MAPEAMENTOS DIRIGIDOS POR DADOS
ENERGY_COLS = ["energia_kcal"]

MACRO_COLS = ["carboidrato_g", "lipideos_g", "proteina_g"]

FIBER_COLS = ["fibra_alimentar_g"]

WATER_COLS = ["umidade_pct"]

# MINERAIS PRINCIPAIS
MINERAL_COLS = [
    "calcio_mg", "magnesio_mg", "fosforo_mg", "sodio_mg", "potassio_mg",
    "ferro_mg", "cobre_mg", "zinco_mg", "manganes_mg", "selenio_mg"
]

# VITAMINAS LIPOSSOLÚVEIS
VITAMIN_LIPOSOLUBLE_COLS = ["vit_a_ui", "vitamina_d", "vit_e_alfatocoferol", "vit_k_filoquinona"]

# COMPLEXO B
COMPLEXO_B_COLS = ["tiamina_mg", "riboflavina_mg", "niacina_mg", "ac_pantontenico", "piridoxina_mg", "folato_dfe", "vit_b12", "colina_total"]

# PRECURSORES VITAMINA A
PRECURSORES_VIT_A_COLS = ["betacaroteno", "rae_mcg"]

# OUTRAS VITAMINAS
OUTRAS_VITAMINAS_COLS = ["c_mg", "luteina_zeoxantina"]

# FRAÇÕES DE LIPÍDIOS
LIPID_FRACTION_COLS = ["colesterol_mg", "ac_graxos_total_saturados", "ac_graxos_totais_monoinsaturados", "ac_graxos_totais_poliinsaturados"]

# AMINOÁCIDOS PRINCIPAIS
AMINO_ACID_COLS = ["alanina", "arginina", "cisteina", "fenilalanina", "glicina", "histidina", "isoleucina", "leucina", "lisina", "metionina", "prolina", "serina", "tirosina", "treonina", "triptofano", "valina"]

# PALETA DE CORES PADRÃO PARA GRÁFICOS
# PALETA DE CORES TERROSA E CONSISTENTE
CHART_COLORS = {
    # Cores específicas por nutriente
    'carboidrato': '#8FBC8F',      # Verde terroso
    'lipideos': '#DAA520',          # Amarelo mostarda
    'proteina': '#4682B4',         # Azul terroso
    'energia': '#CD853F',          # Laranja terroso
    'agua': '#20B2AA',             # Verde água
    'fibras': '#D2B48C',           # Marrom trigo maduro
    
    # Cores para alimentos
    'alimento1': '#CD853F',        # Terracota
    'alimento2': '#9370DB',        # Roxo terroso
    
    # Paletas por categoria
    'macros': ['#8FBC8F', '#DAA520', '#4682B4'],  # Carboidrato, Lipídios, Proteína
    'minerais': ['#CD853F', '#8FBC8F', '#DAA520', '#4682B4', '#9370DB', '#D2B48C', '#20B2AA', '#A0522D'],
    'vitaminas': ['#CD853F', '#8FBC8F', '#DAA520', '#4682B4', '#9370DB', '#D2B48C', '#20B2AA', '#A0522D'],
    'lipidos': ['#DAA520', '#CD853F', '#8FBC8F', '#4682B4', '#9370DB', '#D2B48C', '#20B2AA', '#A0522D'],
    'aminoacidos': ['#4682B4', '#8FBC8F', '#DAA520', '#CD853F', '#9370DB', '#D2B48C', '#20B2AA', '#A0522D'],
    'default': ['#8FBC8F', '#DAA520', '#4682B4', '#CD853F', '#9370DB']
}

def get_micronutrient_categories():
    """
    Retorna as categorias de micronutrientes baseado no modelo SQL
    """
    return MICROS_BY_CATEGORY

def get_complexo_b_mapping():
    """
    Retorna mapeamento específico do Complexo B com coluna "Conhecido como"
    """
    return {
        'Vit B1 | Tiamina (mg)': ('tiamina_mg', 'Vit B1'),
        'Vit B2 | Riboflavina (mg)': ('riboflavina_mg', 'Vit B2'),
        'Vit B3 | Niacina (mg)': ('niacina_mg', 'Vit B3'),
        'Vit B5 | Ác. Pantotênico (mg)': ('ac_pantontenico', 'Vit B5'),
        'Vit B6 | Piridoxina (mg)': ('piridoxina_mg', 'Vit B6'),
        'Vit B9 | Folato DFE (mcg)': ('folato_dfe', 'Vit B9'),
        'Vitamina B12 (µg)': ('vit_b12', 'Vit B12'),
        'Colina Total (mg)': ('colina_total', 'Colina')
    }

def get_lipid_fractions():
    """
    Retorna mapeamento das frações de lipídios
    """
    return LIPID_FRACTIONS

def get_protein_fractions():
    """
    Retorna mapeamento das frações de proteínas (aminoácidos)
    """
    return AMINO_ACIDS

def get_macronutrients():
    """
    Retorna mapeamento dos macronutrientes principais
    """
    return MACROS

def get_basic_nutrients():
    """
    Retorna mapeamento dos nutrientes básicos
    """
    return BASIC_NUTRIENTS

def get_nutrient_unit(column_name):
    """
    Retorna a unidade de um nutriente baseado no nome da coluna
    """
    return NUTRIENT_UNITS.get(column_name, '')

def get_chart_colors(category='default'):
    """
    Retorna paleta de cores para uma categoria específica
    """
    return CHART_COLORS.get(category, CHART_COLORS['default'])

def get_nutrient_color(nutrient_name):
    """
    Retorna cor específica para um nutriente baseado no nome
    """
    nutrient_lower = nutrient_name.lower()
    
    # Carboidrato - sempre verde
    if 'carboidrato' in nutrient_lower or 'carb' in nutrient_lower:
        return CHART_COLORS['carboidrato']
    
    # Lipídios - sempre amarelo mostarda
    elif 'lipideo' in nutrient_lower or 'lip' in nutrient_lower or 'gordura' in nutrient_lower:
        return CHART_COLORS['lipideos']
    
    # Proteína - sempre azul
    elif 'proteina' in nutrient_lower or 'prot' in nutrient_lower:
        return CHART_COLORS['proteina']
    
    # Energia - sempre laranja
    elif 'energia' in nutrient_lower or 'kcal' in nutrient_lower:
        return CHART_COLORS['energia']
    
    # Água - sempre verde água
    elif 'agua' in nutrient_lower or 'umidade' in nutrient_lower:
        return CHART_COLORS['agua']
    
    # Fibras - sempre marrom trigo
    elif 'fibra' in nutrient_lower:
        return CHART_COLORS['fibras']
    
    # Padrão
    else:
        return CHART_COLORS['default'][0]

def get_food_colors():
    """
    Retorna cores para alimentos (Alimento1 e Alimento2)
    """
    return [CHART_COLORS['alimento1'], CHART_COLORS['alimento2']]

# FUNÇÕES GETTER PARA LISTAS DE COLUNAS
def get_energy_columns():
    """
    Retorna lista de colunas para energia
    """
    return ENERGY_COLS

def get_macro_columns():
    """
    Retorna lista de colunas para macronutrientes
    """
    return MACRO_COLS

def get_fiber_columns():
    """
    Retorna lista de colunas para fibra
    """
    return FIBER_COLS

def get_water_columns():
    """
    Retorna lista de colunas para água
    """
    return WATER_COLS

def get_mineral_columns():
    """
    Retorna lista de colunas para minerais principais
    """
    return MINERAL_COLS

def get_vitamin_liposoluble_columns():
    """
    Retorna lista de colunas para vitaminas lipossolúveis
    """
    return VITAMIN_LIPOSOLUBLE_COLS

def get_complexo_b_columns():
    """
    Retorna lista de colunas para Complexo B
    """
    return COMPLEXO_B_COLS

def get_precursores_vit_a_columns():
    """
    Retorna lista de colunas para precursores da vitamina A
    """
    return PRECURSORES_VIT_A_COLS

def get_outras_vitaminas_columns():
    """
    Retorna lista de colunas para outras vitaminas
    """
    return OUTRAS_VITAMINAS_COLS

def get_lipid_fraction_columns():
    """
    Retorna lista de colunas para frações de lipídios
    """
    return LIPID_FRACTION_COLS

def get_amino_acid_columns():
    """
    Retorna lista de colunas para aminoácidos
    """
    return AMINO_ACID_COLS

"""
Configurações da aplicação Streamlit
"""

import streamlit as st

def configure_page():
    """
    Configura a página do Streamlit
    """
    st.set_page_config(
        page_title="Comparação de Alimentos",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Caminho do arquivo de dados
DATA_FILE_PATH = "assets/taco_usda_normalizado.csv"

# Configurações de visualização
CHART_HEIGHT = 400
CHART_HEIGHT_SMALL = 300
CHART_HEIGHT_MINI = 250

# Cores do tema
COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'carboidrato': '#FF6B6B',
    'lipideos': '#4ECDC4',
    'proteina': '#45B7D1',
    'fibra': '#FFEAA7',
    'agua': '#96CEB4',
    'energia': '#DDA0DD',
    'alimento1': '#FF6B6B',
    'alimento2': '#4ECDC4'
}

# Configurações de formatação
NUMBER_FORMAT = {
    'decimal_places': 1,
    'thousands_separator': '.',
    'na_value': 'N/A'
}

# Configurações de interface
UI_CONFIG = {
    'main_title': 'Comparação de Alimentos',
    'main_subtitle': 'Compare os valores nutricionais de diferentes alimentos',
    'food1_label': 'Alimento 1',
    'food2_label': 'Alimento 2',
    'select_food1_placeholder': 'Selecione o primeiro alimento:',
    'select_food2_placeholder': 'Selecione o segundo alimento:',
    'clear_button_text': 'Limpar',
    'filter_groups_text': 'Clique nos grupos para filtrar:',
    'sections_title': 'Seções Disponíveis',
    'sections_subtitle': 'Selecione as seções que deseja visualizar:',
    'macros_title': 'Macros',
    'micros_title': 'Micros',
    'clear_all_sections_text': 'Limpar Todas as Seleções'
}

# Ordem fixa das seções no relatório (layout esperado)
SECTIONS_ORDER = {
    'macros': [
        'Comparativos Macros',
        'Frações Macros'
    ],
    'micros': [
        'Minerais',
        'Vitaminas Lipossolúveis',
        'Precursores Vitamina A',
        'Complexo B',
        'Outras Vitaminas'
    ]
}

# Configurações de seções
SECTIONS_CONFIG = {
    'macros': {
        'comparativos_macros': {
            'id': 'Comparativos Macros',
            'label': 'Comparativos Macros',
            'key': 'btn_comparativos_macros'
        },
        'fracoes_macros': {
            'id': 'Frações Macros',
            'label': 'Frações Macros',
            'key': 'btn_fracoes_macros'
        }
    },
    'micros': {
        'minerais': {
            'id': 'Minerais',
            'label': 'Minerais',
            'key': 'btn_minerais'
        },
        'vitaminas_lipossoluveis': {
            'id': 'Vitaminas Lipossolúveis',
            'label': 'Vitaminas Lipossolúveis',
            'key': 'btn_vitaminas_lipossoluveis'
        },
        'complexo_b': {
            'id': 'Complexo B',
            'label': 'Complexo B',
            'key': 'btn_complexo_b'
        },
        'precursores_vitamina_a': {
            'id': 'Precursores Vitamina A',
            'label': 'Precursores Vitamina A',
            'key': 'btn_precursores_vit_a'
        },
        'outras_vitaminas': {
            'id': 'Outras Vitaminas',
            'label': 'Outras Vitaminas',
            'key': 'btn_outras_vitaminas'
        }
    }
}

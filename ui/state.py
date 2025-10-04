"""
Gerenciamento centralizado de estado da aplicação
"""

import streamlit as st
from typing import Literal, List, Optional
from config.settings import SECTIONS_ORDER

# Chaves de estado centralizadas
class StateKeys:
    # Alimentos
    ALIMENTO_1 = 'alimento1'
    ALIMENTO_2 = 'alimento2'
    
    # Seleção atual (instância persistente)
    CURRENT_SELECTION = 'current_selection'
    CURRENT_FOOD1 = 'current_food1'
    CURRENT_FOOD2 = 'current_food2'
    CURRENT_DATA1 = 'current_data1'
    CURRENT_DATA2 = 'current_data2'
    
    # Grupos selecionados
    GRUPOS_SELECIONADOS_LEFT = 'grupos_selecionados_left'
    GRUPOS_SELECIONADOS_RIGHT = 'grupos_selecionados_right'
    
    # Seções selecionadas
    SECOES_SELECIONADAS = 'secoes_selecionadas'
    
    # Botões de limpeza
    CLEAR_BUTTON_LEFT = 'limpar_1'
    CLEAR_BUTTON_RIGHT = 'limpar_2'
    
    # Botão limpar todas as seções
    CLEAR_ALL_SECTIONS = 'btn_limpar_todas'
    
    # Padrão de key para chips: "chip:{slot}:{group}"
    @staticmethod
    def get_chip_key(slot: str, group: str) -> str:
        """
        Gera key para chip seguindo padrão: chip:{slot}:{group}
        Evita colisões e facilita manutenção
        """
        return f"chip:{slot}:{group}"

def init_state():
    """
    Inicializa o estado da sessão
    """
    if StateKeys.GRUPOS_SELECIONADOS_LEFT not in st.session_state:
        st.session_state[StateKeys.GRUPOS_SELECIONADOS_LEFT] = []
    
    if StateKeys.GRUPOS_SELECIONADOS_RIGHT not in st.session_state:
        st.session_state[StateKeys.GRUPOS_SELECIONADOS_RIGHT] = []
    
    if StateKeys.SECOES_SELECIONADAS not in st.session_state:
        st.session_state[StateKeys.SECOES_SELECIONADAS] = []
    
    # Inicializar seleção atual
    if StateKeys.CURRENT_SELECTION not in st.session_state:
        st.session_state[StateKeys.CURRENT_SELECTION] = None
    if StateKeys.CURRENT_FOOD1 not in st.session_state:
        st.session_state[StateKeys.CURRENT_FOOD1] = None
    if StateKeys.CURRENT_FOOD2 not in st.session_state:
        st.session_state[StateKeys.CURRENT_FOOD2] = None
    if StateKeys.CURRENT_DATA1 not in st.session_state:
        st.session_state[StateKeys.CURRENT_DATA1] = None
    if StateKeys.CURRENT_DATA2 not in st.session_state:
        st.session_state[StateKeys.CURRENT_DATA2] = None

# === NOVA INTERFACE COM SLOTS ===

def get_selected_groups(slot: Literal["left", "right"]) -> List[str]:
    """
    Retorna grupos selecionados para um slot específico
    """
    key = StateKeys.GRUPOS_SELECIONADOS_LEFT if slot == "left" else StateKeys.GRUPOS_SELECIONADOS_RIGHT
    return st.session_state.get(key, [])

def toggle_group(slot: Literal["left", "right"], group: str) -> None:
    """
    Alterna seleção de grupo para um slot específico
    """
    groups = get_selected_groups(slot)
    if group in groups:
        groups.remove(group)
    else:
        groups.append(group)
    
    key = StateKeys.GRUPOS_SELECIONADOS_LEFT if slot == "left" else StateKeys.GRUPOS_SELECIONADOS_RIGHT
    st.session_state[key] = groups

def clear_groups(slot: Literal["left", "right"]) -> None:
    """
    Limpa seleção de grupos para um slot específico
    """
    key = StateKeys.GRUPOS_SELECIONADOS_LEFT if slot == "left" else StateKeys.GRUPOS_SELECIONADOS_RIGHT
    st.session_state[key] = []

def get_selected_foods() -> tuple[str, str]:
    """
    Retorna os alimentos selecionados (food1, food2)
    """
    food1 = st.session_state.get(StateKeys.ALIMENTO_1, '')
    food2 = st.session_state.get(StateKeys.ALIMENTO_2, '')
    return food1, food2

def set_selected_foods(food1: str, food2: str) -> None:
    """
    Define os alimentos selecionados
    """
    st.session_state[StateKeys.ALIMENTO_1] = food1
    st.session_state[StateKeys.ALIMENTO_2] = food2

def get_selected_sections() -> List[str]:
    """
    Retorna seções selecionadas
    """
    return st.session_state.get(StateKeys.SECOES_SELECIONADAS, [])

def toggle_section(name: str) -> None:
    """
    Alterna seleção de seção
    """
    if name == "clear_all":
        st.session_state[StateKeys.SECOES_SELECIONADAS] = []
        return
    
    sections = get_selected_sections()
    if name in sections:
        sections.remove(name)
    else:
        sections.append(name)
    st.session_state[StateKeys.SECOES_SELECIONADAS] = sections

# === FUNÇÕES DE COMPATIBILIDADE (para não quebrar código existente) ===

def get_selected_groups_1():
    """
    Função de compatibilidade - retorna grupos do slot left
    """
    return get_selected_groups("left")

def get_selected_groups_2():
    """
    Função de compatibilidade - retorna grupos do slot right
    """
    return get_selected_groups("right")

def toggle_group_1(group, is_selected):
    """
    Função de compatibilidade - alterna grupo no slot left
    """
    if is_selected:
        groups = get_selected_groups("left")
        if group in groups:
            groups.remove(group)
            key = StateKeys.GRUPOS_SELECIONADOS_LEFT
            st.session_state[key] = groups
    else:
        toggle_group("left", group)

def toggle_group_2(group, is_selected):
    """
    Função de compatibilidade - alterna grupo no slot right
    """
    if is_selected:
        groups = get_selected_groups("right")
        if group in groups:
            groups.remove(group)
            key = StateKeys.GRUPOS_SELECIONADOS_RIGHT
            st.session_state[key] = groups
    else:
        toggle_group("right", group)

def clear_groups_1():
    """
    Função de compatibilidade - limpa grupos do slot left
    """
    clear_groups("left")

def clear_groups_2():
    """
    Função de compatibilidade - limpa grupos do slot right
    """
    clear_groups("right")

def get_food_1():
    """
    Função de compatibilidade - retorna alimento 1
    """
    return st.session_state.get(StateKeys.ALIMENTO_1, '')

def get_food_2():
    """
    Função de compatibilidade - retorna alimento 2
    """
    return st.session_state.get(StateKeys.ALIMENTO_2, '')

def set_food_1(food):
    """
    Função de compatibilidade - define alimento 1
    """
    st.session_state[StateKeys.ALIMENTO_1] = food

def set_food_2(food):
    """
    Função de compatibilidade - define alimento 2
    """
    st.session_state[StateKeys.ALIMENTO_2] = food

def get_ordered_sections():
    """
    Retorna as seções selecionadas ordenadas conforme o layout esperado do relatório.
    
    Returns:
        List[str]: Lista de seções ordenadas (macros primeiro, depois micros)
    """
    selected_sections = get_selected_sections()
    if not selected_sections:
        return []
    
    # Ordem completa: macros primeiro, depois micros
    full_order = SECTIONS_ORDER['macros'] + SECTIONS_ORDER['micros']
    
    # Filtrar apenas as seções selecionadas e manter a ordem
    ordered_sections = []
    for section in full_order:
        if section in selected_sections:
            ordered_sections.append(section)
    
    return ordered_sections

# === SISTEMA DE SELEÇÃO ATUAL (INSTÂNCIA PERSISTENTE) ===

def get_current_selection():
    """
    Retorna a seleção atual (instância persistente)
    """
    return st.session_state.get(StateKeys.CURRENT_SELECTION, None)

def set_current_selection(food1: str, food2: str, data1, data2):
    """
    Define a seleção atual (instância persistente)
    """
    st.session_state[StateKeys.CURRENT_SELECTION] = {
        'food1': food1,
        'food2': food2,
        'data1': data1,
        'data2': data2
    }
    st.session_state[StateKeys.CURRENT_FOOD1] = food1
    st.session_state[StateKeys.CURRENT_FOOD2] = food2
    st.session_state[StateKeys.CURRENT_DATA1] = data1
    st.session_state[StateKeys.CURRENT_DATA2] = data2

def clear_current_selection():
    """
    Limpa a seleção atual
    """
    st.session_state[StateKeys.CURRENT_SELECTION] = None
    st.session_state[StateKeys.CURRENT_FOOD1] = None
    st.session_state[StateKeys.CURRENT_FOOD2] = None
    st.session_state[StateKeys.CURRENT_DATA1] = None
    st.session_state[StateKeys.CURRENT_DATA2] = None

def has_selection_changed(food1: str, food2: str) -> bool:
    """
    Verifica se a seleção mudou comparando com a seleção atual
    """
    current_food1 = st.session_state.get(StateKeys.CURRENT_FOOD1, None)
    current_food2 = st.session_state.get(StateKeys.CURRENT_FOOD2, None)
    
    return (food1 != current_food1) or (food2 != current_food2)

def get_current_foods():
    """
    Retorna os alimentos da seleção atual
    """
    return (
        st.session_state.get(StateKeys.CURRENT_FOOD1, None),
        st.session_state.get(StateKeys.CURRENT_FOOD2, None)
    )

def get_current_data():
    """
    Retorna os dados da seleção atual
    """
    return (
        st.session_state.get(StateKeys.CURRENT_DATA1, None),
        st.session_state.get(StateKeys.CURRENT_DATA2, None)
    )

def is_valid_selection(food1: str, food2: str) -> bool:
    """
    Verifica se a seleção é válida (ambos alimentos diferentes e não vazios)
    """
    return (food1 and food2 and food1 != food2 and 
            food1 != '' and food2 != '')

def should_update_selection(food1: str, food2: str) -> bool:
    """
    Verifica se deve atualizar a seleção (mudou e é válida)
    """
    return (has_selection_changed(food1, food2) and 
            is_valid_selection(food1, food2))

# === SISTEMA DE AUTOCLEAR E CHIPS ===

def clear_food_selection(slot: Literal["left", "right"]):
    """
    Limpa a seleção de alimento para um slot específico
    """
    if slot == "left":
        st.session_state[StateKeys.ALIMENTO_1] = ''
    else:
        st.session_state[StateKeys.ALIMENTO_2] = ''

def should_clear_food_selection(slot: Literal["left", "right"]) -> bool:
    """
    Verifica se deve limpar a seleção de alimento quando grupos mudam
    """
    # Verificar se grupos mudaram
    current_groups = get_selected_groups(slot)
    if slot == "left":
        last_groups_key = 'last_groups_left'
    else:
        last_groups_key = 'last_groups_right'
    
    last_groups = st.session_state.get(last_groups_key, [])
    
    # Se grupos mudaram E há uma seleção atual, deve limpar seleção
    if current_groups != last_groups:
        st.session_state[last_groups_key] = current_groups.copy()
        
        # Só limpar se há alimento selecionado no slot
        if slot == "left":
            current_food = st.session_state.get(StateKeys.ALIMENTO_1, '')
        else:
            current_food = st.session_state.get(StateKeys.ALIMENTO_2, '')
        
        # Só limpar se há alimento selecionado E não há instância fixa ativa
        # Se há instância fixa, não limpar para evitar quebra
        if has_fixed_instance():
            return False
        
        return bool(current_food)
    
    return False

def handle_chips_interaction(slot: Literal["left", "right"]):
    """
    Gerencia a interação das chips com a seleção de alimentos
    """
    # Verificar se deve limpar seleção de alimento
    if should_clear_food_selection(slot):
        # Limpar seleção do alimento no slot
        clear_food_selection(slot)
        
        # NÃO limpar instância fixa para evitar quebra da visualização
        # A filtragem deve funcionar sem quebrar a comparação atual
        # O usuário pode continuar vendo a comparação mesmo com filtros diferentes
        handle_filtering_with_fixed_instance(slot)

def get_safe_food_names(df, selected_groups, slot):
    """
    Obtém nomes de alimentos de forma segura, evitando quebras
    """
    try:
        from logic.filters import get_food_names
        if not selected_groups:
            # Se não há grupos selecionados, retornar todos os alimentos
            return get_food_names(df, None)
        return get_food_names(df, selected_groups)
    except Exception as e:
        st.error(f"Erro ao filtrar alimentos: {str(e)}")
        return []

def handle_food_change_autoclear(slot: Literal["left", "right"], new_food: str):
    """
    Gerencia autoclear quando alimento muda
    """
    if slot == "left":
        last_food_key = 'last_food_left'
        other_slot = 'right'
    else:
        last_food_key = 'last_food_right'
        other_slot = 'left'
    
    last_food = st.session_state.get(last_food_key, '')
    
    # Se alimento mudou, limpar o outro slot se necessário
    if new_food != last_food and new_food:
        st.session_state[last_food_key] = new_food
        
        # Verificar se o outro slot tem o mesmo alimento selecionado
        if other_slot == 'left':
            other_food = st.session_state.get(StateKeys.ALIMENTO_1, '')
        else:
            other_food = st.session_state.get(StateKeys.ALIMENTO_2, '')
        
        # Se o outro slot tem o mesmo alimento, limpar
        if other_food == new_food:
            if other_slot == 'left':
                st.session_state[StateKeys.ALIMENTO_1] = ''
            else:
                st.session_state[StateKeys.ALIMENTO_2] = ''
            st.warning("Alimentos devem ser diferentes. Seleção do outro slot foi limpa.")
        
        # Verificar se deve atualizar a instância fixa
        if handle_food_selection_with_fixed_instance(slot, new_food):
            # Nova seleção detectada - a instância será atualizada no app.py
            pass

# === SISTEMA DE INSTÂNCIA FIXA ===

def create_fixed_instance(food1: str, food2: str, data1, data2):
    """
    Cria uma instância fixa da comparação.
    Esta instância permanece estável independente de filtros.
    """
    st.session_state[StateKeys.CURRENT_SELECTION] = {
        'food1': food1,
        'food2': food2,
        'data1': data1,
        'data2': data2,
        'created_at': st.session_state.get('_timestamp', 0)
    }
    st.session_state[StateKeys.CURRENT_FOOD1] = food1
    st.session_state[StateKeys.CURRENT_FOOD2] = food2
    st.session_state[StateKeys.CURRENT_DATA1] = data1
    st.session_state[StateKeys.CURRENT_DATA2] = data2

def get_fixed_instance():
    """
    Retorna a instância fixa atual, se existir.
    """
    return st.session_state.get(StateKeys.CURRENT_SELECTION, None)

def has_fixed_instance():
    """
    Verifica se existe uma instância fixa ativa.
    """
    return get_fixed_instance() is not None

def clear_fixed_instance():
    """
    Limpa a instância fixa atual.
    """
    st.session_state[StateKeys.CURRENT_SELECTION] = None
    st.session_state[StateKeys.CURRENT_FOOD1] = None
    st.session_state[StateKeys.CURRENT_FOOD2] = None
    st.session_state[StateKeys.CURRENT_DATA1] = None
    st.session_state[StateKeys.CURRENT_DATA2] = None

def should_create_new_instance(food1: str, food2: str) -> bool:
    """
    Determina se deve criar uma nova instância fixa.
    """
    if not has_fixed_instance():
        return True
    
    current_instance = get_fixed_instance()
    current_food1 = current_instance.get('food1', '')
    current_food2 = current_instance.get('food2', '')
    
    # Criar nova instância se os alimentos mudaram
    return (food1 != current_food1 or food2 != current_food2)

def should_update_instance(food1: str, food2: str) -> bool:
    """
    Determina se deve atualizar a instância atual.
    """
    if not has_fixed_instance():
        return False
    
    current_instance = get_fixed_instance()
    current_food1 = current_instance.get('food1', '')
    current_food2 = current_instance.get('food2', '')
    
    # Atualizar se pelo menos um alimento mudou
    return (food1 != current_food1 or food2 != current_food2)

def should_replace_food_in_instance(slot: Literal["left", "right"], new_food: str) -> bool:
    """
    Determina se deve substituir um alimento específico na instância.
    """
    if not has_fixed_instance():
        return False
    
    current_food1, current_food2 = get_instance_foods()
    
    if slot == "left":
        return new_food != current_food1
    else:
        return new_food != current_food2

def get_instance_foods():
    """
    Retorna os alimentos da instância fixa atual.
    """
    if not has_fixed_instance():
        return None, None
    
    instance = get_fixed_instance()
    return instance.get('food1', ''), instance.get('food2', '')

def get_instance_data():
    """
    Retorna os dados da instância fixa atual.
    """
    if not has_fixed_instance():
        return None, None
    
    instance = get_fixed_instance()
    return instance.get('data1', None), instance.get('data2', None)

def is_instance_valid() -> bool:
    """
    Verifica se a instância fixa atual é válida.
    """
    if not has_fixed_instance():
        return False
    
    instance = get_fixed_instance()
    food1 = instance.get('food1', '')
    food2 = instance.get('food2', '')
    data1 = instance.get('data1', None)
    data2 = instance.get('data2', None)
    
    return (food1 and food2 and data1 is not None and data2 is not None)

def handle_filtering_with_fixed_instance(slot: Literal["left", "right"]):
    """
    Gerencia a interação entre filtros e instância fixa.
    Permite filtrar sem quebrar a comparação atual.
    """
    # Se não há instância fixa, não há problema
    if not has_fixed_instance():
        return
    
    # Se há instância fixa, permitir filtragem livre
    # A instância fixa permanece inalterada
    # Não fazer nada - apenas permitir que a filtragem funcione
    pass

def handle_food_selection_with_fixed_instance(slot: Literal["left", "right"], new_food: str):
    """
    Gerencia a seleção de alimento com instância fixa.
    Substitui apenas o alimento do slot específico.
    """
    if not has_fixed_instance():
        return False
    
    # Obter alimentos atuais da instância
    current_food1, current_food2 = get_instance_foods()
    
    if slot == "left":
        # Substituir alimento1, manter alimento2
        if new_food != current_food1:
            # Nova seleção no slot esquerdo
            return True
    else:
        # Substituir alimento2, manter alimento1
        if new_food != current_food2:
            # Nova seleção no slot direito
            return True
    
    return False

"""
Sistema de paleta de cores por slot (alimento1/alimento2)
"""

# Gradientes por slot
GRADIENTS = {
    'left': ('#667EEA', '#764BA2'),    # Roxo/azul para alimento1
    'right': ('#34D399', '#F472B6')    # Verde/rosa para alimento2
}

# Cores primárias por slot
PRIMARY = {
    'left': '#667EEA',     # Azul para alimento1
    'right': '#34D399'     # Verde para alimento2
}

# Cores secundárias por slot
SECONDARY = {
    'left': '#764BA2',     # Roxo para alimento1
    'right': '#F472B6'     # Rosa para alimento2
}

# Cores sólidas para gráficos (sem gradiente)
SOLID_COLORS = {
    'left': '#667EEA',     # Azul sólido para alimento1
    'right': '#34D399'     # Verde sólido para alimento2
}

def get_slot_gradient(slot):
    """
    Retorna gradiente para um slot específico
    """
    return GRADIENTS.get(slot, GRADIENTS['left'])

def get_slot_primary(slot):
    """
    Retorna cor primária para um slot específico
    """
    return PRIMARY.get(slot, PRIMARY['left'])

def get_slot_secondary(slot):
    """
    Retorna cor secundária para um slot específico
    """
    return SECONDARY.get(slot, SECONDARY['left'])

def get_slot_solid(slot):
    """
    Retorna cor sólida para um slot específico
    """
    return SOLID_COLORS.get(slot, SOLID_COLORS['left'])

def get_slot_colors(slot):
    """
    Retorna todas as cores para um slot específico
    """
    return {
        'gradient': get_slot_gradient(slot),
        'primary': get_slot_primary(slot),
        'secondary': get_slot_secondary(slot),
        'solid': get_slot_solid(slot)
    }

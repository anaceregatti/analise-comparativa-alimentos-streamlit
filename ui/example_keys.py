"""
Exemplo de uso da refatoracao de keys e session_state
"""

def example_keys_usage():
    """
    Exemplo de como usar keys centralizadas
    """
    print("=== Exemplo de Uso de Keys Centralizadas ===\n")
    
    # 1. Keys centralizadas em ui/state.py
    print("1. Keys centralizadas em ui/state.py:")
    print("   class StateKeys:")
    print("       # Alimentos")
    print("       ALIMENTO_1 = 'alimento1'")
    print("       ALIMENTO_2 = 'alimento2'")
    print("       ")
    print("       # Grupos selecionados")
    print("       GRUPOS_SELECIONADOS_LEFT = 'grupos_selecionados_left'")
    print("       GRUPOS_SELECIONADOS_RIGHT = 'grupos_selecionados_right'")
    print("       ")
    print("       # Seções selecionadas")
    print("       SECOES_SELECIONADAS = 'secoes_selecionadas'")
    print("       ")
    print("       # Botões de limpeza")
    print("       CLEAR_BUTTON_LEFT = 'limpar_1'")
    print("       CLEAR_BUTTON_RIGHT = 'limpar_2'")
    print("       ")
    print("       # Botão limpar todas as seções")
    print("       CLEAR_ALL_SECTIONS = 'btn_limpar_todas'")
    
    # 2. Padrão de key para chips
    print("\n2. Padrão de key para chips:")
    print("   @staticmethod")
    print("   def get_chip_key(slot: str, group: str) -> str:")
    print("       return f'chip:{slot}:{group}'")
    print("   ")
    print("   # Exemplos:")
    print("   StateKeys.get_chip_key('left', 'fruta') -> 'chip:left:fruta'")
    print("   StateKeys.get_chip_key('right', 'cereal') -> 'chip:right:cereal'")
    print("   StateKeys.get_chip_key('left', 'laticinio') -> 'chip:left:laticinio'")
    
    # 3. Antes da refatoracao
    print("\n3. Antes da refatoracao:")
    print("   ❌ Keys hardcoded espalhadas pelo codigo")
    print("   ❌ 'alimento1', 'alimento2' em app.py")
    print("   ❌ 'limpar_1', 'limpar_2' em app.py")
    print("   ❌ 'btn_limpar_todas' em components.py")
    print("   ❌ 'chip1_0', 'chip2_0' em components.py")
    print("   ❌ Difícil manutencao")
    print("   ❌ Propenso a colisoes")
    
    # 4. Depois da refatoracao
    print("\n4. Depois da refatoracao:")
    print("   ✅ Keys centralizadas em ui/state.py")
    print("   ✅ StateKeys.ALIMENTO_1, StateKeys.ALIMENTO_2")
    print("   ✅ StateKeys.CLEAR_BUTTON_LEFT, StateKeys.CLEAR_BUTTON_RIGHT")
    print("   ✅ StateKeys.CLEAR_ALL_SECTIONS")
    print("   ✅ StateKeys.get_chip_key(slot, group)")
    print("   ✅ Facil manutencao")
    print("   ✅ Evita colisoes")
    
    # 5. Uso em componentes
    print("\n5. Uso em componentes:")
    print("   # Em ui/components.py")
    print("   from ui.state import StateKeys")
    print("   ")
    print("   # Para chips")
    print("   chip_key = StateKeys.get_chip_key(slot, grupo)")
    print("   st.button(grupo, key=chip_key)")
    print("   ")
    print("   # Para botões de limpeza")
    print("   st.button('Limpar', key=StateKeys.CLEAR_BUTTON_LEFT)")
    print("   st.button('Limpar', key=StateKeys.CLEAR_BUTTON_RIGHT)")
    print("   st.button('Limpar Todas', key=StateKeys.CLEAR_ALL_SECTIONS)")
    
    # 6. Uso em app.py
    print("\n6. Uso em app.py:")
    print("   # Em app.py")
    print("   from ui.state import StateKeys")
    print("   ")
    print("   # Para selectbox de alimentos")
    print("   food1 = st.selectbox(..., key=StateKeys.ALIMENTO_1)")
    print("   food2 = st.selectbox(..., key=StateKeys.ALIMENTO_2)")
    print("   ")
    print("   # Para botões de limpeza")
    print("   st.button('Limpar', key=StateKeys.CLEAR_BUTTON_LEFT)")
    print("   st.button('Limpar', key=StateKeys.CLEAR_BUTTON_RIGHT)")
    
    # 7. Vantagens da refatoracao
    print("\n7. Vantagens da refatoracao:")
    print("   ✓ Keys centralizadas: Todas em ui/state.py")
    print("   ✓ Facil manutencao: Mudancas em um lugar")
    print("   ✓ Evita colisoes: Padrao consistente")
    print("   ✓ Padrao para chips: chip:{slot}:{group}")
    print("   ✓ Reutilizacao: Mesmo padrao em toda aplicacao")
    print("   ✓ Organizacao: Estrutura clara e organizada")
    print("   ✓ Debugging: Facil de debugar")
    
    # 8. Estrutura das keys
    print("\n8. Estrutura das keys:")
    print("   StateKeys.ALIMENTO_1 = 'alimento1'")
    print("   StateKeys.ALIMENTO_2 = 'alimento2'")
    print("   StateKeys.GRUPOS_SELECIONADOS_LEFT = 'grupos_selecionados_left'")
    print("   StateKeys.GRUPOS_SELECIONADOS_RIGHT = 'grupos_selecionados_right'")
    print("   StateKeys.SECOES_SELECIONADAS = 'secoes_selecionadas'")
    print("   StateKeys.CLEAR_BUTTON_LEFT = 'limpar_1'")
    print("   StateKeys.CLEAR_BUTTON_RIGHT = 'limpar_2'")
    print("   StateKeys.CLEAR_ALL_SECTIONS = 'btn_limpar_todas'")
    print("   StateKeys.get_chip_key('left', 'fruta') = 'chip:left:fruta'")
    
    # 9. Padrao de key para chips
    print("\n9. Padrao de key para chips:")
    print("   # Formato: chip:{slot}:{group}")
    print("   chip:left:fruta")
    print("   chip:left:cereal")
    print("   chip:left:laticinio")
    print("   chip:right:fruta")
    print("   chip:right:cereal")
    print("   chip:right:laticinio")
    print("   ")
    print("   # Vantagens:")
    print("   ✓ Evita colisoes: Padrao unico")
    print("   ✓ Facil manutencao: Estrutura clara")
    print("   ✓ Debugging: Facil de identificar")
    print("   ✓ Escalabilidade: Facil de adicionar novos")
    
    # 10. Resultado final
    print("\n10. Resultado final:")
    print("   ✅ Keys centralizadas em ui/state.py")
    print("   ✅ Padrao de key para chips: chip:{slot}:{group}")
    print("   ✅ Evita colisoes e facilita manutencao")
    print("   ✅ Facil manutencao e organizacao")
    print("   ✅ Reutilizacao e consistencia")
    print("   ✅ Debugging facilitado")
    
    print("\n=== Exemplo concluido ===")

if __name__ == "__main__":
    example_keys_usage()

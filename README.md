# 🥗 Análise Comparativa de Alimentos - Streamlit v1.0 Stable

## 📋 Visão Geral

Aplicação web desenvolvida em Streamlit para análise comparativa de alimentos baseada na tabela TACO/USDA. Permite comparar dois alimentos selecionados através de visualizações interativas, gráficos e tabelas detalhadas.

**Versão**: 1.0 Stable  
**Desenvolvedor**: Rodrigo Ceregatti (rodrigo@co-labore.com)  
**Data de Lançamento**: 04out2025

## 🚀 Funcionalidades

### **Sistema de Instância Fixa (v1.0)**
- **Comparação Estável**: Instância persistente que mantém a comparação independente de filtros
- **Filtragem Livre**: Chips de filtro funcionam sem quebrar a visualização atual
- **Substituição Inteligente**: Apenas o alimento alterado é substituído, mantendo o outro intacto
- **UX Melhorada**: Análise contínua de diferentes alimentos sem perda de contexto

### **Comparação de Alimentos**
- **Seleção de Alimentos**: Interface intuitiva para escolher dois alimentos da base de dados
- **Análise Nutricional**: Comparação completa de macronutrientes e micronutrientes
- **Visualizações**: Gráficos de pizza, barras e tabelas coloridas
- **Sistema de Cores**: Esquema visual consistente (azul/roxo para alimento1, verde/rosa para alimento2)

### **Seções de Análise**
- **Resumo Macros**: Informações principais em cards coloridos com layout otimizado
- **Frações Macros**: Análise detalhada de proteínas, lipídios e carboidratos
- **Micronutrientes**: Vitaminas, minerais e outros componentes
- **Aminoácidos**: Perfil completo de aminoácidos essenciais

### **Melhorias Técnicas (v1.0)**
- **Estado Persistente**: Sistema robusto de gerenciamento de estado
- **Filtros Inteligentes**: Chips de filtro desacoplados da visualização
- **Performance**: Otimizações para carregamento e renderização
- **Estabilidade**: Correções de bugs e melhorias de UX

## 🏗️ Arquitetura

### **Estrutura Modular**
```
├── app.py                 # Aplicação principal
├── config/                # Configurações
├── data/                  # Carregamento de dados
├── domain/                # Lógica de domínio (nutrientes, paleta)
├── logic/                 # Funções de cálculo e tabelas
├── ui/                    # Componentes de interface
└── styles/                # Estilos CSS
```

### **Componentes Principais**
- **`app.py`**: Orquestração da aplicação com sistema de instância fixa
- **`ui/components.py`**: Componentes reutilizáveis (cards, menus)
- **`ui/charts.py`**: Geração de gráficos Plotly
- **`ui/sections.py`**: Seções de análise
- **`ui/state.py`**: Gerenciamento de estado e instância fixa
- **`logic/compute.py`**: Cálculos e formatação
- **`logic/tables.py`**: Criação de tabelas
- **`domain/palette.py`**: Sistema de cores centralizado

## 🎨 Sistema de Cores

### **Esquema por Slot**
- **Alimento 1 (Left)**: Gradiente azul/roxo (`#667EEA` → `#764BA2`)
- **Alimento 2 (Right)**: Gradiente verde/rosa (`#34D399` → `#F472B6`)
- **Consistência**: Aplicado em cards, gráficos, tabelas e legendas

## 🔄 Sistema de Instância Fixa

### **Arquitetura de Estado**
- **Instância Persistente**: Comparação mantida independente de filtros
- **Filtros Desacoplados**: Chips funcionam sem afetar visualização
- **Substituição Inteligente**: Apenas alimento alterado é substituído
- **Estado Isolado**: Cabeçalho separado da lógica de visualização

### **Fluxo de Funcionamento**
1. **Seleção Inicial**: Cria instância fixa com dados dos alimentos
2. **Filtragem**: Chips atualizam opções sem quebrar comparação
3. **Substituição**: Novo alimento substitui apenas o alterado
4. **Preservação**: Alimento não alterado mantém seus dados

## 📊 Dados

### **Base de Dados**
- **Fonte**: Tabela TACO/USDA normalizada
- **Formato**: CSV com 1925 alimentos
- **Campos**: 50+ nutrientes por alimento
- **Categorias**: Macronutrientes, vitaminas, minerais, aminoácidos

### **Processamento**
- **Carregamento**: Otimizado com cache
- **Formatação**: Números formatados com unidades apropriadas
- **Validação**: Tratamento de dados ausentes

## 🛠️ Tecnologias

### **Backend**
- **Python 3.13**
- **Streamlit**: Framework web
- **Pandas**: Manipulação de dados
- **Plotly**: Visualizações interativas

### **Frontend**
- **CSS Customizado**: Tema dark mode
- **Componentes Responsivos**: Adaptação a diferentes telas
- **Interatividade**: Gráficos e tabelas dinâmicas

## 🚀 Execução

### **Instalação**
```bash
# Clonar repositório
git clone <repository-url>
cd Streamlit

# Instalar dependências
pip install -r requirements.txt
```

### **Execução**
```bash
# Ativar ambiente virtual (se necessário)
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Executar aplicação
streamlit run app.py
```

### **Acesso**
- **URL Local**: http://localhost:8501
- **Interface**: Navegação por seções com menu fixo
- **Responsivo**: Funciona em desktop e mobile

## 📈 Características Técnicas

### **Performance**
- **Cache Inteligente**: Dados carregados uma vez
- **Lazy Loading**: Componentes carregados sob demanda
- **Otimização**: Gráficos renderizados eficientemente

### **Usabilidade**
- **Interface Limpa**: Design minimalista e focado
- **Navegação Intuitiva**: Menu de seções fixo
- **Feedback Visual**: Cores consistentes e indicadores claros

### **Manutenibilidade**
- **Código Modular**: Separação clara de responsabilidades
- **Documentação**: Código autodocumentado
- **Extensibilidade**: Fácil adição de novos nutrientes/seções

## 🔧 Configuração

### **Personalização**
- **Cores**: Modificar `domain/palette.py`
- **Seções**: Adicionar em `ui/sections.py`
- **Gráficos**: Estender `ui/charts.py`
- **Estilos**: Ajustar `styles/theme.css`

### **Dados**
- **Novos Alimentos**: Adicionar ao CSV principal
- **Novos Nutrientes**: Atualizar `domain/nutrients.py`
- **Formatação**: Modificar `logic/compute.py`

## 🆘 Suporte e Contato

### **Desenvolvedor**
- **Nome**: Rodrigo Ceregatti
- **Email**: rodrigo@co-labore.com
- **Versão**: 1.0 Stable

### **Reportar Bugs**
Caso encontre algum bug ou falha na aplicação, documentar caso para o email acima com mais informações:
- Descrição do problema
- Passos para reproduzir
- Screenshots (se aplicável)
- Informações do sistema

### **Funcionalidades**
- **Sistema de Instância Fixa**: Comparação estável independente de filtros
- **Filtragem Inteligente**: Chips desacoplados da visualização
- **Substituição Seletiva**: Apenas alimento alterado é substituído
- **UX Otimizada**: Análise contínua sem perda de contexto

## 📝 Licença

Projeto desenvolvido para análise nutricional comparativa. Uso educacional e de pesquisa.

---

**Desenvolvido com ❤️ usando Streamlit**
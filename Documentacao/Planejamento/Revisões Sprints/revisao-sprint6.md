# 🌀 Sprint Review & Planejamento – Sprint 6

**📅 Data:** 12 de maio de 2025  
**🕒 Hora:** 21h30  

## 👥 Participantes
- **FrontEnd:** Eduarda, Mayra  
- **BackEnd:** Marjorie, Guilherme, Gabriel  
- **Gestão de Projetos:** Eric, Brenda, Maria Eduarda  

---

## ✅ Revisão da Sprint 5

### ⚙️ Backend
- Avanço significativo na implementação dos endpoints.  
- Integrações simuladas entre backend e frontend começaram a ser estruturadas.  
  **Status:** _em andamento_

### 🎨 FrontEnd
- Atrasos persistem, mas apoio da gestão proporcionou progresso nas telas principais.  
  **Status:** _em andamento_

### 📚 Documentação
- Parte da documentação foi migrada para o MkDocs.  
- Iniciada estrutura para documentação técnica via GitHub Pages.  
  **Status:** _em progresso_

### 🧠 Viabilidade Técnica
- Discussões sobre substituição de NLP tradicional por LLMs para análise de gráficos.  
  **Status:** _em análise_

---

## 🎯 Planejamento da Sprint 6

### Objetivos principais:
- Integrar o backend com o front-end, utilizando funções simuladas para viabilizar a experiência completa.  
- Finalizar a documentação dos endpoints e publicar no GitHub Pages.  
- Revisar e adaptar o escopo do projeto com base no cronograma ajustado.  
- Refinar o backlog com novas definições de usuários e desenvolvedores.  
- Validar se as issues atuais são viáveis até o final do ciclo.  
- Implementar o sistema de **alertas por e-mail** com base em detecção de **anomalias** e **mudanças drásticas** previstas por LLM.  
- Remover definitivamente a funcionalidade de **login** do escopo do projeto.  

---

## 🧩 Divisão de Tarefas – Sprint 6

### 👨‍💻 Backend
- **Marjorie:** Integração do `search.py` com a interface web (Streamlit), simulando funções com dados.  
- **Gabriel:** Finalizar documentação técnica dos endpoints e publicar via GitHub Pages.  
- **Time Backend:** Estruturar lógica de alertas automáticos por e-mail baseados em análise do LLM.  
  - Envio de alertas **apenas** quando forem detectadas **mudanças significativas** ou **anomalias de comportamento** nos dados.  

### 🧠 Gestão de Projetos
- Refinamento do backlog, com foco na segmentação dos usuários (usuários finais e desenvolvedores).  
- Reavaliação das issues abertas, assegurando viabilidade até a Sprint 8.  

---

## 🔄 Mudança de Escopo e Fluxo do Projeto

### Atualizações:
- **Funcionalidade de login** removida do escopo.  
- **Sistema de alerta via e-mail** adicionado com base em previsões do modelo LLM.  

### Novo fluxo definido:
1. **Landing Page**  
2. **Tela de Filtros de Seleção (Menu)**  
3. **Tela de Geração de Relatório (LLM)**  
4. **Dashboard Gerada**  
5. **Pop-up para Exportação (Download)**  
6. **Retorno à Dashboard**  
7. **Pop-up de Alertas (E-mail), se aplicável**  

> Os alertas por e-mail serão enviados apenas quando forem detectadas **mudanças drásticas** ou **anomalias** nos dados analisados.

---

## ⚠️ Pontos de Atenção

- **Arquitetura:** O sistema está sendo redesenhado para alinhar com o novo fluxo funcional e exclusão do login.  
- **Backlog:** Importante garantir que o backlog reflita corretamente as novas prioridades.  
- **Documentação:** A publicação via GitHub Pages precisa ser finalizada nesta sprint.  
- **Alertas por E-mail:** Definir critérios técnicos para o que constitui uma "mudança drástica" ou "anomalia".  
- **Viabilidade:** Reavaliar complexidade do uso do LLM frente ao tempo restante até a entrega da release.  

---

## ✅ Encerramento

A Sprint 6 marca a consolidação de decisões técnicas importantes, como a remoção do login e a adição dos alertas inteligentes via LLM. A equipe foca agora na integração de funcionalidades e no refinamento da entrega para a Release 1.

**🖋 Assinatura:** @mariadenis  

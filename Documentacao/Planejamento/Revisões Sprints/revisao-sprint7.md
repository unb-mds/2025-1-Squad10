# 🌀 Sprint Review & Planejamento – Sprint 7

**📅 Data:** 19 de maio de 2025  
**🕒 Horário:** 21h30  

**👥 Participantes:**  
- **Equipe de FrontEnd:** Eduarda, Mayra  
- **Equipe de BackEnd:** Marjorie, Gabriel, Guilherme  
- **Gestão de Projetos:** Eric, Brenda, Maria Eduarda

---

## ✅ Revisão da Sprint 7

Durante esta sprint, o time concentrou-se na finalização das **visualizações interativas com Plotly**, além de realizar ajustes estruturais no projeto, como a **revisão do escopo**, **alteração no fluxo de navegação** e redefinição de **issues no backlog**.

---

## 🔄 Atualizações Técnicas

### 🧱 BackEnd
- Iniciou e avançou na **implementação e integração** dos dados com a estrutura web.  
- Foi incorporado o módulo `search.py` ao app principal, iniciando a adaptação do fluxo com a LLM.  
- Alterações para reduzir a dependência do perfil “usuário genérico” e tornar as respostas mais específicas ao contexto do projeto.

### 📊 Visualização com Plotly
- Gráficos interativos concluídos
- Comportamentos implementados: filtros dinâmicos, tooltips interativos, responsividade e exportação de gráficos.  
- Visualizações totalmente integradas com o Streamlit.

### 🔄 Alterações no Escopo
- **Login removido** do projeto por não ser essencial à experiência final e para simplificar o fluxo.  
- Implementado o conceito de **alertas por e-mail**, que serão disparados **somente** em caso de **mudanças drásticas ou detecção de anomalias** via LLM.  
- Estrutura do projeto foi **reorganizada** em 4 etapas de navegação funcional:

**Landing Page**
→ Tela de Filtros (Menu de Seleção)
→ Geração de Relatório com LLM
→ Dashboard com Dados Interativos
→ Pop-up de Exportação
→ Retorno ao Dashboard
→ Pop-up de Alertas (E-mail, se necessário)


---

## 🧩 Backlog & Organização

- Backlog revisado com foco em funcionalidades essenciais.  
- Issues atualizadas para refletir o escopo real e o tempo restante do projeto.  
- Proposta: categorizar issues em _usuário_ e _desenvolvedor_, para facilitar a priorização e distribuição de tarefas.  
- Levantamento em andamento sobre a **viabilidade de concluir todas as tarefas** nas sprints restantes, com foco na entrega funcional da Release 2.

---

## ✅ Considerações Finais

A Sprint 7 representou um marco importante de reestruturação. A nova sequência de telas proporciona um fluxo mais fluido para o usuário. O uso do Plotly trouxe uma camada de interatividade essencial para a visualização dos dados analisados pela LLM. As decisões tomadas — como a remoção do login e o foco em alertas de alto impacto — refletem uma abordagem mais enxuta e orientada à entrega de valor.

---

**🖋 Assinatura:** @mariadenis  

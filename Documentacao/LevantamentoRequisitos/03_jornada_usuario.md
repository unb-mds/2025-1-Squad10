# 🗺️ Jornada do Usuário  
**Projeto “Relatórios do IPEA” — Toró de Ideias**

## 🎯 O que precisamos resolver e por quê?

**Objetivo central:**  
Promover **inteligência**, **automação** e **acessibilidade** na análise e divulgação de dados financeiros públicos.

### Problemas identificados:
- Acesso difícil ou técnico demais aos dados financeiros.
- Falta de padronização na apresentação das informações.
- Baixa capacidade de monitoramento em tempo real de gastos públicos.
- Dificuldade em interpretar variações e padrões financeiros.
- Falta de ferramentas visuais e acessíveis para diferentes perfis de usuários.

### Soluções propostas:
- Democratizar o acesso a dados financeiros com linguagem clara e visual.
- Gerar relatórios automatizados e personalizados com base em filtros específicos.
- Implementar dashboards interativos para facilitar a navegação e análise.
- Utilizar IA (NLP) para gerar resumos explicativos e alertas inteligentes.
- Apoiar a prestação de contas com visualizações impactantes e transparentes.

---

## 👥 Quem está envolvido e quem se beneficia?

### Usuários beneficiados:
- 🏛️ Cidadãos em geral  
- 📊 Instituições de pesquisa e ONGs  
- 📰 Jornalistas e repórteres investigativos  
- 💼 Contadores, auditores e analistas financeiros  
- 🏢 Empresas e bancos  
- 🧰 Engenheiros públicos (infraestrutura, energia, etc.)  
- 🧑‍⚖️ Órgãos governamentais e gestores públicos  

### Equipe de desenvolvimento:
| Função              | Responsabilidades principais |
|---------------------|------------------------------|
| **Desenvolvedores** | Backend (FastAPI), frontend (Streamlit), integrações |
| **Cientistas de Dados** | NLP, visualização, modelagem e análises |
| **Analistas** | Definição de métricas, validação e regras de negócio |
| **Gestores Públicos** | Usuários estratégicos e tomadores de decisão |
| **Usuários Técnicos** | Profissionais que consomem insights específicos |
| **Designers** _(opcional)_ | Design de interfaces acessíveis e intuitivas |

---

## 🧩 Como vamos resolver o problema?

### Ações e soluções práticas:
- Criação de uma **dashboard interativa** com **Streamlit**, HTML e CSS responsivo.
- Aplicação de **modelos de NLP open-source** (BERTopic, T5, BART) para geração de resumos e insights.
- Automação do pipeline com ferramentas como **Prefect**, Airflow ou cron jobs.
- Implementação de **filtros dinâmicos** (órgão, município, data, categoria).
- Geração de **relatórios exportáveis** (.pdf, .html, .csv).
- Interface com **acessibilidade** para usuários técnicos e não técnicos.
- Emissão de **alertas inteligentes** sobre variações incomuns nos dados.
- Validação constante com feedback de usuários e especialistas.
- Estruturação do projeto como **código aberto reutilizável**.

---

## 🧠 Tecnologias

| Categoria                     | Ferramentas Utilizadas                        |
|------------------------------|-----------------------------------------------|
| Framework principal          | Streamlit + Haystack                         |
| NLP e modelagem de tópicos   | Hugging Face Transformers + BERTopic         |
| Pré-processamento de texto   | spaCy + Pandas                               |
| Visualização e relatórios    | Plotly + Streamlit                           |
| Backend/API                  | FastAPI                                      |
| Orquestração e automação     | Prefect (ou Airflow)                         |
| Monitoramento e validação    | Evidently                                    |

---

## 🔄 Visão Integrada da Jornada

1. **Coleta e pré-processamento:**  
   Dados financeiros são automaticamente obtidos, normalizados e limpos.

2. **Análise e extração de insights com NLP:**  
   Modelos identificam tópicos relevantes, geram resumos e detectam anomalias.

3. **Visualização e interação:**  
   Usuários acessam dashboards com filtros personalizados e gráficos interativos.

4. **Exportação e notificações:**  
   Relatórios são gerados e exportados. Gestores recebem alertas por e-mail ou painel.

5. **Validação e código aberto:**  
   Resultados são validados por especialistas e disponibilizados como projeto público.

---

> 📌 Esta jornada orienta o design de funcionalidades que entregam valor real para diferentes públicos, equilibrando automação, transparência e usabilidade.  
> O foco está em transformar dados públicos em inteligência acessível.


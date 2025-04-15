
# 📊 Sistema Inteligente para Análise Automatizada de Notícias e Indicadores do IPEA

## 🎯 Visão do Produto

**Nome do Projeto:** Sistema Inteligente para Análise Automatizada de Notícias e Indicadores do IPEA

**Missão:** Democratizar o acesso à análise econômica a partir de dados e textos de fontes oficiais, promovendo transparência, eficiência e inteligência analítica através de ferramentas digitais acessíveis.

---

## ❗ Problema que Resolve

Atualmente, dados econômicos e notícias de órgãos como o IPEA estão dispersos e pouco acessíveis para usuários não especialistas. A análise econômica ainda é altamente manual, demorada e restrita a usuários com formação técnica. Isso dificulta o uso dos dados para tomada de decisão, educação e participação cidadã.

---

## 💡 Solução Proposta

Plataforma modular que coleta, analisa e apresenta de forma intuitiva séries temporais econômicas e notícias do IPEA com uso de modelos de NLP open-source e visualizações interativas.

Qualquer usuário poderá:

- Explorar indicadores econômicos com filtros temporais e setoriais
- Gerar relatórios automáticos com análises quantitativas e qualitativas
- Compreender temas, sentimentos e tendências em notícias

---

## 🚀 Diferenciais

- Interface acessível com Streamlit e dashboards integrados com Metabase (a definir)
- Pipeline automatizado de coleta e análise via Django e Airflow (a definir)
- Uso de NLP leve (BERTopic, BERTimbau, DistilBERT, etc.) para insights de texto (a definir)
- Exportação automatizada de relatórios em PDF e HTML

---

## 📈 Impacto Esperado

- Redução no tempo de análise econômica para servidores e pesquisadores
- Estímulo à educação econômica com ferramentas intuitivas
- Melhoria na qualidade de decisão política e gestão pública baseada em dados
- Acesso cidadão facilitado a dados públicos com interpretações semânticas

---

## 🎯 Objetivo Geral

Construir uma plataforma de geração automatizada de relatórios financeiros públicos com painéis interativos e textos gerados por modelos NLP open-source, promovendo transparência e eficiência na gestão pública.

---

## 📋 Backlog do Produto

| Prioridade | User Story | Tipo de Requisito |
|-----------|------------|--------------------|
| Alta | Como desenvolvedor, quero importar arquivos via API, para alimentar o pipeline com dados do IPEA. | Funcional |
| Alta | Como desenvolvedor, quero que os dados sejam obtidos automaticamente (API ou scraping), para garantir atualizações. | Funcional |
| Média | Como desenvolvedor, quero aplicar um pipeline de pré-processamento textual, para alimentar os modelos de NLP. | Funcional |
| Alta | Como desenvolvedor, quero aplicar o BERTopic nos textos, para identificar tópicos relevantes. | Funcional |
| Média | Como analista público, quero visualizar tópicos e exemplos de textos, para entender melhor as áreas críticas. | Funcional |
| Alta | Como cientista de dados, quero normalizar datas, moedas e categorias, para garantir consistência na análise. | Funcional |
| Alta | Como gestor público, quero receber um resumo técnico mensal, para entender rapidamente os principais pontos. | Funcional |
| Média | Como desenvolvedor, quero utilizar modelos generativos (T5, BART) para gerar resumos a partir dos dados. | Funcional |
| Alta | Como gestor, quero receber alertas automáticos sobre gastos anormais, para tomar decisões corretivas. | Funcional |
| Média | Como desenvolvedor, quero configurar regras para alertas, para evitar falsos positivos. | Funcional |
| Alta | Como gestor público, quero visualizar dados e relatórios em uma interface clara, para facilitar a análise. | Funcional |
| Média | Como usuário, quero interagir com filtros e gráficos, para explorar regiões, períodos e categorias. | Funcional |
| Média | Como analista, quero exportar relatórios em PDF ou HTML, para enviar ou arquivar. | Funcional |
| Média | Como gestor, quero salvar relatórios anteriores, para acompanhar a evolução dos indicadores. | Funcional |
| Alta | Como desenvolvedor, quero criar endpoints REST com FastAPI, para a interface acessar dados dinamicamente. | Funcional |
| Alta | Como desenvolvedor, quero escrever testes unitários e de integração, para garantir que o sistema funcione. | Não funcional |
| Alta | Como colaborador, quero ter uma documentação clara do pipeline, para facilitar o onboarding. | Não funcional |
| Média | Como gestor, quero disponibilizar o projeto como código aberto, para outras instituições públicas replicarem. | Não funcional |

---

## 🗺️ Story Map - Projeto Relatórios do IPEA

> *Organizado por Epics, Features e User Stories*

### Epic 1: Ingestão e Pré-processamento dos Dados Financeiros

- **Feature 1.1: Obtenção de dados financeiros do IPEA**
  - Importação de dados via API ou scraping
- **Feature 1.2: Limpeza e preparação dos dados**
  - Normalização de datas, moedas e categorias
  - Pré-processamento textual

### Epic 2: Análise Semântica e Geração de Insights com NLP

- **Feature 2.1: Extração de tópicos relevantes (BERTopic)**
- **Feature 2.2: Geração de resumos automatizados (T5/BART)**
- **Feature 2.3: Emissão de alertas com base em anomalias**

### Epic 3: Visualização dos Dados e Relatórios

- **Feature 3.1: Painel interativo com dados e textos**
- **Feature 3.2: Exportação e compartilhamento dos relatórios**

### Epic 4: Backend e Integração de Componentes

- **Feature 4.1: Servir dados via API (FastAPI)**
- **Feature 4.2: Orquestração de pipelines e notificações**

### Epic 5: Qualidade, Validação e Documentação

- **Feature 5.1: Testes e validação dos modelos e sistema**
- **Feature 5.2: Documentação e código aberto**

---

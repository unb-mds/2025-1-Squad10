# Backlog do produto

| Prioridade | User Story                                                                                                          | Tipo de Requisito             |
| ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Alta       | Como desenvolvedor, quero importar arquivos via API, para alimentar o pipeline com dados do IPEA.                   | Funcional                     |
| Alta       | Como desenvolvedor, quero que os dados sejam obtidos automaticamente (API ou scraping), para garantir atualizações. | Funcional                     |
| Média      | Como desenvolvedor, quero aplicar um pipeline de pré-processamento textual, para alimentar os modelos de NLP.       | Funcional                     |
| Alta       | Como desenvolvedor, quero aplicar o BERTopic nos textos, para identificar tópicos relevantes.                       | Funcional                     |
| Média      | Como analista público, quero visualizar tópicos e exemplos de textos, para entender melhor as áreas críticas.       | Funcional                     |
| Alta       | Como cientista de dados, quero normalizar datas, moedas e categorias, para garantir consistência na análise.        | Funcional                     |
| Alta       | Como gestor público, quero receber um resumo técnico mensal, para entender rapidamente os principais pontos.        | Funcional                     |
| Média      | Como desenvolvedor, quero utilizar modelos generativos (T5, BART) para gerar resumos a partir dos dados.            | Funcional                     |
| Alta       | Como gestor, quero receber alertas automáticos sobre gastos anormais, para tomar decisões corretivas.               | Funcional                     |
| Média      | Como desenvolvedor, quero configurar regras para alertas, para evitar falsos positivos.                             | Funcional                     |
| Alta       | Como gestor público, quero visualizar dados e relatórios em uma interface clara, para facilitar a análise.          | Funcional                     |
| Média      | Como usuário, quero interagir com filtros e gráficos, para explorar regiões, períodos e categorias.                 | Funcional                     |
| Média      | Como analista, quero exportar relatórios em PDF ou HTML, para enviar ou arquivar.                                   | Funcional                     |
| Média      | Como gestor, quero salvar relatórios anteriores, para acompanhar a evolução dos indicadores.                        | Funcional                     |
| Alta       | Como desenvolvedor, quero criar endpoints REST com FastAPI, para a interface acessar dados dinamicamente.           | Funcional                     |
| Alta       | Como desenvolvedor, quero escrever testes unitários e de integração, para garantir que o sistema funcione.          | Não funcional (qualidade)     |
| Alta       | Como colaborador, quero ter uma documentação clara do pipeline, para facilitar o onboarding.                        | Não funcional (documentação)  |
| Média      | Como gestor, quero disponibilizar o projeto como código aberto, para outras instituições públicas replicarem.       | Não funcional (licenciamento) |

---

# Épicos, Features e User Stories
### 🧭 __ÉPICO 1__: Ingestão e Pré-processamento dos Dados Financeiros
#### __Feature 1.1__ – Obtenção de dados financeiros do IPEA
##### User Story 1.1.1: 
Como desenvolvedor, quero importar arquivos através da API, para poder alimentar o pipeline com dados financeiros do IPEA.
##### User Story 1.1.2: 
Como desenvolvedor, quero que os dados sejam obtidos automaticamente (de fontes como API ou scraping), para garantir atualizações frequentes.
#### __Feature 1.2__ – Limpeza e preparação dos dados
##### User Story 1.2.1: 
Como cientista de dados, quero normalizar datas, moedas e categorias, para garantir consistência na análise.
##### User Story 1.2.2: 
Como desenvolvedor, quero aplicar um pipeline de pré-processamento textual (com remoção de stopwords, normalização e tokenização), para alimentar os modelos de NLP com dados limpos.
### 🧠 __ÉPICO 2__: Análise Semântica e Geração de Insights com NLP
#### __Feature 2.1__ – Extração de tópicos relevantes
##### User Story 2.1.1:
Como desenvolvedor, quero aplicar o BERTopic nos textos financeiros, para identificar automaticamente os principais tópicos abordados.
##### User Story 2.1.2: 
Como analista público, quero visualizar os tópicos e exemplos de textos relacionados, para entender melhor as áreas críticas.
#### Feature 2.2 – Geração de resumos automatizados
##### User Story 2.2.1: 
Como gestor público, quero receber um resumo técnico sobre os dados do mês, para entender rapidamente os principais pontos financeiros.
##### User Story 2.2.2: 
Como desenvolvedor, quero utilizar modelos generativos open-source (ex: T5 ou BART), para gerar resumos a partir dos dados analisados.
#### Feature 2.3 – Emissão de alertas com base em anomalias
##### User Story 2.3.1: 
Como gestor, quero receber um alerta automático quando houver aumento anormal em um gasto específico, para tomar decisões corretivas.
##### User Story 2.3.2: 
Como desenvolvedor, quero configurar regras e condições para geração de alertas, para evitar falsos positivos.
### 📊 __ÉPICO 3__: Visualização dos Dados e Relatórios
#### __Feature 3.1__ – Painel interativo com dados e textos
##### User Story 3.1.1: 
Como gestor público, quero visualizar os dados e relatórios em uma interface clara, para facilitar a análise e tomada de decisão.
##### User Story 3.1.2: 
Como usuário, quero interagir com filtros e gráficos no dashboard, para explorar diferentes regiões, períodos e categorias.
#### Feature 3.2 – Exportação e compartilhamento dos relatórios
##### User Story 3.2.1:
Como analista, quero exportar os relatórios gerados em formato PDF ou HTML, para enviar por e-mail ou arquivar.
##### User Story 3.2.2: 
Como gestor, quero salvar os relatórios anteriores, para poder acompanhar a evolução dos indicadores.
### 🔗 __ÉPICO 4__: Backend e Integração de Componentes
#### Feature 4.1 – Servir dados via API
##### User Story 4.1.1: 
Como desenvolvedor, quero criar endpoints REST com FastAPI, para que a interface Streamlit acesse os dados e textos gerados dinamicamente.
### 📄 __ÉPICO 5__: Qualidade, Validação e Documentação
#### Feature 5.1 – Testes e validação dos modelos e sistema
##### User Story 5.1.1: 
Como desenvolvedor, quero escrever testes unitários e de integração, para garantir que o sistema funcione corretamente.
#### Feature 5.2 – Documentação e código aberto
##### User Story 5.2.1: 
Como colaborador, quero ter uma documentação clara do pipeline e de como rodar o sistema, para facilitar o onboarding.
##### User Story 5.2.2:
Como gestor, quero disponibilizar o projeto como código aberto com licença livre, para que outras instituições públicas possam replicá-lo.
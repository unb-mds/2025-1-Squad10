
#  Requisitos de Software: Sistema Inteligente para Análise Automatizada de Notícias e Indicadores do IPEA

## 1. Visão Geral

**Nome do Projeto**: Sistema Inteligente para Análise Automatizada de Notícias e Indicadores do IPEA

**Missão**: Democratizar o acesso à análise econômica a partir de dados e textos de fontes oficiais, promovendo transparência, eficiência e inteligência analítica através de ferramentas digitais acessíveis.

**Problemática**: Dados econômicos e notícias de órgãos como o IPEA estão dispersos e pouco acessíveis para usuários não especialistas. A análise econômica ainda é altamente manual e demorada, restringindo o uso dos dados para tomada de decisão e participação cidadã.

**Solução Proposta**: Plataforma modular que coleta, analisa e apresenta de forma intuitiva séries temporais econômicas e notícias do IPEA com uso de modelos de NLP open-source e visualizações interativas. A solução permitirá:
- Exploração de indicadores econômicos com filtros temporais e setoriais.
- Geração automatizada de relatórios com análises quantitativas e qualitativas.
- Compreensão de temas, sentimentos e tendências em notícias econômicas.

**Impacto Esperado**:
- Redução no tempo de análise econômica para servidores e pesquisadores.
- Estímulo à educação econômica com ferramentas intuitivas.
- Melhoria na qualidade da decisão política e gestão pública baseada em dados.
- Acesso cidadão facilitado a dados públicos com interpretações semânticas.

---

## 2. Objetivos

**Objetivo Geral**: Construir uma plataforma de geração automatizada de relatórios financeiros públicos com painéis interativos e textos gerados por modelos NLP open-source, promovendo transparência e eficiência na gestão pública.

**Objetivos Específicos**:
- Automatizar a coleta de dados financeiros do IPEA.
- Aplicar pré-processamento de dados e modelos de NLP para análise semântica.
- Gerar resumos e insights com base nos dados coletados.
- Criar uma interface interativa para visualização e exportação de relatórios.
- Disponibilizar o código como open-source para replicabilidade em outras instituições públicas.

---

## 3. Requisitos Funcionais

| ID  | Prioridade | User Story | Descrição |
| --- | ---------- | ---------- | --------- |
| RF001 | Alta | Como desenvolvedor, quero importar arquivos via API, para alimentar o pipeline com dados do IPEA. | Permite alimentar o pipeline com dados financeiros do IPEA em tempo real. |
| RF002 | Alta | Como desenvolvedor, quero que os dados sejam obtidos automaticamente (API ou scraping), para garantir atualizações. | Garante que a base de dados seja constantemente atualizada. |
| RF003 | Média | Como desenvolvedor, quero aplicar um pipeline de pré-processamento textual, para alimentar os modelos de NLP. | Realiza o pré-processamento de dados textuais (remoção de stopwords, normalização, tokenização). |
| RF004 | Alta | Como desenvolvedor, quero aplicar o BERTopic nos textos, para identificar tópicos relevantes. | Identifica tópicos relevantes nos textos financeiros utilizando o modelo BERTopic. |
| RF005 | Média | Como analista público, quero visualizar tópicos e exemplos de textos, para entender melhor as áreas críticas. | Visualiza os tópicos e exemplos de textos relacionados, facilitando a análise das áreas críticas. |
| RF006 | Alta | Como cientista de dados, quero normalizar datas, moedas e categorias, para garantir consistência na análise. | Garante a consistência dos dados para análise financeira precisa. |
| RF007 | Alta | Como gestor público, quero receber um resumo técnico mensal, para entender rapidamente os principais pontos. | Gera resumos mensais automáticos com insights financeiros para gestores públicos. |
| RF008 | Média | Como desenvolvedor, quero utilizar modelos generativos (T5, BART) para gerar resumos a partir dos dados. | Utiliza modelos generativos para criar resumos automáticos a partir dos dados coletados. |
| RF009 | Alta | Como gestor, quero receber alertas automáticos sobre gastos anormais, para tomar decisões corretivas. | Envia alertas sobre variações anormais em gastos, ajudando na tomada de decisões. |
| RF010 | Média | Como desenvolvedor, quero configurar regras para alertas, para evitar falsos positivos. | Permite configurar regras de alerta para evitar notificações desnecessárias. |
| RF011 | Alta | Como gestor público, quero visualizar dados e relatórios em uma interface clara, para facilitar a análise. | Proporciona uma interface intuitiva para visualização e interpretação dos dados financeiros. |
| RF012 | Média | Como usuário, quero interagir com filtros e gráficos, para explorar períodos e categorias. | Permite a interação com gráficos e filtros, facilitando a análise personalizada dos dados. |
| RF013 | Média | Como analista, quero exportar relatórios em PDF ou HTML, para enviar ou arquivar. | Facilita a exportação de relatórios para formatos compatíveis com outras plataformas. |
| RF014 | Média | Como gestor, quero salvar relatórios anteriores, para acompanhar a evolução dos indicadores. | Permite salvar relatórios passados para acompanhar a evolução de indicadores financeiros. |
| RF015 | Alta | Como desenvolvedor, quero criar endpoints REST com FastAPI, para a interface acessar dados dinamicamente. | Cria endpoints para que a interface acesse dados financeiros em tempo real. |
| RF016 | Alta | Como desenvolvedor, quero escrever testes unitários e de integração, para garantir que o sistema funcione corretamente. | Garante a estabilidade e funcionamento do sistema por meio de testes automatizados. |
| RF017 | Alta | Como colaborador, quero ter uma documentação clara do pipeline, para facilitar o onboarding. | Fornece documentação clara e detalhada do pipeline de dados e processamento. |
| RF018 | Média | Como gestor, quero disponibilizar o projeto como código aberto, para outras instituições públicas replicarem. | Publica o código com licença open-source, permitindo que outras instituições usem e adaptem. |

---

## 4. Requisitos Não Funcionais

| ID  | Prioridade | Descrição |
| --- | ---------- | --------- |
| RNF001 | Alta | O sistema deve ser escalável para lidar com grandes volumes de dados financeiros em tempo real. |
| RNF002 | Alta | O sistema deve ser seguro, com autenticação e autorização adequadas para garantir a proteção dos dados. |
| RNF003 | Alta | O sistema deve ser capaz de gerar relatórios automaticamente em PDF e HTML com base nos dados financeiros. |
| RNF004 | Média | O sistema deve ser acessível e usável, com uma interface amigável e fácil de navegar para usuários não técnicos. |
| RNF005 | Média | O sistema deve ser modular para facilitar a adição de novos módulos ou componentes no futuro. |

---

## 5. Tecnologias e Ferramentas

- **Backend**: Django, FastAPI, Airflow
- **Modelos de NLP**: BERTopic, T5, BART, BERTimbau, DistilBERT
- **Frontend**: Streamlit (para visualização de dados)
- **Banco de Dados**: PostgreSQL, MongoDB (dependendo da estrutura dos dados)
- **Testes**: pytest, unittest
- **Contêinerização**: Docker
- **Versão**: GitHub

---

## 6. Licenciamento

O projeto será disponibilizado sob a licença **MIT**, permitindo que outras instituições públicas possam replicá-lo, adaptar e distribuir o código conforme necessário.

---

Documento Validado @EricAraujoBsb

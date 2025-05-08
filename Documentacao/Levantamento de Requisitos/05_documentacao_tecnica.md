
# 🛠️ Documentação Técnica  
**Projeto: Relatórios Automatizados do IPEA**

Este documento detalha a arquitetura técnica, ferramentas utilizadas, organização do código e práticas recomendadas para desenvolvimento, manutenção e contribuição no projeto.

---

## 🔧 Arquitetura Técnica

### 📌 Componentes Principais:

| Componente     | Descrição |
|----------------|-----------|
| **Frontend**   | Aplicação interativa em Streamlit com filtros, gráficos e exportação de relatórios. |
| **Backend/API**| Implementado com FastAPI para servir dados e textos dinamicamente via endpoints REST. |
| **NLP/IA**     | Modelos como T5, BART e BERTopic, utilizados para sumarização, extração de tópicos e geração de alertas. |
| **Automação**  | Orquestração com Prefect ou Airflow para executar rotinas de ingestão, análise e geração. |
| **Visualização**| Gráficos interativos com Plotly, exportáveis em HTML e PDF. |

---

## 🧱 Organização do Projeto


---

## 🧠 Modelos de NLP Utilizados

- **BERTopic**: Extração de tópicos com visualização.
- **T5 / BART**: Sumarização automática e explicações de textos.
- **spaCy**: Pré-processamento linguístico (tokenização, lematização).
- **Hugging Face Transformers**: Framework para deploy dos modelos.

---

## 🧪 Testes e Validação


## 💬 Boas Práticas

- Uso de Git Flow para organização de branches
- Commits padronizados (ex: `feat:`, `fix:`, `docs:`)
- Revisões de código via Pull Requests
- Automação de tarefas recorrentes com scripts e CI (opcional)

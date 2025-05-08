
# 🚀 Estratégia de Releases (Sujeito a Modificação)
**Projeto: Relatórios Automatizados do IPEA**

Este documento descreve a abordagem de versionamento, critérios de entrega e planejamento das versões principais do projeto.

---

## 🎯 Objetivo da Estratégia

- Garantir **entregas contínuas e incrementais** com qualidade e estabilidade.
- Facilitar testes, feedback de usuários e melhorias iterativas.
- Apoiar a evolução do projeto com **transparência e previsibilidade**.


## 📅 Ciclo de Releases
<!--
| Tipo de release | Frequência sugerida | Conteúdo típico |
|------------------|----------------------|------------------|
| `patch`          | Ad-hoc (bugfixes)    | Correções pontuais, ajustes visuais |
| `minor`          | A cada 2 semanas     | Novas features não disruptivas |
| `major`          | Trimestral           | Mudanças estruturais ou novas jornadas completas |
-->


---

## 🗂️ Planejamento por Versão

### v0.1.0 — MVP Inicial
- Coleta de dados automatizada via API
- Pré-processamento e normalização
- Visualização básica com Streamlit
- Exportação manual de relatórios

### v0.2.0 — Primeiras Automações Inteligentes
- Integração com modelos NLP (BERTopic + T5)
- Sumarização e extração de tópicos
- Exportação em PDF e HTML
- Alertas simples por e-mail

### v1.0.0 — Primeira Versão Pública
- Interface refinada com acessibilidade
- Painel de filtros e dashboards interativos
- Pipeline completo automatizado
- Validação técnica e release open-source



## 🧩 Versionamento Semântico

Adotamos **SemVer** (Semantic Versioning):


<!--
MAJOR.MINOR.PATCH

- `MAJOR`: Mudanças incompatíveis na API ou estrutura
- `MINOR`: Novas funcionalidades compatíveis
- `PATCH`: Correções ou melhorias menores
-->


## 🧪 Critérios para liberação

- Passar todos os testes automatizados
- Validação funcional pela equipe técnica
- Feedback positivo de pelo menos 1 usuário de teste
- Atualização de documentação e changelog

---

## 📦 Publicação

- Releases registrados via GitHub Releases
- Versões estáveis publicadas com changelog no `README.md`
- Código publicado com tag (`git tag v1.0.0`) e push para `main`

---

> 📌 A estratégia de releases garante que o projeto avance de forma contínua, validada e com entregas significativas para os usuários e gestores públicos.

# ***INTRODUÇÃO A ARQUITETURA DE SOFTWARE***

Arquitetura é uma representação das visões de objetos, coisas ou ideias, seja de forma gráfica ou textual, em seus diferentes níveis de abstração 

Abstrair é a capacidade de transformar ideias ou solicitações em representações que sejam aplicáveis para a construção de um software.

## ***NÍVEIS DE ABSTRAÇÃO E PADRÕES ARQUITETÔNICOS***

A abstração para a criação da arquitetura de um software pode ser feita em diferentes níveis, e em diferentes estilos partindo de pontos de representação do projeto.

Existem dois estilos de abstração de arquitetura:

ARQUITETURA DE ESPECIALIZAÇÃO

Parte de abstração de uma requisição a fim de obter os conceitos técnicos de forma mais concreta possível para que seja realizado o desenvolvimento do software. 

* ***1º Nível***: Muito abstrato, nível genérico
* ***2º Nível***: Abstrato, nível intermediário
* ***3º Nível***: Concreto, nível específico

ARQUITETURA DE GENERALIZAÇÃO

Parte da abstração de um conceito técnico bastante concreto para algo mais generalizado a fim de explorar novas ideias e soluções que possam ser aplicadas no software.

* ***1º Nível***: Concreto, nível específico
* ***2º Nível***: Abstrato, nível intermediário
* ***3º Nível***: Muito abstrato, nível genérico

## ***MODELO DE PROJETO***

O modelo de um projeto de software é proveniente do modelo de análise realizado sobre a descrição do sistema que se quer desenvolver (requisitos de um software).

O modelo de análise dos requisitos de um software englobam:

* ***MODELOS BASEADOS EM CENÁRIOS***: Casos de uso e diagrama, histórias de usuários.

* ***MODELOS DE CLASSES***: Diagramas de classes, diagramas de colaboração.

* ***MODELOS DE FLUXO***: DFDs, modelos e dados.

* ***MODELOS COMPORTAMENTAIS***: Diagramas de estados, diagramas de sequências.


O modelo de análise dos requisitos serve como porta de entrada para a prototipação do modelo de projeto de software a ser desenvolvido:

* ***ELEMENTOS BASEADOS EM CENÁRIOS***: Casos de uso, diagramas de casos de uso, diagramas de atividades.
* ***ELEMENTOS BASEADOS EM CLASSES***: Diagramas de classes, pacotes de análise, modelos CRC, diagramas de colaboração.
* ***ELEMENTOS DE FLUXO DE DADOS***: Diagramas de fluxo de dados e de fluxo de controle, narrativa de processamento.
* ***ELEMENTOS COMPORTAMENTAIS***: Diagramas de estados, diagramas de sequência.

Sendo que cada um desses elementos formam as camadas do modelo do projeto:

PROJETO DE COMPONENTES: Engloba  todos os elementos.
PROJETO DE INTERFACES: Engloba os elementos de fluxos de dados e comportamentais.
PROJETO ARQUITETURAL: Engloba os elementos de fluxo de dados e baseados em classes.
PROJETO DE DADOS/CLASSES: Engloba os elementos baseados em classes.

## ***TÉCNICAS DE ARQUITETURA***

***ITERATIVA***

Ajuda a produzir uma solução candidata que pode ser refinada posteriormente pela repetição dos mesmos 5 passos principais, criando finalmente a arquitetura que melhor define a aplicação.

* ***1º Passo***: Identificar os objetivos da arquitetura

    Identificar os objetivos de arquitetura no início, sendo que a quantidade de tempo gasto em cada fase da arquitetura e design dependerá desses objetivos.
    
    Identificar quem consumirá a arquitetura, que pode ser utilizado por outros arquitetos ou por desenvolvedores e testadores, equipes de operações ou gerenciamento, a finalidade é tornar o design da arquitetura o mais acessível para o público, isso inclui interatividade e necessidades do público em relação a arquitetura.
    
    Identificar restrições, seja de tecnologia, restrições de uso e restrições de implementação, a fim de não perder tempo no futuro durante o processo de desenvolvimento do software.
    
    Definição do escopo e tempo, baseando-se nos objetivos da arquitetura, entre as atividades que ajudam a definir o escopo e tempo temos: criação do design completo do sistema, construção de um protótipo, identificação dos principais riscos técnicos, testar opções possíveis e construção de modelos compartilhados para entendimento do sistema por parte dos colaboradores.

* ***2º Passo***: Identificar os cenários mais importantes

    Os principais cenários são aqueles considerados os cenários mais importantes para o sucesso do sistema a ser desenvolvido, ou sejam os cenários que entregam valor ao cliente.
    
    Evitar riscos.
    
    Identificar se a arquitetura escolhida tem um peso significativo do projeto.


* ***3º Passo***: Criar uma visão geral do sistema

    Rascunho das principais relações do sistema, como por exemplo: client -> web server -> data server.

* ***4º Passo***: Identificar as questões/problemas mais importantes

    Identificar as necessidades do sistema como um todo, como por exemplo: desempenho, segurança, escalabilidade, capacidade de manutenção, reutilização e usabilidade.

* ***5º Passo***: Definir as hipóteses de solução (criação da solução candidata)

    Criação do protótipo de arquitetura baseando-se nos principais cenários

## ***PADRÃO ARQUITETURAL***

É uma solução genérica e reutilizável para um tipo comum de problema na estrutura de um sistema de software estando mais voltado para a organização interna de um único sistema, sobre como os componentes se comunicam dentro de uma aplicação. Ou seja, são formas de estruturar o código dentro de um sistema.

    Exemplos:
    
    * Arquitetura em camadas (Apresentação → Negócio → Dados)
    * MVC (Model-View-Controller)

## ***MODELO ARQUITETURAL***

Um modelo arquitetural descreve um estilo de organização de todo o sistema, incluindo como os módulos (ou serviços) se dividem, se comunicam e são implantados, estando mais voltado para o sistema como um todo gerenciando a distribuição, independência, escalabilidade e a comunicação entre as partes que compõem o sistema. Ou seja, são formas de estruturar e distribuir o sistema inteiro (não só o código, mas também a forma como ele roda e interage com outros sistemas).

    Exemplos:
    
    * Microsserviços
    * Arquitetura orientada a serviços (SOA)

## ***CONCLUSÃO***

O modelo arquitetural é o tipo de construção: prédio comercial, prédio residencial, condomínio de casas, e o  padrão arquitetural é como os cômodos de cada unidade são organizados: sala na frente, quartos nos fundos, cozinha no meio, etc, sendo que o melhor modelo e padrão são definidos através da abstração do projeto de software, dispondo das técnicas de definição de arquitetura.


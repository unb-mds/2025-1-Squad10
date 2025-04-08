# O que é React?

React é uma biblioteca para a criação de interfaces de usuário. Atualmente, é uma das principais ferramentas utilizadas no desenvolvimento web moderno.

Oficialmente é mantido pelo Facebook, com manutenção feita por uma equipe de 8 pessoas. É utilizado em grandes projetos como o próprio Facebook, Twitter, WhatsApp e até mesmo na Netflix.

Foi criado por um engenheiro do Facebook e, inicialmente, era usado apenas internamente. Em 2013, o projeto foi anunciado como Open Source.

---

O React é uma das principais ferramentas de desenvolvimento **front-end**. Em resumo, o React é extremamente eficiente, pois permite compor interfaces completas a partir de pequenos e isolados pedaços de código.

---

## 📦 Setup básico de uma aplicação React

Para iniciar uma aplicação React, é necessário importar duas bibliotecas principais:

- **React DOM**: faz a ligação entre o React e os elementos da página, ou seja, o DOM.
- **React**: contém as funcionalidades principais, como criação de elementos, manipulação de estados, entre outras.

Essas funcionalidades são o que fazem o React ser tão poderoso e popular no desenvolvimento de interfaces web modernas.

## 👋 Exemplo básico: Hello World em React
```html
<!DOCTYPE html>
<html>
<head>
  <title>CDFTV – React</title>

  <!-- Importa o React -->
  <script src="https://unpkg.com/react@16/umd/react.production.min.js" crossorigin></script>

  <!-- Importa o ReactDOM, que faz a ligação com o DOM da página -->
  <script src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js" crossorigin></script>

  <!-- Importa o Babel, que converte JSX em JavaScript puro no navegador -->
  <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
</head>
<body>

  <!-- Div onde o conteúdo React será exibido -->
  <div id="app"></div>

  <!-- Script com JSX que será interpretado pelo Babel -->
  <script type="text/babel">
    ReactDOM.render(
      <h1>Hello CDF!</h1>,
      document.querySelector('#app')
    );
  </script>

</body>
</html>

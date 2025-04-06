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

```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return <h1>Hello, world!</h1>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);


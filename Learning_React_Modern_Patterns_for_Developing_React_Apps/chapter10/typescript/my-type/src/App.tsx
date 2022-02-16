import React from 'react';
import logo from './logo.svg';
import './App.css';

function App(props: AppProps) {
  return (
    <div>
      <h1>{props.item}</h1>
    </div>
  );
}

export default App;

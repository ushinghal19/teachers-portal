import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import LoginPage from './components/login/LoginPage.js'
import Dashboard from './components/dashboard/Dashboard';
import Dashboard_test from './components/dashboard/Dashboard_test.js';
import Dropdown from './components/dashboard/Dropdown';

ReactDOM.render(
  <React.StrictMode>
    <Dashboard_test/>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

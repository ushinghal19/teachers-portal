import logo from './logo.svg';
import './App.scss';
import Login from './components/login/Login.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <Login/>
      <p>
        Not part of the component
      </p>
    </div>
  );
}

export default App;

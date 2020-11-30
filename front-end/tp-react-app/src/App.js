import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import './App.scss';
import Dashboard from "./components/dashboard/Dashboard";
import LoginPage from "./components/login/LoginPage"

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/' component = {LoginPage}/>
          <Route exact path='/dashboard' component = {Dashboard}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

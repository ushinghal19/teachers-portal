import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import './App.scss';
import Dashboard from "./components/dashboard/Dashboard";
import LoginPage from "./components/login/LoginPage";
import Dropdown from "./components/dashboard/Dropdown";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path='/' component = {LoginPage}/>
          <Route exact path='/dashboard' component = {Dropdown}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;

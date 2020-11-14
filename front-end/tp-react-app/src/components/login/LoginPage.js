import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './LoginPage.scss'
import LoginForm from './Login.js'

class LoginPage extends Component {
    render() {
        return (
        <div className="LoginPage">
            <header className="tp-head">
                <h1>Hypatia Teacher's Portal</h1>
            </header>
            <br/>
            <LoginForm/>
        </div>
    );
    }
}
export default LoginPage;
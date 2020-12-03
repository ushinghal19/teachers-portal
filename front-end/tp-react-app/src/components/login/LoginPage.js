import React, { Component } from 'react';
import './LoginPage.scss'
import LoginForm from './Login.js'
import wave from '../../assets/wave.svg'

class LoginPage extends Component {
    render() {
        return (
        <div className="LoginPage">
            <img src={wave} className="Login-wave" alt="waves" />
            <header className="tp-head">
                <h1>hypatia Teacher's Portal</h1>
            </header>
            <br/>
            <LoginForm/>
            
        </div>
    );
    }
}
export default LoginPage;
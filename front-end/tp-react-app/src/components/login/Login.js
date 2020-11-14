import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.scss'

class Login extends Component {
    render() {
        return (
            <div className='LoginBox'>
                <div className="LoginContent">
                    <h1>Teacher Login</h1>
                    <p>Username: </p>
                    
                    <p>Password: </p>

                </div>
            </div>
        );
    }
}

export default Login;


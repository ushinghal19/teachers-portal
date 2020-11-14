import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Login.scss'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';



class Login extends Component {
    render() {
        return (
            <div className='LoginBox'>
                <div className="LoginContent">
                    <h1 className="loginHead">Teacher Login</h1>
                    <Form className="loginForm">
                        <Form.Group controlId="loginUsername">
                            <Form.Label className="formLabel">Username</Form.Label>
                            <Form.Control type="username" placeholder="Username" />
                        </Form.Group>

                        <Form.Group controlId="loginPassword">
                            <Form.Label className="formLabel">Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" />
                        </Form.Group>

                        <Button size="lg" variant="success" type="login">
                            Login
                        </Button>
                    </Form>
                </div>
            </div>
        );
    }
}

export default Login;


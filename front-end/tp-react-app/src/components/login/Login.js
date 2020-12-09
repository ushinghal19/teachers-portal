import React, { Component } from 'react';
import './Login.scss'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import {Redirect} from 'react-router-dom';

class Login extends Component {
    // this component is the login box used on the LoginPage
    constructor(props) {
        // State for login component:
        // username: store the username inputted
        // password: store the password inputted
        // successfulLogin: boolean for if login was valid
		super(props);
		this.state = {
          username: "",
          password: "",
          successfulLogin: false
		};
	  }
	
    handleFormChange = (e, key) => {
        // handle the username and password state
        this.setState({[key]: e.target.value});
    }

    handleFormSubmit = e => {
        // TODO: handle login verification

        // if not successful (api returns 400 error):
        // render in an error message for user

        // if login successful redirect to dashboard
        e.preventDefault();
        this.setState({ successfulLogin: "/dashboard"});
    }

    render() {
        if (this.state.successfulLogin){
            return <Redirect to={this.state.successfulLogin}/>
        }
        return (
            <div className='LoginBox'>
                <div className="LoginContent">
                    <h1 className="loginHead">Teacher Login</h1>
                    <Form className="loginForm" onSubmit = {e => this.handleFormSubmit(e)}>
                        <Form.Group controlId="loginUsername">
                            <Form.Label className="formLabel">Username</Form.Label>
                            <Form.Control type="username" placeholder="Username" onChange = {e => this.handleFormChange(e, 'username')}/>
                        </Form.Group>

                        <Form.Group controlId="loginPassword">
                            <Form.Label className="formLabel">Password</Form.Label>
                            <Form.Control type="password" placeholder="Password" onChange= {e => this.handleFormChange(e, 'password')}/>
                        </Form.Group>

                        <Button size="lg" variant="success" type="submit">
                            Login
                        </Button>
                    </Form>
                </div>     
            </div>
        );
    }
}

export default Login;


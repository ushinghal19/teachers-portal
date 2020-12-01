import React, { Component } from 'react';
import './Login.scss'
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import {Redirect} from 'react-router-dom';

class Login extends Component {
    constructor(props) {
		super(props);
		this.state = {
          username: "",
          password: "",
          successfulLogin: false
		};
	  }
	
    handleFormChange = (e, key) => {
        this.setState({[key]: e.target.value});
    }

    handleFormSubmit = (e) => {
        //if not successful (api returns 401 or 400 error I think):

        //render in an error message

        //if login successful:
        e.preventDefault();
        this.setState({ successfulLogin: "/dashboard"});
    }

    render() {
        if (this.state.successfulLogin){
            return <Redirect to={this.state.successfulLogin} />
        }
        return (
            <div className='LoginBox'>
                <div className="LoginContent">
                    {this.state.username}
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


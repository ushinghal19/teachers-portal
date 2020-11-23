import React, { Component } from 'react';
import './LeastErrors.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class LeastErrors extends Component {
    render() {
        const student1 = this.props.student1; // TODO: Figure out what the input type is (list, dict, string, tuple)
        return (
            <div className='least-error-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Students With Least Errors</div>
                <div className="least-errors">
                    <ListGroup variant="flush">
                        <ListGroup.Item>{student1}</ListGroup.Item>
                        <ListGroup.Item>{student1}</ListGroup.Item>
                        <ListGroup.Item>{student1}</ListGroup.Item>
                    </ListGroup>
                </div>
            </div>
        );
    }
}

export default LeastErrors;
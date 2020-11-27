import React, { Component } from 'react';
import './MostErrors.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class MostErrors extends Component {
    render() {
        const student1 = this.props.student1; // TODO: Figure out what the input type is (list, dict, string, tuple)
        return (
            <div className='most-error-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Most Errors</div>
                <div className="most-errors">
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

export default MostErrors;
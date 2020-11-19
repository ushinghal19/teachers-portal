import React, { Component } from 'react';
import './AverageTime.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class TotalErrors extends Component {
    render() {
        const student1 = this.props.student1; // TODO: Figure out what the input type is (list, dict, string, tuple)
        return (
            <div className='average-time-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Students With Most Errors</div>
                <div className="average-time">
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

export default TotalErrors;
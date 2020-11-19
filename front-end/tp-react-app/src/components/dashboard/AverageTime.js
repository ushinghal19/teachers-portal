import React, { Component } from 'react';
import './AverageTime.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class AverageTime extends Component {
    render() {
        const averageTime = this.props.averageTime; // TODO: Figure out what the input type is (list, dict, string, tuple)
        return (
            <div className='average-time-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Average Time Taken</div>
                <div className="average-time">
                    On average, students took {averageTime} minutes
                </div>
            </div>
        );
    }
}

export default TotalErrors;
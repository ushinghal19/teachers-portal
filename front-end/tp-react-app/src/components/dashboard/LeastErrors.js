import React, { Component } from 'react';
import './LeastErrors.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class LeastErrors extends Component {
    constructor(props) {
        super(props);
        this.state = {
            students: this.props.students,
        };
    }
    render() {
        //const student1 = this.props.student1; // TODO: Figure out what the input type is (list, dict, string, tuple)
        //console.log(Object.keys(this.state.students));
        return (
            <div className='least-error-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Students With Least Errors</div>
                <div className="least-errors">
                    <ListGroup variant="flush">
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students)[0]}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students)[0]]}</p></ListGroup.Item>
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students)[1]}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students)[1]]}</p></ListGroup.Item>
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students)[2]}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students)[2]]}</p></ListGroup.Item>
                    </ListGroup>
                </div>
            </div>
        );
    }
}

export default LeastErrors;

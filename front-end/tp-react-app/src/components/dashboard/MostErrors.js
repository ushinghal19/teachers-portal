import React, { Component } from 'react';
import './MostErrors.scss'
import '../login/LoginPage.scss'
import ListGroup from 'react-bootstrap/ListGroup'

class MostErrors extends Component {
    constructor(props) {
        super(props);
        this.state = {
            students: this.props.students,
        };
    }
    render() {
        //const students = this.props.students; // TODO: Figure out what the input type is (list, dict, string, tuple)
        return (
            <div className='most-error-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Students With Most Errors</div>
                <div className="most-errors">
                    <ListGroup variant="flush">
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students).slice(-1)}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students).slice(-1)]}</p></ListGroup.Item>
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students).slice(-2,-1)}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students).slice(-2,-1)]}</p></ListGroup.Item>
                        <ListGroup.Item><p style={{float: "left"}}>{Object.keys(this.state.students).slice(-3,-2)}</p><p style={{float: "right"}}>{this.state.students[Object.keys(this.state.students).slice(-3,-2)]}</p></ListGroup.Item>
                    </ListGroup>
                </div>
            </div>
        );
    }
}

export default MostErrors;

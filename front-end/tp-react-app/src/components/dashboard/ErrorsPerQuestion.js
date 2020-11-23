import React, { Component } from 'react';
import './ErrorsPerQuestion.scss'
import '../login/LoginPage.scss'

class ErrorsPerQuestion extends Component {
    render() {
        return (
            <div className='errors-per-question-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Errors Per Question</div>
                    <div className="errors-per-question">
                        Graph here
                    </div>
            </div>
        );
    }
}

export default ErrorsPerQuestion;
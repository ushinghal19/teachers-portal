import React, { Component } from 'react';
import './TotalErrors.scss'
import '../login/LoginPage.scss'
import ErrorIcon from 'react-bootstrap-icons/dist//icons/exclamation-triangle-fill';

class TotalErrors extends Component {
    render() {
        const numErrors = this.props.numErrors;
        return (
            <div className='total-error-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Total Errors</div>
                <div className="total-errors"><ErrorIcon size={55} color="#FFC107"/> {numErrors}</div>
            </div>
        );
    }
}

export default TotalErrors;

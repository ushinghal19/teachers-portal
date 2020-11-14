import React, { Component } from 'react';
import './TotalErrors.scss'

class TotalErrors extends Component {
    render() {
        const numErrors = this.props.numErrors;
        return (
            <div className='total-error-box'>
                Total Errors
                Icon {numErrors}
            </div>
        );
    }
}

export default TotalErrors;

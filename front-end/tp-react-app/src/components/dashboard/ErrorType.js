import React, { Component } from 'react';
import './ErrorType.scss'
import '../login/LoginPage.scss'

class ErrorType extends Component {
    render() {
        return (
            <div className='error-type-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Error Type</div>
                    <div className="error-type">
                        Legend {/*victory comes with its own legend*/}
                    </div>
            </div>
        );
    }
}

export default ErrorType;
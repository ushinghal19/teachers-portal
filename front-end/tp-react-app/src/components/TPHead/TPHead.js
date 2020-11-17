import React, { Component } from 'react';
import './TPHead.scss'
import '../login/LoginPage.scss'

class TPHead extends Component {
    render() {
        return (
            <div className="tp-head tp-navbar" style={{fontSize: 35,}}>
                Teacher's Portal
            </div>
        );
    }
}

export default TPHead;
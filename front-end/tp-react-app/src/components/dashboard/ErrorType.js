import React, { Component } from 'react';
import './ErrorType.scss'
import '../login/LoginPage.scss'
import * as V from 'victory';

function makeDataUsable(data){
    let newList = []
    for (const key in data) {
      let newObj = {}
      newObj.x = key
      newObj.y = data[key]
      newList.push(newObj)
    }
    return(newList)
}

class ErrorType extends Component {
    constructor(props) {
        super(props);
        this.state = {
            errorTypes: this.props.errorTypes,
        };
    }
    render() {
        return (
            <div className='error-type-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Error Type</div>
                    <div className="error-type">
                    <V.VictoryPie
                          data={makeDataUsable(this.state.errorTypes)}
                          colorScale={"cool"}
                          labels={({ datum }) => datum.x + " : " + datum.y}
                          innerRadius={100}
                    />
                    </div>
            </div>
        );
    }
}

export default ErrorType;
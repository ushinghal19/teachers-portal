import React, { Component } from 'react';
import './ErrorType.scss'
import '../login/LoginPage.scss'
import * as V from 'victory';

const data = {"LogicError":23, "MathError":17, "ChessError":5, "CodeError":15}

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
    render() {
        return (
            <div className='error-type-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Error Type</div>
                    <div className="error-type">
                    <V.VictoryPie
                          data={makeDataUsable(data)}
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
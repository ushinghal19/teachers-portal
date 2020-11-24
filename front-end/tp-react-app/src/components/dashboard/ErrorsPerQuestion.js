import React, { Component } from 'react';
import './ErrorsPerQuestion.scss'
import '../login/LoginPage.scss'
import * as V from 'victory';

const data = [  {1: 5}, 
                {2: 3},
                {3: 2},
                {4: 7},
                {5: 10},
                {6: 1},
                {7: 4},
                {8: 12},
                {9: 3},
                {10: 6},]


function makeDataUsable(data){
    let newObj = [{"x":0, "y":0}];
    for(let i=0; i<data.length; i++){
        newObj.push({"x":parseInt(Object.keys(data[i])[0]), "y":data[i][parseInt(Object.keys(data[i])[0])]});
    }
    return(newObj);
}


function getTicks(data){
    let newObj = [];
    for(let i=0; i<=data.length+1; i++){
        newObj.push(i);
    }
    return(newObj);
}

class ErrorsPerQuestion extends Component {
    render() {
        return (
            <div className='errors-per-question-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Errors Per Question</div>
                    <div className="errors-per-question-chart">
                    <V.VictoryChart
                        theme={V.VictoryTheme.material}
                        domainPadding={10}  
                        width={1000}
                    >
                    <V.VictoryAxis crossAxis
                        width={400}
                        height={400}
                        domain={[0, 8]}
                        theme={V.VictoryTheme.material}
                        style={{
                            axisLabel: {fontSize: 20, padding: 30},
                            ticks: {stroke: "grey", size: 5},
                            tickLabels: {fontSize: 15, padding: 4},
                        }}
                        tickValues = {getTicks(data)}
                        label = "Question Number"
                    />
                    <V.VictoryAxis dependentAxis crossAxis
                        width={400}
                        height={400}
                        domain={[0, 8]}
                        theme={V.VictoryTheme.material}
                        style={{
                            axisLabel: {fontSize: 20, padding: 30},
                            ticks: {stroke: "grey", size: 5},
                            tickLabels: {fontSize: 15, padding: 4},
                        }}

                        label = "Number of Errors"
                    />
                        <V.VictoryBar
                            data={makeDataUsable(data)}
                            animate={{
                                duration: 4000,
                                onLoad: { duration: 1500 }
                              }}
                            barRatio={.5}
                            labels={({ datum }) => `${Math.round(datum.y)}`}
                        />
                    </V.VictoryChart>

                 </div>
            </div>
        );
    }
}

export default ErrorsPerQuestion;
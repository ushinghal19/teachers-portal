import React, { Component } from 'react';
import './ErrorsPerQuestion.scss'
import '../login/LoginPage.scss'
import * as V from 'victory';


function makeDataUsable(data){
    let newList = [{x:0, y:0}];
    for(const key in data) {
        let newObj={}
        newObj.x = parseInt(key)
        newObj.y = data[key]
        newList.push(newObj)
    }
    return(newList)
}


function getTicks(data){
    let newObj = [];
    for(const key in data){
        newObj.push(key);
    }
    return(newObj);
}


class ErrorsPerQuestion extends Component {
    render() {
        const problemErrors = this.props.problemErrors;
        return (
            <div className='errors-per-question-box'>
                <div className="tp-head" style={{fontSize: 35,}}>Errors Per Question</div>
                    <div className="errors-per-question-chart">
                    <V.VictoryChart
                        theme={V.VictoryTheme.material}
                        domainPadding={10}  
                        width={1000}
                        minDomain={{ x: 0 }}
                    >
                    <V.VictoryAxis crossAxis
                        width={400}
                        height={400}
                        // domain={[0, 8]}
                        theme={V.VictoryTheme.material}
                        style={{
                            axisLabel: {fontSize: 20, padding: 30},
                            ticks: {stroke: "grey", size: 5},
                            tickLabels: {fontSize: 15, padding: 4},
                        }}
                        tickValues = {getTicks(problemErrors)}
                        label = "Question Number"
                    />
                    <V.VictoryAxis dependentAxis crossAxis
                        width={400}
                        height={400}
                        // domain={[0, 8]}
                        theme={V.VictoryTheme.material}
                        style={{
                            axisLabel: {fontSize: 20, padding: 50},
                            ticks: {stroke: "grey", size: 5},
                            tickLabels: {fontSize: 15, padding: 4},
                        }}

                        label = "Number of Errors"
                    />
                        <V.VictoryBar
                            data = {makeDataUsable(problemErrors)}
                            animate={{
                                duration: 4000,
                                onLoad: { duration: 1500 }
                              }}
                            barRatio={.5}
                            labels={({ datum }) => `${Math.round(datum.y)}`}
                            style={{ data: { fill: "#17A2B8" } }}
                        />
                    </V.VictoryChart>

                 </div>
            </div>
        );
    }
}

export default ErrorsPerQuestion;
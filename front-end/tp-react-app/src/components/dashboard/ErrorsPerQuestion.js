import React, { Component } from 'react';
import './ErrorsPerQuestion.scss'
import '../login/LoginPage.scss'
import * as V from 'victory';

const data = [{"Question Number": 0, "Number of Errors": 0},
                {"Question Number": 1, "Number of Errors": 5}, 
                {"Question Number": 2, "Number of Errors": 3},
                {"Question Number": 3, "Number of Errors": 2},
                {"Question Number": 4, "Number of Errors": 7},
                {"Question Number": 5, "Number of Errors": 2},
                {"Question Number": 6, "Number of Errors": 1},
                {"Question Number": 7, "Number of Errors": 4},
                {"Question Number": 8, "Number of Errors": 5}]

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
                        <V.VictoryAxis
                            style={{
                                grid: { stroke: "#818e99", strokeWidth: 0.5 },
                            }}
                        />
                        <V.VictoryBar
                            style={{ data: { fill: "#c43a31" } }}
                            data={data}
                            x = "Question Number"
                            y = "Number of Errors"
                            animate={{
                                duration: 4000,
                                onLoad: { duration: 1500 }
                              }}
                            barRatio={.5}
                        />
                        </V.VictoryChart>
  }}
                 </div>
            </div>
        );
    }
}

export default ErrorsPerQuestion;
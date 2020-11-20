import React, {Component} from 'react'
import './Dashboard.scss'
import '../login/LoginPage.scss'
import TotalErrors from './TotalErrors.js'
import LeastErrors from './LeastErrors.js'
import MostErrors from './MostErrors.js'
import ErrorsPerQuestion from './ErrorsPerQuestion.js'
import ErrorType from './ErrorType.js'
import AverageTime from './AverageTime.js'
import TPHead from '../TPHead/TPHead.js'

class Dashboard extends Component{
	render(){
		return(
			<div className = 'dashboard-box'>
				<header><TPHead/></header>
				<div className='tp-head' style={{fontSize: 45, textAlign: 'left', alignSelf: 'stretch'}}>Assignment 1</div>
				<TotalErrors numErrors="32"/>
				<LeastErrors student1 = "Utsav"/>
				<MostErrors student1="Utsav"/>
				<ErrorsPerQuestion/>
				<ErrorType/>
				<AverageTime/>
			</div>
		);
	}
}

export default Dashboard;
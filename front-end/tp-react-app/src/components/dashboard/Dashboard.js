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
			<div className = 'dashboard-page'>
				<header><TPHead/></header>
				<div className = 'dashboard-box'>
					<div className='tp-head' style={{fontSize: 45, textAlign: 'left', alignSelf: 'stretch'}}>Assignment 1</div>
					<div className='dashboard-content'>
						<div className='row one'>
							<div className='col one'><TotalErrors numErrors="32"/></div>
							<div className='col two'><LeastErrors student1 = "Utsav"/></div>
							<div className='col two'><MostErrors student1="Utsav"/></div>
						</div>
						<div className='row two'>
							<div className='col one' ><ErrorsPerQuestion/></div>
						</div>
						<div className='row three'>
							<div className='col one'><ErrorType/></div>
							<div className='col one'><AverageTime/></div>
						</div>
					</div>
				</div>
			</div>
		);
	}
}

export default Dashboard;
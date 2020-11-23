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
		getAssignmentStats(321);
		return(
			<div className = 'dashboard-page'>
				<header><TPHead/></header>
				<div className = 'dashboard-box'>
					<div className='tp-head' style={{fontSize: 45, textAlign: 'left', alignSelf: 'stretch'}}>Assignment 1</div>
					<div className='dashboard-content'>
						<div className='box-1'><TotalErrors numErrors="32"/></div>
						<div className='box-2'><LeastErrors student1 = "Utsav"/></div>
						<div className='box-3'><MostErrors student1="Utsav"/></div>
						<div className='box-4'><ErrorsPerQuestion/></div>
						<div className='box-5'><ErrorType/></div>
						<div className='box-6'><AverageTime/></div>
					</div>
				</div>
			</div>
		);
	}
}

const URL = 'http://127.0.0.1:8000/graphql'
function getAssignmentStats(id){
	fetch(URL, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json'},
		body: JSON.stringify({ query: 'getAssignmentStats($id: ID!){assignment(id: $id){studentsByErrors,typeOfErrors,problemErrors,aggregateErrors}}',
								variables: {"id": id}
		}),
	  })
	  .then(res => res.json())
	  .then(res => console.log(res.data));
}

export default Dashboard;
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

const URL = 'http://localhost:8000/graphql';
let statistics = {assignment: {}};
function getAssignmentStats(id){
	fetch(URL, {
		method: 'POST',
		// credentials: "same-origin",
		headers: {
			"Accept": "application/json",
			"Referer": "http://localhost:3000",
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ query: 'query getAssignmentStats($id: ID!){assignment(id: $id){studentsByErrors,typeOfErrors,problemErrors,aggregateErrors}}',
			variables: {"id": id},
			operationName: "getAssignmentStats",
		}),
	})
		.then(res => res.json())
		.then(res => {statistics = res.data;
						return res})
		.then(res => console.log(res.data))
		.then(() => console.log(statistics.assignment.problemErrors));
}

// function getCookie(name) {
// 	var cookieValue = null;
// 	if (document.cookie && document.cookie !== '') {
// 		var cookies = document.cookie.split(';');
// 		for (var i = 0; i < cookies.length; i++) {
// 			var cookie = jQuery.trim(cookies[i]);
// 			// Does this cookie string begin with the name we want?
// 			if (cookie.substring(0, name.length + 1) === (name + '=')) {
// 				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
// 				break;
// 			}
// 		}
// 	}
// 	return cookieValue;
// }

class Dashboard extends Component{
	render(){
		getAssignmentStats(123)
		return(
			<div className = 'dashboard-page'>
				<header><TPHead/></header>
				<div className = 'dashboard-box'>
					<div className='tp-head' style={{fontSize: 45, textAlign: 'left', alignSelf: 'stretch', color: '#252525'}}>Assignment 1</div>
					<div className='dashboard-content'>
						<div className='box-1'><TotalErrors numErrors = {statistics.assignment.aggregateErrors}/></div>
						<div className='box-2'><LeastErrors student1 = 'Utsav'/></div>
						<div className='box-3'><MostErrors student1 = 'Utsav'/></div>
						{/* <div className='box-4'><ErrorsPerQuestion/></div> */}
						<div className='box-5'><ErrorType/></div>
						<div className='box-6'><AverageTime/></div>
					</div>
				</div>
			</div>
		);
	}
}

export default Dashboard;
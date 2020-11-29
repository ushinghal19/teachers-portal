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

class Dashboard extends Component{
	// Use forceupdate for button: https://reactjs.org/docs/react-component.html#forceupdate 
	constructor(props) {
		super(props);
		this.state = {
		  error: null,
		  isLoaded: false,
		  statistics: {assignment: {}},
		  id: 321
		};
	  }
	
	getAssignmentStats(id){
		fetch(URL, {
			method: 'POST',
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
			.then((result) => {
								this.setState({
									isLoaded: true,
									statistics: result.data
								});
							},
							(error) => {
								this.setState({
								  isLoaded: true,
								  error
								});
							  }
			)
	}

	componentDidMount() {
		this.getAssignmentStats(this.state.id)
	}


	render(){
		const { error, isLoaded, statistics } = this.state;
		if (error) {
		return <div>Error: {error.message}</div>;
		} else if (!isLoaded) {
		return <div>Loading...</div>;
		} else {
			console.log(statistics.assignment);
		return(
			<div className = 'dashboard-page'>
				<header><TPHead/></header>
				<div className = 'dashboard-box'>
					<div className='tp-head' style={{fontSize: 45, textAlign: 'left', alignSelf: 'stretch', color: '#252525'}}>Assignment 1</div>
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
}

export default Dashboard;
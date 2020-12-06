import React, {Component} from 'react'
// styling imports
import './Dashboard.scss'
import '../login/LoginPage.scss'
// dashboard components
import TotalErrors from './TotalErrors.js'
import LeastErrors from './LeastErrors.js'
import MostErrors from './MostErrors.js'
import ErrorsPerQuestion from './ErrorsPerQuestion.js'
import ErrorType from './ErrorType.js'
import AverageTime from './AverageTime.js'
// loading animation
import { css } from '@emotion/core'
import RingLoader from 'react-spinners/RingLoader'
// refresh button
import Button from 'react-bootstrap/Button'
import { ArrowRepeat } from 'react-bootstrap-icons'

const URL = 'http://localhost:8000/graphql';

class Dashboard extends Component{
	constructor(props) {
		super(props);
		
		// State of dashboard component:
		// error: used to store any potential errors during fetch function
		// isLoaded: boolean for storing True when API results are returned
		// statistics: object used to store the API results
		// id: used to store the assignment id to make the API request
		this.state = {
		  error: this.props.error,
		  isLoaded: this.props.isLoaded,
		  statistics: this.props.statistics,
		  id: this.props.id
		};
	  }
	
	getAssignmentStats(id){
		// function to set the statistics prop to results from API
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
									// handle succesful API call
									isLoaded: true,
									statistics: result.data
								});
							},
							(error) => {
								// handle unsuccessful API call by return the error recieved
								this.setState({
								  isLoaded: true,
								  error
								});
							  }
			)
	}

	componentDidMount() {
		// make API call when components load
		this.getAssignmentStats(this.state.id)
	}

	handleRefresh = e => {
		// handle refresh button click
		e.preventDefault();
		this.setState({isLoaded: false});
		this.getAssignmentStats(this.state.id);
	};

	render(){
		const { error, isLoaded, statistics } = this.state;
		if (error) {
		return <div>Error: {error.message}</div>;
		} else if (!isLoaded) {
			// handle loading screen
			const loader = css`
				display: block;
				margin: 0 auto;
				border-color: red;
			`;
			return (
					<div className='loading-page'>
						<Button className='refresh-button' size='lg' variant="info" onClick={e => this.handleRefresh(e)}>Refresh <ArrowRepeat size={25}/></Button>
						<RingLoader 
							css={loader}
							size={400}
							color={"#1FB299"}/>
						<br/>
						<div className='tp-head' style={{fontSize: 45, alignSelf: 'stretch', color: '#252525'}}>Loading data...</div>
					</div>
			);
		} else {
			// everything is successful, display the data
		return(
			<div className = 'dashboard-page'>
				<Button className='refresh-button' size='lg' variant="info" onClick={e => this.handleRefresh(e)}>Refresh <ArrowRepeat size={25}/></Button>
				<div className = 'dashboard-box'>
					<div className='dashboard-content'>
						
						<div className='row one'>
							<div className='col one'><TotalErrors numErrors = {statistics.assignment.aggregateErrors}/></div>
							<div className='col two'><LeastErrors students = {statistics.assignment.studentsByErrors}/></div>
							<div className='col two'><MostErrors students = {statistics.assignment.studentsByErrors}/></div>
						</div>

						<div className='row two'>
							<div className='col one' ><ErrorsPerQuestion problemErrors= {statistics.assignment.problemErrors}/></div>
						</div>
						
						<div className='row three'>
							<div className='col one'><ErrorType errorTypes = {statistics.assignment.typeOfErrors}/></div>
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
import React, {Component} from 'react'
import './Dashboard.scss'
import '../login/LoginPage.scss'
import TotalErrors from './TotalErrors.js'
import LeastErrors from './LeastErrors.js'
import MostErrors from './MostErrors.js'
import ErrorsPerQuestion from './ErrorsPerQuestion.js'
import ErrorType from './ErrorType.js'
import AverageTime from './AverageTime.js'
import RingLoader from 'react-spinners/RingLoader'
import { css } from '@emotion/core'

const URL = 'http://localhost:8000/graphql';

class Dashboard extends Component{
	// Use forceupdate for button: https://reactjs.org/docs/react-component.html#forceupdate 
	constructor(props) {
		super(props);
		this.state = {
		  error: this.props.error,
		  isLoaded: this.props.isLoaded,
		  statistics: this.props.statistics,
		  id: this.props.id
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
			const loader = css`
				display: block;
				margin: 0 auto;
				border-color: red;
			`;
			return (
					<div className='loading-page'>
						<RingLoader 
							css={loader}
							size={400}
							color={"#1FB299"}/>
						<br/>
						<div className='tp-head' style={{fontSize: 45, alignSelf: 'stretch', color: '#252525'}}>Loading data...</div>
					</div>
			);
		} else {
			//add conditionals to check which are empty, set var and call it bellow
		return(
			<div className = 'dashboard-page'>
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
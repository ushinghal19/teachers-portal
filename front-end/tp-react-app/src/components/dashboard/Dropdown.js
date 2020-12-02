import React, {Component} from 'react'
import Select from 'react-select'
import './Dropdown.scss'
import Dashboard from './Dashboard.js'
import TPHead from '../TPHead/TPHead.js'

// GraphQL URL
const URL = 'http://localhost:8000/graphql';

// Style for Dropdown
// Font size is handled in .scss
const customStyles = {
  control: base => ({
    ...base, 
    height: 45, minHeight: 45
  })
}

class Dropdown extends Component{
    constructor(props) {
      super(props);
      this.state = {
        selectedOption: null,
        options: [],
        teacherId: '5fb6d6ce00c239d5bffb4b15',
      };
    }
    handleChange = selectedOption => {
        this.setState({ selectedOption });
      };

    getTeacherAssignments(id){
      fetch(URL, {
        method: 'POST',
        headers: {
          "Accept": "application/json",
          "Referer": "http://localhost:3000",
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: 'query getTeacherAssignments($id: ID!){teachers(id: $id){assignmentsBelow{assignmentId}}}',
          variables: {"id": id},
          operationName: "getTeacherAssignments",
        }),
      })
        .then(res => res.json())
        .then((result) => {
                  var TeacherAssignments = result.data.teachers[0].assignmentsBelow;
                  var allAssignments = [];
                  for (let i = 0; i < TeacherAssignments.length; i++) {
                    allAssignments.push({value: TeacherAssignments[i].assignmentId, label: "Assignment "+TeacherAssignments[i].assignmentId})
                    }
                    this.setState({options: allAssignments})
                },
                (error) => {
                  this.setState({
                    error
                  });
                  }
        )
    }
  
    componentDidMount() {
      this.getTeacherAssignments(this.state.teacherId)
    }
    
    render() {
      const { selectedOption } = this.state;
      let content;
      if (this.state.selectedOption == null) {
        content = <div className='null-option'><p>Please select an assignment to teacher statistics!</p></div>
      } else {
        content = <div className='some-option'>
                    <Dashboard error={null} isLoaded={false} statistics={{assignment: {}}} id={this.state.selectedOption}/>
                  </div>
      }
      return (
        <div className='dropdown-box'>
          <header><TPHead/></header>
          <div className='dropdown'>
            <Select
              styles={customStyles}
              placeholder={"Select an assignment..."}
              value={selectedOption}
              onChange={this.handleChange}
              options={this.state.options}
              isSearchable={true}
              isClearable={true}
            />
          </div>
          {content}
        </div>
      );
    }
}

export default Dropdown;
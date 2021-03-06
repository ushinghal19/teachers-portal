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
      
      // State of the dropdown:
      // selectedOption is currently selected assignment, defaults to null if none selected
      // options is array of assignment IDs in form {value: assignmentID, label: Assignment ???}
      this.state = {
        selectedOption: null,
        options: [],
        teacherId: '5fb6d6ce00c239d5bffb4b15',
      };
    }

    // Changes state of dropdown when different assignment selected
    handleChange = selectedOption => {
        this.setState({ selectedOption });
      };
    
    // Run query to fill dropdown options with assignments
    getTeacherAssignments(id){
      fetch(URL, {
        method: 'POST',
        headers: {
          "Accept": "application/json",
          "Referer": "http://localhost:3000",
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: 'query getTeacherAssignments($id: ID!){teachers(id: $id){assignmentsBelow{assignmentId,assignmentName}}}',
          variables: {"id": id},
          operationName: "getTeacherAssignments",
        }),
      })
        .then(res => res.json())
        .then((result) => {
                  var TeacherAssignments = result.data.teachers[0].assignmentsBelow;
                  var allAssignments = [];
                  for (let i = 0; i < TeacherAssignments.length; i++) {
                    var assignmentLabel = "Assignment "+TeacherAssignments[i].assignmentId;   // Set assignment name to the id nubmer
                    if (!TeacherAssignments[i].assignmentName==""){                           // If assignment has a name us it
                      assignmentLabel = TeacherAssignments[i].assignmentName;  
                    }
                    allAssignments.push({value: TeacherAssignments[i].assignmentId, label: assignmentLabel})
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
    
    // Fill dropdown options with assignments
    componentDidMount() {
      this.getTeacherAssignments(this.state.teacherId)
    }
    
    render() {
      const { selectedOption } = this.state;
      let content;
      if (this.state.selectedOption == null) {
        content = <div className='null-option'><p>Please select an assignment to view statistics!</p></div>
      } else {
        content = <div className='some-option'>
                    <Dashboard key={this.state.selectedOption.value} error={null} isLoaded={false} statistics={{assignment: {}}} id={this.state.selectedOption.value}/>
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
import React, {Component} from 'react'
import Select from 'react-select'
import './Dropdown.scss'
import Dashboard from './Dashboard.js'
import TPHead from '../TPHead/TPHead.js'

class Dropdown extends Component{
    constructor(props) {
      super(props);
      this.state = {
        selectedOption: null,
        options: [
          {value: '0', label: 'Test Assignment'},
        ],
        teacher_id: '5fb6d6ce00c239d5bffb4b15',
      };
    }
    handleChange = selectedOption => {
        this.setState({ selectedOption });
        console.log(`Option selected:`, selectedOption);
      };

    // content() {
    //   const select = this.state.selectedOption;
    //   if (select == null) {
    //     return <div>Please select an assignment to view statistics!</div>
    //   }
    // }

    getTeacherAssignments(id){
      fetch(URL, {
        method: 'POST',
        headers: {
          "Accept": "application/json",
          "Referer": "http://localhost:3000",
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: 'query getTeacherAssignments($id: ID!){teacher(id: $id){assignments_below}}',
          variables: {"id": id},
          operationName: "getTeacherAssignments",
        }),
      })
        .then(res => res.json())
        .then((result) => {
                  var x = result.data.teacher.assignments_below;
                  for (let i = 0; i < x.length; i++) {
                    this.setState(prevState => ({
                      objects: [...prevState.objects, {value: x[i].assignment_id, label: x[i].assignment_id}]
                    }));
                  }
                },
                (error) => {
                  this.setState({
                    error
                  });
                  }
        )
    }
  
    componentDidMount() {
      this.getTeacherAssignments(this.state.teacher_id)
    }
    
    render() {
      const { selectedOption } = this.state;
      let content;
      if (this.state.selectedOption == null) {
        content = <div className='null-option'><p>Please select an assignment to view statistics!</p></div>
      } else {
        content = <div className='some-option'>
                    <Dashboard error={null} isLoaded={false} statistics={{assignment: {}}} id={this.state.selectedOption}/>
                  </div>
      }
      return (
        <div>
          <header><TPHead/></header>
          <div className='dropdown'>
            <Select
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

export default Dropdown
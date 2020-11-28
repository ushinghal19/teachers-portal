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
        ]
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
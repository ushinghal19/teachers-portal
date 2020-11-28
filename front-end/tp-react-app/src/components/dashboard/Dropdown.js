import React, {Component} from 'react'
import Select from 'react-select'
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
    
    render() {
      const { selectedOption } = this.state;
      return (
        <div className='dropdown'>
          <header><TPHead/></header>
          <Select
            width='100px'
            value={selectedOption}
            onChange={this.handleChange}
            options={this.state.options}
            isSearchable={true}
            isClearable={true}
          />
        </div>
      );
    }
}

export default Dropdown
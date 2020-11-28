import React, {Component} from 'react'
import Select from 'react-select'

const options = [
];

class Dropdown extends Component{
    state = {
        selectedOption: null,
    };
    handleChange = selectedOption => {
        this.setState({ selectedOption });
        console.log(`Option selected:`, selectedOption);
      };
      render() {
        const { selectedOption } = this.state;
     
        return (
          <Select
            value={selectedOption}
            onChange={this.handleChange}
            options={options}
            isSearchable={true}
            isClearable={true}
          />
        );
      }
}

export default Dropdown
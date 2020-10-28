# Companion App Documentation

## Development Setup

### Requirements

* Python 3.8.5+
* The `pipenv` Python package
* Hypatia Desktop Application

### Instructions
1. Install Dependencies by navigating to the `companion-app` directory and then use the command
    ```
    pipenv install
    ```
    Other variations of this command, depending on your Python setup,
    are `python3 -m pipenv install` or `py -m pipenv install`.
    
2. Add the Hypatia API to the Hypatia App by going to Help > Add a Licence and
entering `api-tli-2020`. 

3. Start the server by executing 
    ```
   pipenv run default_websocket.py
    ```
    

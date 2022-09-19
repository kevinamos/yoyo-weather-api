# yoyo-weather-api

# Payments

The API Service provides a simple API to fetch weather data

The goal of this `README` is to:
1. Establish a common language to be used by engineers, product managers, and customer success 
2. Walk engineers through local setup without needing help from others


## Common Language 

This section establishes ubiquitous language that is accross all stakeholders.  
This language should be usable by both engineers in code and also other stakeholders.  

Min_temp:  
Minimum temperature.  

Max_temp:  
Maximum temperature.  

## Developer Guide

### Local setup and Running the project
Install Pipenv locally (Or your preferred virtualization library.)
cd into the project directory and run
Pipenv install

To run Unit tests, run the following command:
  pipenv run pytest weather_calculator/tests/tests.py
  sample response 
    Sample {"success": true, "error": false, "maximum": 22.3, "minimum": 18.1, "average": 20.56, "median": 20.85}



### System inputs and outputs


###System outputs to external services
- We make HTTP calls to https://www.weatherapi.com/ for all our weather information.

### Software architecture
  - To be added. 
#### Software structure requirements

Conform to the existing layered structure, and use the entities, statics, and repositories in the same manner as existing code.

__Logging__ 

__Test Strategies__ Main regression tests. 

# Learning Resources
https://www.weatherapi.com/docs/
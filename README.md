# yoyo-weather-api

# Overview

The API Service provides a simple API to fetch weather data.
Currently the API fetches historical weather data for a given city and returns
the min, max, median and average temperatures.

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
Ensure you have python 3.8 and above installed.
Install Pipenv locally (Or your preferred virtualization library).
cd into the project directory and run.
Pipenv install.

To run the api, run the following commands:
  - pipenv install
  - pipenv shell (assuming you are using pipenv
  - In the root folder of your project, create a .env file (touch .env).
  - Copy the following contents in your .env.
      weatherapi_api_key=<"YOUR WEATHERAPI KEY">.
      DJANGO-SECRET='COPY YOUR DJANGO SECRET HERE'
  - ./manage.py migrate
  - ./manage.py runserver

To run Unit tests, run the following command.
-pipenv run pytest weather_calculator/tests/tests.py.

-sample api  response:
  - {"success": true, "error": false, "maximum": 22.3, "minimum": 18.1, "average": 20.56, "median": 20.85}

- To fetch the data for London over past 9 days for instance (Assuming you are using port 8000
  -Head to your browser and access http://localhost:8000/api/locations/London/?days=9

### System inputs and outputs


###System outputs to external services
- We make HTTP calls to https://www.weatherapi.com/ for all our weather information.

### Software architecture
- A simple Python/Django APP that uses an external api to fetch city weather data.
  - More details to be added. 
#### Software structure requirements

Conform to the existing layered structure, and use the entities, statics, and repositories in the same manner as existing code.

__Logging__ Errors logged to help in troubleshooting common problems.

__Test Strategies__ Main regression tests. 

# Learning Resources
https://www.weatherapi.com/docs/
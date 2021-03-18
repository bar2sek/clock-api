# Simple Clock API

## Challenge

Create a simple web service that returns the current time as JSON data, such as:

`{ "currentTime": "24-01-2050 15:06:26" }`

Then create a client application that connects to the web service, parses the response, and displays the time.

Brian P. Hogan. Exercises for Programmers, P1.0 The Pragmatic Bookshelf, LLC.

## Proposed Solution

### _Web Service:_

- AWS Lambda running Python
    - get current local time
    - return a single key value pair in JSON format
    - **attempted deployment via Zappa but unable to use python 3.9**

### _Client Application:_

- Python script run locally
    - hit endpoint of the clock Lambda created above **have to run flask locally and hit localhost:5000**
    - convert the returned JSON to human readable string
    - return string for display to the user

### _CI/CD:_

- GitHub Actions
    - run tests for both client and web service python applications **(learn mocking for client tests)**
    - deploy all AWS services using CDK stack **(future enhancement)**

## How to install and run (currently)

- `git clone https://github.com/bar2sek/clock-api.git`
- `cd clock-api`
- `pip install -r requirements.txt`
- start flask server locally `python3 src/time_webservice.py`
- In another terminal run client app `python3 src/client_application.py`
# Simple Clock API

## Challenge

Create a simple web service that returns the current time as JSON data, such as:

`{ "currentTime": "2050-01-24 15:06:26" }`

Then create a client application that connects to the web service, parses the response, and displays the time.

Brian P. Hogan. Exercises for Programmers, P1.0 The Pragmatic Bookshelf, LLC.

## Proposed Solution

### _Web Service:_

AWS Lambda that returns a single key value pair in JSON format labeled "currentTime" with the time of day in Central Standard Time in the United States.

### _Client Application:_

Python script run locally to hit the time API Lambda endpoint created above, this converts the returned JSON to a nice human readable date and time in the console output complete with unit tests to ensure functions operate as intended.

### _CI/CD:_

GitHub Actions will run the tests for the client application as well as deploy the Lambda function via an AWS CDK stack.
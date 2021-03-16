# Simple Clock API

## Challenge

Create a simple web service that returns the current time as JSON data, such as:

`{ "currentTime": "2050-01-24 15:06:26" }`

Then create a client application that connects to the web service, parses the response, and displays the time.

Brian P. Hogan. Exercises for Programmers, P1.0 The Pragmatic Bookshelf, LLC.

## Proposed Solution

### _Web Service:_

- AWS Lambda running Python
    - get current time
    - convert time to Central Standard Time in the United States
    - return a single key value pair in JSON format

### _Client Application:_

- Python script run by the GitHub Action pipeline
    - hit endpoint of the clock Lambda created above
    - convert the returned JSON to human readable string
    - return string for display to the user

### _CI/CD:_

- GitHub Actions
    - run tests for both client and web service python applications
    - deploy all AWS services using CDK stack
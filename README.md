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

- AWS S3 Bucket
    - publicly host an index.html file with a single button that says "Get Time"
- AWS Lambda running Python
    - triggered by "Get Time" button
    - hit endpoint of the clock Lambda created above
    - convert the returned JSON to human readable string
    - return string to html for display to the user

### _CI/CD:_

- GitHub Actions
    - run tests for both client and web service python applications
    - deploy all AWS services using CDK stack
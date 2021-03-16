from flask import Flask, request
import json
import requests
import time
from datetime import datetime


app = Flask(__name__)
url = 'blah' # from AWS when gets built


# Do time stuff here
def get_time():
    time = datetime.now(timezone('US/Central'))
    time_of_day = 0
    return time_of_day


def convert_time(time_of_day):
    # Make time into a single json key value pair
    json_time = { "currentTime": "2050-01-24 15:06:26" }
    return json_time


@app.errorhandler(404)
def page_not_found(e):
    return ("something went wrong...", 404, None)


@app.route('/')
def main_route():
    return json_time


if __name__ == '__main__':
    app.run() # need anything in the run method?
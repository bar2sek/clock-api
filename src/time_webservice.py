from flask import Flask, request
import json
import requests
import time
from datetime import datetime


app = Flask(__name__)
url = 'blah' # from AWS when gets built


# Do time stuff here
def get_time():
    # time = datetime.now(timezone('US/Central'))
    time_of_day = 0
    return time_of_day


def convert_time(time_of_day):
    something = 0
    return something


@app.route('/')
def main_route():
    return json_time


if __name__ == '__main__':
    app.run() # need anything in the run method?
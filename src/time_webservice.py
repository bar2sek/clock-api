from flask import Flask
import json
from datetime import datetime


app = Flask(__name__)
now = datetime.now()


def get_time():
    time_string = now.strftime("%d-%m-%Y %H:%M:%S")
    return time_string


def time_to_json(time_string):
    Dictionary = {"currentTime": time_string}
    formatted_time = json.dumps(Dictionary)
    json_time = json.loads(formatted_time)
    return json_time


@app.route('/')
def main_route():
    return time_to_json(get_time())


if __name__ == '__main__':
    app.run(debug=True)
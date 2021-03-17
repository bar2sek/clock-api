import requests
import json
import re

url = "http://127.0.0.1:5000" # make lambda url when complete

def get_json_time():   
    response = requests.get(url)
    return response


def parse_json_to_string(response):
    time = str(json.loads(response.text))
    s = re.split('[\']', time)
    # make print out month and day more human readable
    time_string = f"The current date and time is {s[-2]}"
    return time_string


if __name__ == "__main__":
    print(parse_json_to_string(get_json_time()))
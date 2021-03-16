import pytest
from flask import Flask
import src.time_webservice as webservice
import json
from datetime import datetime


def test_webservice_is_able_to_get_current_time():
    now = datetime.now()
    expected_time_now = now.strftime("%d-%m-%Y %H:%M:%S")
    actual_time_now = webservice.get_time()
    assert actual_time_now == expected_time_now


def test_convert_string_time_to_json():
    time = "16-03-2021 15:29:21"
    json_time = json.dumps({ "currentTime": "16-03-2021 15:29:21" })
    expected_result = json.loads(json_time)
    actual_result = webservice.time_to_json(time)
    assert expected_result == actual_result
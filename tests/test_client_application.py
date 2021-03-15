import pytest
import client_application
import json


def test_parse_json_to_string():
    expected_string = "In Iowa it is currently 3:06:26pm on January 24th, 2050"
    json_body = json.dumps('{ "currentTime": "2050-01-24 15:06:26" }')
    actual_string = parse_json_to_string(json_body)
    assert expected_string == actual_string
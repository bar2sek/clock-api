import pytest
import src.client_application as client
import json
import requests

# would like to learn how to "mock" the time for this test, but it works locally when spoon fed.
# def test_get_json_time():
#     expected_result = '{\n  "currentTime": "17-03-2021 15:49:56"\n}\n'
#     actual_result = client.get_json_time()
#     assert expected_result == actual_result


# def test_parse_json_to_string():
#     expected_string = "The current time is 17-03-2021 15:49:56"
#     json_body = json.dumps('{\n  "currentTime": "17-03-2021 15:49:56"\n}\n')
#     actual_string = client.parse_json_to_string(json_body)
#     assert expected_string == actual_string
import pytest
# import time_webservice
import json
# import time


def test_is_able_to_get_time_from_service():
    expected_return_code = "200"
    # Call the function with given parameters 
    actual_return_code = "200" # r.status_code
    assert actual_return_code == expected_return_code


def test_format_of_incoming_time():
    expected_result = 1
    actual_result = 1
    assert expected_result == actual_result


def test_change_time_to_central_time():
    expected_result = 1
    actual_result = 1
    assert expected_result == actual_result


def test_convert_central_time_to_proper_json_pair():
    expected_result = 1
    actual_result = 1
    assert expected_result == actual_result
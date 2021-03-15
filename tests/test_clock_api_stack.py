import json
import pytest

from aws_cdk import core
from clock_api.clock_api_stack import ClockApiStack


def get_template():
    app = core.App()
    ClockApiStack(app, "clock-api")
    return json.dumps(app.synth().get_stack("clock-api").template)


def test_bucket_created():
    assert("AWS::S3::Bucket" in get_template())


def test_lambda_created():
    assert("AWS::Lambda::Lambda" in get_template()) # I don't know :p
import requests
import json
from behave import given, then


@given('Checking API Request with URL "{url}"')
def step_make_get_request(context, url):
    context.response = requests.get(url)


@then('the response status code should be {status_code}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code)


@then('the response should have a valid JSON format')
def step_check_json_format(context):
    json_response = context.response.json()
    assert json_response is not None


@then('the "{field}" field in the response should be "{value}"')
def step_check_json_field(context, field, value):
    json_response = context.response.json()
    assert json_response.get(field) == value

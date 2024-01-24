import json
from jsonschema import validate,ValidationError
import requests
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


@then('the response should be valid with the schema file "{schema_file_path}"')
def step_check_json_with_json_schema(context, schema_file_path):
    try:
        json_response = context.response.json()
    except json.JSONDecodeError:
        raise AssertionError("Response is not a valid JSON")

    try:
        with open(schema_file_path, "r") as schema_file:
            json_schema = json.load(schema_file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise AssertionError(f"Invalid or missing schema file at: {schema_file_path}")

    try:
        validate(instance=json_response, schema=json_schema)
    except ValidationError as e:
        raise AssertionError(f"JSON validation error: {e}")

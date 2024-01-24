import json
from jsonschema import validate


def text(url: str, type: str, schema_file_path: str):
    json_response_path = "sample/sample_res_failed.json"

    # Load JSON schema from file
    with open(schema_file_path, "r") as schema_file:
        json_schema = json.load(schema_file)

    # Load JSON response from file
    with open(json_response_path, "r") as schema_file:
        json_response = json.load(schema_file)

        # Validate JSON response against the schema
    try:
        validate(instance=json_response, schema=json_schema)
        print("JSON response is valid against the schema.")
    except Exception as e:
        print(f"JSON response does not match the schema: {e}")


def test_Add_new_ACO_with_primarycontact_Id():
    text("http://", "POST", "sample/sample_1.json")


def test_Add_new_ACO_with_primarycontact_Form():
    text("http://.,asf,b", "POST", "sample/sample_1.json")


Feature: API Response Validation

  Scenario: Verify the response from the Device ListAPI
    Given Checking API Request with URL "https://iot.sudhi.in/api/v1/device/list/1/2"
    Then the response status code should be 200
    And the response should have a valid JSON format
    And the "status" field in the response should be "SUCCESS"
    And the response should be valid with the schema file "sample/sample_res.json"

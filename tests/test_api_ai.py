import json
import pytest

@pytest.mark.api
def test_all_apis_with_ai_validation(setup_components, config):
    """Runs validation and AI checks for all APIs defined in config."""
    api_client, validator, ai = setup_components

    for api_conf in config["apis"]:
        name = api_conf["name"]
        endpoint = api_conf["endpoint"]

        print(f"\nTesting API: {name}\nEndpoint: {endpoint}")

        # Step 1: Make API call
        response = api_client.get(endpoint)

        # Step 2: Traditional validation
        data = validator.validate_basic(response, api_conf)
        json_text = json.dumps(data, indent=2)

        # Step 3: AI validation
        ai_verdict = ai.validate_response(name, json_text)
        print(f"\nAI Verdict for '{name}':\n{ai_verdict}")

        # Step 4: AI suggested test cases
        ai_ideas = ai.suggest_tests(name, json_text)
        print(f"\nAI Suggested Tests for '{name}':\n{ai_ideas}\n")

        # Step 5: AI-guided assertion
        assert "fail" not in ai_verdict.lower(), f"AI flagged issues in '{name}'"

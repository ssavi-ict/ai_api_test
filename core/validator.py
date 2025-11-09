class Validator:
    """Performs traditional API validations."""

    def validate_basic(self, response, api_conf):
        assert response.status_code == api_conf["expected_status"], \
            f"{api_conf['name']}: Expected {api_conf['expected_status']}, got {response.status_code}"

        data = response.json()

        if "required_fields" in api_conf:
            for field in api_conf["required_fields"]:
                assert field in data, f"{api_conf['name']}: Missing field '{field}'"

        return data

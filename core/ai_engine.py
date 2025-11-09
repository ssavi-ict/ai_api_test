from openai import OpenAI

class AITestEngine:
    """Handles AI-based validation and test idea generation."""

    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def validate_response(self, api_name: str, json_text: str):
        prompt = f"""
        You are an experienced API Test Engineer.
        Review the following JSON response from API '{api_name}' and check:
        - If data is valid, logical, and consistent
        - If any fields look incorrect or missing
        Provide a short PASS/FAIL verdict with one-line reasoning.

        JSON:
        {json_text}
        """
        resp = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        return resp.choices[0].message.content.strip()

    def suggest_tests(self, api_name: str, json_text: str):
        prompt = f"""
        You are creating new API test ideas for '{api_name}'.
        Given this example response:
        {json_text}

        Suggest 3 to 5 meaningful test cases to expand coverage.
        Keep it concise.
        """
        resp = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return resp.choices[0].message.content.strip()

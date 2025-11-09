import requests

class APIClient:
    """Handles API HTTP requests."""

    def get(self, endpoint: str):
        return requests.get(endpoint)

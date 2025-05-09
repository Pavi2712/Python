import requests
from test_api.test_apicreds.data.sampledata import TestData

class BaseClient:
    """Base client for making HTTP requests."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None 

    def set_token(self, token: str):
        """Set the authentication token for the session."""
        self.token = token
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def get(self, endpoint: str):
        response = self.session.get(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: dict):
        response = self.session.post(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()


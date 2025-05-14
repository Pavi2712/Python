import pytest
import requests

class ApiContext:
    def __init__(self):
        self.headers = {}

    def post(self, url, json=None):
        return requests.post(url, json=json, headers=self.headers)

    def get(self, url):
        return requests.get(url, headers=self.headers)

@pytest.fixture(scope="session")
def api_context():
    try:
        api_context = ApiContext()
        api_context.headers.update({"Content-Type": "application/json"})
        
        response = api_context.post("https://dummyjson.com/auth/login", json={
            "username": "emilys", "password": "emilyspass", "expiresInMins": 30
        })
        
        if not response.ok:
            raise Exception(f"Login failed: {response.status_code} - {response.text}")
    
        api_context.headers.update({"Authorization": f"Bearer {response.json().get('accessToken')}"} )
        yield api_context

        refresh_token = response.json().get("refreshToken")
        if refresh_token:
            refresh_access_token(api_context, refresh_token)

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

def refresh_access_token(api_context, refresh_token):
    """Function to refresh access token using the refresh token."""
    try:
        refresh_response = api_context.post("https://dummyjson.com/auth/refresh", json={
            "refreshToken": refresh_token,
            "expiresInMins": 1
        })
        
        if not refresh_response.ok:
            raise Exception(f"Token refresh failed: {refresh_response.status_code} - {refresh_response.text}")
        
        new_access_token = refresh_response.json().get("accessToken")
        if not new_access_token:
            raise Exception("New access token is missing in the refresh response")
        
        api_context.headers.update({"Authorization": f"Bearer {new_access_token}"} )
        print("\nAccess token refreshed successfully.")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error while refreshing token: {e}")

def test_access_protected_route(api_context):
    try:
       
        response = api_context.get("https://dummyjson.com/auth/me")
        if not response.ok:
            raise Exception(f"Failed to access protected route: {response.status_code} - {response.text}")
        
        protected_data = response.json()
        print("\nResponse Data:")
        for key, value in protected_data.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")

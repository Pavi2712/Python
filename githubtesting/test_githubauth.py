import pytest
import requests

@pytest.fixture(scope="session")
def api_session():
    try:
        session = requests.Session()  # Using session for efficiency(same connection for multiple requests)
        session.headers.update({"Content-Type": "application/json"})
        #making a request to get the access token and storing that in the variable response.
        response = session.post("https://dummyjson.com/auth/login", json={
            "username": "emilys", "password": "emilyspass", "expiresInMins": 30
        })
        if not response.ok:
            pytest.fail(f"Login failed: {response.status_code} - {response.text}")
        #Authorization header
        session.headers.update({"Authorization": f"Bearer {response.json().get("accessToken")}"})
        yield session 

        #refresh token 
        refresh_token = response.json().get("refreshToken")
        if refresh_token:
            refresh_access_token(session, refresh_token)  # Refresh token before closing the session

        session.close() 
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")

def refresh_access_token(session, refresh_token):
    """Function to refresh access token using the refresh token."""
    try:
        refresh_response = session.post("https://dummyjson.com/auth/refresh", json={
            "refreshToken": refresh_token,
            "expiresInMins": 1
        })
        if not refresh_response.ok:
            pytest.fail(f"Token refresh failed: {refresh_response.status_code} - {refresh_response.text}")

        # Get the new access token from the response
        new_access_token = refresh_response.json().get("accessToken")
        if not new_access_token:
            pytest.fail("New access token is missing in the refresh response")

        # Update the session's Authorization header with the new access token
        session.headers.update({"Authorization": f"Bearer {new_access_token}"})
        print("\nAccess token refreshed successfully.")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error while refreshing token: {e}")

def test_access_protected_route(api_session):
    try:
        response = api_session.get("https://dummyjson.com/auth/me")

        if not response.ok:
            pytest.fail(f"Failed to access protected route: {response.status_code} - {response.text}")

        # Print the protected route response data
        protected_data = response.json()
        print("\nResponse Data:")
        for key, value in protected_data.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        pytest.fail(f"Request failed: {e}")

#requests.Session() object, which allows us to reuse the same connection for multiple requests. This is more efficient than making separate requests, 
#as it uses persistent connections and keeps cookies across requests.

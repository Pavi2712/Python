import pytest
from test_apicreds.pages.api_client import APIClient
from test_api.test_apicreds.data.sampledata import TestData

@pytest.fixture(scope="session")
def api_client():
    """Fixture for initializing API client with token."""
    client = APIClient(TestData.BASE_URL)
    login_response = client.login(TestData.Credentials.EMAIL, TestData.Credentials.PASSWORD)
    if login_response.status_code == 200:
        client.set_token(login_response.json().get("token"))
    return client

@pytest.mark.api
def test_list_users(api_client):
    response = api_client.get(TestData.Endpoints.LIST_USERS)
    assert response.status_code == 200

@pytest.mark.api
def test_single_user(api_client):
    response = api_client.get(TestData.Endpoints.SINGLE_USER)
    assert response.status_code == 200

@pytest.mark.api
def test_single_user_not_found(api_client):
    response = api_client.get(TestData.Endpoints.SINGLE_USER_NOT_FOUND)
    assert response.status_code == 404

@pytest.mark.api
def test_login(api_client):
    # Ensure that the token is set after the login process
    assert api_client.token is not None, "Login failed, token not set."

@pytest.mark.api
def test_login(api_client):
    response = api_client.login(TestData.Credentials.EMAIL, TestData.Credentials.PASSWORD)
    print(f"Login Response: {response.json()}")
    assert response.status_code == 200
    assert "token" in response.json(), "Login response does not contain a token"


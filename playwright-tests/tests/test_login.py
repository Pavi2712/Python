import pytest
import json
from pages.login_page import LoginPage # Actions on the login page

def load_user_data():
    with open("data/users.json") as f: #It will open the data file
        return json.load(f) #load() method will load and return the data in a python list of dictionary format

@pytest.mark.parametrize("user", load_user_data()) #User data has tree set of values, so test_multiple_user_login function will run 3 times
def test_multiple_user_login(browser, user): # browser is the fixture which helps to open the browser , user - in dictionary format
    login_page = LoginPage(browser)
    login_page.navigate("https://practicetestautomation.com/practice-test-login/")
    login_page.login(user["username"], user["password"])

    if user["username"] == "student" and user["password"] == "Password123":
        assert browser.locator("h1").text_content() == "Logged In Successfully"
    else:
        assert browser.locator("#error").is_visible()

import pytest
import json
import allure
from pages.login_page import LoginPage # Actions on the login page

def load_user_data():
    with open("data/users.json") as f: #It will open the data file
        return json.load(f) #load() method will load and return the data in a python list of dictionary format
    
#User data has tree set of values, so test_multiple_user_login function will run 3 times
@pytest.mark.parametrize("user", load_user_data())
# @allure.feature("Login")
# @allure.story("Valid Login")
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.title("Test successful login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_multiple_user_login(page, user): # browser is the fixture which helps to open the browser , user - in dictionary format
    login_page = LoginPage(page) 
    # with allure.step("Navigate to login page"):
    login_page.navigate("https://practicetestautomation.com/practice-test-login/")
    # with allure.step("login with username"):
    login_page.login(user["username"], user["password"])
    # with allure.step("Check Status"):
    if user["username"] == "student" and user["password"] == "Password123":
        assert page.locator("h1").text_content() == "Logged In Successfully"
    else:
        assert page.locator("#error").is_visible()
# from playwright.sync_api import Page

# def test_visit_admin_dashboard(page: Page):
#     page.goto("https://practicetestautomation.com/practice-test-login/")
#     import time
#     time.sleep(10)
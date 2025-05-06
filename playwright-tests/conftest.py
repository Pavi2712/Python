import pytest
from playwright.sync_api import sync_playwright # The synchronous version of Playwright's API

@pytest.fixture(scope="session") #This registers the below function as a fixture. Here, we mention scope as session because the fixture will be set up only once for the entire test session and shared among all tests.
def playwright_instance():
    with sync_playwright() as playwright: # initializes a synchronous Playwright instance
        yield playwright # This will yields the Playwright instance to the test function.

#We use yield because it enables setup before the test and teardown after the test, ensuring resources are properly managed.
@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False) #headless=False meaning visible browser window will appear on the screen
    context = browser.new_context() #Creates a new isolated browsing context in Playwright
    page = context.new_page() #Since after creating the new context will open a tab with the page
    yield page
    context.close()
    browser.close()
# import pytest
from paviallure_plugin import PaviAllurePlugin
# import allure

# Automatically add Allure feature and story based on test name
def pytest_configure(config): # it is called before every test starts.
    config.pluginmanager.register(PaviAllurePlugin(), "pavi_allure_plugin")
    
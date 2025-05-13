# import pytest
import allure

# Automatically add Allure feature and story based on test name
class PaviAllurePlugin:
    # def __init__(self):
    #     self.feature = None
    #     self.story = None

    def pytest_collection_modifyitems(self, items):
        for item in items:
            item.add_marker(allure.feature("Pavi"))
            item.add_marker(allure.story("hjfgjf"))
        # Modify the test items here if needed
        pass



    
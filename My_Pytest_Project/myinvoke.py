import sys
import pytest

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")
if __name__ == "__main__":
    # You can pass a path like ["tests"] or individual test files
    test_args = ["-qq", "tests"] # -qq denotes double quite mode and tests is the test file.
    exit_code = pytest.main(test_args, plugins=[MyPlugin()]) #The exit code is captured and returned as output.
    sys.exit(exit_code)

#We have imported pytest and passed the main function inside itself. Instead of calling pytest in the command prombt, we just run python pythonfile.
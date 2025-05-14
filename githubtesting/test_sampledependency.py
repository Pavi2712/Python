import pytest

@pytest.mark.dependency(name = "one")
def test_one():
    print("one")
@pytest.mark.dependency(name = "two", depends = ["one"])
def test_two():
    print("two")
@pytest.mark.dependency(name = "done", depends = ["one","two"])
def test_three():
    print("three")
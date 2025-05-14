import pytest
@pytest.fixture(scope="session")
def fixture_a():
    # print("Setup A")
    return "A"
@pytest.fixture(scope="module")
def fixture_b(fixture_a):
    print(f"Setup B depends on {fixture_a}")
    return f"{fixture_a} + B"
def test_one(fixture_b):
    assert fixture_b == "A + B"

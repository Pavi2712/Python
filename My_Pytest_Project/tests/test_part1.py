# def test_add():
#     assert 1 + 1 == 2

import pytest
@pytest.mark.parametrize("input_val, expected", [  #We are giving mark.parametrize to run test multiple times with different data  #pytest.mark.parametrize It is the decorator from pytest. input_val, expected these are the 2 arguements that the test function will receive.Mark in pytest means tagging or labeling your test to modify or control its behavior.
    ("x", 10), # We provide different type of test cases. It means x1 is the input value. and 10 is the expected output value.
    ("y2", 20),
    ("y13",30)
])
def test_func(input_val, expected):
    # A fake function for demo purposes
    result = len(input_val) * 10
    assert result == expected 

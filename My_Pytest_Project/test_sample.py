# import pytest
# def func(x):
#     return x + 1
# def test_answer():
# assert func(3) == 4  #assert keyword is used for debugging and testing purpose.

import pytest

def f(): #f is a function which raises the SystemExit exception and with the exit code 1
    raise SystemExit()
def test_mytest(): #writing a test function(We tell this as test function because the function name starts with test_)
    with pytest.raises(SystemExit): #this line is used to assert that the with block will raise the SystemExit error. 
        f() #function f() is called and it will raise the SystemExit error and the test case will pass.
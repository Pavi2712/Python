import pytest
# def test_recursion_depth():
#     with pytest.raises(RuntimeError) as excinfo:
#         def f():
#             f()
#         f()
#     assert "RuntimeError" in str(excinfo.value) #Here excinfo is the Exception Instance.

#To check specific errors, we need to follow below function

def foo_implementation():
    def foo():
        raise NotImplementedError
    with pytest.raises(RuntimeError) as execinfo:
        foo()
    assert execinfo.type in RuntimeError 

# def myfunc():
#     raise ValueError("Exception 123 Occured")

# def test_match():
#     with pytest.raises(ValueError, match=r".*123.*"):
#         myfunc()

# Matching exception groups:

# def test_exception_in_group():
#     with pytest.raises(ExceptionGroup) as excinfo:
    #     raise ExceptionGroup(
    #         "Group Message",
    #         [
    #             RuntimeError("Exception 123 occured"),
    #             ExceptionGroup(
    #                 "Nested Group",
    #                 [
    #                     TypeError(),
    #                 ],
    #             ),
    #         ],
    #     )
    # assert excinfo.group_contains(RuntimeError, depth = 1)
    # assert excinfo.group_contains(TypeError, depth = 2)

# def func(x):
#     if x<=0:
#         raise ValueError("x needs to be larger than zero")
# pytest.raises(RuntimeError, func , x=-2)


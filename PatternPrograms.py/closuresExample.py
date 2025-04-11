def outer_function(outer_variable):
    def inner_function(inner_variable):
        return outer_variable + inner_variable
    return inner_function

my_closure = outer_function(8)
print("my_closure",my_closure)
result = my_closure(8)
print("result",result)


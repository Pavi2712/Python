def is_palindrome(value):
    original = str(value)
    reversed_str = ''
    index = -1
    for character in original:
        reversed_str += original[index]
        index -= 1       
    if original == reversed_str:
        print("Hence, the given value is a palindrome.")
    else:
        print("The given value is not a palindrome.")
input_value = input("Enter a string or number: ")
is_palindrome(input_value)

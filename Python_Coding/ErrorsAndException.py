import sys
# Syntax Error

# while True print("Hello World") 
# the error is detected at the function print(), since a colon (':') is missing just before it.

# Exceptions:
# print(10 * (1/0)) # Anything divided by 0 is infinite and it gives ZeroDivisionError.
# print(4 + spam*3) # It will give NameError as 'spam' is not defined.

# print('2' + 2) # Type Error Concadination does not take place with different types.

# while True: # It will run the infinite loop until break
#     try: 
#         x = int(input("Please enter a number: ")) # Gets the input from the user and will try to convert it into integer. If done it will store the value in x and will break the statement.
#         break
#     except KeyboardInterrupt: #It will capture if any interuption performed by the user through keyboard.
#         print("Oops! It is the keyboardInterrupt error")
#     except ValueError: # If the expected error is Value error then print the below message
#         print("Oops!  That was no valid number.  Try again...")
    

# while True:
#     try:
#         if(10* (1/0)): # It will give ZeroDivisionError error. But we only capturing ValueError so, It is passed on to outer try statements; and print the error message.
#             break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# We can also mention multiple expection in the same line itself. It is mentioned inside the tuple separated by commas.

# while True:
#     try:
#         if(2<sample): # Here it gives NameError
#             print("miracle")
#     except(RuntimeError , NameError , TypeError): # We can mention all the excepted errors inside the tuple itself.
#         print("Wonderful")
#         break # Since while is True it will go for infinite loops.It is important to add break statement to stop unwanted running.

# class B(Exception): #Exception is a builtin base class exceptiom
#     pass
# class C(B): # C is the derived class of B
#     pass 
# class D(C): # D is the derived class of C 
#     pass
# for cls in [B, C, D]: #We are looping the B,C,D
#     try:
#         raise cls() #class B is called first then C is called and finally class D is called.
#     except D:
#         print("D") 
#     except C:
#         print("C")
#     except B:
#         print("B")

# # Since B is called first and since it is the parent class B is printed first. 
# #Then comes class C. Since C is the derived class of B it has the instance of B also.But in except C is satisfied first. So, C is printed second.
# #And finally class D is called and it has the instance of C and B but in except D is satisfield first and D is printed.

# try:
#     raise Exception('spam', 'eggs') # Raise the exception and it has the args builtin to store the variables.
# except Exception as inst: # Excepting the exception and will store the exception to the variable inst
#     print(type(inst)) # Print the type of inst that is class exception. 
#     print(inst.args) # Since these exceptions are stored in the variable inst and we can access those things using args attribute
#     print(inst) # the values are stored in the exception variable inst
#     x,y = inst.args # Assigning the values to x,y (Destructuring)
#     print("x=",x)
#     print("y=",y)

# printing the exceptions
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# Here if the try is passed the else statement is executed. If the try is failed the except is checked.
# x = 1
# try:
#     print(5/x)
# except ZeroDivisionError:
#     print("I am the except class")
# else:
#     print("I am the else class")

# Expection Handlers do not handle expections that occur immediatly in the try clause,but also those that occur inside functions that are called (even indirectly) in the try clause. 

# def this_fails():
#     x = 1/0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Function call error:', err)

# Re-raising Exception

# def divide(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError as e:
#         print(f"Error: {e}")  
#         raise  # Re-raise the exception to propagate it further

# def main():
#     try:
#         divide(10, 0)
#     except ZeroDivisionError as e:
#         print(f"Handling error in main: {e}")  # Handle it at a higher level

# main()

# try:
#     raise NameError('Hi There')
#     print("check whether it is running")
# except NameError:
#     print("The error inside the except")
#     raise

# Exception Chaning:

# try:
#     open("database.sqlite") # We are trying to open the database.
# except OSError: # We are expecting OSError. But the error is FileNotFound which is the subclass of OSError. So it goes inside this.
#     raise RuntimeError("unable to handle error") # Since above exception is printed next we are raising Runtime Error.So, both the errors are printed.

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     open("database.sqlite")
#     ~~~~^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
#     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error

# raise ... from ...
# try:
#     open("database.sqlite")
# except FileNotFoundError as e:
#     raise RuntimeError("Something went wrong") from e

# Difference of using raise.. from .. / raise / None

# Just raise : During handling of the above exception, another exception occurred:
#  raise.. from ..:The above exception was the direct cause of the following exception:
# None it only prints the new exception and the old exception is hidden
# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None # Since the old exception is FilenotFound error but as we mentioned None it does not returned that error

#User defined Exceptions

# class MyCustomError(Exception):
#     pass
# raise MyCustomError("Something custom went wrong!") # MyCustomError:Something custom went wrong! is printed

def divide(x, y): # defining a function
    try:
        result = x / y
    except ZeroDivisionError: # Expecting ZeroDivisionError
        print("division by zero!")
    else: # If the exception is not ZeroDivisionError then else part is executed
        print("result is", result)
    finally: # Evertime it executes and if no value given as output by try then it is reraised to print the error message. So Finally is executed just brfore the try statement gets terminate.
        print("executing finally clause")

divide(3,9)
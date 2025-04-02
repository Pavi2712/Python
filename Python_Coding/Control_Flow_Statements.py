# If Statement
#inputValue = int(input("Enter a value:")) # Gets the input from the User.
#if (inputValue%2 == 0): # Checks whether the entered value is Even if yes Print as Even. Or print Odd in else block
#print("Entered value is Even")
#else:
 #   print("Entered value is Odd")

# for Statement:
# for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# range() function:
#If we want to iterate over a sequence of numbers, the built-in function range() is used.
for x in range(0,10):
    print (x)

#Example2:
print(list(range(0,10,2))) # We are trying to print the result as a list. 0 indicates the starting value, 10 indicates the stopping value where as 2 is the increment value.
#output = [0, 2, 4, 6, 8]

#enumerate() function: enumerate(iterable, start=0) Start value is default, returns the enumerate object. iterable must be a sequence and the start value default is 0 and we can mention the random value.
seasons = ['spring','autumn','summer','winter']
print(list(enumerate(seasons,start=2)))

# Break Statement ,It will break the loop. Also, we can use this statement to break the innermost loop also
for n in range(1,10):
     for x in range(2,n):
        if n%x == 0:
            print(f"{n} equals {x} and {n//x}")
            break

#continue() Statement:Continue statement just skip the current iteration and move to nest iteration.

for n in range(1,10):
    if n%2 == 0:
        print(f"The number is a even number {n}")
        continue
    print(f"The number is a odd number {n}")

#else Clauses on Loops:In for loop the else part is executed only after final iteration. that is, if no break occurred.
for x in range(2,10):
    for n in range(2,x):
        if x%2==0: 
            print(f"{x} It is not a prime number")
            break
    else:
        print(f"{x} This is a Prime number")

# pass Statement: It does nothing. It can be used when a statement is required syntactically but the program requires no action.

#while True:
 #   pass

#match() Statement:A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.Only the first pattern that matches gets executed and it can also extract components (sequence elements or object attributes) from the value into variables.
def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not found"
        case 500:
            return "Bad Gateway"
print(http_error(404))

#If you are using classes to structure your data you can use the class name followed by an argument list resembling a constructor, but with the ability to capture attributes into variables.
class Point:
    def __init__(self , x , y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0,y=0):
            print("Origin")
        case Point(x=x,y=0):
            print(f"The value of x is {x}")
        case Point(x=0,y=y):
            print(f"The value of y is {y}")
        case Point(x=x , y=y):
            print("Nothing")
P = Point(0,0)
where_is(P)

#__match_args__ is an attribute that can be defined in a class to specify how an object of that class should be destructured when used in pattern matching.

class Sample:
    __match_args__ = ('x','y')
    def __init__(self , x , y):
        self.x = x
        self.y = y
def describe(point):
    match point:
        case Sample(0,0):
            print("Origin")
        case Sample(x,y):
            print(f"The value of x is {x} and y is {y}")
P = Sample(2,3)
describe(P)

#We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block. Note that value capture happens before the guard is evaluated.

class Sample:
    __match_args__ = ('x','y')
    def __init__(self , x , y):
        self.x = x
        self.y = y
def describe(point):
    match point:
        case Sample(0,0) if x==y:
            print("Origin")
        case Sample(x,y):
            print(f"The value of x is {x} and y is {y}")
P = Sample(2,3)
describe(P)

#Defining Function
def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end='')
        a,b = b , a+b
        print()
fib(10)

#Default Arguement Values:  We can specify the default value for the arguements for one or more and we can able to pass values also.
def ask_ok(prompt , retrives = 3 , reminder ='Please try again'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye' , 'yes'}:
            return("The answer is yes")
        if reply in {'n','no','nope'}:
            return("The answer is no")
        retrives = retrives - 1
        if retrives < 0:
            raise ValueError('invalid user response')
            print(reminder)

#ask_ok('no',2)

#Keyword Arguement:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage , "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot('2 million', state='stiff' , action = 'sing')

#Arbitrary Arguement Lists:
def concat(*args , sep='/'):
    return sep.join(args)

print(concat('pavi','sri','suba','revathi'))

#UnPacking Argument Lists:
args = [3,10,1]
print(list(range(*args))) # * means it can accept n number of arguments

#Dictionaries can deliver keyword arguments with the **-operator.
def parrot(voltage , state = 'a stiff' ,action = 'voom'):
    print("Voltage", voltage)
    print("State" , state)
    print("Action" , action)
d = {"voltage":"4 million" , "state":"TN", "action":"VOOM"}
parrot(**d)

#Lambda Expression:
#Example1
def write_lambda(n):
    return lambda x: x+n
f = write_lambda(25)
print(f(2))

#Example2
pairs = [(1,'one') , (2,'two'), (3,'three') , (4,'four')]
pairs.sort(key = lambda pair: pair[1])
print("Pairs",pairs)

#Documentation Strings:
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#Function Annotations:
def my_function(ham: str , egg: str = 'eggs')->str:
    print("Annotations" , my_function.__annotations__)
    print("The value of ham and eggs :" , ham , egg)
my_function('spam')



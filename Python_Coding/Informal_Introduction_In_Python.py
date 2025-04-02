# Python as a Calculator:
# Numbers

a=10
b=20
print(a+b) 
# Output = 30.
  
#The multiplication takes place first and addition is performed second based on BODMAS Rule
print("SimpleOperation", 2+2*4) # output  = 10

#Division operator returns float value and returns the quotient.
Example1 = (50 - 5*6) / 4
print("Example1",Example1) # output  = 5.0

#Floor Division operator returns integer value and returns the quotient.
Example2 = (50 - 5*6) // 4
print("Example2",Example2) # output  = 5

#Percentage returns the integer value and returns the remainder.
Example3 = 17%3
print("Example3",Example3) # output  = 2

#It returns the integer value and ** returns the power value.
Example4 =  5 ** 2 
print("Example4",Example4) # output  = 25

#In interactive mode, the last printed expression is assigned to the variable _. But this is not good practice. We need to define a variable and assign the value.
price = 12.5 
tax = 10
price * tax
#print("price", price +_)

#Text

Example5 = 'spam eggs'  #Single quote
print(Example5)

Example6 = "spam eggs"  #Double quotes
print(Example6)

#To quote a quote, we need to “escape” it, by preceding it with \. 

Example7 = 'doesn\'t' 
print("Example7",Example7) #output = doesn't Note: Escape \ is given inside single quotes

Example8 = "doesn't"
print("Example8",Example8) #output = doesn't Note: Escape \ is given inside double quotes

#To Escape we use \ , To Newline we use \n , To print raw data we use r 
print('C:\some\name')

#Output: 
#C:\some
#ame

print(r'C:\some\name')
#Output = C:\some\name

#Strings can be concatenated with the + operator.
Example9 = 4*'pavi' + 'thra'
print("Example9",Example9)

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
Example10 = 'Pavi' 'thra ' ' ramasamy'
print("Example10",Example10)

#Strings are immutable, we cant insert the values in string and we can only access it. The negative index starts with -1.
Word = 'Pavithra'
print(Word[0])
print(Word[-1])
print(Word[0:6])
print(Word[0:])
print(Word[:4])
print(Word[:-3])

#List 
sampleList = ['pavi' , 10 , 20 , 'thra'] 
print("sampleList",sampleList)






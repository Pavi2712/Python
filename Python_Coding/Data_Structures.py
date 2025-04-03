from collections import deque
#List Methods:
#Append: Used to add values at the end of the list.
Example1 = [20,4,39,40,29]
Example1.append(27) # It will add the value 27 at the end of the list.
print("Example1",Example1)
#Extend: It will extend the list by appending all the elements from the iterable.
Example2 = [20,4,39,40,29]
Example2.extend('Welcome')
print("Example2",Example2)
#Insert: It is used to insert the value at the desired index position.
Example3 = [20,4,39,40,29]
Example3.insert(3,27) # 3 is the index position and 27 is the value to be inserted at the index position 3.
print("Example3",Example3)

#Remove: It is used to remove the 1st element / specified elements .If no elements available then ValueError is raised.
Example4 = [20,4,39,40,29]
Example4.remove(4)
print("Example4", Example4)

#Pop: If no index id is specified then last element is removed and if we mention the index value then specified index value is removed.
Example5 = [20,4,39,40,29]
Example5.pop()
print("Example5", Example5)

#Clear: Remove all the elements from the list.
Example6 = [20,4,39,40,29]
Example6.clear()
print("Example6", Example6)

#Index: It will return the index of the element.
Example7 = [20,4,39,40,29]
print("Example7",Example7.index(4,1)) # It will return the index number. Here, 4 is the element and 1 is the starting index.

#Count: It will return the count of the value occured(how many times the value occured)
Example8 = [20,4,39,40,29,29]
print("Example8",Example8.count(29))

#Sort: This method is used to sort the values. The Default is Ascending. For Descending mention reverse is True.
Example9 = [20,4,39,40,29]
Example9.sort(key=None , reverse = True)
print("Example9",Example9)

Example10 = ['Pavi' , 'Sri' , 'Suba' , 'Revathi']
Example10.sort(reverse= True) #Key is optional
print("Example10",Example10) 

# Reverse : Used to reverse the elements in the List.
Example11 = [20,4,39,40,29]
Example11.reverse()
print("Example11",Example11)

#Copy: used to copy the original list. That is shallow copy of the list is returned.
Example12 = [20,4,39,40,29]
SampleCopy = Example12.copy()
SampleCopy.append(3)
print("SampleCopy",SampleCopy)

# Usage of deque
queue = deque(["Pavi","Sri","Suba"])
queue.append("Revathi") # Will add the element at the right
queue.popleft() # Will pop the element at the left
queue.appendleft("Revathi") # Will append the element in the left side of the list.
print("queue",queue)

#List Comprehensions: 
ListExample1 = []
for x in range(0,10): # Here we used for loop for iterating the range values.Even we can make it simple ny using the built in map function.
    ListExample1.append(x**2)
print("ListExample1",ListExample1)

# Using the built-in map function
ListExample2 = list(map(lambda x : x**2 , range(6)))
print("ListExample2",ListExample2)

#Also, we can directly mention the square brackets instead of defining it.
ListExample3 = [x**2 for x in range(7)]
print("ListExample3",ListExample3)

# We can also combine the two list values.
ListExample4 = [(x,y) for x in [1,2,3] for y in [2,7,8] if x!=y]
print("ListExample4",ListExample4)

# We can also write the above one as follows also:
ListExample5 = []
for x in [1,2,7]:
    for y in [2,7,8]:
        if x!=y:
            ListExample5.append((x,y))
print("ListExample5", ListExample5)

#Tasks.
#1.create a new list with the values doubled vec = [-4, -2, 0, 2, 4]
vec = [-4, -2, 0, 2, 4]
Task1 = list(x*2 for x in vec)
print("Task1", Task1)

#2.Filter the list to exclude negative numbers
vec = [-4, -2, 0, 2, 4]
Task2 = list(x for x in vec if x>=0)
print("Task2", Task2)

#3.apply a function to all the elements
vec = [-4, -2, 0, 2, 4]
Task3 = list(abs(x) for x in vec)
print("Task3", Task3)

#4.call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
Task4 = list(weapon.strip() for weapon in freshfruit)
print("Task4", Task4)

#5.create a list of 2-tuples like (number, square)
Task5 = list((x,x**2) for x in range(0,10))
print("Task5", Task5)

#Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
NestedList1 = list([row[i] for row in matrix] for i in range(4))
print("NestedList1",NestedList1)

#Also we can write the above in the below format

NestedList2 = []
for i in range(4):
    NestedList2.append([row[i] for row in matrix])
print("NestedList2",NestedList2)

# Also, we can able to write the above converstion using built in method Zip().

NestedList3 = list(zip(*matrix))
print("NestedList3",NestedList3)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

#Tuble
t = 1,2,3
print("TubleExample1", t[0] , t)

# the trailing comma example
singleton = 'hello', 
print(len(singleton))

#reverse operation in tubles is also possible and list also possible
tSample = [12345, 54321, 'hello!']
x,y,z = tSample
print("tSample",tSample)
print("x",x)
print("y",y)
print("z",z)

#Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("SetExample1",basket)  # The Duplicates has been removed

#Membership testing - in , not in 
print('apple' in basket)
print('orange' not in basket)

#Set Operation 
SetExample2 = set('abracadabra')
print("SetExample2",SetExample2) # removes the duplicates and return the set.
sampleA = set('abracadabra')
sampleB = set('alacazam')
print("SetExample3",sampleA - sampleB) # Letters in sampleA but not in SampleB
print("SetExample4",sampleA|sampleB) # Letters in sampleA or sampleB or both
print("SetExample5",sampleA&sampleB) # Both sampleA and sampleB
print("SetExample6",sampleA^sampleB) # Except Both sampleA and sampleB

# Set Comprehension
SetExample7 = {x for x in "abracadabra" if x not in "abc"}
print("SetExample7",SetExample7)

#Dictionary
dictExample1 = {'jack': 4098, 'sape': 4139}
dictExample1['guido'] = 6548
print("dictExample1",dictExample1)
print(dictExample1['jack'])
del dictExample1['jack']
print("dictExample1",dictExample1)
print(list(dictExample1))
print(sorted(dictExample1))
print("sape" in dictExample1)
print("sape" not in dictExample1)

# dict() constructor builds dictionary directly from sequence of key-value pairs

dictExample2 = dict([('pavi',27),('suba',26),('revathi',32)])
print("dictExample2",dictExample2)

# dict() Comprehension
dictExample3 = {x:x*2 for x in range(0,10)}
print("dictExample3",dictExample3)

# If the keys are simple strings then it is easy to make a dictionary
dictExample4 = dict(sape=4139, guido=4127, jack=4098)
print("dictExample4",dictExample4)

# this is nothing but list(key:value) returns the value of list.
dictExample5 = [sape:=4139, guido:=4127, jack:=4098]
print("dictExample5",dictExample5)

#Looping Techniques
#items method => It is return the dictionary items in new key and value pairs.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for sampleKey , sampleValue in knights.items():
    print("sampleKey", sampleKey ,"sampleValue", sampleValue)

#When looping through a sequence the index and the positional value can be retrieved at the same time using enumerate() function.

for i,v in enumerate(['pavi' , 'suba' , 'revathi']):
    print("enumerateExample",i,v)

#To loop two or more sequence at same time we can use zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print("What is your {0}? It is {1}.".format(q,a))

#To reverse the sequence of values we can use reversed() function.
for x in reversed(range(0,10)):
    print(x,end='')

#To remove the duplicate and to sort the elements we can specify set() and sorted() methods.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for x in sorted(set(basket)):
    print("Set&Sort", x)






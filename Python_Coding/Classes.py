from dataclasses import dataclass
class Complex:
    def __init__(self, realpart, imagpart, counters=None):
        self.r = realpart
        self.i = imagpart
        self.counters = counters
x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counters = 1
while x.counters < 10:
    x.counters = x.counters * 2
print(x.counters)
del x.counters

class Hello:
    def f(self):
        return "Hello World"
Y = Hello()
z = Y.f()
print(z)

class Dog:
    kind = "canine"
    def __init__(self, name):
        self.name = name
d = Dog("Buddy")
e = Dog("Fido")
e.age = 18
print(d.kind , e.kind)
print(d.name,e.name)
print(e.age)

# Here the list is declared as Global. Since if we use for all instance then all the value from different objects will get appended.

class DogList:
    category = []
    def __init__(self,name):
        self.name = name
    def tricks(self, trick):
        self.category.append(trick)
d = DogList('val1')
e = DogList('val2')
d.tricks('Sample1')
e.tricks('Sample2')
print(d.category)

#To solve the above issue, we can define the property inside the method. So, each instance can access the different list attributes.

class DogList1:
    def __init__(self , name):
        self.name = name
        self.trick1 = []
    def add_tricks(self, trickValue):
        self.trick1.append(trickValue)
a = DogList1("Pavi")
b = DogList1("Suba")
a.add_tricks("Pavi1")
b.add_tricks("Suba1")
print(a.trick1)
print(b.trick1)

# If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritizes the instance.


class House:
    location = 'chennai'
    area = 'ASV'

area1 = House()
print(area1.location , area1.area)

area2 = House()
area2.area = 'Perungudi' # we gave another area for instance. Since Python gives priority to instances
print(area2.location , area2.area)

# isinstance(object, classinfo) 

class Animal:
    pass
class Dog(Animal):
    pass
dog = Dog()
print(isinstance(dog ,Animal)) # here, dog is object of the Derived class and the base class
print(isinstance(dog , Dog))
print(isinstance(Dog , Animal)) # False because Dog is not object instance of Animal. We are deriving only.

#issubclass(class, classinfo)

class School:
    pass
class Pavithra(School):
    pass
class Suba(School):
    pass

print(issubclass(Pavithra , School)) # Pavithra , Suba is the subclass of school
print(issubclass(Suba , School))
print(issubclass(Suba , Pavithra)) # Pavithra , Suba is the subclass of school but is does not mean Suba should be a subclass of Pvithra

# Example of multiple Inheritance with super()
class A:   # Define Class A
    def __init__(self): # Function Definition of __init__
        print("A _init_")
    def greet(self): # Function Definition of greet
        print("Greeting from A")
class B(A):
    def __init__(self):
        super().__init__() #refers A
        print("B's __init__")
    def greet(self):
        super().greet() #refers A
        print("Greeting from B")
class C(A):
    def __init__(self):
        super().__init__() #refers A
        print("C's __init__")
    def greet(self):
        super().greet() #refers A
        print("Greeting from C")
class D(B,C):
    def __init__(self):
        super().__init__() # Here starts the operation. D->B->C->A The parent class A is obtained based on the base class given order.
        print("D's __init__")
    def greet(self):
        super().greet()
        print("Greeting from D")

d = D()
d.greet()

#Example of Mangling:

class ManglingExample:
    def __init__(self):
        self.__private_variable = 47
    def get_private_var(self):
        return self.__private_variable
obj = ManglingExample()
print("obj",obj)
print("Mangled1", obj.get_private_var())
print("Mangled2",obj._ManglingExample__private_variable)


#Odds and Ends # Example of uding data types.

@dataclass
class Employee:
    name:str
    dept:str
    year:int
john = Employee('john', 'computer lab', 1000)
print(john.name)
print(john.dept)
print(john.year)

# Iterator:
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

#Generators:
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)

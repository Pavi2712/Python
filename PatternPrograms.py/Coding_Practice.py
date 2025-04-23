# Write a generator function even_numbers(n) that yields even numbers from 0 to n.
def even_numbers(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i
for num in even_numbers(10): # We are iterating because even_number function will return only the generator object.
    print(num)

# Write a Python function to count the frequency of each word in a string.

def find_frequency(val):
    freq = {}
    words = val.split()
    for word in words:
        if word in freq:
           freq[word]+=1
        else:
            freq[word]=1
    return freq
output =  find_frequency("hello this this is Pavi Pavi")
print(output)

#Recursion - The function which called itself for solving the problem. Need to split the larger program into smaller , subtasks until it reached the base case.
# Example for recursion is Flattening the array.Also, it will the example of closures.

def is_list(obj):
    return type(obj) == list
def flatten_array(arr):
    result = []
    def helper(val):
        for item in val:
            if is_list(item):
                helper(item)
            else:
                result.append(item)
    helper(arr)
    return result

arrayValue = [1, [2, [3, 4,[2]], 5], 6]
output = flatten_array(arrayValue)
print(output)

#Write a Python class to represent a bank account with deposit and withdraw methods.

class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
    def depositAmount(self,amount):
        if amount >0:
            self.balance +=amount
            print(f"The current balance after deposit is {self.balance}")
        else:
            print("Deposit amount should be positive")
    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            print(f"The current balance after withdrawal is {self.balance}")
        else:
            print("Insufficient funds")
    def display(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: ₹{self.balance}")

account = BankAccount("Pavithra", 1000)
account.depositAmount(10)
account.withdrawal(100)
account.display()

# Print the following pattern using a loop:
# *
# **
# ***
# ****

strval = '*'
for i in range(5):
    print(i*strval)
i=0
while i<=5:
    print(strval*i)
    i+=1

#Use a lambda function to sort a list of tuples by the second value.
pairs = [(1,"one"),(2,"two"),(3,"three")]
pairs.sort(key= lambda pair:pair[1])
print(pairs)

# Write a program to print each character of a string in reverse order on new lines.
def reverse_string(strValues):
    reverse_str = ''
    for i in range(len(strValues)-1, -1,-1):
        reverse_str += strValues[i]
    return reverse_str
output = reverse_string("Pavithra")
print("reverse",output)

#Write a function to return the longest word in the list

def longest_word(wrd):
    longest_wrd = ''
    word_list = wrd.split()
    for word in word_list:
        if len(word) > len(longest_wrd):
            longest_wrd = word
    return longest_wrd

outputs = longest_word("Hi I am learning Python")
print(outputs)





            



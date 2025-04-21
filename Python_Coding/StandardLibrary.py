#Operating System Interface:
# os is the module which provides functions for interacting with operating systems.
import os
import shutil
import glob
import sys
import re
from urllib.request import urlopen
from datetime import date
import zlib
from timeit import Timer
import reprlib
import pprint 
import textwrap
from string import Template
from array import array
from collections import deque
import bisect
# print(os.getcwd()) # It is used to get the current working directory.
# os.chdir('/server') # It is used to change the currnt directory.
# Note: It is working when we not give the /

# os.system('mkdir today') 
# It is used to create a directory ,called 'today'. And if the directory is created successfully it 
# returns 0. Since, there is no error returned while creating that directory.

# dir(os) # It will return all the module functions
# help(os) #returns an extensive manual page created from the module's docstrings. It will return the NAME , MODULE REFERENCE.

#For daily file and directory management tasks,the shutil module provides a higher level interface that is easier to use.
# shutil.copyfile('Sampletest.txt','NewSampleTest.txt') 
# It will copy the contents from 'Sampletest.txt' to 'NewSampleTest.txt' .
# It returns the copied content file name.

# shutil.move('Sampletest.txt','moveSampleTest.txt') # It will change the file name from 'Sampletest.txt' to 'moveSampleTest.txt'
# Also, if we try to change the file name inside some folder then the file name is changed and 
# the file will pop out from inside the folder.

# File Wildcards:
   # The glob module provides a function for making file lists from directory wildcard searches. It means we will provide the wildcard so the glob module helps to find all the matching pattern files for the given one.

# glob.glob('*txt') # from glob module using the attribute glob which will take the argument as a wildcard searches. It is useful when the user forgets the filename or to get the group of files. 
# ['moveSampleTest.txt', 'NewSampleTest.txt']

# print(sys.argv)
# argv ['StandardLibrary.py','hello','world'] Whatever we pass in the command line those arguments are stored in sys.argv.

#Error Output Redirection and Program Termination:
# The sys module also has attributes for stdin, stdout, and stderr. 

# print(sys.stderr.write('Local Warning')) # It returns the Warning message and the length of the message.

#String Pattern Matching:
print(re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))  #\b tells that it is the begginning of the word(Word Boundary). f--> start of the word. So it returns all the words starting with f
print(re.sub(r'(\b[a=z]) \1', r'\1','cat in in the hat')) #substitute repeated words 

#replace
print('tea for too'.replace('too','two'))

#Mathematics:
#1. math module - cos, log
#2. random module - choice,sample , random.random() 0.0 <= result < 1.0 , random.randrange(6) 
#3. statistics - mean (sum of all values/number of values), median(need to sort and pick the median value) , variance

#Internet Access:
# Both below modules for accessing the internet and processing internet protocols
#  urllib.request for retrieving data from URLs
#  smtplib for sending mail

# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip())   

#Dates and Times:
now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y.%b"))

birthday = date(1999,12,12)
age = now - birthday
print(age)

# Data Compression:
#zlib module is used for compressing

s =b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))

#Performance Measurement:
#timeit module is used to measure the performance timing.

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

#Quality Control:
# The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings. 
# The unittest module is not as effortless as the doctest module, but it allows a more comprehensive set of tests to be maintained in a separate file.


#Output Formatting:
# repr() is the "official" string representation. reprlib module is  “safe” and shortened version of repr(). It is specifically useful for debugging purposes.
print(reprlib.repr(set('supercalifragilisticexpialidocious'))) 

#pprint module is nothing but pretty print. Which makes nested data structures easier to read.
t = [[[['black', 'cyan'], 'white', ['green', 'red']],
      [['magenta', 'yellow'], 'blue']]]   # t contains nested lists.
pprint.pprint(t, width=30) # We are passing the list to pprint and width = 30; which means one line width should not exit 30.

#The textwrap module formats paragraphs of text to fit a given screen width
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print("TextWrap",textwrap.fill(doc, width=55))

#locale module which helps format data according to cultural conventions (e.g., U.S. vs Europe formatting).

#Templating:
# 1.The string module includes a versatile Template class with a simplified syntax suitable for editing by end-users. This allows users to customize their applications without having to alter the application.
# 2.The format uses placeholder names formed by $ with valid Python identifiers.$$ creates a single escaped $.

t = Template('${village} folk send $$10 to ${cause}.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

# The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument. Its better to use safe_substitute(), so if we didnt pass the argument also it just print as it is.

# Working with Binary Data Record Layouts:
# The struct module provides pack() and unpack() functions for working with variable length binary record formats. The following example shows how to loop through header information in a ZIP file without using the zipfile module. Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. The "<" indicates that they are standard size and in little-endian byte order

#Multithreading:
# Threading is a technique for decoupling tasks which are not sequentially dependent. Threads can be used to improve the responsiveness of applications that accept user input while other tasks run in the background. A related use case is running I/O in parallel with computations in another thread.

#Logging:
# The logging module offers a full featured and flexible logging system. At its simplest, log messages are sent to a file or to sys.stderr.By default, informational and debugging messages are suppressed and the output is sent to standard error. Other output options include routing messages through email, datagrams, sockets, or to an HTTP Server. New filters can select different routing based on message priority: DEBUG, INFO, WARNING, ERROR, and CRITICAL.

#Weak References:
# Python does automatic memory management.
# This approach works fine for most applications but occasionally there is a need to track objects only as long as they are being used by something else. Unfortunately, just tracking them creates a reference that makes them permanent.
# The weakref module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. 

#Tools for Working with Lists:

# The array module provides an array object that is like a list that stores only homogeneous data and stores it more compactly.

a = array('H', [4000, 10, 700, 22222]) #Here H is just a type code. a stores the list value.
print(sum(a))
print(a[1:3]) # here 10,700 is in index 1 and 2

# The collections module provides a deque object that is like a list with faster appends and pops from the left side but slower lookups in the middle. These objects are well suited for implementing queues and breadth first tree searches
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
print("d",d)

#The bisect module with functions for manipulating sorted lists. We can also add values and sort them too.
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

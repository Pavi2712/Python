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








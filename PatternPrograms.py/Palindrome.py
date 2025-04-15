str1 = input("Enter a string:")
str2 = ''
index = -1
for i in str1:
    str2 += str1[index]
    index-=1
print("The given string = {} \n The Reversed string = {}".format(str1,str2))
if(str1 == str2):
    print("Hence,the given string is Palindrome")
else:
    print("The given string is not a Palindrome")

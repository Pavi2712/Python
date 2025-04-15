str1 = input("Enter the string")
str2 = "aAeEiIoOuU"
vowels , consonants = 0,0
for i in str1:
    if i in str2:
        vowels+=1
    else:
        consonants+=1
print("The given string contains {} vowels and {} consonants".format(vowels, consonants))

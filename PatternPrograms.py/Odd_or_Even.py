def odd_or_even(num):
    if num%2 == 0:
        print(f"{num} is a even Number")
    else:
        print(f"{num} is a odd Number")

Num = int(input("Enter a number:"))
odd_or_even(Num)
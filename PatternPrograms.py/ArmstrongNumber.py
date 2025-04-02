def is_armstrong(num):
    value = str(num)
    value_len = len(value)
    power_value = sum(int(digit) ** value_len for digit in value )
    return power_value == num

num = int(input("Enter a number:"))

if is_armstrong(num):
    print("Entered number is a ArmStrong Number")
else:
    print("Entered number is not a ArmStrong Number")
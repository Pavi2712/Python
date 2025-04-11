m1 = int(input("Enter mark in first subject:"))
m2 = int(input("Enter mark in second subject:"))
avg = (m1+m2)/2
if avg >=80:
    print("Grade:A")
elif avg < 80 and avg >=70:
    print("Grade:B")
elif avg >=60 and avg < 70:
    print("Grade:C")
elif avg <60 and avg>=40:
    print("Grade:D")
else:
    print("Better luck next time")
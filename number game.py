import random

phone= random.randint(1,10)
app=int(input("Enter a number"))
if phone == app:
    print("yes the number is correct")
else:
    print("the number is incorrect and correct is",phone)    
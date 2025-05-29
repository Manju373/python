import random

fruits=["mango","banana","apple","cherry"]
computer= random.choice(fruits)
user=input("Enter your choice ")
if computer==user:
    print("user choice is correct")
else:
    print("user choice is wrong the correct is",computer)
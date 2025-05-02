import random 

h=random.randint(1,100)
print("Welcome to the number guessing game")
print("i will choose a number between 1 & 100 you need to guess")
print("i will till you it's odd or even or lower or higher")
attempts=0
while True: 
    try:
        w=int(input("Enter the number"))
        attempts+=1
        if w==h:
            
            print("Congrats you have guessed right in ",attempts)
            break 
        else:
            if h > w:
                print("go higher")
            else:
                print("go lower")
            if h % 2==0:
                print("it's even")
            else :
                print("it's odd")
    except: 
        print("Please enter the valid number")                        

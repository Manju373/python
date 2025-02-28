m =input("Enter y for yes and n for no.")
if m=="y": 
    print("Allowed")
else:
    a=int(input("Enter your attendence"))
    if a>75:
        print("Allowed") 
    else:
        print("Not Allowed")       
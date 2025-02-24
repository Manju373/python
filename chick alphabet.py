char = input("Enter a character: ")
if int(char) == 1 and char.isalpha(): 
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet")
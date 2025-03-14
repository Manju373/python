rows = int(input("Enter the number of rows"))
number=65
for i in range (1,rows+1):
    for j in range (1,i+1):
        character=chr(number)
        print(character,end=" ")
        number=number+1
    print() 
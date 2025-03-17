rows = int(input("Enter the number of rows"))

for i in range(1,rows+2):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
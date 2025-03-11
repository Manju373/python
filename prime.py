number=int(input("Enter the number: "))
for i in range(2, number):
    if number%i==0 :
        print("non prime")
        break
else:
    print("prime")
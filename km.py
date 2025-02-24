a=int(input("Enter the first speed"))
b=int(input("Enter the Sceand speed"))
c=int(input("Enter the Third speed"))
ave = (a+b+c)/3
print(ave)
if a>ave and b>ave :
    print("a and b is greater then ave")
elif a> ave and c>ave :
    print("a and c is greater")
elif b> ave and c >ave :
    print("b and c is greater")
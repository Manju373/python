a=int(input("Enter the Grammer marks"))
b=int(input("Enter the English marks"))
c=int(input("Enter the Science marks"))
d=int(input("Enter the Math marks"))

avg=(a+b+c+d)/4
print(avg)
if avg> 80 : 
    print("grade a")
elif avg> 60:
    print("grade b")
elif avg> 40:
    print("grade c")
else:
    print("grade d")
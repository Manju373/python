word = input("Enter the message ")
rk = input("Enter the character ")
count=0
for i in word:
    if i==rk:
        count=count+1
print(count)        
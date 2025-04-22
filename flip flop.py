j=(2,3,4)
orignal=j
j=list(j)
j.reverse()
j=tuple(j)
if orignal==j:
    print("flip flop")
else:
    print("not a flip flop")
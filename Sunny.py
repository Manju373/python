f= (0,1,0,0,0,1,1,0)
zeros=f.count(0)
ones=f.count(1)
if zeros>ones:
    print("weather is sunny")
else:
    print("weather is rainy")
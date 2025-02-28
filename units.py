units=int(input("enter the units"))
if units <50:
    print("total bill",units*5)
elif  units>=50 and units<100 :
    print("total bill",units*8)
elif units>=100 and units<150:
    print("total bill", units*10)
else:
    print("total bill",units*15)
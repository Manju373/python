def travell(persons,amount):
    return persons*amount
def food(persons,times,amount):
    return persons*times*amount
def hotel(persons, rooms,amount):
    return persons*rooms*amount
def total():
    a=travell(5,12000)
    b=food(5,2,2300)
    c=hotel(5,1,4000)
    print("please pay the amuunt",a+b+c)
total()

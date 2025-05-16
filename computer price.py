class computer:
    def __init__ (self):
        self.__maxprice=34000
    def display(self):
        print(self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price

obj=computer()
obj.display()
obj.__maxprice=20000
obj.display()
obj.setmaxprice(19000)
obj.display()
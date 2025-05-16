class privateclass:
    __h=23
    def __private(self):
        print("i am a private method")
    def hello(self):
        print("the value of h is this",privateclass.__h)
obj = privateclass()
obj.hello()
obj.__private()
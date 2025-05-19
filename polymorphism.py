class India:
    def captial(self):
        print("new delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("developing country")
class Usa:
    def captial(self):
        print("washington dc")
    def language(self):
        print("English")
    def type(self):
        print("developed country")

obj=India()
obj1=Usa()
for i in (obj,obj1):
    i.captial()
    i.language()
    i.type()


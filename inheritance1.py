class parent:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
class child(parent):
    pass
obj=child("Ather","Black")
print(obj.name)
print(obj.colour)
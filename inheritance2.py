class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id) 
class Employee(person):
    def __init__(self,name,id,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id)
obj=Employee("Manju",5166,45000,"test engineer")
obj.display()
print(obj.salary,obj.post)
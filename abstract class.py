from abc import ABC, abstractmethod
class parent(ABC):
    def display(self):
        print("Iam a parent class method")
    @abstractmethod
    def test(self):
        print("parent class method")

class child(parent):
    def test(self):
        print("child class method")
obj = child()
obj.display()
obj.test()


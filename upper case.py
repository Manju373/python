class upper:
    def __init__ (self):
        self.ring=""
    def getstring(self):
        self.ring=input("Enter the values")
    def Display(self):
        print(self.ring.upper())
r=upper()
r.getstring()
r.Display()
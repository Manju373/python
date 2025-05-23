class BMW:
    def fuel_type(self):
        print("diesel")
    def max_speed(self):
        print("200 Kmp/h")
class Ferrari:
    def fuel_type(self):
        print("gasline")
    def max_speed(self):
        print("217 Kmp/h")
obj=BMW()
obj1=Ferrari()
for i in (obj,obj1):
    i.fuel_type()
    i.max_speed()

class Recerse:
    def __init__(self, s=""):
        self.s = s

    def reversed_string(self):
        return self.s[::-1]
user_input = input("Enter the string to reverse:")
reverse_instance = Recerse(user_input)
print("Reversed string:",reverse_instance.reversed_string())
test_dict = {'Codingal':3, 'is':2, 'best':2, 'Coding':1}
print("Test Dictiionary:",test_dict)

val = int(input("Enter the value to chick its frequency: "))
print("Frequency of value",val,"is",list(test_dict.values()).count(val))
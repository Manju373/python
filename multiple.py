try:
    num1,num2 =eval(input("Enter two numbers separated by a coma:"))
    result = num1 / num2 
    print("Result:",result)
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("comma is missing")
except :
    print("invalid input")
else:
    print("No exception occurred") 
finally: 
    print("Excution Successful")       
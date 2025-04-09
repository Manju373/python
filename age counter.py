def check_age():
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)

        if age <0:
            print("Age connot be nagitive.")
        else:
            if age % 2 == 0:
                print("The age is even")
            else:
                print("THe age is odd") 
    else:
        print("Invalid input. Please enter a valid age as a number.")
check_age()                          
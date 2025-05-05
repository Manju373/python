n = int(input("Enter a number: "))
odd_numbers =[i for i in range(n) if i % 2 !=0]
even_numbers =[i for i in range(n) if i % 2 !=0]

print("Odd number:", odd_numbers)
print("even number:", even_numbers)

fruits =['graps','banana','papya','mango']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:",capitalized_fruits)
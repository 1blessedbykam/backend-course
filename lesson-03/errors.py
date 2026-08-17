try:
    age = int(input("Enter your age: "))
    print("Your age is", age)
except ValueError:
    print("Invalid age. Please enter a number.")
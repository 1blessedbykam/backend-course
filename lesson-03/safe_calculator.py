try:
    number1 = int(input("Enter your first number: "))
    number2 = int(input("Enter your second number: "))
    result = number1 / number2
    print(result)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("You can't divide with 0!")
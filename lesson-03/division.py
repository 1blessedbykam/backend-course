try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("That is not a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
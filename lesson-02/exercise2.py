def check_age(age):
    if age >= 18:
        return "adult"
    elif age >= 13:
        return "teenager"
    else:
        return "Child"

result = check_age(int(input("Enter your age: ")))

print(f"You're a {result}")
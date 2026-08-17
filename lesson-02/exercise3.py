def check_password(password):
    if len(password) >= 8:
        return "Password is strong enough"
    else:
        return "Password is too short"

result = check_password(input("Enter your password: "))

print(result)

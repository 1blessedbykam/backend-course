def validate_username(username):
    if len(username) >= 3:
        return True
    return False
def validate_password(password):
    if len(password) >= 8:
        return True
    return False
def validate_age(age):
    if age >= 13:
        return True
    return False

print("=== Backend Registration Simulator ===")

username = input("Choose a username: ")
password = input("Choose a password: ")
age = int(input("Enter your age: "))

username_ok = validate_username(username)
password_ok = validate_username(password)
age_ok = validate_age(age)

if username_ok and password_ok and age_ok:
    print(f"Succes! Account created for {username}.")
else:
    print("Registration failed:")

    if not username_ok:
        print("- Username must be at least 3 characters.")
    if not password_ok:
        print("- Password must be at least 9 characters.")
    if not age_ok:
        print("- Age must be between 13 and 100")
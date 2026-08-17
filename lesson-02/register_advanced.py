def validate_username(username):
    if len(username) < 3:
        return False
    return True


def validate_password(password):
    if len(password) < 8:
        return False
    return True


def validate_age(age):
    if age < 13 or age > 100:
        return False
    return True


def register_user(username, password, age):
    errors = []

    if not validate_username(username):
        errors.append("Username must be at least 3 characters.")

    if not validate_password(password):
        errors.append("Password must be at least 8 characters.")

    if not validate_age(age):
        errors.append("Age must be between 13 and 100.")

    if len(errors) == 0:
        return {
            "success": True,
            "message": f"Account created for {username}"
        }
    else:
        return {
            "success": False,
            "errors": errors
        }


print("=== Advanced Backend Registration Simulator ===")

username = input("Choose a username: ")
password = input("Choose a password: ")
age = int(input("Enter your age: "))

result = register_user(username, password, age)

print(result)
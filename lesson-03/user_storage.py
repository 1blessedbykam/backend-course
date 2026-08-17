import json
import os

FILENAME = "users.json"

def load_users():
    if not os.path.exists(FILENAME):
        return []

    if os.path.getsize(FILENAME) == 0:
        return []
    with open(FILENAME, "r") as file:
        return json.load(file)


def save_users(users):
    with open(FILENAME, "w") as file:
        json.dump(users, file, indent=4)

def validate_username(username):
    return len(username) >= 3

def validate_password(password):
    return len(password) >= 8

def validate_age(age):
    return 13 <= age <= 100

def username_exists(users, username):
    for user in users:
        if user["username"] == username:
            return True
    return False

def register_user(user, username, password, age):
    errors = []

    if not validate_username:
        errors.append("Username must be at least 3 characters.")

    if not validate_password(password):
        errors.append("Password must be at least 8 characters.")

    if not validate_age(age):
        errors.append("Age must be between 13 and 100.")

    if username_exists(users, username):
        errors.append("Username already exists.")

    if len(errors) > 0:
        return {
            "succes": False,
            "errors": errors
        }

    users.append({
        "username": username,
        "age": age
    })

    return {
        "succes": True,
        "message": f"Account created for {username}"
    }


users = load_users()

print("=== User Storage System ===")

username = input("Choose a username: ")
password = input("Choose a password: ")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age. Please enter a number.")
    raise SystemExit

result = register_user(users, username, password, age)

if result["succes"]:
    save_users(users)
    print(result["message"])
    print("User saved to users.json")
else:
    print("Registration failed:")

    for error in result["errors"]:
        print("-", error)
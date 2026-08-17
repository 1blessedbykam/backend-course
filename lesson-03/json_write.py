import json

user = {
    "username": "Clouned",
    "age": 15,
    "goal": "Software Engineer"
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

print("User saved to user.json")
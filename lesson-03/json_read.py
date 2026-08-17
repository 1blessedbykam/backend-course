import json

with open("user.json", "r") as file:
    user = json.load(file)

print(user)
print(user["username"])
print(user["age"])
print(user["goal"])
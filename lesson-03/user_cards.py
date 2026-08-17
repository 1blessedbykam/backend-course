users = [
    {
        "username": "Clouned",
        "age": 15,
        "goal": "programmer"
    },
    {
        "username": "sukkel1",
        "age": 13,
        "goal": "voetballer"
    },
    {
        "username": "sukkel2",
        "age": 14,
        "goal": "dumbass"
    }
]

for user in users:
    print(f"{user["username"]} is {user["age"]} and wants to become a {user["goal"]}")
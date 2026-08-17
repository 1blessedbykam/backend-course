correct_username = "Clouned"
correct_password = "backend123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login succesful.")
else:
    print("Invalid username or password.")
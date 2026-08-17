note = input("Enter your note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Saved notes:")

with open("notes.txt", "r") as file:
    print(file.read())
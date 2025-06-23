# Handle file-not-found exception
try:
    with open("non_existent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
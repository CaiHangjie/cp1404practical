# Demonstrating different ways to read files
filename = "example.txt"
with open(filename, "r") as file:
    print("Using read():")
    print(file.read())

with open(filename, "r") as file:
    print("\nUsing readline():")
    print(file.readline())

with open(filename, "r") as file:
    print("\nUsing readlines():")
    print(file.readlines())

with open(filename, "r") as file:
    print("\nUsing for loop:")
    for line in file:
        print(line.strip())
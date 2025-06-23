# Print lines that start with "#"
filename = "example.txt"
with open(filename, "r") as file:
    for line in file:
        if line.startswith("#"):
            print(line.strip())
# Read a CSV-style file and print formatted output
filename = "guitars.csv"
with open(filename, "r") as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        print(f"{name} ({year}) costs ${float(cost):,.2f}")
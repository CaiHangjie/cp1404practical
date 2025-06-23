
"""
Program to read and display country data from a CSV file.
"""

FILENAME = "countries.csv"

def main():
    countries = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            name, code, population = line.strip().split(",")
            countries.append({"name": name, "code": code, "population": int(population)})

    for country in countries:
        print(f"{country['name']} ({country['code']}) has a population of {country['population']:,}")

if __name__ == "__main__":
    main()

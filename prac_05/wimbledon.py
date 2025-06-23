"""
Wimbledon Results Analysis
Assumes a CSV file with winner and country data
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_data(FILENAME)
    champions = count_champions(records)
    countries = get_countries(records)

    print("Wimbledon Champions:")
    for name, wins in sorted(champions.items()):
        print(f"{name} {wins}")
    print(f"
These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # skip header
        records = [line.strip().split(",") for line in in_file]
    return records


def count_champions(records):
    champions = {}
    for record in records:
        winner = record[2]
        champions[winner] = champions.get(winner, 0) + 1
    return champions


def get_countries(records):
    return set(record[1] for record in records)


if __name__ == '__main__':
    main()

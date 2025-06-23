FILENAME = "subject_data.csv"

def main():
    with open(FILENAME) as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")

if __name__ == "__main__":
    main()


import csv

FILENAME = "movies.csv"

def load_movies():
    with open(FILENAME, 'r') as in_file:
        reader = csv.reader(in_file)
        return [row for row in reader]

def save_movies(movies):
    with open(FILENAME, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(movies)

def list_movies(movies):
    for i, movie in enumerate(movies, 1):
        watched = " " if movie[3] == "w" else "*"
        print(f"{i}. {watched} {movie[0]} ({movie[1]}) - {movie[2]}")

def add_movie(movies):
    title = input("Title: ").strip()
    year = input("Year: ").strip()
    category = input("Category: ").strip()
    movies.append([title, year, category, "u"])

def mark_movie(movies):
    list_movies(movies)
    choice = int(input("Enter the number of a movie to mark as watched: ")) - 1
    if movies[choice][3] == "w":
        print("You have already watched this movie.")
    else:
        movies[choice][3] = "w"

def main():
    movies = load_movies()
    menu = "Menu:\nL - List movies\nA - Add new movie\nW - Watch a movie\nQ - Quit"
    print("Movies To Watch 1.0 - by Your Name")
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            mark_movie(movies)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    save_movies(movies)
    print(f"{len(movies)} movies saved to {FILENAME}")
    print("Have a nice day :)")

if __name__ == "__main__":
    main()

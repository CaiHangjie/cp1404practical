"""
CP1404/CP5632 - Practical
Score Menu
"""
def main():
    score = float(input("Enter score: "))
    choice = display_menu()
    while choice != "Q":
        if choice == "P":
            print(f"Score: {score}")
        elif choice == "R":
            print(get_result(score))
        else:
            print("Invalid choice")
        choice = display_menu()
    print("Farewell.")

def display_menu():
    print("(P)rint score\n(R)esult\n(Q)uit")
    return input(">>> ").upper()

def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

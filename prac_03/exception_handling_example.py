# Demonstrate exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result is {result}")
except ValueError:
    print("Invalid input; please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
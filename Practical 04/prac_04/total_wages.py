def calculate_wage(name, hours, rate):
    return f"{name} earned ${hours * rate:.2f}"

def main():
    name = input("Enter name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: "))
    print(calculate_wage(name, hours, rate))

if __name__ == "__main__":
    main()

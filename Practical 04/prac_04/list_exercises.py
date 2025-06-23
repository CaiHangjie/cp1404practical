numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average is {sum(numbers)/len(numbers):.2f}")

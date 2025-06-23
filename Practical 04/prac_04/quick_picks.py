import random

NUM_PICKS = int(input("How many quick picks? "))
for _ in range(NUM_PICKS):
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print(" ".join(f"{n:2}" for n in numbers))

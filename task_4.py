import random

def random_numbers(num_of_samples:int):
    count = [0] * 10

    for i in range(num_of_samples):
        num = random.randint(0, 99)
        rand = num // 10
        count[rand] += 1

    for i, count in enumerate(count):
        lower = i * 10
        upper = (i + 1) * 10 - 1
        print(f"Group {lower} - {upper}: {count}")

number = 100000
random_numbers(number)

def is_even(number):
    return number % 2 == 0

numbers = [10, 23, 40, 50, 75, 45, 89]

for num in numbers:
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is not even")
import random

while True:
    roll = input("Roll? (y, n)\n")
    if roll == 'y':
        print(random.randint(1, 6))
    if roll == 'n':
        break

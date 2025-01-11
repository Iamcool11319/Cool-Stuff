import random

print("Welcome to the Guessing Game! Try to guess the\nright number in the shortest number of guesses\npossible!\n")

ask_range = input(
    "What is the range of numbers you want to guess\nfrom?\n\nOptions: 10, 100, 1000, 10000, 100000,\n1000000, 10000000, 100000000, 1000000000,\n10000000000, 100000000000\n")

if ask_range == "10":
    numbers_to_guess_from = range(1, 11)
elif ask_range == "100":
    numbers_to_guess_from = range(1, 101)
elif ask_range == "1000":
    numbers_to_guess_from = range(1, 1001)
elif ask_range == "10000":
    numbers_to_guess_from = range(1, 10001)
elif ask_range == "100000":
    numbers_to_guess_from = range(1, 100001)
elif ask_range == "1000000":
    numbers_to_guess_from = range(1, 1000001)
elif ask_range == "10000000":
    numbers_to_guess_from = range(1, 10000001)
elif ask_range == "100000000":
    numbers_to_guess_from = range(1, 100000001)
elif ask_range == "1000000000":
    numbers_to_guess_from = range(1, 1000000001)
elif ask_range == "10000000000":
    numbers_to_guess_from = range(1, 10000000001)
elif ask_range == "100000000000":
    numbers_to_guess_from = range(1, 100000000001)
else:
    print("Please try again.")
    ask_range = input(
        "What is the range of numbers you want to guess\nfrom?\n\nOptions: 10, 100, 1000, 10000, 100000,\n1000000, 10000000, 100000000, 1000000000,\n10000000000, 100000000000\n")

    if ask_range == "10":
        numbers_to_guess_from = range(1, 11)
    elif ask_range == "100":
        numbers_to_guess_from = range(1, 101)
    elif ask_range == "1000":
        numbers_to_guess_from = range(1, 1001)
    elif ask_range == "10000":
        numbers_to_guess_from = range(1, 10001)
    elif ask_range == "100000":
        numbers_to_guess_from = range(1, 100001)
    elif ask_range == "1000000":
        numbers_to_guess_from = range(1, 1000001)
    elif ask_range == "10000000":
        numbers_to_guess_from = range(1, 10000001)
    elif ask_range == "100000000":
        numbers_to_guess_from = range(1, 100000001)
    elif ask_range == "1000000000":
        numbers_to_guess_from = range(1, 1000000001)
    elif ask_range == "10000000000":
        numbers_to_guess_from = range(1, 10000000001)
    elif ask_range == "100000000000":
        numbers_to_guess_from = range(1, 100000000001)
    else:
        print("Sorry, but your request is unavailable. the range is now set to 1-10.")
        numbers_to_guess_from = range(1, 11)

number = random.choice(numbers_to_guess_from)
number_of_guesses = 0
while True:
    guess = int(input("Guess a number: "))
    number_of_guesses += 1
    if guess == number:
        print("You guessed the right number! It took you " + str(number_of_guesses) + " guesses!")
        break
    elif guess > number:
        print("Your guess is too high!")
    elif guess < number:
        print("Your guess is too low!")

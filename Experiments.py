import random

my_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# Get a list of all keys in the dictionary
keys = list(my_dict.keys())

# Select a random key from the list
random_key = random.choice(keys)

# Get the value associated with the random key
random_value = my_dict[random_key]

print("Random key:", random_key)
print("Random value:", random_value)
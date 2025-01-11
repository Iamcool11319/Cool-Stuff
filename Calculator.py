def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


keys = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

action = input("Action: ")
print(keys[action](int(input("First number: ")), int(input("Second number: "))))

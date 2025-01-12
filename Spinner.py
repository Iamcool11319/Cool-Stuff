import random

things = []
while True:
    add = input("What do you want to add? ('$stop' to stop)\n")
    if add == '$stop':
        break
    things.append(add)
while True:
    spin = input("Spin? (y, n)\n")
    if spin == 'y':
        print(random.choice(things))
    if spin == 'n':
        break

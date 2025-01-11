inputs = input("Enter the numbers with spaces in between\n").split()

total = 0
number_of_inputs = 0
for input in inputs:
    total += int(input)
    number_of_inputs += 1
average = total / number_of_inputs
rounded_average = round(average)
print(f'''total = {total}
number of inputs = {number_of_inputs}
average = {average}
rounded average = {rounded_average}''')

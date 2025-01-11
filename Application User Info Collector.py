while True:
    print("Welcome to the application!")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    password = input("Password: ")
    phone_number = input("Phone number: ")

    print(f'''
  Name: {name}
  Age: {age}
  Email: {email}
  Password: {password}
  Phone Number: {phone_number}''')
    confirmation = input("Is this correct? (y/n)")
    if confirmation == "y":
        print("Thank you for signing up!")
        break
    if confirmation == "n":
        print("Please try again.")

while True:
    secret_message = input('Message: ')
    password = input("What will you set the password as?\n")
    print("\n" * 1000)
    reveal_secret_message = input('Secret Password: ')
    if reveal_secret_message == password:
        print(secret_message)

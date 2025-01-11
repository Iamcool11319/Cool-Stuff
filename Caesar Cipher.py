alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

while True:
    new_message = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        for letter in text:
            if letter not in alphabet:
                new_message.append(letter)
            else:
                new_letter = alphabet.index(letter) + shift
                new_message.append(alphabet[new_letter])
    elif direction == 'decode':
        for letter in text:
            if letter not in alphabet:
                new_message.append(letter)
            else:
                new_letter = alphabet.index(letter) - shift
                new_message.append(alphabet[new_letter])
    print(''.join(new_message))
    again = input("Go again?\n")
    if again == 'no':
        break

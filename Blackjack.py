import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
bank = 1000
print("Welcome to Blackjack")
while True:
    start_game = input('''
    Would you like to play? (y, n)
    ''')
    if start_game == 'y':
        your_cards = []
        computers_cards = []
        bet = int(input(f'''
        Bank: {bank}
        How much will you bet? (1, 5, 25, 50, 100, 500, 1000)
        '''))
        your_cards.append(random.choice(cards))
        your_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))
        computers_cards.append(random.choice(cards))
        print(f'''
        Your cards: {your_cards}, {sum(your_cards)}
        Computer's first card: {computers_cards[0]}
    ''')
        while True:
            another_card = input("Hit or stand? (h, s)")
            if another_card == 'h':
                your_cards.append(random.choice(cards))
                print(f'''
                Your_cards: {your_cards}, {sum(your_cards)}
                Computer's first card: {computers_cards[0]}
                ''')
            if sum(computers_cards) < 17:
                computers_cards.append(random.choice(cards))
                if sum(computers_cards) > 21:
                    print(f'''
                    Computer bust
                    Your cards: {your_cards}, {sum(your_cards)}
                    Computer's cards: {computers_cards}, {sum(computers_cards)}
                    You won!
                    ''')
                    bank += bet
                    break
            if sum(your_cards) > 21:
                print(f'''
                Bust
                Your cards: {your_cards}, {sum(your_cards)}
                Computer's cards: {computers_cards}, {sum(computers_cards)}
                You lost!
                ''')
                bank -= bet
                break
            if another_card == 's':
                print(sum(your_cards))
                print(sum(computers_cards))
                your_distance = 21 - sum(your_cards)
                computers_distance = 21 - sum(computers_cards)
                if your_distance < computers_distance:
                    print("You won!")
                    bank += bet
                elif your_distance > computers_distance:
                    print("You lost!")
                    bank -= bet
                elif your_distance == computers_distance:
                    print("Draw")
                break
    elif start_game == 'n':
        break
    else:
        print("I don't understand. Please try again.")

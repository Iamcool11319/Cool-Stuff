print("Welcome to the Rock Paper Scissors!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

span = 0
wins = 0
while span <= 10:
    print("Rock, paper, scissors, shoot!")
    computor = random.randint(0, 2)
    strplayer = input("Type 0 for rock, 1 for paper, and 2 for scissors\n")
    player = int(strplayer)
    print("Rock, Paper, Scissors, shoot!")
    if computor == 0 and player == 0:
        print(f"Computer chose:\n{rock}\nYou chose:\n{rock}\nTie")
    if computor == 0 and player == 1:
        print(f"Computer chose:\n{rock}\nYou chose:\n{paper}\nYou win!")
        wins += 1
    if computor == 0 and player == 2:
        print(f"Computer chose:\n{rock}\nYou chose:\n{scissors}\nYou lose.")
    if computor == 1 and player == 0:
        print(f"Computer chose:\n{paper}\nYou chose:\n{rock}\nYou lose.")
    if computor == 1 and player == 1:
        print(f"Computer chose:\n{paper}\nYou chose:\n{paper}\nTie")
    if computor == 1 and player == 2:
        print(f"Computer chose:\n{paper}\nYou chose:\n{scissors}\nYou win!")
        wins += 1
    if computor == 2 and player == 0:
        print(f"Computer chose:\n{scissors}\nYou chose:\n{rock}\nYou win!")
        wins += 1
    if computor == 2 and player == 1:
        print(f"Computer chose:\n{scissors}\nYou chose:\n{paper}\nYou lose.")
    if computor == 2 and player == 2:
        print(f"Computer chose:\n{scissors}\nYou chose:\n{scissors}\nTie")
    span += 1
win_percentage = (wins / 10) * 100
print(f"You win {win_percentage}% of the time")

your_score = 0
opponent_score = 0
print(
    "Directions: 'y' = your point, 'o' = opponent's \npoint\n type 'quit' 2 times to quit\n click enter to add the points\n")
while True:
    score = f"{your_score} - {opponent_score}"
    print("\nSCOREBOARD\n" + score)
    add_score = input("Add point: ")
    how_many_points = input("How many points?\n")
    if add_score == "y":
        your_score += int(how_many_points)
    if add_score == "o":
        opponent_score += int(how_many_points)
    if add_score == "quit":
        print("FINAL SCORE\n" + score)
        break

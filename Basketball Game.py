print('''                  .
                         ,-; . ,
                ________i_,',//
          _odHHHHHHHHHHHHHHHHbo_
        dP^'         ;.| ||,; `^?b
       |H           ))`'||/';    H|
        ?bo.     .=;'   |||.' ,odP
          `?oo.-','     ||'oodP'
            /'  /      / |/
           |   |    _-'  ||
          ||  |   ,'     J|
          | \ |   |     / |
           |_\ L  L  .-' |
            \.)`-.;-;__./
              "-._;_.-"''')
print(
    "You are about to face off against your biggest opponent in NBA! Good luck!"
)
play1 = input(
    "You have the ball. A big fat guy is guarding you. Will you 'a'. dribble past him, or 'b'. take the shot?"
)
if play1 == "b":
    print(
        "You missed the shot, and the coach yells at you for taking such a far shot, and you are to sit out for the rest of the big game."
    )
if play1 == "a":
    play2 = input(
        "You've dribbled past him, and got into the three-point line. All of a sudden, the other team starts quintiple teaming you. Will you a. pass the ball, or b. shoot it, or c. try to dribble out?"
    )
    if play2 == 'b':
        print(
            "The ball bounced and bounced out. How close! The other team grabs the rebound and dribbles down."
        )
        play3 = input(
            "Will you a. guard your man, or b. get off of your man and guard ball?"
        )
        if play3 == 'b':
            print(
                "The person who has the ball passes to the open opponent you were guarding, and the other team scores. Your coach yells at you and you are to sit out for the rest of the big game."
            )
        if play3 == 'a':
            print(
                "When the person who has the ball passes, you intercept the ball! Great job!"
            )
            play4 = input(
                "The first quarter is about to end with 10 seconds left! Your opponent team is winning 6-0! You have to score something in the first quarter or you will lose for sure! Will you a. shoot a half court, b. dribble very quickly down and shoot a three, c. dribble as fast as possible down and shoot a easy layup?"
            )
            if play4 == 'a':
                print(
                    "You airball the half court. You, humiliated, gets yelled at by the coach. You are to sit out for the rest of the big game."
                )
            if play4 == 'c':
                print(
                    "You run out of time. Your coach yells at you for trying to shoot a layup when there's 10 seconds left! You are to sit out for the rest of the game."
                )
            if play4 == 'b':
                print(
                    "OOOOOOH! YOU MADE THE BUZZERBEATER THREE! GOOD JOB! Now that you made that, you might have a chance!"
                )
            print(
                "At the end of the game, your team won 117 to 114. What a close game! If it weren't for your great playing at the beginning, your team wouldn't have won. Congratulations! Your teammates throw a big party for you and you are very happy."
            )
    if play2 == 'c':
        print("The other team steals the ball and dribbles down.")
        play3 = input(
            "Will you a. guard your man, or b. get off of your man and guard ball?"
        )
        if play3 == 'b':
            print(
                "The person who has the ball passes to the open opponent you were guarding, and the other team scores. Your coach yells at you and you are to sit out for the rest of the big game."
            )
        if play3 == 'a':
            print(
                "When the person who has the ball passes, you intercept the ball! Great job!"
            )
            play4 = input(
                "The first quarter is about to end with 10 seconds left! Your opponent team is winning 6-0! You have to score something in the first quarter or you will lose for sure! Will you a. shoot a half court, b. dribble very quickly down and shoot a three, c. dribble as fast as possible down and shoot a easy layup?"
            )
            if play4 == 'a':
                print(
                    "You airball the half court. You, humiliated, gets yelled at by the coach. You are to sit out for the rest of the big game."
                )
            if play4 == 'c':
                print(
                    "You run out of time. Your coach yells at you for trying to shoot a layup when there's 10 seconds left! You are to sit out for the rest of the game."
                )
            if play4 == 'b':
                print(
                    "OOOOOOH! YOU MADE THE BUZZERBEATER THREE! GOOD JOB! Now that you made that, you might have a chance!"
                )
            print(
                "At the end of the game, your team won 117 to 114. What a close game! If it weren't that three at the beginning, your team wouldn't have won. Congratulations! Your teammates throw a big party for you and you are very happy."
            )
    if play2 == 'a':
        print("Great pass! Your teammate catches the ball and scores.")
        print(
            "At the end of the game, you, tired, sit on the bench. Your team won 116 to 114! If it weren't for your great playing at the beginning, your team wouldn't have won. Congratulations! Your teammates throw a big party for you and you are very happy."
        )

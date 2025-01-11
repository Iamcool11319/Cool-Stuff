print("Welcome to the Win Percentage Calculator")
pct1 = float(input("Enter the overall win percentage this season of one team:\n"))
pct2 = float(input("Enter the overall win percentage this season of the other:\n"))
in_all = pct1 + pct2
average_without_home = pct1 / in_all * 100
other_average = pct2 / in_all * 100
home = input("Which team is the home team? ('1' for the team you want to win, '2' for the other one:\n")
if home == '1':
    home_advantage = other_average * 10.11 / 100
    print(f"The percentage of the team you want to win winning is {average_without_home + home_advantage}%")
if home == '2':
    home_advantage = average_without_home * 10.11 / 100
    print(f"The percentage of the team you want to win winning is {average_without_home - home_advantage}%")
if home == '':
    print(f"The percentage of the team you want to win winning is {average_without_home}%")

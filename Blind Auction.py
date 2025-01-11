auction = {}
while True:
    name = input("Name:\n")
    bid = int(input("Bid:\n"))
    auction[name] = bid
    bidder_check = input("More bidders?\n")
    if bidder_check == 'no':
        break

highest_bid = 0
winner = ""

for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid = auction[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}

bidding_finished = False

def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amt = bidding_record[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
    
    print(f"The winner is {winner}, and the bid amount is {highest_bid}")

while not bidding_finished:
    name = input("What is your name :")
    price = int(input("What is you price $"))
    bids[name] = price
    should_continue = input("Are there any other bidders, type \"yes\" or \"no\" ")
    if should_continue == "no":
        bidding_finished = True
        find_winner(bids)
        



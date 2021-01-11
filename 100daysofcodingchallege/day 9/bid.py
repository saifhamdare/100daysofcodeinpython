from replit import clear
from art import logo
print(logo)
bids={}
bidding_finished=False

def find_highest_bidder(bid_record):
  highest_bid=0
  winner=""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount>highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"the winner is {winner} with a bid of ${highest_bid}")


#HINT: You can call clear() to clear the output in the console.

while not bidding_finished:
  name=input("what is Your Name?: ")
  price=int(input("what's your bid?: "))
  bids[name]=price
  should_continue=input("is there any other bid?Type yes Or no: \n ")
  if should_continue=="no":
    bidding_finished=True
    find_highest_bidder(bids)
  elif should_continue=="yes":
    clear()

  
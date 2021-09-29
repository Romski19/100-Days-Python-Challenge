from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
  
dict_bid = []
no_other_user = True
while no_other_user:
 
  name = input("Please provide your name: ").lower()
  bid_price = int(input("How much is your bid price?:$ "))
  new_dict_bid = {}
  new_dict_bid["name"] = name
  new_dict_bid["price"] = bid_price
  dict_bid.append(new_dict_bid)

  other_user = input("Is there any other bidder?Y/N: ").lower()
  if other_user == "n":
    no_other_user = False
    max_num = dict_bid[0]["price"]
    for dict_names in dict_bid:
      if dict_names["price"] > max_num:
        max_num = dict_names["price"]
        max_name = dict_names["name"]
    print(f"The winner of the bid is: {max_name} \n With bidding price: $ {max_num}")

  else:
    clear()


#Angela yu's solution:


def find_highest_bidder(bidding_record):
  highest_bid = 
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount  
      winner = bidder
  print(f"The winner is {winner} with the highest bid amount of {highest_bid}")

bids = {}
bidding_done = False
while not bidding_done:
  name = input("Input name:")
  price = input("Input bid:")
  bids[name] = price
  to_continue = input("Is there any other bidders?Y/N: ")

  if to_continue == "no":
    bidding_done = True
    find_highest_bidder(bidding_record=bids)
  else:
    clear()

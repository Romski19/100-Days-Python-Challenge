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

    

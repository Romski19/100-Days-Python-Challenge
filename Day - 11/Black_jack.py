import random
from art import logo
from replit import clear

def deal_cards(user_cards, comp_cards):
  if comp_cards == 21:
    print(computer)
    print(user)
    print("You lose")
  elif user_cards == comp_cards:
    print(computer)
    print(user)
    print("Draw")
  elif user_cards > comp_cards and user_cards < 21:
    print(computer)
    print(user)
    print("You win")
  elif comp_cards > user_cards and comp_cards < 21:
    print(computer)
    print(user)
    print("You lose")
  elif comp_cards > 21 and user_cards > 21:
    if comp_cards < user_cards:
      print(computer)
      print(user)
      print("You lose")
    elif user_cards < comp_cards:
      print(computer)
      print(user)
      print("You win")
  elif user_cards < 21 and comp_cards > 21:
    print("You win")
  elif comp_cards < 21 and user_cards > 21:
    print("You lose")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = random.sample(cards, 2)
computer = random.sample(cards, 2)
sum_user = sum(user)
sum_comp = sum(computer)
first_card_comp = computer[0]

play_game = True
while play_game:
  to_play = input("Do you want to play a game of Black Jack? y/n: ").lower()

  if to_play == "y":
    clear()
    print(logo)
    print(f"Your card is {user}, current score is: {sum_user}")
    print(f"Computer's first card: {first_card_comp}")

    draw_card = input("Type 'y' to get another card, 'n' to pass: ").lower()

    if draw_card == 'y':
      get1 = random.choice(cards)
      user.append(get1)
      sum_user= sum(user)
      deal_cards(sum_user, sum_comp)
    else:
      deal_cards(sum_user, sum_comp)

    print(sum_comp)
    print(sum_user)

  else:
    play_game = False
  

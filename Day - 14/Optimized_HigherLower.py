from game_data import data
import random
from art import logo
from replit import clear

def format_data(account):
  """format the account data"""
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from account_country"


def check_answer(guess, a_follower, b_follower):
  """checking answering if correct"""
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
should_continue = True
account_b = random.choice(data)


while should_continue:
  
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)


  print(f"Compare A: {format_data(account_a)}.")
  print("VERSUS")
  print(f"Against B: {format_data(account_b)}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"Correct! Your current score is: {score}")
  else:
    should_continue = False
    print(f"Wrong! Your final score is: {score}")
    
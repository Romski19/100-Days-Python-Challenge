import random
from art import logo
print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def the_round(number_random, user_life):
  life_attempts = user_life
  off_loop = True
  while life_attempts > 0 and off_loop:
    user_number = int(input("Make a guess: "))
    if number_random > user_number:
      life_attempts -= 1
      if life_attempts == 0:
        print("Too Low")
        print("You've run out of guess")
        
      else:
        print("Too low")
        print("Gues Again.")
        print(f"You have {life_attempts} remaining to guess the number")
    elif number_random < user_number:
      life_attempts -= 1
      if life_attempts == 0:
        print("Too high")
        print("You've run out of guess")
      else:
        print("Too high")
        print("Gues Again.")
        print(f"You have {life_attempts} remaining to guess the number")
    else:
      print(f"You got it! the answer is {number_random}")
      off_loop = False
      return
    
  
  print(f"You Lost! the number is {number_random}")
  
the_number = random.randrange(1, 100)
print(f"Hint: the number is {the_number}")
if difficulty == "easy":
  live_attempts = 100
  the_round(the_number, live_attempts)
else:
  live_attempts = 10
  the_round(the_number, live_attempts)
from random import randint
from art import logo
print(logo)

HARD_TURN  = 10
EASY_TURN = 5

def check_guess(guess, thenumber, turns):
  if guess > thenumber:
    print("Too High")
    return turns - 1
  elif guess < thenumber:
    print("Too Low")
    return turns - 1
  else:
    print(f"You have guessed the number: {thenumber}")


def difficulty_level():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level =="easy":
    return EASY_TURN
  else:
    return HARD_TURN

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100!")

  answer = randint(1,100)
  print(f"Hint: The number is {answer}")

  turns = difficulty_level()
  guess = 0
  while guess != answer:
    print(f"You have {turns} remaining to guess the number")
    guess = int(input("Make a guess: "))
    turns = check_guess(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose")
      return
    elif guess != answer:
      print("Guess Again.")

game()
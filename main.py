#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
randomword = random.choice(word_list)

chosen = input("Select a letter: ").lower()

for letter in randomword:
  if letter == chosen:
    print("Yes")
    print(letter)
  else:
    print("No")
    print(letter)
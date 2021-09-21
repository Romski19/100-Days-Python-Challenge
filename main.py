import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock,paper,scissors]
chosen = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))
versus_comp = random.randint(0,2)


if chosen >= 3 or chosen < 0:
  print("Invalid Tanga!")
else:

  print(game_image[chosen])
  versus_comp = random.randint(0,2)
  print(f"Computer choose: \n {game_image[versus_comp]}")

  if chosen == versus_comp:
    print("It's a draw!")
  elif chosen == 0 and versus_comp == 2:
    print("You win!")
  elif versus_comp == 0 and chosen == 2:
    print("You lose!")
  elif chosen > versus_comp:
    print("You win!")
  elif versus_comp > chosen:
    print("You lose!")
  else:
    print("It's a draw!")


# if chosen == 0:
#   print(rock)
#   if versus_comp == 0:
#     print(f"Computer chose: \n{rock}\n It's a Tie!" )
#   elif versus_comp == 1:
#     print(f"Computer chose: \n{paper}\n You lose!" )
#   else:
#     print(f"Computer chose: \n{scissors}\n You Win!" )

# elif chosen == 1:
#   print(paper)
#   if versus_comp == 0:
#     print(f"Computer chose: \n{rock}\n  You Win!" )
#   elif versus_comp == 1:
#     print(f"Computer chose: \n{paper}\n It's a Tie!" )
#   else:
#     print(f"Computer chose: \n{scissors}\n You lose!" )

# elif chosen == 2:
#   print(scissors)
#   if versus_comp == 0:
#     print(f"Computer chose: \n{rock}\n  You lose!" )
#   elif versus_comp == 1:
#     print(f"Computer chose: \n{paper}\n You win!" )
#   else:
#     print(f"Computer chose: \n{scissors}\n It's a Tie!" )

# else:
#   print("booo! Tanga!") 
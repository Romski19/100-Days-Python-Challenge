import random
from art import logo
from game_data import data
from replit import clear



def compare(user,comp,score):
  user_num_followers = user['follower_count']
  comp_num_followers = comp['follower_count']
  if user_num_followers > comp_num_followers:
    score +=1
    to_continue = True
    return score, to_continue
  else:
    to_continue = False
    return score, to_continue



def user_choice_compare(a_data,b_data):
  user_choice = input("Who has more followers, type 'A' or 'B': ").lower()
  if user_choice == "a":
    user_choice = a_data
    comp_choice = b_data
    return user_choice, comp_choice
  else:
    user_choice = b_data
    comp_choice = a_data
    return user_choice, comp_choice
    
def game():
  a_random = random.randint(0,49)
  b_random = random.randint(0,49)
  this_a = data[a_random]
  this_b = data[b_random]
  until_not = 0
  user_score = 0
  while until_not == 0:
    print(f"Compare A: {this_a['name']}, {this_a['description']}, {this_b['country']}")
    print("VERSUS")
    print(f"Against B: {this_b['name']}, {this_b['description']}, {this_b['country']}")
    user_chosen = user_choice_compare(this_a,this_b)
    user = user_chosen[0]
    comp = user_chosen[1]
    cur_score, continue_this = compare(user,comp,user_score)
    if continue_this == False:
      print(f"Wrong answer! You're total score is: {cur_score}")
      return
    elif continue_this == True:
      this_a = this_b
      new_b_random = random.randint(1,50)
      this_b = data[new_b_random]
      user_score = cur_score
      clear()
      print(f"current score: {user_score}")
print(logo)
game()




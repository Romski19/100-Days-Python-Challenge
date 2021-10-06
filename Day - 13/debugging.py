############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   """ before: range(1, 20) """
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()



# Reproduce the Bug
# """before dice_num = randint(1,6)"""
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5)
# # dice_num = 6 - to reproduce
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# """before: if year > 1980 and year < 1994: - no result"""
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# Before fixing the code:
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# after fixing:
# age = int(input("How old are you?: "))
# if age > 18:
#   print(f"You can drive at age {age}.")
# else:
#   print("You can drive if you're over 18 years old.")

# #Print is Your Friend
# # before - word_per_page == int(input("Number of words per page: "))
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
#before - b_list.append(new_item) - is not indented or not inside the For loop
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
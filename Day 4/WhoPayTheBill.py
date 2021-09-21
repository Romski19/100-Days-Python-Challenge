import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_elements = len(names)
rand_num = random.randint(0, number_of_elements - 1)

paidby = names[rand_num]

print(f"{paidby} is going to buy the meal today")
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1 + name2
lower_case_names = names.lower()

result1 = 0
result2 = 0

t = lower_case_names.count("t")
r = lower_case_names.count("r")
u = lower_case_names.count("u")
e = lower_case_names.count("e")
  
result1 = t + r + u + e

l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v") 
e = lower_case_names.count("e")
 
result2 = l + o + v + e

result = int('{}{}'.format(result1,result2))

if result < 10 or result > 90:
  print(f"Your score is {result}. you go together like coke and mentos.")
elif result >= 40 and result <= 50:
  print(f"Your score is {result}. you are alright together.")
else:
  print(f"Your score is {result}.")
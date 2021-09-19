# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_left =  ((90 - int(age) ) * 365)
weeks_left = round(days_left / 7)
months_left = (90 - int(age)) * 12 

print(f"You have {days_left} days OR {weeks_left} weeks OR {months_left} months left")

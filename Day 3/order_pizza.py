# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

Pizza_Price = 0


if size == "S":
  Pizza_Price += 15
elif size == "M":
  Pizza_Price += 20
else:
  Pizza_Price += 25


if add_pepperoni == "Y":
    if size == "S"
      Pizza_Price += 2
    else:
      Pizza_Price += 3


if extra_cheese == "Y":
  Pizza_Price += 1

print(f"Your final bill is: ${Pizza_Price}")
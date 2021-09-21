# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇



hor = int(position[0]) - 1
ver = int(position[1]) - 1

if hor <= -1 or hor >= 3:
  print("wrong number")
elif ver <= -1 or ver >= 3:
  print("wrong number")
else:
  map[hor][ver] = "X"
  
#Write your code above this row 👆

  print(f"{row1}\n{row2}\n{row3}")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
#without using sum() and len()
total_height = 0
for x in student_heights:
  total_height += x 
average_height = round(total_height /(n + 1))
print(average_height)

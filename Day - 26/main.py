with open("file1.txt") as f1:
    list1 = f1.read().splitlines()
with open("file2.txt") as f2:
    list2 = f2.read().splitlines()

result = [x for x in list1 if x in list2]

# Write your code above 👆
print(result)



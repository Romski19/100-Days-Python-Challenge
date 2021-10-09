def all_equal(numbers):
    counter =0
    if numbers == []:
      return True
    else:
      for x in range(len(numbers)):
          temp = numbers[0]
          if numbers[x] == temp:
              counter +=1
              if counter == len(numbers):
                  return True
          else:
              return False
all_equal([1, 2 , 1])


# other solution

# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)
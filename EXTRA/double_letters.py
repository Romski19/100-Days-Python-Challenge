def double_letters(check_string):
    first_list = list(check_string)
    compare_list = list(check_string)
    if len(compare_list) <= 0:
      return False
    else:
      compare = compare_list[0]
      compare_list.remove(compare)
      let_num = len(compare_list)
      y = 0
      while compare_list[y] != first_list[y]:
          y +=1
          if y == let_num:
              return False
      return True

double_letters("Hello")
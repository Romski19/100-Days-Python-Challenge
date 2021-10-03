def add_dots(word_sample):
    new_word = []
    number_of_letters = len(word_sample)
    for x in range(number_of_letters):
        new_word += word_sample[x]        
        new_word += "."
    if len(new_word) <= 0:
        return False
    else:
        new_word.pop()
        added_dots = ''.join(new_word)
        return added_dots

def remove_dots(rem_dots):
    removed_dots = rem_dots.replace(".","")
    print(removed_dots)
  
          
remove_dots(add_dots("tested"))


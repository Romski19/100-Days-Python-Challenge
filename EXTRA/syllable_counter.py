def count(word):
    to_list = list(word)
    num_word = len(word) - 1
    counter = 1
    for x in range(num_word):
      if to_list[x] == "-":
        counter +=1
    return counter

count("ca-ter-pi-llar")
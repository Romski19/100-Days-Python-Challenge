def capital_indexes(thestring):
    final_list = []
    num_letters = len(thestring)
    for x in range(num_letters):
        if thestring[x].isupper():
            final_list.append(x)
    return final_list
            
capital_indexes("hElLo")

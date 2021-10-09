def triple_and(one,two,three):
    if one == True and two == True and three == True:
        return True
    else:
        return False
triple_and(True,False,True)
# other short hand
def triple_and(a, b, c):
    return a and b and c
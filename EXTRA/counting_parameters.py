# # Challenge
# Challenge
# Counting parameters
# Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.


# My solution is the same as the solution from challenger

def param_count(*param):
    return len(param)
param_count()


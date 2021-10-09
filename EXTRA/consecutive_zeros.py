def consecutive_zeros(binary):
    listed = []
    count = 0 
    for x in range(len(binary)):
        if binary[x] == "0":
            count +=1
        else:
             count = 0
             
        listed.append(count)
    return max(listed)           
consecutive_zeros("1001101000110")


# other solution
# naive solution
def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

# shorter solution
def consecutive_zeros(bin_str):
    return max([len(s) for s in bin_str.split("1")])
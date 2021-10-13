letters = ['1','0','0','0','0','0']

print([x for y in (letters[i:i+3] + ['x'] * (i < len(letters) - 2) for i in range(0, len(letters), 3)) for x in y])

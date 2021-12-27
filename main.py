# letters = ['1','0','0','0','0','0']
#
# print([x for y in (letters[i:i+3] + ['x'] * (i < len(letters) - 2) for i in range(0, len(letters), 3)) for x in y])
#
# print(sum(x for x in range(334,365)))

# for x in range(334, 365):
#     print(x)
# sum = 0
# for x in range(334, 365):
#     sum += x
# print(sum)

# Saving Money in year 2022- Increment every 1 per day

days = [x for x in range(1, 366)]
length = len(days)

y = 31
g = 30
x = 28

j = days[0:y]
f = days[y:y + x]
m = days[f[x - 1]:f[x - 1] + y]
ap = days[m[g]:m[g] + g]
ma = days[ap[g - 1]:ap[g - 1] + y]
jn = days[ma[g]:ma[g] + g]
jl = days[jn[g - 1]:jn[g - 1] + y]
au = days[jl[g - 1]:jl[g - 1] + y]
s = days[au[g]:au[g] + g]
o = days[s[g - 1]:s[g - 1] + y]
n = days[o[g]:o[g] + g]
d = days[n[g - 1]:n[g - 1] + y]

print(f"total save: ",
      sum([sum(j), sum(f), sum(m), sum(ap), sum(ma), sum(jn), sum(jl), sum(au), sum(s), sum(o), sum(n), sum(d)]))

print(f"month of January: ", (sum(j)))
print(f"month of February: ", (sum(f)))
print(f"month of March:", (sum(m)))
print(f"month of April: ", (sum(ap)))
print(f"month of May: ", (sum(ma)))
print(f"month of June: ", (sum(jn)))
print(f"month of July: ", (sum(jl)))
print(f"month of August: ", (sum(au)))
print(f"month of September: ", (sum(s)))
print(f"month of October: ", (sum(o)))
print(f"month of November: ", (sum(n)))
print(f"month of December: ", (sum(d)))

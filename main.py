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

# days = [x for x in range(1, 366)]
# length = len(days)
#
# y = 31
# g = 30
# x = 28
#
# j = days[0:y]
# f = days[y:y + x]
# m = days[f[x - 1]:f[x - 1] + y]
# ap = days[m[g]:m[g] + g]
# ma = days[ap[g - 1]:ap[g - 1] + y]
# jn = days[ma[g]:ma[g] + g]
# jl = days[jn[g - 1]:jn[g - 1] + y]
# au = days[jl[g - 1]:jl[g - 1] + y]
# s = days[au[g]:au[g] + g]
# o = days[s[g - 1]:s[g - 1] + y]
# n = days[o[g]:o[g] + g]
# d = days[n[g - 1]:n[g - 1] + y]

# print(f"total save: ",
#       sum([sum(j), sum(f), sum(m), sum(ap), sum(ma), sum(jn), sum(jl), sum(au), sum(s), sum(o), sum(n), sum(d)]))
#
# print(f"month of January: ", (sum(j)))
# print(f"month of February: ", (sum(f)))
# print(f"month of March:", (sum(m)))
# print(f"month of April: ", (sum(ap)))
# print(f"month of May: ", (sum(ma)))
# print(f"month of June: ", (sum(jn)))
# print(f"month of July: ", (sum(jl)))
# print(f"month of August: ", (sum(au)))
# print(f"month of September: ", (sum(s)))
# print(f"month of October: ", (sum(o)))
# print(f"month of November: ", (sum(n)))
# print(f"month of December: ", (sum(d)))


# from calendar import monthrange, month_name
#
# month_name = list(month_name[1:])
# days = [x for x in range(1, 366)]
#
# month_days = []
# for month in month_name:
#     month_days.append(monthrange(2021, list(month_name).index(month) + 1)[1])
#
# print("Total Saved:", sum([sum(days[sum(month_days[:i]):sum(month_days[:i+1])]) for i, j in enumerate(month_days)]))
# print([sum(days[sum(month_days[:i]):sum(month_days[:i+1])]) for i, j in enumerate(month_days)])

# from calendar import monthrange
#
# days_in_month = [monthrange(2021, m)[1] for m in range(1, 13)]
# monthly_totals = []
# daynum = 0
# for month in range(1, 13):
#     month_total = 0
#     for day in range(1, days_in_month[month - 1] + 1):
#         daynum += 1
#         month_total += daynum
#     monthly_totals.append(month_total)
#
# print(monthly_totals)
# print(sum(monthly_totals))


from calendar import monthrange, isleap
from itertools import accumulate


def save(y):
    d_in_m = [0] + [monthrange(y, m)[1] for m in range(1, 13)]
    cum_d = list(accumulate(d_in_m))
    daily = range(1, 367 if isleap(y) else 366)
    return [sum(daily[cum_d[m]: cum_d[m + 1]]) for m in range(12)]


year = 2021
res = save(year)
print(res)
print(sum(res))

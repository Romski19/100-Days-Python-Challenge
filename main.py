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

# import os
# from calendar import monthrange, isleap
# from itertools import accumulate

# db_pass = os.environ["DB_PASS"]

# print(db_pass)


# def save(y):
#     d_in_m = [0] + [monthrange(y, m)[1] for m in range(1, 13)]
#     cum_d = list(accumulate(d_in_m))
#     daily = range(1, 367 if isleap(y) else 366)
#     return [sum(daily[cum_d[m]: cum_d[m + 1]]) for m in range(12)]
#
#
# year = 2021
# res = save(year)
# print(res)
# print(sum(res))

# mp2_object = \
#     dict(January=1.00, February=0.92, March=0.83, April=0.75, May=0.67, June=0.58, July=0.50, August=0.42,
#          September=0.33, October=0.25, November=0.17, December=0.08)
#
# monthly_contri = 50000.00
# dividend = 0.07
# v = []
# for key, value in mp2_object.items():
#     x = value * monthly_contri
#     y = round(x * dividend, 2)
#     v.append(y)
#
# print(sum(v))
# import requests
# from datetime import datetime, timedelta


# TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
# TEQUILA_API_KEY = "0B-Jdrq704EiKJIYOC6KLoa6aaIrQFaR"

# header = {
#     "apikey": TEQUILA_API_KEY,
# }
# date_tom = datetime.now() + timedelta(days=1)
# date_42days = datetime.now() + timedelta(days=(6 * 30))

# parameters = {
#     "fly_from": "BKK",
#     "fly_to": "BER",
#     "date_from": date_tom.strftime("%d/%m/%Y"),
#     "date_to": date_42days.strftime("%d/%m/%Y"),
#     "curr": "USD",
#     "nights_in_dst_from": 3,
#     "nights_in_dst_to": 28,
#     "flight_type": "round",
#     "one_for_city": 1,
# }

# response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=header)
# number = 0
# data_now = response.json()["data"]
# for x in data_now:
#     number +=1
#     # print(x["cityCodeTo"])
#     # print(x["price"])
#     print(f"{number} : {x['price']}")
#     print(x["route"][0]["local_departure"].split("T")[0])
#     print(x["route"][1]["local_departure"].split("T")[0])

import requests

response = requests.get("https://catfact.ninja/fact")
cat = response.json()
print(cat.get('fact'))

#  Chalenge my self lotto RUMBLE
my_number = 589763
list_num = list(map(int,str(my_number)))    
winning_numbers = [819763,556879,638597,124578,668932]
won = []
winning_num = []

for x in range(len(winning_numbers)):
    list_win = list(map(int,str(winning_numbers[x])))
    num = len(list_win)
    for v in range(num):
        if list_num[v] in list_win:
           won.append(winning_numbers[x])        
    winning_num.append(won.count(winning_numbers[x]))


if 6 in winning_num:
    get_index = winning_num.index(6)
    print(f"the winning number if you rumble {my_number} is : {winning_numbers[get_index]}")


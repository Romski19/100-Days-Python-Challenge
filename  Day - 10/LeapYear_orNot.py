def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return "Leap year."
    return "Leap year."

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  the_month = month - 1
  last_day = month_days[the_month]
  check_leap = is_leap(year)
  the_year = year
  if check_leap == "Leap year.":
    month_days[1] = 29
    last_day = month_days[the_month]
    print(check_leap)
    return f"end of the month is: {last_day} for the year: {the_year}"
  else:
    print("Not leap year")
    return f"end of the month is: {last_day} for the year: {the_year}"
    

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
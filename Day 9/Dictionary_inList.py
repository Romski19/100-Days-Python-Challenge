travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, num_visits,city):
  insert_dict = {"country": country, "visits": num_visits, "cities": city}
  travel_log.append(insert_dict.copy())
  
  # Angela Yu's solution
  
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = num_visits
  new_country["cities"] = city
  travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# My solution
new_country = travel_log[2]["country"]
new_visits = travel_log[2]["visits"]
new_city = travel_log[2]["cities"]

print(f"You've visited {new_country} {new_visits} times")
print(f"You've been to {new_city[0]} and {new_city[1]}.")







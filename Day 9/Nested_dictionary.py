# Nesting Dictionary in a Dictionary

philippines = {
  "cities": ["Manila", "Cebu", "Davao"],
  "France": {"cities_visited": ["Paris", "Lile", "Dijon"]}
}

# calling manila
print(philippines["cities"][0])
# calling Paris
print(philippines["France"]["cities_visited"][0])

# Nesting Dictionary in a List

travel_list =[
  {"country": "France", "cities_visitied":["Paris","Lile", "Dijon"], "numbers_visited": 12},
  {"place": "Germany", "cities_visitied":["Berlin","Manila", "Cebu"], "numbers_visited": 2},
]
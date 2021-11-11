# names = ["Alex", "Sam", "George", "Reynaldo", "Catherine","Penelope", "Wash"]
# students_score = {student:random.randint(1, 100) for student in names}
# passed_score = {student:score for (student, score) in students_score.items() if score >= 60}
#    Challenge  - 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {i: len(i) for i in sentence.split()}
# print(result)


# Challenge - 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}

print(weather_f)

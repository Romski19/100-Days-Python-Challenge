# with open("weather_data.csv", "r") as list_data:
#     data = list_data.readlines()

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     # one line below is to remove the first data in the row (next)
#     next(data_file)
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temperature.append(int(row[1]))
#     print(temperature)

# panda package - easy

import pandas

data = pandas.read_csv("weather_data.csv")
# data = data["temp"]
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# getting the average temp
# temp_list = data["temp"].tolist()
# num_of_temp = len(temp_list)
# old way
# average_temp = sum(temp_list) / num_of_temp
# print(average_temp)

# panda method way
# print(data['temp'].mean())

# maximum
# print(data['temp'].max())

# # calling series
# data.condition
# # the same with  - (Take note of syntax)
# data["condition"]

# getting data row (can be conditional)
# print(data[data.day == "Monday"])
# # getting all rows with above 20 temps
# print(data[data.temp > 20])
# # getting row with the maximum
# print(data[data.temp == data.temp.max()])

# pinpoint conditional
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # challenge - get monday temp and convert to fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp_far = (monday.temp * (9/5)) + 32
# print(monday_temp_far)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
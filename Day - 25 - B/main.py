import pandas
df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = df["Primary Fur Color"].dropna().unique().tolist()
counted = df["Primary Fur Color"].value_counts().tolist()

data_dict = {
    "Fur Color": colors,
    "Count": counted
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
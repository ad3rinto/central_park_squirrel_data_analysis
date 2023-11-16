import csv
import pandas as pd

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231115.csv", mode="r") as csvfile:
    data = pd.read_csv(csvfile)
    gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    # print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")

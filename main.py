import csv
import pandas as pd

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231115.csv", mode="r") as csvfile:
    data = pd.read_csv(csvfile)
    print(data["Primary Fur Color"].describe())

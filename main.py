# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
# sum = sum(temp_list)
# avg = sum/len(temp_list)
# print(avg)

print(data["temp"].max())

'''This version was made on Macbook Air to be pushed to github as a pull request to Jeff's repo.'''
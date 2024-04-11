# import csv
#
# with open("weather_data.csv") as data:
#     data_lines = csv.reader(data)
#     # you can loop through a csv reader objetc to get each line as a row
#
#     temperatures = []
#     for row in data_lines:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas as pd
table = pd.read_csv(("weather_data.csv"))
#
# temperature_series = table.temp
# temperature_list = temperature_series.to_list()
# print(temperature_series.nlargest()[temperature_series.nlargest().size + 1])

# access the table row when the day is Monday
# print(table[table.day == "Monday"])

# # access the table row when the temp is max
# day_table_with_highest_temp = table[table.temp == table.temp.max()]
# highest_temp = day_table_with_highest_temp.temp
# # (0°C * 9/5) + 32 = 32°F
# print((highest_temp[6] * 9/5) + 32)


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# loop through the primary fur series of the dataframe and increment each count, create a dictionary
fur_types = ['Gray', 'Cinnamon', 'Black']
fur_counts = [0, 0, 0]

fur_series = data["Primary Fur Color"]

for color in fur_series:
    if color == 'Gray':
        fur_counts[0] += 1
    if color == 'Cinnamon':
        fur_counts[1] += 1
    if color == 'Black':
        fur_counts[2] += 1

print(fur_counts)
dict = {

    'Fur': fur_types,
    'count': fur_counts
}

data_table = pd.DataFrame(dict)
data_table.to_csv("SQUIRRELS")
print(data_table)
# with open("weather_data.csv") as data_file:
#     content = data_file.readlines()
#     print(content)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# total = 0
# for i in temp_list:
#     total+=i
# average = total/len(temp_list)
# print(data["temp"].max())
# print(data["day"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
#
# print((monday.temp *9/5) +32)

# Create Data Frame from scratch

# data_dict = {
#     "students" : ["Stefan", "Bubuci", "Papaci"],
#     "scores": [99, 80,65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_csv.csv")

# Read Data
data = pandas.read_csv("squirrel_data.csv")
fur_color = data["Primary Fur Color"]

gray = fur_color[fur_color == "Gray"]
red = fur_color[fur_color == "Cinnamon"]
black = fur_color[fur_color == "Black"]


data_dict = {
    "fur color" : ["grey", "red", "black"],
    "count": [gray.count(), red.count(), black.count()],
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")


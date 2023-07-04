# # import csv (this is the harder non pandas way)

# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
#
# # import csv (this is the harder non pandas way)

# # #This converts the data into string we can loop through
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# Pandas method

#import the CSV From external file

# # import pandas

# #
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"]))
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # data_list = data["temp"].to_list()
#

# # # Average

# # print(data["temp"].mean())

# # # Max #

# # print(data["temp"].max())
# #

# # #Get data in columns

# # print(data["condition"])
# # print(data.condition)
#

# #Get data in a row

# # data_list = data["temp"].to_list()
#

# #Get row from the highest temp day

# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#

# # #Get data from 1 item in row monday condition

# # monday = data[data.day == "Monday"]
# # print(monday.temp * 9 / 5 + 32)
# #

# # #Create a dataframe from scratch

# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)

# # #Save data to csv file in the root folder

# # data.to_csv("new_data.csv")
# #
#
#

# #How many grey squirrels are there in central park?

#
#
#
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# Grey_Squirells = len(data[data["Primary Fur Color"] == "Gray"])
# Red_Squirells = len(data[data["Primary Fur Color"] == "Cinnamon"])
# Black_Squirells = len(data[data["Primary Fur Color"] == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "# Per Color": [Grey_Squirells, Red_Squirells, Black_Squirells]
# }
#

# #Very unsorted

# print(data_dict)
#

# #Turned into nice table

# Use both functions below to get the CSV out, you need to convert it to a data frame

# total = pandas.DataFrame(data_dict)
# total.to_csv("squirrel_count.csv")
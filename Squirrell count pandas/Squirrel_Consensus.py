#How many grey squirrels are there in central park?



import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Grey_Squirells = len(data[data["Primary Fur Color"] == "Gray"])
Red_Squirells = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_Squirells = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "# Per Color": [Grey_Squirells, Red_Squirells, Black_Squirells]
}

#Very unsorted
print(data_dict)

#Turned into nice table
total = pandas.DataFrame(data_dict)

total.to_csv("squirrel_count.csv")
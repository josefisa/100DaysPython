
""" Here a simple explanation how to read csv with Python """
# import csv
# with open("ProyectosIntermedios/Day-25-GuessStates_Pandas/weather_data.csv") as file:
#     weather_data = csv.reader(file)
#     next(weather_data)
#     temperature = [int(row[1]) for row in weather_data]
#     print(temperature)

""" Now lets use pandas """

# import pandas as pd

# data = pd.read_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/weather_data.csv")
# data['temp']

# tempt_list = data['temp'].to_list()
# print(len(tempt_list))
# ave_temp = data['temp'].mean()
# print(ave_temp)
# print(f"The maximun value is: {data['temp'].max()}")

# #Accessing the data in a data frame...
# print(data["condition"])
# print(data.condition)
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]

# data_dict = {
#     "students" : ["Amarna","Monica","Amaia"],
#     "scores" : [4.5,4.8,3.8]
# }
# new_data = pd.DataFrame(data_dict)
# new_data.to_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/new_data.csv")

""" Here starts the exploration of Great Squirrel Census Map """

import pandas as pd

data = pd.read_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = ['Gray', 'Cinnamon', 'Black']
number =[]
p_color = ['Gray', 'Red', 'Black']
for color in colors:
    number.append(len(data[data["Primary Fur Color"] == f"{color}"]))
        
# color_Dict['Red'] = color_Dict.pop('Cinnamon')
color_Dict = {'p_color': p_color, 'number' : number}
print(color_Dict)

color_DataFrame = pd.DataFrame(color_Dict)
color_DataFrame.to_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/Squirrels_Colors.csv")
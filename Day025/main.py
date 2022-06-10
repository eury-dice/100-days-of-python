import pandas
#
# WEATHER_PATH = "./weather_data.csv"
#
# data = pandas.read_csv(WEATHER_PATH)
#
# temp_list = data["temp"].to_list()
# print(f"Temperatures in a week: {temp_list}")
#
# ave_temp = data["temp"].mean()
# print(f"Average temperature: {ave_temp}")
#
# max_temp = data["temp"].max()
# print(f"Maximum Temperature: {max_temp}")
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# monday = data[data.day == "Monday"]
# temp_in_F = 9/5 * monday.temp[0] + 32
# print(f"Temp in Celsius: {monday.temp[0]}, Temp in Fahrenheit: {temp_in_F}")
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "grades": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
df = data["Primary Fur Color"].value_counts().reset_index()
df.columns = ["Fur Color", "Count"]
df.to_csv("squirrel_count.csv")

# # List Comprehension
#
# # Exercise 1 - Square the original list
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
# squared_numbers = [(n ** 2) for n in numbers]
# # Write your code 👆 above:
#
# print(squared_numbers)
#
# # Exercise 2 - Make a list containing only even numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
# result = [n for n in numbers if n % 2 == 0]
# # Write your code 👆 above:
#
# print(result)
#
# # Exercise 3 - Output a list with integers that match
#
# # Using multiple lines
# with open("file1.txt") as file1:
#     data1 = file1.readlines()
# with open("file2.txt") as file2:
#     data2 = file2.readlines()
#
# result = [int(n) for n in data1 if n in data2]
#
# # As a single line
# # result = [int(line) for line in open("file1.txt").readlines() if line in open("file2.txt")]
#
# print(result)
#
# # Dictionary Comprehension
#
# # Exercise 4 - Make each word of the sentence as a key, with its length as the value
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word: len(word) for word in sentence.split()}
# print(result)
#
# # Exercise 2 - Convert the temperatures in celsius to fahrenheit
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
# weather_f = {day:(9/5*temp_c + 32) for (day, temp_c) in weather_c.items()}
# print(weather_f)
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

df_student = pandas.DataFrame(student_dict)
print(df_student)

# for (key, value) in df_student.items():
#     print(value)

for (index, row) in df_student.iterrows():
    print(row.score)  # Each row is a panda.Series

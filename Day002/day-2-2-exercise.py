#BMI Calculator 1.0
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(float(weight) / (float(height) ** 2))

print(f'Your BMI is {bmi}')
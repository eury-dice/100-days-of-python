#Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Commented below is a quick way to compute the average
#average = round(sum(student_heights) / len(student_heights))

sum = 0
length = 0
for height in student_heights:
    sum += height
    length += 1

average = round(sum / length)
print(average)
#Highest Score 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = None

for score in student_scores:
    if max == None:
        max = score
    elif score > max:
        max = score

print(f'Highest Score: {max}')
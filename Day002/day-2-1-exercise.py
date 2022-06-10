#Add digits of 2-digit number
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

tens_digit = two_digit_number[0]
ones_digit = two_digit_number[1]

print(tens_digit + ' + ' + ones_digit + ' = ' + str(int(tens_digit) + int(ones_digit)))


#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# nr_password = []
# easy_password = ''

# for n in range(0, nr_letters):
#     char = random.choice(letters)
#     nr_password.append(char)
#     easy_password += char

# for n in range(0, nr_symbols):
#     char = random.choice(symbols)
#     nr_password.append(char)
#     easy_password += char

# for n in range(0, nr_numbers):
#     char = random.choice(numbers)
#     nr_password.append(char)
#     easy_password += char


# print('Here is your password (Easy): ' + easy_password)

# hard_password = ''
# pass_length = len(nr_password)
# new_length = pass_length - 1

# for n in range(0, pass_length):
#     index = random.randint(0, new_length)
#     hard_password += nr_password.pop(index)
#     new_length -= 1

# print('Here is your password (Hard): ' + hard_password)

rand_letters = ''.join(random.choices(letters, k=nr_letters))
rand_symbols = ''.join(random.choices(symbols, k=nr_symbols))
rand_numbers = ''.join(random.choices(numbers, k=nr_numbers))

easy_password = rand_letters + rand_symbols + rand_numbers

print('Here is your (unscrambled) password: ' + easy_password)

hard_password = ''.join(random.sample(easy_password, len(easy_password)))
print('Here is your random password: ' + hard_password)
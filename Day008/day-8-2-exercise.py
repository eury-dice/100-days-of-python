#Prime Number Checker
#Write your code below this line 👇
import math
def prime_checker(number):
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        limit = math.ceil(math.sqrt(number))
        for n in range(2, number):
            if number % n == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is a composite number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
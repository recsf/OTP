from random import *

user_pass = 4

password = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

otp = ""

for letter in range(user_pass):
    guess_letter = password[randint(0, 9)]
    otp = str(guess_letter) + str(otp)


print(otp)

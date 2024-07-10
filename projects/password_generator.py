import random
import string

pwd = []
alb = string.ascii_letters
symbolstr = "!@#$%^&*()-_=+[{;'/><.}]"
password = ""

letters = int(input("How many letters?: "))
symbols = int(input("How many symbols?: "))
numbers = int(input("How many numbers?: "))
length = letters + symbols + numbers

# Generate a list of needed symbols, letters and numbers.
for i in range(0, letters):
    pwd.append(alb[random.randint(0, len(alb) - 1)])
for i in range(0, numbers):
    pwd.append(str(random.randint(0, 9)))
for i in range(0, symbols):
    pwd.append(symbolstr[random.randint(0, len(symbolstr) - 1)])
# Randomise it
random.shuffle(pwd)

# Stringify
for i in range(0, len(pwd)):
    password += str(pwd[i])

print(f"Your random password is: {password}")
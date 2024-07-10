import random
import sys

print('''
Rock beats scissors.
Scissors beat paper.
Paper beats rock.

Rock -> 0
Paper -> 1
Scissors -> 2
''')

Choice = input("Pick an option: ")
options=["rock", "paper", "scissors"]
pythonChoice = random.randint(0, 2)
winning = False

if Choice in "012":
    Choice = int(Choice)
else:
    print("Invalid input, start again")
    sys.exit()

print(f"You picked {options[Choice]} and computer picked {options[pythonChoice]}")

if Choice == pythonChoice:
    print("It's a draw!")
    sys.exit()
elif Choice == 1:
    if pythonChoice == 0:
        winning = True
elif Choice == 0:
    if pythonChoice == 2:
        winning = True
elif Choice == 2:
    if pythonChoice == 1:
        winning = True

if winning:
    print("You won!")
else:
    print("You lost!")
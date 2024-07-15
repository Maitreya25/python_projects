import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
computer =[]
notto = True
pSum = 0
cSum = 0

def return_card() -> int:
    return random.choice(cards)

def drawC(choice: str):
    if choice in "yY":
        player.append(return_card())
        print(f"You drew a card, your current hand: {player}")
    if random.randint(0, 1):
        computer.append(return_card())
        print("Computer picked to draw another card")

while notto:
    player.append(return_card())
    player.append(return_card())
    computer.append(return_card())
    computer.append(return_card())
    if player[0] + player[1] > 21 or computer[0] + computer[1] > 21:
        player = []
        computer = []
    else:
        notto = False 

print(f"Your cards: {player}, current socre: {player[0] + player[1]}")
print(f"Computer's first card: {computer[0]}\n")

draw = input("Draw another (y/n): ")
while draw in "yY":
    drawC(draw)
    draw = input("Draw another (y/n): ")

for i in player:
    pSum += i
for i in computer:
    cSum += i

print(f"\nPlayer's score: {pSum}, hand: {player}")
print(f"Computer's score: {cSum}, hand: {computer}")

if ((pSum > cSum and pSum <= 21) or cSum > 21):
    print("Player won!")
elif ((cSum > pSum and cSum <= 21) or pSum > 21):
    print("Computer won!")
else:
    print("It's a draw!")

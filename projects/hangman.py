import random
from random_word import RandomWords

r = RandomWords()
pickedWord = r.get_random_word()
deaths = 0
guessedLetters = 0
guesses = []
word = "_" * len(pickedWord)
print(word)

while deaths < 5:
    guess = input("Pick a letter: ").lower()
    correct = False
    for index in range(0, len(pickedWord)):
        if guess == pickedWord[index]:
            word = [i for i in word]
            word[index] = guess
            word = "".join(word)
            if guess not in guesses:
                guessedLetters += 1
                correct = True
            else:
                print("You already guessed this!")

    if not correct:
        deaths += 1
    else:
        guesses.append(guess)

    print(word)
    if guessedLetters == len(pickedWord):
        print("You won!")
        break

if deaths == 5:
    print(f"You lost, the word was {pickedWord}")
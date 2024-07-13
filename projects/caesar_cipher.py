import string
import sys

# To avoid unreachable indexes.
letters = string.ascii_lowercase + string.ascii_lowercase

def encrypt(message: str, shift: int) -> str:
    newText = ""
    for i in message:
        if i in letters: # I honestly don't know how ceaser handles numbers and symbols, use them as is.
            position = letters.index(i)
            newPosition = position + shift
            newText += letters[newPosition]
        else:
            newText += i
    return newText

def decrypt(message: str, shift: int) -> str:
    newText = ""
    for i in message:
        if i in letters: # I honestly don't know how ceaser handles numbers and symbols, use them as is.
            position = letters.index(i)
            newPosition = position - shift
            newText += letters[newPosition]
        else:
            newText += i
    return newText

choice = input(("1 -> encode \n2 -> decode \nPick one: "))
shift = input("Pick the shift number: ")
text = input("Enter text: ").lower()

if choice not in "12" or not shift.isnumeric or not text.isalpha :
    print("Invalid input!")
    sys.exit()

shift = int(shift)
if shift > 26:
    print("Max permissible shift is 25.")

if choice == "1":
    print(f"Encrypted message: {encrypt(text, shift)}")
else:
    print(f"Decrypted message: {decrypt(text, shift)}")

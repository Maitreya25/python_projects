# `LESSON 15 DAY 4 - TREASURE MAP` from 100DOC by Angela.
import sys

'''
This is a difficult challenge. 💪
You are going to write a program that will mark a spot on a map with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Your job is to write a program that allows you to mark a square on the map using a letter-number system. 
First, your program must take the user input and convert it to a usable format.
Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:
[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
Example Input 1
B3
Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
'''

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Pick a two lettered position example A2: ")

if len(position) == 2: # Make sure input is as expected
    if (position[0] not in "abcABC") or (position[1] not in "123"): # No out of bound boxes
      sys.exit()

if position[0] in "aA":
    map[int(position[1]) - 1][0] = "X"
elif position[0] in "bB":
    map[int(position[1]) - 1][1] = "X"
else:
    map[int(position[1]) - 1][2] = "X"

print(f"{line1}\n{line2}\n{line3}")

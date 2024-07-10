# A year is leap if:
# 1. Divisible by 4 and not divisible by 100.
# 2. Divisible by 400.

year = int(input("What year do you wish to check?: "))
leap = False

# Half condition satisfied
if year % 4 == 0:
  if year % 400 == 0: # Divisble by 400
    leap = True
  elif year % 100 != 0: # Not divisible by 100
    leap = True

if leap:
  print("Leap year")
else:
  print("Not leap year")
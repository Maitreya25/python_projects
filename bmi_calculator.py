height = float(input("What's your height (in Meters)? \n"))
weight = float(input("What's your weight (in Kilograms) \n"))

print('''
BMI Categories:
Underweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater''')

print("\nSource: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm")

# BMI = weight / (height^2)
BMI = weight / height ** 2
print("\nYour BMI is = " + str(round(BMI, 1)))

if  (BMI > 25):
    target_weight = 25 * height ** 2
    print("\nYou must reduce your weight to less than " + str(target_weight) + " to attain a normal BMI.")
else:
    print("\nThis is a normal BMI.")
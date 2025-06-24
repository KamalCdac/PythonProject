# Python weight converter

weight = float(input("Enter your weight: "))
units = input("Kilograms or Pounds? (K or L): ")

if units == 'K' or units == 'k':
    weight = weight * 2.205
    units = "Lbs."
    print(f"your weight is {round(weight,1)} {units}")
elif units == 'L' or units == 'l' :
    weight = weight / 2.205
    units = "Kgs."
    print(f"your weight is {round(weight,1)} {units}")
else:
    print(f"{units} was not valid")

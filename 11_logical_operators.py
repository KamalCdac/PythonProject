# logical operators = evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be True
#                   and = both conditions must be True
#                   not = inverts the condition (not False, not True)

####### OR Operator
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is still scheduled.")


####### AND Operator
# press windows + .(dot) together to insert any emoji
temp = -3
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT Outside 🥵")
elif temp <= 0 and is_sunny:
    print("It is COLD Outside 🥶")
elif 28 > temp > 0 and is_sunny:
    print("It  is warm outside 😊")


###### NOT Operator
temp = -3
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It is HOT Outside 🥵")
elif temp <= 0 and not is_sunny:
    print("It is COLD Outside 🥶")
elif 28 > temp > 0 and not is_sunny:
    print("It  is warm outside 😊")
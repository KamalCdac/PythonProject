# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          Return X if condition is TRUE else return Y if condition is FALSE
#                           Formulae = X if condition else Y

temp = 222
a = 15
b = 6
age = 25
temperature = 30
user_role = "admin"

print("Positive" if temp > 0 else "Negative")
result = "EVEN" if temp % 2 == 0 else "ODD"
print(result)

min_num = b if a>b else a
max_num = a if a>b else b
print(f"Maximum number is {max_num} and minimum number is {min_num}")

status = "Adult" if age >=18 else "Minor"
print(status)

weather = "HOT" if temperature > 20 else "COLD"
print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
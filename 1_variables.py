# This is my first python file
print("I like travelling!")
print("Its really Good!")

# Variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it  was the value it contains

# f-string
# To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark.
# Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.

# Strings
first_name = "Bro"
food = "Pizza"
email = "brocode@fake.com"
print(first_name)
print(f"Hello {first_name}")
print(f"Hello {first_name} you like {food}")
print(f"Your email is {email}")

# Integers
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"Your class has {num_of_students} students")

# Floats
Price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${Price} ")
print(f"Your gpa is: {gpa} ")
print(f"Your ran is: {distance} km ")

# Boolean : A boolean is either True or False ( first letter is capital) They are binary
is_student = True
print(f"Are you a student: {is_student}")
if is_student:
    print("You are a student")
else :
    print("You are not a student")
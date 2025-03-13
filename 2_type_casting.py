# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa =3.2
is_student = True

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(gpa)) #<class 'float'>
print(type(is_student)) #<class 'bool'>



# age = float(age)
# print(age)

# if age is integer
age = str(age)
print(type(age))
#age += 1 # it will be an error as we can only concatenate strings not int
age += "1" # in this we will be using string concatenation No error (251 will be the output as 1 is concatenated with 25
print(age)

name = bool(name)
print(name) # it will return True

name_empty = ""
name_empty = bool(name_empty)
print(name_empty) # it will return False

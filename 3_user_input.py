# input() = A function that prompts the user to enter data. Returns the entered data as a String

name = input("What is your name ? : ")
age = input("How old are you ? : ")
print(f"Hello {name}")
print(f"You are {age} years old")
age = age +"1" #TypeError: can only concatenate str (not "int") to str . As type of age is string
print(age) # output will be 201. if age was input 20

age = int(age)
age = age+1 # output will be 202
print(age)

# either we can type cast age variable after getting input or enclose input() to int() function
marks = float(input("Enter total marks obtained"))
# marks = int(input("Enter total marks obtained"))
percentage = float(marks/100*100)
print(f"you obtained {marks} out of 100. Therefore your percentage is {percentage}")


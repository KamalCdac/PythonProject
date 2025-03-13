#while loop = execute some code while some condition remain true

name = input("Enter your name? :")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name? :")
print(f"Hello {name}")

food = input("Enter a food item you like (q to quit): ")

while food!='q':
    print(f"you like {food}")
    food = input("Enter a food item you like (q to quit): ")
print(f" Your name is {name}")
print("dsir")

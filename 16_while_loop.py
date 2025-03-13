#while loop = execute some code while some condition remain true
from idlelib.configdialog import changes

name = input("Enter your name? :")
print("this line is added using mobile")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name? :")
print(f"Hello {name}")

food = input("Enter a food item you like (q to quit): ")

while food!='q':
    print(f"you like {food}")
    food = input("Enter a food item you like (q to quit): ")
print(f" Your name is {name}")

# First commit changes
# Second push changes

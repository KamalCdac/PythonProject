#while loop = execute some code while some condition remain true


# name = input("Enter your name? :")
# print("this line is added using mobile")
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name? :")
# print(f"Hello {name}")
#
# food = input("Enter a food item you like (q to quit): ")
#
# while not food == 'q':
# while food!='q':
#     print(f"you like {food}")
#     food = input("Enter a food item you like (q to quit): ")
# print(f" Your name is {name}")

# First commit changes
# Second push changes

num = int(input("Enter a number between 1 and 10: "))
while num <1 or num >10:
     print(f"{num} is not valid")
     num = int(input("Enter a number between 1 and 10: "))
print(f"You have entered {num}")

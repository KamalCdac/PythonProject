#  random numbers

import random

# print(help(random))
low = 1
high =16

number = random.randint(low,high)
print(number)

number1 = random.random() # floating point number between 0 and 1
print(number1)

options = ("salt","paper","scissor")

print(random.choice(options))
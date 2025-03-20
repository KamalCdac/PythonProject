# Collection = Single "variable" used to store multiple values
# List  =  [] Ordered and Changeable. Duplicates OK.
# Set   =  {} Unordered and Immutable, But Add/Remove OK. NO Duplicates.
# Tuple =  () Ordered and Changeable. Duplicates OK. FASTER

# WE CAN USE ALL METHODS FUNCTIONS ON LIST AS WE USED IN STRINGS
##################   LIST    ###################
fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(fruits[0:3])
print(fruits[:3])
print(fruits[::2]) # prints every second element
print(fruits[::-1]) # Prints list in reverse order

print(fruits[2:]) # prints elements from second index to last as i didn't mention last index


for fruit in fruits:
    #print(fruit)
    print(fruit, end=", ") # prints on same line with comma(,)

print(dir(fruits))

print(help(fruits))
# Collection = Single "variable" used to store multiple values
# List  =  [] Ordered and Changeable. Duplicates OK.
# Set   =  {} Unordered and Immutable, But Add/Remove OK. NO Duplicates.
# Tuple =  () Ordered and Changeable. Duplicates OK. FASTER

# WE CAN USE ALL METHODS FUNCTIONS ON LIST AS WE USED IN STRINGS
##################   LIST  []   ###################
fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(fruits[0:3])
print(fruits[:3])
print("kkkk")
print(fruits[::2]) # prints every second element
#print(fruits[0:2:2]) # prints every second element
print(fruits[::-1]) # Prints list in reverse order

print(fruits[2:]) # prints elements from second index to last as I didn't mention last index


for fruit in fruits:
    print(fruit)
    # print(fruit, end=", ") # prints on same line with comma(,)

# print(dir(fruits)) #bunch of different methods that this list can perform

# print(help(fruits)) # description of each method mentioned in dir(fruits)

print("Oranges" in fruits) # we can use in operator to find element in list
fruits[0] = "pineapple"

print(len(fruits))

#append() method to add an element to the end of an list
fruits.append("Kiwi")
fruits.append("pineapple")
print(fruits)

fruits.remove("pineapple") # remove the first occurrence of duplicate element
print(fruits)

fruits.insert(0,"Papaya")
print(fruits)

fruits.sort() # sort all elements in alphabetical order
print(fruits)

fruits.reverse() # to reverse the list
print(fruits)

# fruits.clear() # to clear all the elements of list
# print(fruits)

#we can return the index of the element
print(fruits.index("Kiwi"))

fruits.append("Kiwi")
print(fruits.count("Kiwi"))
print(fruits.count("Watermelon"))


##################   SET  {}  ###################

print("##################   SET  {}  ###################")
set_fruits = {'Apple', 'Banana', 'Orange', 'Grapes', 'Apple'}
print(set_fruits)


##################   TUPLE  ()  ###################

print("##################   TUPLE  ()  ###################")
tuple_fruits = ('Apple', 'Banana', 'Orange', 'Grapes', 'Apple')
print(tuple_fruits)
print("Apple" in tuple_fruits)
print(tuple_fruits.index('Grapes'))
print(tuple_fruits.count("Apple"))

for fruit in tuple_fruits:
    print(fruit)
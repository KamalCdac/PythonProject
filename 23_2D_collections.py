# 2dlist = [list1, list2, list3] . It is useful when we want data in grid or matrix , excel format. rows and columns.

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]


print(groceries[0])
print(groceries[1])
print(groceries[2])

# if i want to print carrot from vegetables list
print(groceries[1][1])

#more effective way to write

groceries1 = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]
print(groceries)
print(groceries1)
print()
for collections in groceries:
    for food in collections:
        print(food, end=" ")
    print()
    # print(collections)

#--------------------------------  Keypad  using tuple coz unchangeable and ordered  -------------------------#

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ('*',0,'#'))

for row in num_pad:
    # print(row)
    for num in row:
        print(num, end=" ")
    print()

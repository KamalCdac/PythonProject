# dictionary  = a collection of {key:value} pairs
#                ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals)) # list of all dictionary attributes and methods
#print(help(capitals)) # description of all dictionary attributes and methods

# get()
print(capitals.get("USA"))
if capitals.get("Japan"):
    print("This exist in list")
else:
    print("This doesn't exist in list")

# update()
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Kamal"})
print(capitals)

#pop() remove element from list

capitals.pop("China")
print(capitals)

#popitem() will pop the latest item inserted
print(capitals)

#clear()
# capitals.clear()
# print(capitals)


# keys() method will return all of the keys in capital dictionary
key = capitals.keys()
print(key)

# if anytime i want to iterate over dictionary keys i can use keys() method using for loop
for key in capitals.keys():
    print(key)


#values() method to print all the values
values = capitals.values()
print(values)

# if anytime i want to iterate over dictionary values i can use values() method using for loop
for value in capitals.values():
    print(value)


# items() method
item = capitals.items()
print(item)

for key, value in capitals.items():
    print(f"{key}:{value}")
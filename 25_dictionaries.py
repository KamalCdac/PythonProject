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

#popitem()
capitals.popitem()
print(capitals)

#clear()

capitals.clear()
print(capitals)


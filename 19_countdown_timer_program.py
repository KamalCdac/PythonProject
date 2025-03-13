import time
my_time = int(input("Enter time in seconds: "))

for x in range(0, my_time):
    time.sleep(1)
    print(x)
print("Time's UP1")

# count backwards
for x in reversed(range(0, my_time)):
    time.sleep(1)
    print(x)
print("Time's UP2")

# Another technique to reverse  function is
# range(start, end , step)
# range(my_time, 0, -1)


for x in range(my_time, 0, -1):
    time.sleep(1)
    print(x)
print("Time's UP3")
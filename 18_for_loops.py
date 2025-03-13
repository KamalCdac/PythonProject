# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.
#               range(start, end, counter)
for x in range(1,10,3):
    print(x)

print("HAPPY HOLI")

# Reversed function to print loop in reverse order
for x in reversed(range(1,10)):
    print(x)

print("HAPPY HOLI AGAIN")

credit_card = "1234-5678-9012-786"
for x in credit_card:
    print(x)

# to skip an iteration we can use the keyword continue
print("Use of continue keyword")
for x in range(1, 21):
    if x == 13: # this will not print number 13
        continue
    else:
        print(x)
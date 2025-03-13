# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"
print(credit_number[0:4]) # it will return first 4 characters/ digits start=0 and end=4
print(credit_number[:4]) # same output as above line's as python assumes starting index will be 0 by default
print(credit_number[5:9])
# if we need everything upto the end of the string dont specify end for example [5:]
print(credit_number[5:])
print(credit_number[-1]) # prints 6 from last
print(credit_number[-2]) # prints 5 from last second digit
print(credit_number[-3])

print(credit_number[::2]) # it will print the every 2nd character in the string
last_digits = credit_number[-4:] # starts from last fourth digit as we require whatever is the card number we need last 4 digits of Credit Card
print(f"XXXX-XXXX-XXXX-{last_digits}")

# Reverse the characters in the string
credit_number = credit_number[::-1]
print(credit_number)

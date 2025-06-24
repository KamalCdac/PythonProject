# A loop within another loop is called nested loop (outer, inner)
#                 outer loop:
#                 inner loop:
# if we want each character on same line use end keyword
# we could use print() function also without any argument to print inner foreach contents on new line on every outer loop iteration

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to print: ")

for  y in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
#    print(end="\n") or
    print()

print("Item 1", end=" ")
print("Item 2")



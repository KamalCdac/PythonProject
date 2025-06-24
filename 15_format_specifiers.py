
# format specifiers = {value: flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :<  = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :=  = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

# 1.
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"Price 1 is ${price1:.3f}") #Price 1 is $3.142
print(f"Price 2 is ${price2:.3f}") #Price 2 is $-987.650
print(f"Price 3 is ${price3:.3f}") #Price 3 is $12.340

print(f"Price 1 is ${price1:10}")   #Price 1 is $   3.14159
print(f"Price 2 is ${price2:10}")   #Price 2 is $   -987.65
print(f"Price 3 is ${price3:10}")   #Price 3 is $     12.34
# if we precede number with 0 well these numbers will be

print(f"Price 1 is ${price1:010}")      #Price 1 is $0003.14159
print(f"Price 2 is ${price2:010}")      #Price 2 is $-000987.65
print(f"Price 3 is ${price3:010}")      #Price 3 is $0000012.34

print(f"Price 1 is ${price1:<10}")        #left justify
print(f"Price 2 is ${price2:<10}")        #left justify
print(f"Price 3 is ${price3:<10}")        #left justify

print(f"Price 1 is ${price1:>10}")        #right justify (by default)
print(f"Price 2 is ${price2:>10}")        #right justify (by default)
print(f"Price 3 is ${price3:>10}")        #right justify (by default)

print(f"Price 1 is ${price1:^10}")         # center align
print(f"Price 2 is ${price2:^10}")         # center align
print(f"Price 3 is ${price3:^10}")         # center align

print(f"Price 1 is ${price1:+}")     # make number positive
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
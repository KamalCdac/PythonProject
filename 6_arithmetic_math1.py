import math
print(math.pi)
x=9.5
#result = math.sqrt(25)
result = math.ceil(x)
result1 = math.floor(x)
print(result)
print(result1)


# Calculate circumference of circle = 2*pi*radius
radius = float(input('Enter the radius: '))
circumference = 2 * math.pi * radius
print(f"Circumference of circle is {round(circumference,2)}")


# Area of circle = pi *r*r

area = math.pi * pow(radius,2)
print(f"Area of circle is {round(area,2)}")

#area of triangle c= sqrt(a^2 + b^2)

a = float(input("Enter the value of side a: "))
b = float(input("Enter the value of side b: "))
area_triangle = math.sqrt(pow(a,2) * pow(b,2))
print(f"Area of triangle is {area_triangle}")
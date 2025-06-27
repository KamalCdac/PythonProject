#  concession stand program

menus = {
    "pizza": 1.00,
    "nachos":3.00,
    "popcorn": 5.00,
    "fries": 2.50,
    "chips": 6,
    "soda":3.70,
    "lemonade":4.25
}

cart = []

total =0

print("      MENU                       ")
for key, value in menus.items():
    print(f"{key:10}:${value:.2f}")

print("---------------------------------")

while True:
    food = input("Enter a food item (q to quit): ").lower()
    if food == 'q':
        break;
    # elif not menus.get(food):
    elif menus.get(food) is not None:
        price = menus.get(food)
        total += price
        cart.append(food)
    else:
        print("this food item not available")

for food in cart:
    print(food, end=" ")
print(f'Your total is {total:.2f}')
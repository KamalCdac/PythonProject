# shopping cart program
# i am going to use list . because set is uunordered i want shopping list to be in ordered manner . i am not going to use tuple because tuples are unchangeble.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) : ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'''Enter the price of a {food} : $ '''))
        foods.append(food)
        prices.append(price)
print("------   YOUR CART   ------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total is $ {total}")
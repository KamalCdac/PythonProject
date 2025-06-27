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

for key, value in menus.items():
    print(f"{key:10}:${value:.2f}")
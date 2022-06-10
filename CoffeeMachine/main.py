MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def check_ingredients(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def make_coffee(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]


def get_payment(coffee):
    profit = 0
    print("Please insert coins.")
    payment = float(input("How many quarters? ")) * 0.25
    payment += float(input("How many dimes? ")) * 0.1
    payment += float(input("How many nickels? ")) * 0.05
    payment += float(input("How many pennies? ")) * 0.01

    cost = MENU[coffee]["cost"]
    if cost > payment:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        make_coffee(coffee)
        profit = cost
        change = payment - cost
        if change > 0:
            print(f"Here is ${change:0.2f} in change.")
        print(f"Here is your {coffee}, enjoy!")
    return profit


is_on = True
while is_on:
    choice = input("\tWhat would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:0.2f}")
    elif choice in MENU:
        if check_ingredients(choice):
            money += get_payment(choice)
    elif choice == "off":
        is_on = False
    else:
        print("Choose only 'espresso', 'latte', or 'cappuccino'.")

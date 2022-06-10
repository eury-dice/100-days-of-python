from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee is not None:
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)

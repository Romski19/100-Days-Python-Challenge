from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
available = CoffeeMaker()
menu = Menu()

to_continue = True

while to_continue:
    option = menu.get_items()
    choice = input(f"What would you like to drink? {option}?: ").lower()
    if choice == "off":
        to_continue = False
    elif choice == "report":
        available.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if available.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            available.make_coffee(drink)

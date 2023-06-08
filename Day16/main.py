# Day16 Coffe Machine

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Start the coffee machine
is_on = True

while is_on:
    # Get user's choice
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    # Check if choice is valid
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Get the drink from the menu
        drink = menu.find_drink(choice)
        # Check if there are enough resources
        if coffee_maker.is_resource_sufficient(drink):
            # Check if there is enough money
            if money_machine.make_payment(drink.cost):
                # Make the drink
                coffee_maker.make_coffee(drink)

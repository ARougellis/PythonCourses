from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating objects from classes
coffee_maker = CoffeeMaker()
MENU = Menu()
money_machine = MoneyMachine()

continue_to_order = True
while continue_to_order:
    order = input(f"What would you like? ({MENU.get_items()}) ").lower()

    if order == "stop":
        continue_to_order = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = MENU.find_drink(order)
        significant_resources = coffee_maker.is_resource_sufficient(coffee)
        if significant_resources is True:
            print(f"Your {coffee.name} will cost ${coffee.cost}")
            successful_payment = money_machine.make_payment(coffee.cost)
            if successful_payment:
                coffee_maker.make_coffee(coffee)

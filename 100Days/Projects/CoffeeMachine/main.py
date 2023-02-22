from variables import MENU, default_resources

# --->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->--->
# FUNCTIONS


def restock(available_resources, baseline_resources):
    """
    This function is used to restock resources of the coffee machine.
    """
    continue_to_restock = True
    while continue_to_restock:
        restock_ingredient = input(f"Which ingredient do you want to restock? (water/milk/coffee/none)").lower()
        if restock_ingredient == 'none':
            continue_to_restock = False
        elif restock_ingredient not in ['water', 'milk', 'coffee']:
            print(f"{restock_ingredient} is not a resource this coffee machine uses.")
        else:
            available_resources[restock_ingredient] = baseline_resources[restock_ingredient]
    return available_resources


def calc_coins(order, cost):
    print(f"Your {order} will cost ${cost}. Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    print(f"total money given : ${total}")

    return total


# <---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---<---


# def order_coffee(MENU, default_resources):
current_resources = default_resources.copy()
current_resources["money"] = 0
continue_to_order = True

while continue_to_order:
    # Setting up some variables
    sufficient_resources = False
    sufficient_funds = False

    # STEP 1: Order Coffee
    coffee = input("What would you like? (espresso/latte/cappuccino) ").lower()

    # Step 2: Management Options
    if coffee == 'report':
        print(f"""
        Water : {current_resources['water']}ml
        Milk : {current_resources['milk']}ml
        Coffee : {current_resources['coffee']}g
        Money : ${current_resources['money']}
        """)
    elif coffee == 'restock':
        current_resources = restock(current_resources, default_resources)
    elif coffee == 'stop':
        continue_to_order = False
    elif coffee in MENU:
        order_ingredients = MENU[coffee]['ingredients']
        order_cost = MENU[coffee]['cost']
        # STEP 3: Checking for sufficient resources and using resources
        for ingredient in order_ingredients:
            if current_resources[ingredient] < order_ingredients[ingredient]:
                print(f"Sorry, there is not enough of {ingredient}.")
                sufficient_resources = False
                break
            else:
                sufficient_resources = True

    # STEP 4: Payment
    if sufficient_resources is True:
        order_cost = MENU[coffee]['cost']
        total_coins = calc_coins(coffee, order_cost)
        if total_coins < order_cost:
            print("Insufficient funds. Money refunded.")
            sufficient_funds = False
        else:
            refund = total_coins - order_cost
            if refund > 0:
                print(f"Here is ${round(refund, 2)} in change")
            sufficient_funds = True
            current_resources["money"] += order_cost

    # Complete the Order
    if sufficient_funds is True:
        order_ingredients = MENU[coffee]['ingredients']
        for ingredient in order_ingredients:
            current_resources[ingredient] -= order_ingredients[ingredient]
        print(f"Enjoy your {coffee}!")

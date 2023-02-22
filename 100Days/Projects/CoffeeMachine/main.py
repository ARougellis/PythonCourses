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

default_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




coffee = input("What would you like? (espresso/latte/cappuccino) ").lower()

current_resources = {
    "water": 300,
    "milk": 50,
    "coffee": 50,
}

if coffee == 'report':
    print(f"""
    Water : {current_resources['water']}ml
    Milk : {current_resources['milk']}ml
    Coffee : {current_resources['coffee']}g
    Money : $<TBI>
    """)
elif coffee == 'restock':
    # TODO 2: include restock() function here
    # current_resources = restock()

order_ingredients = MENU[coffee]['ingredients']
order_cost = MENU[coffee]['cost']

for ingredient in ['water', 'milk', 'coffee']:
    if current_resources[ingredient] < order_ingredients[ingredient]:
        print(f"Sorry, there is not enough of {ingredient}.")

# def calc_coins():
print("Please insert coins.")
quarters = input("How many quarters?: ")
dimes = input("How many dimes?: ")
nickles = input("How many nickles?: ")
pennies = input("How many pennies?: ")

total_coins = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies

print(f"total : ${total_coins}")

# return total_coins



# TODO 1: Restock function
# def stock():
restock = input(f"Which ingredient do you want to restock? (water/milk/coffee)").lower()
"""
current stock [ingred] = default stock [ingredient]

note:
    - i want to iterate this till we are done
        - therefore may need a while loop that closes hwn we no longer want to restock. 
"""

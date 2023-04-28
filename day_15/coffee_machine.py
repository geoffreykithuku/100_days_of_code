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


def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def process_coins():
    total = 0
    print("Please insert coins. ")
    total += int(input("How many quaters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total
    
def is_transaction(payment, cost_of_drink):
    if payment >= cost_of_drink:
        change = round(payment-cost_of_drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry, that is not enough money. Money refunded")
        return False
    
def make_coffee(drink, ingredients):
    # global resources
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}")
    
is_on = True


profit = 0
while is_on:
    choice = input("What would you like? (espresso, latte or cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            
            if is_transaction(payment, drink["cost"]):
               make_coffee(choice, drink["ingredients"])
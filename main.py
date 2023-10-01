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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

logo = """
┓ ┏  ┓               ┏┓  •╹   ┏┓  ┏┏    ╻
┃┃┃┏┓┃┏┏┓┏┳┓┏┓  ╋┏┓  ┣ ┏┓┓ ┏  ┃ ┏┓╋╋┏┓┏┓┃
┗┻┛┗ ┗┗┗┛┛┗┗┗   ┗┗┛  ┻ ┗┻┗ ┛  ┗┛┗┛┛┛┗ ┗ •
"""


def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coin_process():
    print("Please insert coins.")
    total = int(input("how many 10 cents: ")) * 0.10
    total += int(input("how many 20 cents: ")) * 0.20
    total += int(input("how many 50 cents: ")) * 0.50
    total += int(input("how many 1 dollar: ")) * 1
    return total


def successful_transaction(money_paid, drink_cost):
    if money_paid >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_paid - drink_cost, 2)
        print(f"Here is your change: ${change}.")
        return True
    else:
        print("Sorry there's insufficient money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


machine_on = True

while machine_on:
    print(logo)
    choice = input("What would you like? Espresso, latte or cappuccino: ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = coin_process()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
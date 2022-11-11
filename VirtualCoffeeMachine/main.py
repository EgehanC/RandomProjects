from art import logo

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


def check_resources(drink):
    needed_resources = MENU[drink]["ingredients"]
    for item in needed_resources:
        if needed_resources[item] > resources[item]:
            print("There is not enough resources.")
            return False
    return True


def pay(drink):
    print("Please insert coins...")
    pennies = 0.01 * float(input("Pennies: "))
    nickles = 0.05 * float(input("Nickles: "))
    dimes = 0.10 * float(input("Dimes: "))
    quarters = 0.25 * float(input("Quarters: "))
    balance = round(pennies + nickles + dimes + quarters, 2)
    change = balance - MENU[drink]["cost"]
    if change >= 0:
        print(f"Here's your change: ${change}")
        return f"Here is your {drink}☕️"
    else:
        return f"Your balance isn't enough. You need to insert {-change}$ more."


def play():
    is_on = True
    while is_on:
        print(logo)
        drink = input(
            "What would you like to drink? espresso/latte/cappuccino\n")
        if drink == "off":
            print("Turning off...")
            is_on = False
        else:
            enough_resources = check_resources(drink)
            if enough_resources == True:
                print(pay(drink))
            new_order = input("Order again? y/n\n")
            if new_order == "n":
                is_on = False


play()

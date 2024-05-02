MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 12,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False when there is sufficient in resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True

def coin_process():
    """Returns the total calculated from inserted coins"""
    print("Please enter coins!")
    total = int(input("How many 1 rupee coins?: ")) * 1
    total += int(input("How many 2 rupee coins?: ")) * 2
    total += int(input("How many 5 rupee coins?: ")) * 5
    total += int(input("How many 10 rupee coins?: ")) * 10
    return total

def is_transaction_sucessful(money_received, drink_cost):
    """Return True when payment is accepted , False when money is insufficient"""
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not the money, Money refunded")
        return False

def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🍵\nHave a nice day!")



is_on = True
while is_on:
    choice = input("What would u like? (Expresso/Latte/Cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit}/-")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = coin_process()
            if is_transaction_sucessful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])


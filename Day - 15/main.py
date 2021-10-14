# TODO: 2. Check resources sufficient tp make a drink order.

from data import MENU, resources

profit = 0


def resources_available():
    tubig = resources["water"]
    gatas = resources["milk"]
    kape = resources["coffee"]
    return tubig, gatas, kape


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print("Sorry there is not enough water.")
            return False
    return True


def process_coins():
    """returns the total from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.25
    total += int(input("How many nickles: ")) * 0.25
    total += int(input("How many pennies: ")) * 0.25
    return total


def is_transaction_successful(money_received, cost_drink):
    """"Return true if payment accepted else false if insufficient"""
    if money_received >= cost_drink:
        change = round(money_received - cost_drink, 2)
        print(f"Here is ${change}")
        global profit
        profit += cost_drink
        return True
    else:
        print("Sorry not enough money. Money Refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {drink_name} ")


# TODO: 1. Print report of all the machine resources
is_continue = True
while is_continue:
    choice = input("What would you like?(espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_continue = False
    elif choice == "report":
        water, milk, coffee = resources_available()
        print(f"Water: {water} ml")
        print(f"Milk: {milk} ml")
        print(f"Coffee: {coffee}g")
        print(f"Money:$ {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])

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

# TODO 1. show machine status
# TODO 2. check for resource
# TODO 3. ask for orders
# TODO 4. check if eligible
# TODO 5. deducted resources add money
# TODO 6. delivery order
is_on = True
print("bright day coffee")


def insufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry! there is no enough {item}.")
            return False
    return True


def coins():
    print("please insert coins")
    total = int(input("how many quarters"))*0.25
    total += int(input("how many dimes"))*0.10
    total += int(input("how many nickles"))*0.05
    total += int(input("how many pennies"))*0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    order_item = input("what would you like to have ? (espresso,latte cappuccino)")
    if order_item == "off":
        is_on = False
    elif order_item == "report":
        print(f"water {resources['water']}ml")
        print(f"coffee {resources['coffee']}gm")
        print(f"milk {resources['milk']}ml")
        print(f"profit ${profit}")
    else:
        drink = MENU[order_item]
        if insufficient(drink["ingredients"]):
            payment = coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order_item, drink["ingredients"])


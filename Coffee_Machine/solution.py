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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >resources[item]:
            print(f"Sorry not enough {item} ")
            return False
    return True

def process_coints():
    print("Process coints")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transition_successful(user_pay):
    if user_pay>=drink['cost']:
        change=round(user_pay-drink['cost'],2)
        print(f"Your change is {change}")
        global profit
        profit+=user_pay
        return True
    else:
        print("Sorry not enough money")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"This is you {drink_name}")

is_work=True
while is_work:
    choice=input("What would you like? (espresso/latte/cappucino): ")
    if choice=="off":
        is_work=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(profit,2)}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coints()
            if is_transition_successful(payment):
                make_coffee(choice, drink["ingredients"])


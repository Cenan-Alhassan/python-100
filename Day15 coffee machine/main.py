# TODO 1. make a report() function that prints the current resources


# main function asks for coffee type
# function calculate_resources() takes the coffee type, and calculates whether the resources are
# sufficient. If yes, returns True. If not, prints a string.

# create calculate_cost() function which takes coffee type, finds cost and asks for money.
# ask for money and convert to int. If enough money then add money and deduct resources and give back change
# .. quarters, dimes, nickles, pennies = input("").split(" ", 4)
# if not enough, terminate function

from menu import MENU, resources


def report():
    for key, value in resources.items():
        print(f"{key}: {value}")


def calculate_resources(coffee):
    """Takes the coffee type and returns TRUE if enough resources are available"""
    cont = True
    for item in MENU[coffee]['ingredients']:
        if MENU[coffee]['ingredients'][item] > resources[item]:
            print(f"Not enough {item}")
            cont = False

    return cont


def calculate_cost(coffee):
    """takes the coffee type, asks for money and checks if sufficient. If so, adds money and deducts from resources"""
    cost_of_coffee = MENU[coffee]["cost"]
    print(f"A {coffee} costs {cost_of_coffee}")

    quarters, dimes, nickles, pennies = input("Enter number of quarters, dimes, nickles and pennies: ").split(" ", 4)
    money_entered = int(quarters)*0.25 + int(dimes)*0.10 + int(nickles)*0.05 + int(pennies)*0.01

    if money_entered >= cost_of_coffee:
        change = '{:.2f}'.format(money_entered - cost_of_coffee)
        print(f'You entered ' + '{:.2f}'.format(money_entered) + f'$. Your change is: {change}$')
        print("Teşekkürler ve iyi günler ☕")
        resources['money'] += cost_of_coffee
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
        resources['milk'] -= MENU[coffee]['ingredients']['milk']

    else:
        print(f"You entered {money_entered}$. Insufficient funds. Money refunded.")


while True:
    coffee_type = input("What kind of coffee would you like? latte/cappuccino/espresso: ")

    if coffee_type == 'report':
        report()
    elif coffee_type == 'off':
        exit()
    elif coffee_type != 'latte' and coffee_type != 'espresso' and coffee_type != 'cappuccino':
        print("Please enter a valid option.")
    else:
        if calculate_resources(coffee_type):
            calculate_cost(coffee_type)



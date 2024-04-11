from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# menu = Menu()
# coffee_machine = CoffeeMaker()
#
# print(menu.find_drink("latte"))
# latte = menu.find_drink("latte")
# print(coffee_machine.is_resource_sufficient(latte))
# coffee_machine.report()
# coffee_machine.make_coffee(latte)
# coffee_machine.report()
# print(coffee_machine.is_resource_sufficient(latte))


menu = Menu()  # now all 3 MenuItem objects have been created
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
while True:

    coffee = input("What kind of coffee would you like? latte/cappuccino/espresso: ")

    if coffee == 'report':
        coffee_machine.report()
        money_machine.report()
    elif coffee == 'off':
        exit()
    elif coffee != 'latte' and coffee != 'espresso' and coffee != 'cappuccino':
        print("Please enter a valid option.")
    else:
        drink = menu.find_drink(coffee)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            print("yay")
            coffee_machine.make_coffee(drink)


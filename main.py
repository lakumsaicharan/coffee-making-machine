<<<<<<< HEAD
from data import Menu, resources
from functions import make_coffee, transaction_successful, resource_sufficient, process_coins, report
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino):​').lower()
    if choice == 'off':
        print('Turning off the coffee machine. Goodbye!')
        is_on = False
    elif choice == 'report':
        report(resources)
    else:
        if choice in Menu:
            drink = Menu[choice]
            if resource_sufficient(choice,resources):
                payment = process_coins()
                if transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink["ingredients"])
                else:
                    continue
        else:
            print('Invalid selection. Please choose espresso, latte, or cappuccino.')
=======


##USING OOPS CONCEPTS

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options}: ').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


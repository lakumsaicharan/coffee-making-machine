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
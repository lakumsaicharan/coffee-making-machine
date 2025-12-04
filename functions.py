from data import Menu, resources
profit = 0
#make cofee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

#check transactions
def transaction_successful(user_money, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    global profit
    if user_money>=drink_cost:
        profit += drink_cost
        if user_money>drink_cost:
            print(f'your total is {user_money}, drink cost is {drink_cost}')
            change = user_money-drink_cost
            print(f'Here is your change: ${change}')
        return True
    else:
        print('Sorry, not enough money. Money refunded.')
        return False

#check resources
def resource_sufficient(drink, resources):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in Menu[drink]['ingredients']:
        if Menu[drink]['ingredients'][item]>resources[item]:
            print(f'Sorry, Not enough {item}.')
            return False
        else:
            return f'processing {drink}'
    return False

# process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please insert coins.')
    total = int(input('How many quarters?: '))*0.25
    total += int(input('How many dimes?: '))*0.10
    total += int(input('How many nickels?: '))*0.05
    total += int(input('How many pennies?: '))*0.01
    return total
# print report
def report(resources):
    """Prints a report of all resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
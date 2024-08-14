# #TODO:
import ingredients
drink_name = ingredients.MENU
turnOn = True

def transaction(drink):
    print(f'Amount inserted is: ${ingredients.resources['amount_inserted']:.2f}'.format())
    print(f'Drink cost is: ${drink_name[drink]['cost']:.2f}'.format())
    if drink_name[drink]['cost'] < ingredients.resources['amount_inserted']:
        change = ingredients.resources['amount_inserted'] - drink_name[drink]['cost']
        ingredients.resources['money'] += drink_name[drink]['cost']
        print(f"Here is ${change:.2f} in change".format())
        for ingredient in drink_name[drink]['ingredients']:
            ingredients.resources[ingredient] -= drink_name[drink]['ingredients'][ingredient]
        print(f"Here is your {drink} enjoy!")
    else:
        print("Insufficient coins inserted. Money refunded")
    ingredients.resources['amount_inserted'] = 0
def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    ingredients.resources['amount_inserted'] = 0.25 * quarters + 0.1 * dimes + 0.01 * pennies +  0.05 * nickels

def check_resource(drink):
        for ingredient in drink_name[drink]['ingredients']:
            if drink_name[drink]['ingredients'][ingredient] > ingredients.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True


def user_input():
    global turnOn
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == 'report':
        print(ingredients.resources)
    elif choice in ['espresso','latte','cappuccino']:
        if check_resource(choice):
            insert_coins()
            transaction(choice)
    elif choice == 'off':
        turnOn = False
    else:
        print("Invalid option. Please choose espresso, latte or cappuccino!")





while turnOn:
    user_input()



# for ingredient in drink_name['espresso']['ingredients']:
#     print(drink_name['espresso']['ingredients'][ingredient])
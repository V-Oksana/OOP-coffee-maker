from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

OFF = False

# Create a menu
espresso = MenuItem("espresso", 100, 0, 20, 1.5)
latte = MenuItem("latte", 150, 150, 22, 3.5)
cappuccino = MenuItem("cappuccino", 160, 100, 18, 2.75)

my_menu = Menu()

my_coffee_maker = CoffeeMaker()

my_money_machine = MoneyMachine()


while not OFF:
    choice_of_drink = input(f"What would you like to drink? {my_menu.get_items()}: \n")
    print(f"You chose {choice_of_drink}.")
    if choice_of_drink == "off":
        OFF = True
    elif choice_of_drink == "report":
        print(my_coffee_maker.report())
        print(my_money_machine.report())
    else:
        drink = my_menu.find_drink(choice_of_drink)

        try:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)
        except AttributeError:
            print("Please select another drink.")



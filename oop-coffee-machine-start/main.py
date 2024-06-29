from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    order = input("What would you like? espresso / latte / cappuccino: ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        check_drink = menu.find_drink(order)
        check_ingredients = coffee_maker.is_resource_sufficient(check_drink)
        if check_ingredients:
            money_machine.make_payment(check_drink.cost)
            coffee_maker.make_coffee(check_drink)
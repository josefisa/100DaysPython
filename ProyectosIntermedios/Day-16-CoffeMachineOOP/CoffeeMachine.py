# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("tan")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(200)
# timmy.left(90)
# timmy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable
# import pandas
# table = PrettyTable()
# #print(table)

# table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander","Petrosky"])
# table.add_column("Pokemon name",["Electric","Water","Fire","Printing"])

# table.align = "l"

# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option})")
    if choice == "off":
        print('Paso por el off')
        is_on = False
    elif choice  == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    
    
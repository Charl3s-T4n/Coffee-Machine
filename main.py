from data import MENU, resources

# Create function that shows resources left in machine, with parameters
#money = 0
#water_initial = 300
#milk_initial = 200
#coffee_initial = 100


#resources = {
   # "water": 300,
    #"milk": 200,
    #"coffee": 100,}
profit = 0
# Create flag varaible so i won't ask customer to insert coins when not enough resources,
# will ask what would you like instead
enough_resources = True
# Create flag variable so resources in machine won't change if not enough ingredient/$ given


def resources_in_machine(water_used, milk_used, coffee_used, cost_price, print_report):
    """changes the ingredients and $ left in machine, can choose to print out report"""
    resources["water"] = resources["water"] - water_used   # leftover gets replaced in the dict
    resources["milk"] = resources["milk"] - milk_used
    resources["coffee"] = resources["coffee"] - coffee_used
    global profit      # Create global variable so i can add profit to $ in machine
    profit += cost_price
    if print_report == "yes":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit} ")


# Create function that process coins when sufficient resources
def when_sufficient_resources(choice_of_drink, price_of_drink):
    """will tell customer not enough $, give refund, give change, tell him enjoy drink"""
    print("Please insert coins.")
    global enough_resources  ### IMPORTANT: Have to specify global variable here and not inside if statement---> because there is no block scope in python
    no_of_quarters = int(input("How many quarters?: "))     # $0.25
    no_of_dimes = int(input("How many dimes?: "))           # $0.10
    no_of_nickles = int(input("How many nickles?: "))       # $0.05
    no_of_pennies = int(input("How many pennies?: "))       # $0.01
    total_amount_inserted = float((no_of_quarters*0.25)+(no_of_dimes*0.10)+(no_of_nickles*0.05)+(no_of_pennies*0.01))
    if price_of_drink > total_amount_inserted:     # When not enough $ inserted, refund
        enough_resources = False  # will not change resources in machine
        print("Sorry, that's not enough money. Money refunded.")
    elif price_of_drink < total_amount_inserted:   # To give change back to customer
        leftover_change = round((total_amount_inserted - price_of_drink), 2)   # round to 2 dec places
        print(f"Here is ${leftover_change} in change.")
        print(f"Here is your {choice_of_drink}. Enjoy!")
    elif price_of_drink == total_amount_inserted:  # No need give change, just nice
        print(f"Here is your {choice_of_drink}. Enjoy!")


# Create function to check if resources is sufficient


def check_resources(water_left, milk_left, coffee_left, water_needed, milk_needed, coffee_needed):
    """will print out error to customer when not enough ingredients"""   # ADD docstring
    global enough_resources    ### IMPORTANT: Have to specify global variable here and not inside if statement---> because there is no block scope in python
    if water_left < water_needed:
        print("Sorry, there is not enough water.")
        enough_resources = False
    if milk_left < milk_needed:
        print("Sorry, there is not enough milk.")
        enough_resources = False
    if coffee_left < coffee_needed:
        print("Sorry, there is not enough coffee.")
        enough_resources = False


# Create flag variable so that i can continue/exit while loop
# TODO 1: promt user

flag_variable = False
while not flag_variable:     # While True
    enough_resources = True  ### IMPORTANT: Solves bugs 1-3: restarts status of enough_resources, so that even if not enough for latte/cappuccino, espresso can still have
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":    # Always show this when user input 'report'
        resources_in_machine(water_used=0, milk_used=0, coffee_used=0, cost_price=0,print_report="yes")  # Initial

    elif user_input == "espresso":
        check_resources(water_left= resources['water'],milk_left= resources['milk'], coffee_left= resources['coffee'], water_needed= 50 , milk_needed= 0, coffee_needed= 18)
        if enough_resources == True:  # While True: there's enough resources
            when_sufficient_resources(choice_of_drink = "espresso", price_of_drink= 1.5)

            if enough_resources == True: # While True: there's enough $ inserted
                resources_in_machine(water_used=50, milk_used=0, coffee_used=18, cost_price=1.5,print_report="no")

    elif user_input == "latte":
        check_resources(water_left=resources['water'],milk_left=resources['milk'],coffee_left=resources['coffee'],water_needed=200,milk_needed=150,coffee_needed=24)
        if enough_resources == True:  # While True: there's enough resources
            when_sufficient_resources(choice_of_drink="latte",price_of_drink=2.5)

            if enough_resources == True:  # While True: there's enough $ inserted
                resources_in_machine(water_used=200,milk_used=150,coffee_used=24,cost_price=2.5,print_report="no")

    elif user_input == "cappuccino":
        check_resources(water_left=resources['water'],milk_left=resources['milk'],coffee_left=resources['coffee'],water_needed=250,milk_needed=100,coffee_needed=24)
        if enough_resources == True:  # While True: there's enough resources
            when_sufficient_resources(choice_of_drink="cappuccino",price_of_drink=3.0,)

            if enough_resources == True:  # While True: there's enough $ inserted
                resources_in_machine(water_used=250,milk_used=100,coffee_used=24,cost_price=3.0,print_report="no")

    elif user_input == 'off':
        flag_variable = True  # Stop while loop, ends program



    # Current bug:
    #    1)can't get espresso if there's not enough for latte or cappuccino, even if
    #      there's enough for espresso
    #    2) report -> espresso -> not enough money, refunded -> only can type report after
    #         only can type not enough money after first time
    #    3) cappuccino -> latte -> not enough ingredient -> can't type espresso afterwards
    #       same as 1)
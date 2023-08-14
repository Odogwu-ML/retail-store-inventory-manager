import dbfunctions as dbf 
import os
# list of possible functionalitie
possible_actions  = {
    "add product": dbf.add_product, 
    "update product": dbf.update_product, 
    "search for product": dbf.search
    }

# welcome message 
print("Hello welcome to this inventory management system")
# get user name
userName = input("\nPlease enter your name: ")

def action():
    # display available actions
    for count, act in enumerate(possible_actions, start=1):
        print(count, act)

    # get desired action
    db_action= input(f"Hi {userName} pick an operation: ")

    should_continue = True

    while should_continue:

        # perform action
        result = possible_actions[db_action]
        print(result())

        cont = input(f"enter 'y' to add another product, 'r' to choose different operation and 'n' to end:").lower()

        if cont == 'y':
            print(result())
        elif cont == 'r':
            should_continue == False
            os.system("clear")
            action()
        else:
            should_continue == False
            return

action()
def show_inventory()


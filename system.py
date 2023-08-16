import dbfunctions as dbf 
import os
import creating_db as cdb

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


should_continue = True

def action(): 

    global should_continue 
    # display available actions
    for count, act in enumerate(possible_actions, start=1):
        print(count, act)

    # get desired action
    db_action= input(f"Hi {userName} choose an operation: ")

    if db_action in possible_actions.keys():
        # perform action
        result = possible_actions[db_action]
        print(result())
    else:
        print("Invalid action. Please choose a valid operation.")

    while should_continue:
        
        cont = input(f"Enter 'y' to perform another operation and 'n' to end: ").lower()
        
        if cont == 'y':
            os.system("clear")
            action()
        elif cont == "n":
            cdb.conn.close()
            should_continue = False
            
    return

action()


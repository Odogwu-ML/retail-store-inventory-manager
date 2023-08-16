import creating_db as cdb
import sqlite3

# add product function
def add_product():
    # Get the product's details
    product_id = int(input("Insert products id: "))
    product_name = input("Insert product name: ")
    product_cat = input("What category does the product fall into: ")
    product_price = float(input("Insert product price: "))
    product_qt = float(input("Insert quantity available: "))

    product_details = [product_id, product_name, product_cat, product_price, product_qt]

    # Add the product to the inventory
    try:
        cdb.cursor.execute("""
            INSERT INTO products (id, name, category, price, quantity) VALUES (?, ?, ?, ?, ?)
        """, product_details
        )
    except sqlite3.IntegrityError:
        return "Id already in use try again with another id"
    else:
        cdb.conn.commit()
        return "\nproduct has been added successfully"

def update_product():

    # get the product id
    product_id = input("\nEnter product id: ")

    # select desired row
    cdb.cursor.execute("SELECT * FROM products WHERE id=?", [product_id])

    row = cdb.cursor.fetchone()

    if row:
        print("\nHere are the products details: \n")
        print(f"id: {row[0]} \nname: {row[1]} \ncategory: {row[2]} \nprice: {row[3]} \nquantity: {row[4]}")

        should_continue = True

        while should_continue:

            print("\nWhere would you like to make channges to: \n\nname \nid \ncategory \nprice or \nquantity\n")

            required_change = input("")

            if required_change == "name":
                change = input(f"\nEnter new product name: ")
            elif required_change == "id":
                change = int(input(f"\nEnter new product id: "))
            elif required_change == "category":
                change = input(f"\nEnter new product category: ")
            elif required_change == "price":
                change = float(input(f"\nEnter new price: "))
            elif required_change == "quantity":
                change = input(f"\nEnter new product quantity: ")
            else:
                print("Invalid Entry")
                continue

            # make required change to the product
            cdb.cursor.execute(f"UPDATE products SET {required_change}=? WHERE id=?",(change, product_id))
            cdb.conn.commit()
            print("\nProduct updated successfully")

            # Fetch and display the updated row
            cdb.cursor.execute("SELECT * FROM products WHERE id=?", [product_id])
            updated_row = cdb.cursor.fetchone()
            print("\nUpdated information:")
            print(f"id: {updated_row[0]} \nname: {updated_row[1]} \ncategory: {updated_row[2]} \nprice: {updated_row[3]} \nquantity: {updated_row[4]}")

            if input("Do you still want to make changes to this product yes/no: ").lower() == "no":
                should_continue = False
    else:
        return "\nNo row found with the specified ID."
    
    return "\n"


def search():

    should_continue = True

    while should_continue:
        # get desired product id
        product_id = input("Enter products id: ")

        # select desired row
        cdb.cursor.execute("SELECT * FROM products WHERE id=?", [product_id])

        row = cdb.cursor.fetchone()

        if row:
            print("\nHere are the product details: \n")
            print(f"id: {row[0]} \nname: {row[1]} \ncategory: {row[2]} \nprice: {row[3]} \nquantity: {row[4]}")

            if input("\nDo you want to search for another row? yes/no: ") == "no":
                should_continue = False
        else:
            return "\nNo row found with the specified ID."

    return

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
        return "Your product has been added successfully"

def update_product():
    print("nil")

def search():
    print("nil")
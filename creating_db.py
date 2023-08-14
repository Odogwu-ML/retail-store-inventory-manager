# data base

import sqlite3

# create database for the retail store
conn = sqlite3.connect("RetailStore.db")

# create cursor which allows us work with the database 
cursor = conn.cursor()

# create a relation in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')
               
if __name__  == '__main__':
# Insert sample data into the products table
    data = [
        ('101', 'T-Shirt', 'Clothing', 15.99, 50),
        ('102', 'Jeans', 'Clothing', 29.99, 30),
        ('103', 'Shoes', 'Footwear', 49.99, 20),
        ('104', 'Hat', 'Accessories', 9.99, 100),
        ('105', 'Backpack', 'Accessories', 39.99, 25)
    ]

    # insert the sample data in each repective column in the database
    cursor.executemany('INSERT INTO products (id, name, category, price, quantity) VALUES (?, ?, ?, ?, ?)', data)

    # Commit changes and close the connection: apply what we have done to the database
    conn.commit()
    conn.close()

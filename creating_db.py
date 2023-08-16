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
